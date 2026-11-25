---
name: launch-a-sequence
description: Turn a Oneprofile table into an email outreach sequence, show the messages it will send, clear its launch checks and launch it when the user says so. Use when the user asks to write a cold email campaign, set up outreach or follow-ups to a list, build, edit or tailor a sequence, change its steps, voice or goal, pick senders, preview messages, find out what blocks a launch, or launch, pause or resume a sequence.
---

# Launch a sequence

Build a draft sequence from a table, let the user judge real messages, clear what blocks it, and launch only when the user says to. A draft sends nothing. A launch reaches real people and cannot be undone.

## The tools

Every tool named here is on the Oneprofile connector's list under its own name. Send each argument as its JSON type: `true`, never `"true"`. A job with no tool here is done in Oneprofile: say so, with the link an answer gave.

`launch_sequence` and `resume_sequence` with `dry_run: true` only report what they would do.

## 1. Read the workspace

Call `get_business_context` and `list_reference_documents`. The sequence's writer uses them, and they answer most of what you would otherwise ask the user.

For a new sequence, or advice on cadence, openers or tone, call `search_playbooks` and then `read_playbook` on what fits (for example `oneprofile-outbound-agents`). Skip the playbooks when the user has fully specified the change they want, and make exactly that change.

## 2. Check the audience

Read the table with `get_table`. Email steps need an email column. Sequences from Claude send by email only: LinkedIn steps are added in Oneprofile itself. If many rows have no email, say how many, and offer to find them first (the `enrich-a-table` skill) or later with `find_missing_emails`.

To write to only part of a table, use a saved view (`list_table_views`) or specific rows.

## 3. Build the draft

Call `build_sequence` with:

- `name`: unique in the workspace
- `table_id`, and `view_id` when writing to only part of the table
- `goal` and `voice`, in the user's words
- `campaign`: leave it `none` unless the user asks for a campaign that introduces their company (`introduce_company`)
- `senders`: leave it empty when the workspace has one sender, since it is assigned for you, or to choose later. List them with `list_senders`.
- `steps`: leave it empty to keep the cadence every new sequence starts with: three emails the agent writes for each contact. Give steps only when the user specified the cadence, because what you give replaces the cadence whole.

To add condition branches, use `edit_sequence_steps` after it.

Building is free and sends nothing. Its answer says roughly what sending will cost.

## 4. Show real messages

In the same reply, call `write_sequence_previews` for a few contacts. It is free but has a daily cap. Show two or three previews as written, with each one's subject and body, so the user judges the actual writing and not a description of it.

Change what the user asks for:

- **What the writing says or how it sounds** ("too salesy", "shorter"): `mark_needs_work` on one contact, with the user's own words as the `reason`. It writes that contact's message again for free (up to 100 a day), and proposes what the agent should learn. The user keeps the lesson with **Looks good** on the sequence's Preview.
- **The steps themselves**: read them first with `get_sequence` or `read_sequence_steps`, then call `edit_sequence_steps` with the full list. Mark every step you keep with `keeps_step`, because a step left out is deleted.
- **The agent's goal, call to action or research**: these are changed in Oneprofile, on the sequence's AI writing tab.

When the user wants to see a message in a real inbox, `send_test_email` sends one step, rendered for one contact. With `to_address` empty it goes to the signed-in user. It costs no credits and enrols nobody.

## 5. Clear the launch checks

`get_sequence` with the sequence lists what blocks launch, such as no sender, no audience, a missing subject, or no business context. For each blocker:

- fix it with the matching tool when the user's request covers it, or
- tell the user exactly what to do, with the link the tool returned when one is needed in the app. Connecting a mailbox happens in Oneprofile.

`find_missing_emails` is optional and priced. Offer it with its price, and run it only on a yes.

## 6. Launch only on an explicit instruction

Launch only when the user has asked for it in so many words, such as "launch it" or "start sending". Approving the draft, liking the previews or saying "looks good" is not a launch instruction. Ask.

Right before launching, say in a few lines:

- who it reaches: the number of contacts, and how many are left out and why
- who it sends as
- the steps and their timing
- when the first messages go out
- what it costs

Then call `launch_sequence`. Pass on the price line and the link from its answer.

- **Pause**: `pause_sequence`. No confirmation needed when the user asks.
- **Resume**: `resume_sequence`. It sends again, so confirm first.

### Example

> **Ready to launch "UK fintech RevOps"**
> - Reaches 284 contacts. 16 are left out: 11 have no email, 5 are on your do-not-contact list
> - Sends as Maya Chen (2 mailboxes)
> - 3 emails: day 0, day 3, day 7, each written per contact
> - First emails go out today from 9:00, in each sender's own timezone
> - Up to [N] credits, from the launch check
>
> Say "launch" and I'll start it.

## Next steps

- Replies as they come in: the `triage-replies` skill
- How it is performing: the `outreach-review` skill
