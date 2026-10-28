---
name: dispute-letter-generator
description: This skill should be used when the user asks to "draft a dispute letter", "generate a dispute PDF", "analyze a credit report for errors", "write a debt validation letter", "draft a goodwill letter", "draft a pay-for-delete letter", "create a dispute packet", or needs a credit-bureau/creditor/collector letter exported as a professional PDF.
---

# Dispute Letter Generator

## Purpose

Turn a client's credit-report errors into a legally grounded dispute, validation,
goodwill, or negotiation letter, and render it as a signature-ready PDF. Covers the
seven letter types in `references/letter-playbook.md`: bureau dispute, furnisher
dispute, debt validation, goodwill adjustment, pay-for-delete, follow-up, and the
client-facing completion note (handed off to the `client-communications` skill for
sending).

## When to Use

Use whenever a credit-repair business owner has identified a specific disputable item
(inaccurate, unverifiable, outdated, or a procedural violation) and needs a letter
drafted and exported as a PDF to mail or hand to the client. Pairs with
`client-communications` for the email side (sending the resulting PDF to the client,
and sending validation/goodwill/negotiation letters to creditors who accept email).

## Required Input

1. **Letter type** — one of the seven in `references/letter-playbook.md`.
2. **Client identity** — name, mailing address, phone, email (for the letterhead and
   for the bureau/creditor to reach them back).
3. **The specific item(s)** — creditor/furnisher name, account identifier (whatever the
   client actually has — full account numbers should never be requested or stored),
   what's reported, and why it's wrong/unverifiable/outdated/violative. Never infer or
   invent this — if the business owner hasn't supplied it, ask, or insert
   `[CONFIRM: ...]` placeholders in the draft rather than guessing.
4. **Recipient** — which bureau (pull address from
   `references/bureau-contacts.md`) and/or which furnisher/collector (business owner
   supplies name + address).
5. **Supporting documents the client actually has** — ID copy, proof of address,
   statements, payoff letters — only list what's confirmed to exist.
6. **Business letterhead info** — read from `config.yml` at the plugin root (copy from
   `config.example.yml` if it doesn't exist yet; prompt the business owner to fill it in
   rather than inventing a business name, license number, or address).

## Instructions

1. **Identify the letter type and pull its rules** from
   `references/letter-playbook.md` — which citation applies (or none, for goodwill/
   pay-for-delete), who it's addressed to, and what must be established before drafting.
2. **Check the legal basis** against `references/legal-citations.md` before drafting.
   Refuse (and explain why) if the request is to dispute an item the client has
   confirmed is accurate purely to exploit the investigation window, or involves a
   synthetic identity / CPN scheme — these are consumer-fraud patterns, not legitimate
   dispute tools.
3. **Draft the body paragraphs** in plain, factual, first-person-as-the-client prose.
   State the specific item, the specific inaccuracy/basis, and the specific requested
   outcome. Never promise an outcome ("will be deleted") — use "requesting," "disputing,"
   "may." Never fabricate an account number, date, or dollar figure not supplied.
4. **Assemble the letter JSON** (see schema in
   `scripts/generate_pdf.py` docstring) — sender (client), date, recipient, reference
   number if any, subject line naming the letter type + citation, salutation, the drafted
   body_paragraphs, enclosures list, and signature_name.
5. **Render the PDF**:
   ```
   python scripts/generate_pdf.py --data <letter.json> --output <path>.pdf --config <path-to-config.yml>
   ```
   `config.yml` lives at the plugin root (`${CLAUDE_PLUGIN_ROOT}/config.yml`); if it
   doesn't exist yet, tell the business owner to copy `config.example.yml` and fill it
   in before continuing — do not fabricate business letterhead details.
6. **Show the business owner the drafted letter text before rendering** when the item's
   basis is anything other than a clear-cut, previously-confirmed inaccuracy — a human
   should sign off on the specific claim being made to a bureau or creditor.
7. **Hand off for sending.** This skill only drafts and renders; invoke
   `client-communications` to actually email anything, and default to recommending the
   bureau copy be mailed (ideally certified) per `references/bureau-contacts.md` rather
   than emailed, since bureaus generally don't process disputes by email.

## Additional Resources

- **`references/letter-playbook.md`** — the seven letter types, recipients, citations, required facts
- **`references/legal-citations.md`** — FCRA/FDCPA/CROA citations and what never to generate
- **`references/bureau-contacts.md`** — bureau mailing addresses and the mail-vs-email rule
- **`scripts/generate_pdf.py`** — renders a letter JSON file into a PDF (requires `reportlab`, `PyYAML` — see `scripts/requirements.txt`)
