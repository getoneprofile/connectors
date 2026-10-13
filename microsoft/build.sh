#!/bin/sh
# Build the ZIP uploaded to Partner Center for Microsoft MCP server certification
# (offer type "Apps and Agents for M365 and Copilot").
# The archive holds the package files at its root, without OS junk or the dist folder.
set -eu
cd "$(dirname "$0")"
if grep -q 'REPLACE-WITH' manifest.json; then
  echo "manifest.json still has a placeholder: set the Azure Key Vault URI first." >&2
  exit 1
fi
if LC_ALL=C grep -q '[^ -~]' manifest.json mcptools.json; then
  echo "manifest.json and mcptools.json must be ASCII only." >&2
  exit 1
fi
schema=$(python3 -c 'import json; print(json.load(open("manifest.json"))["$schema"])')
uvx check-jsonschema --schemafile "$schema" manifest.json
version=$(python3 -c 'import json; print(json.load(open("manifest.json"))["version"])')
out="dist/oneprofile-microsoft-$version.zip"
mkdir -p dist
rm -f "$out"
zip -qrX "$out" manifest.json mcptools.json intro.md color.png outline.png \
  -x '*.DS_Store' -x '__MACOSX/*'
echo "$out"
