# Oneprofile for Claude

Oneprofile is a go-to-market workspace: you build lists of companies and people, fill them in with researched facts, and write to the ones worth writing to, by email and LinkedIn. This plugin connects Claude to your Oneprofile workspace and teaches it the workflows that get good results there, so you can find leads, research them, run outreach and work your replies from a conversation.

It bundles two things:

- **The Oneprofile connector**, Oneprofile's remote MCP server at `https://api.getoneprofile.ai/mcp`. It gives Claude the same tools the AI Assistant inside Oneprofile has, acting as you, in the one workspace you pick when you sign in.
- **Six skills** that tell Claude when and how to use those tools: which step comes first, what is free and what costs credits, and what to confirm with you before anything is sent or removed.

## Skills

| Skill | Use it when you want to |
| --- | --- |
| `find-leads` | Turn a description of who you sell to into a counted search, then a table of people or companies |
| `import-and-export` | Bring a CSV, a pasted list or records from a connected tool such as your CRM into a table, and send results back to your CRM or out as CSV |
| `enrich-a-table` | Fill in work emails, phone numbers, company details or AI research on a table's rows |
| `launch-a-sequence` | Turn a table into an email and LinkedIn sequence and get it through its launch checks |
| `triage-replies` | Work through replies in the inbox: read, label, draft answers and send the ones you approve |
| `outreach-review` | Get a plain summary of how your sequences, replies, tables and credits are doing |

You don't need to name a skill. Ask in your own words, such as "find heads of RevOps at Series B fintechs in London", "get work emails for my Q4 list" or "what came in overnight?", and Claude picks the skill that fits.

## Set up

1. Install the plugin from the Claude directory.
2. Open the plugin's **Connectors** tab and connect **Oneprofile**. In Claude Code, run `/mcp`, choose the Oneprofile server and sign in from the browser tab it opens.
3. Sign in to Oneprofile, pick the workspace Claude should work in, and choose **Read and write** or **Read only**. Read only lets Claude look things up and never change them. Making changes from an AI app needs a paid Oneprofile plan.

Email steps send from a Google Workspace mailbox connected in Oneprofile, and LinkedIn steps run in your browser through the Oneprofile extension.

You need a Oneprofile account. Sign up at [getoneprofile.ai](https://www.getoneprofile.ai). Setup details for each app are in the [AI apps guide](https://docs.getoneprofile.ai/integrations/ai-apps).

## What it costs

Looking things up, counting search matches and reading your workspace are free. Creating a table from a search, running enrichment or research columns, and launching sequences spend Oneprofile credits from your workspace balance. The skills tell Claude to say what a step will cost before it spends, and every priced change Claude makes comes back with the price it ran at. A lookup that finds nothing is not charged.

## Safety and approvals

Claude works as you, so what it changes counts as your change. Oneprofile's tools come in three separate kinds: one that only reads, one that changes your workspace, and one for anything that sends to people outside your workspace, removes something or changes where a payout goes. Your app can ask before each kind, so you can let Claude look things up freely and still approve every send. The skills add their own rule on top: Claude never launches a sequence, sends a reply or deletes anything without your explicit go-ahead in the conversation.

## Data and privacy

The plugin itself stores nothing and runs no code. Its skills are instructions only. Everything Claude does in Oneprofile goes through the Oneprofile connector to `api.getoneprofile.ai`, over HTTPS, signed in with your own Oneprofile account through OAuth. What Claude sends there is what the task needs: search filters, table and column settings, rows from a file you ask it to import, message drafts and reply text. Oneprofile processes that data under its [privacy policy](https://www.getoneprofile.ai/privacy-policy) and [terms](https://www.getoneprofile.ai/terms). The plugin sends nothing to any other service.

To disconnect, open **Settings > AI apps** in Oneprofile and click **Disconnect** beside the connection, or remove the connector in Claude. A connection unused for 30 days signs out on its own.

## Support

- Documentation: [docs.getoneprofile.ai](https://docs.getoneprofile.ai)
- Email: support@getoneprofile.ai
- Security: [getoneprofile.ai/security](https://www.getoneprofile.ai/security)

## License

MIT. See [LICENSE](LICENSE).
