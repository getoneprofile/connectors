# Oneprofile

Oneprofile is a go-to-market workspace: you build lists of companies and people, fill them in with researched facts, and write to the ones worth writing to, by email and LinkedIn. The Oneprofile MCP server lets Copilot do that work from a conversation. It finds leads, researches them, runs outreach and works through the replies, in your Oneprofile workspace.

## Publisher: Oneprofile

## Prerequisites

- A Oneprofile account. Sign up at [getoneprofile.ai](https://www.getoneprofile.ai).
- To send email, a Google Workspace mailbox connected in Oneprofile. Microsoft 365 / Outlook mailboxes are not supported yet.
- For LinkedIn steps, the Oneprofile browser extension, signed in to the sender's own LinkedIn account.

## Supported operations

The server acts as you, in the one Oneprofile workspace you pick when you sign in, with the everyday tools of the AI Assistant inside Oneprofile. Each tool does one job and says whether it only looks things up, changes the workspace, or can send, remove or overwrite something.

### Looks things up

| Tool | What it does |
| --- | --- |
| `find_people` | Count and sample people |
| `find_companies` | Count and sample companies |
| `list_enrichment_options` | List enrichment options |
| `find_similar_companies` | Count similar companies |
| `list_search_filters` | Read a search's filters |
| `list_tables` | List the tables |
| `get_table` | Read a table |
| `read_table_rows` | Read table rows |
| `list_table_views` | List the views |
| `list_table_runs` | Read the table runs |
| `list_enrichment_catalog` | Read the enrichment catalog |
| `get_sequence` | Read the sequence |
| `list_sequences` | List the sequences |
| `get_outreach_analytics` | Read the outreach numbers |
| `get_sequence_performance` | Read the sequence numbers |
| `read_sequence_steps` | Read the steps |
| `search_help` | Search the help |
| `get_pricing` | Check prices |
| `list_connected_sources` | List the connected sources |
| `preview_connected_records` | Preview a connected tool's records |
| `export_table_to_csv` | Export a table as CSV |
| `list_export_destinations` | List the export destinations |
| `preview_export_column` | Preview an export column |
| `get_export_column_summary` | Read an export column's pushes |
| `list_senders` | List the senders |
| `list_approval_queue` | Read Tasks |
| `get_approval_task` | Read a task |
| `read_inbox` | Read the inbox |
| `read_conversation` | Read a conversation |
| `list_reply_labels` | List the inbox labels |
| `get_credit_balance` | Check the credit balance |
| `get_business_context` | Read the business context |
| `list_reference_documents` | List the reference documents |
| `list_connections` | List the connections |
| `search_playbooks` | Check outreach guidance |
| `read_playbook` | Read outreach guidance |
| `get_first_sequence` | Read the first sequence |

### Changes the workspace

| Tool | What it does |
| --- | --- |
| `create_table_from_find_people` | Save found people to a table |
| `create_table_from_find_companies` | Save found companies to a table |
| `create_table_from_similar_companies` | Save similar companies to a table |
| `create_table` | Create a table |
| `add_table_column` | Add a column |
| `build_sequence` | Build a sequence |
| `pause_sequence` | Pause a sequence |
| `find_missing_emails` | Find missing work emails |
| `create_table_from_connected_tool` | Create a table from a connected tool |
| `add_export_column` | Add an export column |
| `draft_reply` | Draft a reply |
| `approve_first_sequence_emails` | Mark the first emails as good to send |
| `show_first_sequence_steps` | Write every step |

### Can send, remove or overwrite

| Tool | What it does |
| --- | --- |
| `edit_table_rows` | Edit rows |
| `update_table` | Update a table |
| `stop_table_runs` | Stop a table's runs |
| `run_table_column` | Run a column |
| `launch_sequence` | Launch a sequence |
| `resume_sequence` | Resume a sequence |
| `edit_sequence_steps` | Set or rewrite a sequence's steps |
| `add_contacts_to_sequence` | Add contacts to a sequence |
| `write_sequence_previews` | Preview every contact's messages |
| `send_test_email` | Send a test email |
| `approve_tasks` | Approve tasks |
| `reject_tasks` | Reject tasks |
| `rewrite_task_message` | Rewrite a task's message |
| `mark_conversations_done` | Mark conversations done, or take the mark off |
| `mark_do_not_contact` | Add a contact to Do not contact |
| `set_conversation_labels` | Set a conversation's labels |
| `revise_draft` | Revise a draft |
| `approve_and_send_draft` | Send a drafted reply |
| `update_business_context` | Update the business context |
| `write_business_context_from_website` | Write the business context from a website |
| `mark_needs_work` | Mark what an agent wrote as Needs work |
| `start_first_sequence` | Set up the first sequence |
| `pick_first_sequence_audience` | Pick the first sequence's audience |
| `remove_first_sequence_people` | Take people out of the first sequence |
| `reshape_first_sequence_audience` | Change the first sequence's region or company size |
| `choose_first_sequence_business_line` | Choose what the first sequence sells |
| `set_first_sequence_sender` | Sign the first sequence's emails |
| `edit_first_sequence_email` | Edit a first email |
| `give_first_sequence_feedback` | Give feedback on the first emails |

## Obtaining credentials

Sign-in is OAuth 2.1, using the authorization code flow with PKCE. When you connect Oneprofile, a Oneprofile sign-in page opens. Sign in with your Oneprofile account, pick the workspace Copilot should work in, and choose **Read and write** or **Read only**.

## Getting started

1. Add the Oneprofile connector to your agent, or turn it on where your organization makes it available.
2. Sign in when asked, pick a workspace and choose the access to give.
3. Ask in your own words, such as "find heads of RevOps at Series B fintech companies in London", "find work emails for the people in my newest table" or "what replies came in this week, and who is interested?".

Searching, counting search matches and reading your workspace are free. Creating a table from a search, running enrichment or research columns, and launching sequences spend Oneprofile credits from your workspace balance.

## Known issues and limitations

- Email sends only from a Google Workspace mailbox connected in Oneprofile. Microsoft 365 / Outlook mailboxes are not supported yet.
- LinkedIn steps run in the sender's own browser through the Oneprofile extension.
- A connection works in one workspace. To work in another, connect again and pick it.
- A connection that goes unused for 30 days signs out, and you sign in again.
- The connector covers the everyday jobs. The rest of Oneprofile is in the app.
- The tool list grows as Oneprofile adds features. The server's own `tools/list` answer is always current.
- Some tool descriptions are long, because they carry the guidance the model needs to use the tool well.
- Lead searches and enrichment cover business data only. Oneprofile does not look up home addresses or private individuals.

## Frequently asked questions

### What does it cost?

The connector is free. Actions that spend credits use the credits your Oneprofile workspace already holds, and every priced change comes back with the price it ran at. Most lookups that find nothing are not charged.

### How do I disconnect?

In Oneprofile, open **Settings > Connections > Claude & ChatGPT** and click **Disconnect** beside the connection, or remove the connector in Copilot.

### Where is my data processed?

Everything goes to `api.getoneprofile.ai` over HTTPS and is processed under Oneprofile's [privacy policy](https://www.getoneprofile.ai/privacy-policy) and [terms](https://www.getoneprofile.ai/terms).

## Support

- Documentation: [AI apps guide](https://docs.getoneprofile.ai/integrations/ai-apps)
- Email: support@getoneprofile.ai
- Security: [getoneprofile.ai/security](https://www.getoneprofile.ai/security)
