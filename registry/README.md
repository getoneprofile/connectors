# Oneprofile in the MCP Registry

`server.json` lists Oneprofile's remote MCP server, `https://api.getoneprofile.ai/mcp` (Streamable HTTP, signed in with OAuth), in the [official MCP Registry](https://registry.modelcontextprotocol.io) as `ai.getoneprofile/oneprofile`. The registry holds metadata only. Directories and MCP clients that read from it pick up the listing from there.

## Ownership

The `ai.getoneprofile` namespace is proven through DNS: a TXT record on the `getoneprofile.ai` apex, `v=MCPv1; k=ed25519; p=<public key>`, managed in Terraform (`terraform/mcp-registry.tf` in the Oneprofile monorepo). The matching Ed25519 private key is kept outside this repo. Never commit it.

## Publish a new version

1. Raise `version` in `server.json`. The registry rejects a version it already has.
2. Check the file: `mcp-publisher validate`.
3. Sign in with the private key, then publish from this folder:

   ```sh
   PRIVATE_KEY="$(openssl pkey -in /path/to/mcp-registry-key.pem -noout -text | grep -A3 'priv:' | tail -n +2 | tr -d ' :\n')"
   mcp-publisher login dns --domain getoneprofile.ai --private-key "$PRIVATE_KEY"
   mcp-publisher publish
   ```

4. Confirm it: `curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=ai.getoneprofile/oneprofile"`.

Install the CLI with `brew install mcp-publisher`. Publishing guides are at [modelcontextprotocol.io/registry](https://modelcontextprotocol.io/registry/quickstart).

## Support

[docs.getoneprofile.ai](https://docs.getoneprofile.ai) · support@getoneprofile.ai
