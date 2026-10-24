# Oneprofile for Microsoft 365 Copilot

Oneprofile is a go-to-market workspace: you build lists of companies and people, fill them in with researched facts, and write to the ones worth writing to, by email and LinkedIn. This package submits Oneprofile's MCP server to Microsoft's MCP server certification. Once certified, the server is available in Microsoft 365 Copilot chat, Cowork, Copilot Studio and Azure Foundry, acting as the signed-in person in the one Oneprofile workspace they pick.

## Package layout

| Path | What it is |
| --- | --- |
| `manifest.json` | Microsoft 365 app manifest (schema 1.30) declaring the MCP server under `agentConnectors`, with its OAuth settings read from Azure Key Vault |
| `mcptools.json` | The server's `tools/list` answer for a read-and-write connection |
| `intro.md` | Public documentation: tools, sign-in, getting started, known issues and limitations |
| `color.png`, `outline.png` | Full-bleed color icon (192 px) and white-on-transparent outline icon (32 px) |

Build the upload ZIP from this folder with `KEY_VAULT_URI=https://<vault>.vault.azure.net/ ./build.sh`. `manifest.json` keeps a placeholder for the Key Vault URI, and the script fills it in only in the copy it packages. It refuses a non-ASCII character, checks the manifest against its schema, and writes `dist/oneprofile-microsoft-<version>.zip`.

## Data and safety

The package holds no secrets and runs no code. Everything Copilot does in Oneprofile goes through the MCP server to `api.getoneprofile.ai`, over HTTPS, signed in with the person's own Oneprofile account. Reads, changes, and sends or removals reach Oneprofile through separate tools, so each kind can be approved on its own. Oneprofile processes data under its [privacy policy](https://www.getoneprofile.ai/privacy-policy) and [terms](https://www.getoneprofile.ai/terms).

## Support

[AI apps guide](https://docs.getoneprofile.ai/integrations/ai-apps) · support@getoneprofile.ai

## License

MIT. See [LICENSE](LICENSE).
