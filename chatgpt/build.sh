#!/bin/sh
# Build the ZIP uploaded to the OpenAI plugin portal (platform.openai.com/plugins).
# The archive holds the package files at its root, without OS junk or the dist folder.
set -eu
cd "$(dirname "$0")"
version=$(python3 -c 'import json; print(json.load(open("plugin.json"))["version"])')
out="dist/oneprofile-chatgpt-$version.zip"
mkdir -p dist
rm -f "$out"
zip -qrX "$out" plugin.json mcp.json README.md LICENSE assets skills \
  -x '*.DS_Store' -x '__MACOSX/*'
echo "$out"
