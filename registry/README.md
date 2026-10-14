# Oneprofile in the MCP Registry

`server.json` lists Oneprofile's remote MCP server, `https://api.getoneprofile.ai/mcp` (Streamable HTTP, signed in with OAuth), in the [official MCP Registry](https://registry.modelcontextprotocol.io) as `ai.getoneprofile/oneprofile`. The registry holds metadata only. Directories and MCP clients that read from it pick up the listing from there.

See the current listing with:

```sh
curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=ai.getoneprofile/oneprofile"
```

## Support

[docs.getoneprofile.ai](https://docs.getoneprofile.ai) · support@getoneprofile.ai
