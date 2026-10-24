#!/bin/sh
# Build the ZIP uploaded to Partner Center for Microsoft MCP server certification
# (offer type "Apps and Agents for M365 and Copilot").
# The Key Vault URI stays out of git: manifest.json keeps a placeholder, and the
# copy packaged here gets KEY_VAULT_URI in its place.
# The archive holds the package files at its root, without OS junk or the dist folder.
set -eu
cd "$(dirname "$0")"
placeholder='https://REPLACE-WITH-KEY-VAULT-NAME.vault.azure.net/'
: "${KEY_VAULT_URI:?Set KEY_VAULT_URI to the Azure Key Vault URI, such as https://<vault>.vault.azure.net/}"
if ! printf '%s\n' "$KEY_VAULT_URI" | grep -Eq '^https://[A-Za-z0-9-]{3,24}\.vault\.azure\.net/$'; then
  echo "KEY_VAULT_URI must look like https://<vault>.vault.azure.net/" >&2
  exit 1
fi
if ! grep -qF "$placeholder" manifest.json; then
  echo "manifest.json must keep the Key Vault placeholder; the URI is set at build time." >&2
  exit 1
fi
if LC_ALL=C grep -q '[^ -~]' manifest.json mcptools.json; then
  echo "manifest.json and mcptools.json must be ASCII only." >&2
  exit 1
fi
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
sed "s|$placeholder|$KEY_VAULT_URI|" manifest.json > "$stage/manifest.json"
cp mcptools.json intro.md color.png outline.png "$stage/"
schema=$(python3 -c 'import json; print(json.load(open("manifest.json"))["$schema"])')
uvx check-jsonschema --schemafile "$schema" "$stage/manifest.json"
version=$(python3 -c 'import json; print(json.load(open("manifest.json"))["version"])')
out="dist/oneprofile-microsoft-$version.zip"
mkdir -p dist
rm -f "$out"
dest="$PWD/$out"
(cd "$stage" && zip -qX "$dest" manifest.json mcptools.json intro.md color.png outline.png)
echo "$out"
