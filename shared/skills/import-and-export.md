---
name: import-and-export
description: Move lists in and out of Oneprofile. Bring rows pasted into the chat, a CSV or spreadsheet, or contacts and companies from a connected tool such as a CRM (HubSpot, Salesforce, Pipedrive, Attio and others) into a Oneprofile table, and send a table's rows back to a CRM or out as CSV. Use when the user says import, upload, paste this list, bring in my contacts or accounts, sync from their CRM, push or export to their CRM, or download a table.
---

# Import and export

Get an existing list into a Oneprofile table so it can be researched and reached, and send the results back to where the team works. Importing costs no credits. Exporting to a CRM writes into the user's CRM, so preview it and confirm before running.

## The tools

Every tool named here is on the {{server}}'s list under its own name. Send each argument as its JSON type: `true`, never `"true"`. A job with no tool here is done in Oneprofile: say so, with the link an answer gave.

## Bring in rows from the chat or a file

`create_table` takes `name` and `csv_text`, up to **200 rows and 25 columns**. The first line holds the column names, and every column comes in as text.

1. Get the rows as CSV. If the user pasted a list, use it. {{attached}} it yourself and turn the rows you need into CSV text.
2. Tidy without changing meaning: trim spaces, drop fully empty rows, keep the user's own column names, and put quotes around any value that contains a comma.
3. Keep the columns that later steps need: name, job title, company, company domain or website, email, LinkedIn URL. If the file has more than 25 columns, keep those and tell the user what you left out.
4. Call `create_table` with a name in the user's words.
5. Check it with `get_table` and a few rows from `read_table_rows`, then say how many rows and columns landed.

**More than 200 rows**: `create_table` refuses them. Point the user to **Import from file** on the [Tables page](https://app.getoneprofile.ai/tables). It takes CSV and `.xlsx` up to 50 MB, with as many rows as your plan holds, and types each column. Offer to load the first 200 rows now if they want to try the workflow first. Don't split a list across several tables unless they ask.

## Bring in records from a connected tool

1. `list_connected_sources`: the tools this workspace has connected, and the objects each can import, such as contacts or companies.
2. If the tool the user means isn't connected, they connect it in Oneprofile under Connections. Continue once they say they have.
3. `preview_connected_records`: a few real rows from that object. Show them, because every tool means something different by "contact".
4. `create_table_from_connected_tool`. It costs no credits.
   - Match rows on the tool's own record ID. It never changes, so later refreshes update the right row. Matching on email adds a new row whenever someone edits the email in the tool.
   - Bring in everything, or set a row limit when the user only wants a sample.
   - Fields not given a column stay on each row and can become columns later, in Oneprofile.
5. How often the table refreshes is set on the table in Oneprofile.

## Send rows to a CRM

The export column alone sends nothing. Running it is what writes into the CRM.

1. `list_export_destinations`: the connected tools and objects a table can push to.
2. `add_export_column` with `match_on` and `field_mappings`. Say which object it writes, which fields, and whether it creates new records, updates matching ones, or both.
3. `preview_export_column`: a dry run that writes nothing. Show the user what would be created and what would be updated.
4. Only after the user agrees, run that column with `run_table_column`. Start with `scope: "first_n"` on a few rows, check them, then run the rest.
5. `get_export_column_summary`: report how many records were created, updated or failed.

## Download a table

`export_table_to_csv` returns the table as CSV text. {{give_csv}}

## Next steps

- Research or fill in the imported rows: the `enrich-a-table` skill
- Write to them: the `launch-a-sequence` skill
