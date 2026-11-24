---
name: set-up-your-first-sequence
description: Set up a new workspace's first email and LinkedIn sequence from the company website, in the five steps of Oneprofile's setup page (research your company, choose who to reach, find people, review the messages, connect your mailbox). Use when the user has just connected Oneprofile or signed up, says they are new, asks how to get started, or asks to set up outreach from their website.
---

# Set up your first sequence

A new workspace (nothing launched yet) can have its first sequence set up from the company website, the same setup Oneprofile's own page at `/start` runs. The conversation and the page work on one setup: a link in any answer opens the page on the step it has reached, and what the person does there shows up here. So say each step the way the page says it, by its name, with the numbers the answers give.

## The tools

The first sequence tools are on the Oneprofile connector's list: `start_first_sequence`, `get_first_sequence`, `pick_first_sequence_audience`, `set_first_sequence_sender`, `give_first_sequence_feedback` and `approve_first_sequence_emails`. Each answer says which step the setup is at and gives the link to that step.

## The five steps

1. **Research your company.** Confirm the company website with the user, then call `start_first_sequence` with it as `domain`. Reading the website is free and takes about a minute; `get_first_sequence` with `wait` answers once the audiences are in. Called with no website while a setup is under way, it answers where that one stands.
2. **Choose who to reach.** Show the audiences as the answer lists them: three at a time, each with why these people, its Ideal customer profile, its Buyer persona and about how many people match. Ask which one. The answer's coverage line says how many the credits reach, for example "Your 200 credits research and write to 28 of them." Oneprofile finds up to 100 people; the credits decide how many are researched and written to, so use the number the answer gives. A pick researches and writes to the first 10 right away and spends about 40 credits: say so before `pick_first_sequence_audience` with the audience's number.
3. **Find people.** The people are found and researched. `get_first_sequence` with `wait` answers once the first messages are written.
4. **Review the messages.** Show the first emails as written, with their subjects. A change the user asks for goes to `give_first_sequence_feedback` in their own words; the email is written again and the agent keeps the lesson for the rest. When they say the messages look good, call `approve_first_sequence_emails`. If the answer says nobody signs the emails yet, ask for the user's name and title and call `set_first_sequence_sender`.
5. **Connect your mailbox.** No tool connects a mailbox. The link in the answer opens Connect your mailbox, where the user presses "Continue with Google and start sending", with the price on the button. That one press connects their Google account and starts the sequence: it sends to the people the credits cover, without asking first, and they can pause any time. Outlook is offered there only when the page says it is; otherwise the page takes their work email for its waitlist.

Until `get_first_sequence` says it is sending, it is not. Once it is, the same tool says whether it is sending, not sending yet or paused, as the sequence's own page does.

## Words

- What it builds is a **sequence**, who it goes to is an **audience**, the people it finds are **people**.
- Never promise 100 emails, 100 customers or free emails. The free plan has 200 credits a month; what they reach is the number the answer gives.
- There is no Launch button: the Connect your mailbox button starts sending.

## Switching the audience

`pick_first_sequence_audience` with `switch` finds new people for another audience and writes to 10 of them, for the price the answer gives. The people and messages of the audience picked before are removed, so confirm the switch first.
