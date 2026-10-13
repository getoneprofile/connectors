# Oneprofile for Microsoft 365 Copilot

Oneprofile is a go-to-market workspace: you build lists of companies and people, fill them in with researched facts, and write to the ones worth writing to, by email and LinkedIn. This package submits Oneprofile's MCP server to Microsoft's MCP server certification. Once certified, the server is available in Microsoft 365 Copilot chat, Cowork, Copilot Studio and Azure Foundry, acting as the signed-in person in the one Oneprofile workspace they pick.

## Package layout

| Path | What it is |
| --- | --- |
| `manifest.json` | Microsoft 365 app manifest (schema 1.30) declaring the MCP server under `agentConnectors`, with its OAuth settings read from Azure Key Vault |
| `mcptools.json` | The server's `tools/list` answer for a read-and-write connection |
| `intro.md` | Public documentation: tools, sign-in, getting started, known issues and limitations |
| `color.png`, `outline.png` | Full-bleed color icon (192 px) and white-on-transparent outline icon (32 px) |

Build the upload ZIP from this folder with `./build.sh`. It refuses to build while the manifest still has a placeholder or a non-ASCII character, checks the manifest against its schema, and writes `dist/oneprofile-microsoft-<version>.zip`.

## Before you upload

Microsoft's certification signs in through a fixed OAuth client and doesn't support Dynamic Client Registration, so the package needs three things in place first.

1. **A Partner Center account** with business verification done and the **Microsoft 365 and Copilot** program joined. The offer type is **Apps and Agents for M365 and Copilot**.
2. **An OAuth client for Microsoft.** Register a confidential client at `https://api.getoneprofile.ai/oauth/register` with `token_endpoint_auth_method` set to `client_secret_post` and Microsoft's redirect addresses. Keep the `client_id` and `client_secret` it returns.
3. **An Azure Key Vault** holding these secrets, with names exactly as written:

   | Secret | Value |
   | --- | --- |
   | `ClientId` | The client's `client_id` |
   | `ClientSecret` | The client's `client_secret` |
   | `AuthorizationUrl` | `https://api.getoneprofile.ai/oauth/authorize` |
   | `TokenUrl` | `https://api.getoneprofile.ai/oauth/token` |
   | `RefreshUrl` | `https://api.getoneprofile.ai/oauth/token` |
   | `Scopes` | `mcp` |

   Give the service principal of Microsoft application `8e91e74f-afe9-41cd-8c3f-17a9562a74ea` the **Key Vault Secrets User** role on the vault, then put the vault's URI (`https://<vault>.vault.azure.net/`) in `manifest.json` in place of the placeholder.

## Updating

Raise `version` in `manifest.json` and refresh `mcptools.json` from the server's `tools/list` whenever tools are added or their descriptions change, then rebuild and resubmit. Microsoft certifies the package as submitted.

## Data and safety

The package holds no secrets and runs no code. Everything Copilot does in Oneprofile goes through the MCP server to `api.getoneprofile.ai`, over HTTPS, signed in with the person's own Oneprofile account. Reads, changes, and sends or removals reach Oneprofile through separate tools, so each kind can be approved on its own. Oneprofile processes data under its [privacy policy](https://www.getoneprofile.ai/privacy-policy) and [terms](https://www.getoneprofile.ai/terms).

## Support

[docs.getoneprofile.ai](https://docs.getoneprofile.ai) · support@getoneprofile.ai

## License

MIT. See [LICENSE](LICENSE).
