---
name: find-leads
description: Find people or companies who match a description and save them to a Oneprofile table. Use when the user asks to find leads, prospects, accounts or contacts, build a prospect or target list, search by job title, seniority, department, industry, company size, location, technology or funding, or find companies similar to ones they already sell to.
---

# Find leads

Turn a description of who the user sells to into a counted search, then into a table they own. Counting matches is free and landing rows costs credits, so shape the search first and spend once.

## The tools

Every tool named here is on the {{server}}'s list under its own name. Send each argument as its JSON type: `true`, never `"true"`. A job with no tool here is done in Oneprofile: say so, with the link an answer gave.

Each search is two tools: one that counts and samples for free, and one that saves what it found to a new table.

## 1. Read the workspace first

Call `get_business_context` and `list_reference_documents`. Use what they say about the product, the market and the ideal customer to fill gaps in the request instead of asking.

Ask one question only when the request could mean two different searches and the context does not settle it, such as Apple the employer against Apple as a keyword.

When the user wants advice on who to target rather than a specific search, call `search_playbooks` and then `read_playbook` on what fits (for example `oneprofile-lead-finders`) before you answer.

## 2. Pick the search

| The user wants | Count for free | Save to a table |
| --- | --- | --- |
| People by title, seniority, department, place, employer or past roles | `find_people` | `create_table_from_find_people` |
| Companies by industry, headcount, location, technology, funding or a new executive | `find_companies` | `create_table_from_find_companies` |
| Companies like up to ten domains they name | `find_similar_companies` | `create_table_from_similar_companies` |

To see every filter a search accepts, call `list_search_filters` with that search. Other searches (open roles, local businesses, buying signals, social posts) are on the Find leads page in Oneprofile: tell the user they run there.

## 3. Count for free

Call the search. It answers with the number of matches and a sample of up to five rows. The sample is a preview, not the result.

- Tell the user the count and what the sample looks like (titles, companies, places).
- If the count is far too large or too small, say which filter you would tighten or loosen, then count again. Counting again is still free.
- If nothing matches, say so and offer to widen a filter. Never create a table to stand in for a search that found nobody.

Similar companies cost 5 credits a row and have no sample.

## 4. Choose what to fill in

Call `list_enrichment_options` for the search. It gives the price per row of each detail Oneprofile can fill in, whether it is available, and whether the table would already cover it.

- Never propose an option marked not available or already covered.
- If the user named what they want, use exactly that.
- If they named nothing, choose yourself without asking: `find_email` when the list is for outreach, otherwise the cheapest option that fits the goal.

## 5. Quote, then land the table

Before you spend, tell the user in a few lines:

- how many rows you will add (`row_limit`)
- what will be filled in
- the most it can cost: the rows times the per-row price. Call `get_pricing` if you need a price you don't have, and `get_credit_balance` when the total is large

Wait for a go-ahead unless the user already told you to go ahead and spend.

Then call the saving tool beside that search with exactly the same filters, plus `table_name`, `row_limit` and `enrichments`. Using the same filters keeps the rows in line with the count the user approved.

- People already in one of the workspace's tables are skipped. Set `include_known_people` only when the user asks for them.

## 6. Report

The answer to a saving call starts with its price line and ends with an "Open in Oneprofile" link. Pass both on. Then say:

- the table's name, as a link
- how many rows are being added, and how many people were skipped because they were already in the workspace
- what is filling in, and that it runs in the background

Do not report enrichment values from the saving call. Rows and details keep arriving after it returns. To check on them, read the table later with `read_table_rows`.

A people table has no company size or revenue column, even when those were filters. Say so when they were, and offer to add company details with the `enrich-a-table` skill.

### Example

> Found 1,240 heads of RevOps at Series A and B fintech companies in the UK. The sample has Heads of Revenue Operations at Northwind Pay, Ledgerly and Fernbank.
>
> To save the first 300 with work emails: up to [300 × the per-row price from `list_enrichment_options`] credits, charged only for the emails found. Shall I go ahead?

After the user agrees:

> Price: [the price line the tool returned].
>
> Created **UK fintech RevOps** with 300 people (12 skipped, already in your tables). Work emails are filling in now. [Open in Oneprofile](…)
>
> Next I can score each company against your ideal customer, or build a sequence to them.

## Next steps

- Research, scoring or more details on the new rows: the `enrich-a-table` skill
- Outreach to the list: the `launch-a-sequence` skill
