# Oneprofile

Oneprofile is a go-to-market workspace: you build lists of companies and people, fill them in with researched facts, and write to the ones worth writing to, by email and LinkedIn. The Oneprofile MCP server lets Copilot do that work from a conversation. It finds leads, researches them, runs outreach and works through the replies, in your Oneprofile workspace.

## Publisher: Oneprofile

## Prerequisites

- A Oneprofile account. Sign up at [getoneprofile.ai](https://www.getoneprofile.ai).
- A workspace on a paid Oneprofile plan, to make changes. On any plan, a read-only connection can look things up.
- To send email, a Google Workspace mailbox connected in Oneprofile. Microsoft 365 / Outlook mailboxes are not supported yet.
- For LinkedIn steps, the Oneprofile browser extension, signed in to the sender's own LinkedIn account.

## Supported operations

The server acts as you, in the one Oneprofile workspace you pick when you sign in, with the same tools as the AI Assistant inside Oneprofile. It lists the everyday tools by name. The rest are reached through three runner tools, one for each kind of call, so a person can allow look-ups and still approve every send.

### Running any tool

| Tool | What it does |
| --- | --- |
| `run_read_tool` | Runs any Oneprofile tool that looks things up, by name. A call of another kind is refused with the runner to use. |
| `run_change_tool` | Runs any Oneprofile tool that changes the workspace, by name: creates, edits, runs and searches that save, and the reply drafts and previews it keeps. A priced call's answer says what it was priced at. |
| `run_send_or_remove_tool` | Runs a tool that sends to people outside the workspace, removes or overwrites something, changes where a payout goes, or loosens what waits for a person's approval. Only those. |
| `describe_tool` | Reads any tool in full: what it does, what it answers with, and every argument. |

### Tables and leads

| Tool | What it does |
| --- | --- |
| `list_tables` | Lists the workspace's tables, most recently changed first. |
| `get_table` | Reads one table: its columns, row count, folder, owner and settings. |
| `read_table_rows` | Reads a table's rows, filtered, sorted and searched. |
| `create_table` | Creates a table, empty or filled from pasted CSV. |
| `import_file_as_table` | Builds a table from a file attached in Oneprofile's own assistant chat. |
| `read_file` | Reads the rows of a file attached in Oneprofile's own assistant chat as CSV. |
| `update_table` | Renames a table or changes its description. |
| `add_table_column` | Adds a column: a plain column, a formula, an enrichment lookup or an AI research column. |
| `list_find_leads_tools` | Lists the lead searches: people, companies, local businesses, lookalikes and buying signals. |
| `list_enrichment_options` | Lists what can be found out about rows, and what each costs per row. |
| `list_table_tools`, `list_column_tools`, `list_table_sync_tools` | List the rest of what can be done to tables, columns, imports and exports. |
| `list_agent_tools`, `list_agent_learning_tools` | List the tools for saved research agents and for what they learn from feedback on their answers. |

### Outreach and replies

| Tool | What it does |
| --- | --- |
| `get_sequence` | Reads one sequence in full: its status, audience, senders, steps and launch checks. |
| `build_sequence` | Builds a draft sequence in one go: three emails, or three emails and a LinkedIn connection request. Other LinkedIn steps are added afterwards with `edit_sequence_steps`. |
| `write_sequence_previews` | Writes and shows the messages a sequence will send to up to ten contacts. |
| `read_inbox` | Reads the replies waiting in the shared inbox, as summaries. |
| `list_sequence_tools`, `list_message_tools`, `list_sender_tools`, `list_mailbox_tools`, `list_outbound_agent_tools` | List the tools for sequences, their wording, who they send as, the mailboxes they send through and the AI writer behind them. |
| `list_inbox_tools`, `list_task_tools` | List the tools for replies, for approvals waiting on a person, and for who may never be contacted. |

### Workspace

| Tool | What it does |
| --- | --- |
| `get_pricing` | Reads what things cost in credits, and the workspace's balance. |
| `search_help` | Looks up how something in Oneprofile works. |
| `search_playbooks`, `read_playbook` | Find and read maintained outreach guidance. |
| `list_billing_tools`, `list_context_tools`, `list_integration_tools`, `list_notification_tools`, `list_account_tools` | List the tools for credits, business context, connected tools, notifications, and onboarding, referrals and the affiliate program. |

## Obtaining credentials

Sign-in is OAuth 2.1, using the authorization code flow with PKCE. When you connect Oneprofile, a Oneprofile sign-in page opens. Sign in with your Oneprofile account, pick the workspace Copilot should work in, and choose **Read and write** or **Read only**.

## Getting started

1. Add the Oneprofile connector to your agent, or turn it on where your organization makes it available.
2. Sign in when asked, pick a workspace and choose the access to give.
3. Ask in your own words, such as "find heads of RevOps at Series B fintech companies in London", "find work emails for the people in my newest table" or "what replies came in this week, and who is interested?".

Searching, counting search matches and reading your workspace are free. Creating a table from a search, running enrichment or research columns, and launching sequences spend Oneprofile credits from your workspace balance.

## Known issues and limitations

- Making changes needs a Oneprofile workspace on a paid plan. On any other plan, every connection is read-only, whatever was chosen at sign-in.
- Email sends only from a Google Workspace mailbox connected in Oneprofile. Microsoft 365 / Outlook mailboxes are not supported yet.
- LinkedIn steps run in the sender's own browser through the Oneprofile extension.
- A connection works in one workspace. To work in another, connect again and pick it.
- A connection that goes unused for 30 days signs out, and you sign in again.
- Only the everyday tools are listed by name. Everything else, a few hundred tools, is reached through `run_read_tool`, `run_change_tool` or `run_send_or_remove_tool`, using the names the `list_..._tools` tools give and the arguments `describe_tool` gives.
- The tool list grows as Oneprofile adds features. The server's own `tools/list` answer is always current.
- Some tool descriptions are long, because they carry the guidance the model needs to use the tool well.
- Lead searches and enrichment cover business data only. Oneprofile does not look up home addresses or private individuals.

## Frequently asked questions

### What does it cost?

The connector is free. Actions that spend credits use the credits your Oneprofile workspace already holds, and every priced change comes back with the price it ran at. A lookup that finds nothing is not charged.

### How do I disconnect?

In Oneprofile, open **Settings > Connections > Claude & ChatGPT** and click **Disconnect** beside the connection, or remove the connector in Copilot.

### Where is my data processed?

Everything goes to `api.getoneprofile.ai` over HTTPS and is processed under Oneprofile's [privacy policy](https://www.getoneprofile.ai/privacy-policy) and [terms](https://www.getoneprofile.ai/terms).

## Support

- Documentation: [AI apps guide](https://docs.getoneprofile.ai/integrations/ai-apps)
- Email: support@getoneprofile.ai
- Security: [getoneprofile.ai/security](https://www.getoneprofile.ai/security)
