# Oneprofile listing copy

The one source for every listing in this repo: Claude (`claude/`), ChatGPT (`chatgpt/`), Cursor (`cursor/`, `.cursor-plugin/`), Microsoft 365 Copilot (`microsoft/`) and the MCP Registry (`registry/`). Change the wording here first, then copy it into each package and raise every package's version together.

## Name

Oneprofile. Always one word, lower-case "p".

## Tagline (28 characters, fits ChatGPT's 30)

Find, enrich and reach leads

Used as the ChatGPT short description (shown as the subtitle).

## Short description (96 characters, fits the Registry's 100)

Find prospects, research them, and run email and LinkedIn outreach in your Oneprofile workspace.

Used for the Claude, Cursor and ChatGPT `description` fields, the Cursor marketplace entry and the Registry.

## Short description for Microsoft (68 characters, fits the manifest's 80)

Find, enrich and reach the right people in your Oneprofile workspace

## Long description

Replace `[App]` with Claude, ChatGPT, Copilot or Cursor's agent, and `[package]` with plugin or connector.

> Oneprofile is a go-to-market workspace: you build lists of companies and people, fill them in with researched facts, and write to the ones worth writing to, by email and LinkedIn. This [package] lets [App] do that work in your Oneprofile workspace from a conversation.
>
> What you can ask for:
> - Set up your first sequence from your company website: Oneprofile suggests who to reach, finds up to 100 people, writes to as many as your credits cover, and starts sending once you connect your Google account.
> - Find people or companies by title, seniority, industry, size, location, technology or funding, or find companies that look like your best customers. Most searches are counted for free before anything is saved.
> - Save the matches to a table, or bring in a pasted list, a file or records from a connected CRM such as HubSpot, Salesforce, Pipedrive or Attio, and send results back to your CRM or out as CSV.
> - Fill in work emails, phone numbers and company details, or research each row with AI: fit against your ideal customer, company and person research, and personalized openers.
> - Build an email and LinkedIn sequence for a table, preview the messages it will send, and clear what blocks its launch.
> - Work through replies: summarize what came in, label conversations, and draft answers.
> - Report how your outreach is doing, including replies, positive replies, bounces and credits left.
>
> How it works: [App] acts as you, in the one Oneprofile workspace you pick when you sign in, with the everyday tools of the AI Assistant inside Oneprofile. Each tool does one job and says whether it only looks things up, changes your workspace, or can send to people or remove something, so you can approve each one on its own. Actions that spend your workspace's Oneprofile credits say the price they ran at, and Oneprofile asks [App] to tell you the price and wait for your go-ahead before spending.
>
> Requirements: You need a Oneprofile account. A read-only connection can look things up; making changes spends your workspace's credits, and every new workspace starts with the free plan's 200 a month. Email sends from a connected Google Workspace mailbox, and LinkedIn steps run in your browser through the Oneprofile extension.

ChatGPT variant: OpenAI's metadata check asks listings to leave out pricing and plan offers. In the ChatGPT copy, the first bullet ends "Most searches are counted before anything is saved.", the reporting bullet ends "including replies, positive replies and bounces.", the credits sentence at the end of "How it works" is left out, capability 8 reads "Report on outreach results", and the requirements paragraph reads:

> Requirements: You need a Oneprofile account. When you connect, choose read only to let ChatGPT look things up without changing anything, or read and write. Email sends from a connected Google Workspace mailbox, and LinkedIn steps run in your browser through the Oneprofile extension.

## Capabilities

1. Set up your first sequence from your website
2. Find people and companies that match your ideal customer
3. Save search results, pasted lists, files or CRM records to a table
4. Fill in work emails, phone numbers and company details
5. Research and score accounts with AI
6. Build email and LinkedIn sequences and clear their launch checks
7. Summarize, label and draft answers to replies
8. Report on outreach results and credits left

## Starter prompts

General:

- Set up my first sequence from my website.
- Find heads of RevOps at Series B fintech companies in London.
- Find work emails for the people in my newest table.
- What replies came in this week, and who is interested?

One per skill:

| Skill | Display name | Prompt |
| --- | --- | --- |
| `set-up-your-first-sequence` | Set up your first sequence | Set up my first sequence from my website. |
| `find-leads` | Find leads | Find heads of RevOps at Series B fintech companies in London. |
| `import-and-export` | Import and export | Turn this list of companies into a Oneprofile table. |
| `enrich-a-table` | Enrich a table | Find work emails for the people in my newest table. |
| `launch-a-sequence` | Launch a sequence | Build an email sequence to my UK fintech table. |
| `triage-replies` | Triage replies | What replies came in this week, and who is interested? |
| `outreach-review` | Outreach review | How are my sequences doing this month? |

The skill descriptions live in each skill's `SKILL.md` front matter and are the same on every platform. The skill bodies are written once in `shared/skills/` and built into each package with `python3 shared/build.py` (`--check` fails when one is out of date or names a tool no app is listed). Never edit a package's `SKILL.md` by hand.

## Microsoft extras

The Microsoft manifest has two fields the other listings don't.

Features (`description.features`):

| Title | Description |
| --- | --- |
| Find and save leads | Search people and companies by title, industry, size or location, or find similar companies. Most count free first. |
| Enrich and research | Fill in work emails, phone numbers and company details, or research and score each account with AI. |
| Run outreach and work replies | Build email and LinkedIn sequences, clear their launch checks, and summarize, label and answer replies. |

Connector description (`agentConnectors[0].description`):

> Oneprofile's MCP server: lead search, enrichment and AI research, tables, email and LinkedIn sequences, the reply inbox and outreach reporting, acting as the signed-in person in the one Oneprofile workspace they pick. Each tool does one job and says whether it only reads, changes the workspace, or can send or remove something.

`microsoft/mcptools.json` is the server's `tools/list` answer for a read and write connection. Refresh it whenever the server's tools change.

## Keywords

sales, prospecting, lead-generation, enrichment, outreach, cold-email, crm, go-to-market

Cursor also adds `oneprofile` and `mcp`, for its marketplace search.

## Categories

| Platform | Category |
| --- | --- |
| ChatGPT | Business & Operations |
| Cursor | integrations |
| Microsoft (Partner Center) | Sales |

## Links

| Field | URL |
| --- | --- |
| Homepage, website | https://www.getoneprofile.ai |
| Documentation | https://docs.getoneprofile.ai/integrations/ai-apps |
| Support URL | https://docs.getoneprofile.ai |
| Support email | support@getoneprofile.ai |
| Privacy policy | https://www.getoneprofile.ai/privacy-policy |
| Terms of service | https://www.getoneprofile.ai/terms |
| Security | https://www.getoneprofile.ai/security |
| Repository | https://github.com/getoneprofile/connectors |
| MCP server | https://api.getoneprofile.ai/mcp |

## Writing rules

- Say "each tool does one job", never "doors", "runner tools" or "any tool by name".
- Say "changes where a payout goes", not "moves money".
- No em dashes, en dashes or spaced hyphens used as dashes.
- Don't promise that nothing happens without confirmation. Say each kind of tool can be approved on its own, and that the skills ask before launching, sending or deleting.
