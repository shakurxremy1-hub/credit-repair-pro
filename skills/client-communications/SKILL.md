---
name: client-communications
description: This skill should be used when the user asks to "send the dispute letters", "email the bureau/creditor", "notify the client", "send a completion email", "email Jane the dispute packet", or needs to actually send any dispute PDF, negotiation letter, or client status update by email.
---

# Client Communications

## Purpose

Send the PDFs produced by `dispute-letter-generator` — and client status updates — by
email through the business's own SMTP account, with a mandatory dry-run confirmation
step before anything actually goes out.

## When to Use

Use after a dispute/validation/goodwill/negotiation letter PDF already exists and needs
to reach its recipient, or when a client needs a status/completion notification. Do not
use this skill to email a bureau a formal dispute — bureaus generally require mail, not
email (see `dispute-letter-generator/references/bureau-contacts.md`); this skill is for
the client's own copy, creditors/collectors who accept email correspondence, and status
updates.

## Required Input

1. **Recipient email(s)** — client, or a creditor/collector email the business owner
   has confirmed accepts correspondence that way. Never guess or search for a bureau
   "dispute email" — none of the three bureaus publish one for general use.
2. **Message type** — dispute-packet copy, negotiation/validation cover note, or
   completion notification. See `references/email-templates.md` for the subject-line and
   body conventions for each.
3. **Attachments** — the PDF(s) from `dispute-letter-generator`, if any.
4. **`config.yml`** at the plugin root — must exist with real SMTP credentials (copy
   from `config.example.yml` if missing; never fabricate credentials).

## Instructions

1. **Pick the message type** and pull the subject/body conventions from
   `references/email-templates.md` — in particular the CROA-safe language rules, which
   apply to every client-facing message without exception.
2. **Draft the email body** to a plain text file. Keep it factual: what was done, what
   happens next, no guaranteed outcomes, no implication that unpaid-for work is
   underway.
3. **Always compose with `--dry-run` first**:
   ```
   python scripts/send_email.py --config <path-to-config.yml> --to <email> \
     --subject "<subject>" --body <body.txt> --attach <file.pdf> --dry-run
   ```
   Show the business owner the exact From/To/Subject/attachments/body before sending
   anything — this is an irreversible, externally-visible action (an email to a client
   or a third party), not a draft.
4. **Only re-run without `--dry-run` after explicit confirmation** from the business
   owner that the recipient, subject, and attachments are correct.
5. **Never CC or BCC** a recipient not explicitly named by the business owner.
6. **Log what was sent** (to whom, when, which attachment) in the conversation so the
   business owner has a record — this skill does not persist a send log to disk.

## Additional Resources

- **`references/email-templates.md`** — subject/body conventions per message type and the CROA-safe language rules
- **`scripts/send_email.py`** — SMTP sender with a `--dry-run` mode (requires `PyYAML`; stdlib `smtplib` otherwise)
