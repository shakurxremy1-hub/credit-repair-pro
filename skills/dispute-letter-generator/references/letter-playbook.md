# Letter Type Playbook

Each letter type below maps to a `subject`, the right legal citation (see
`legal-citations.md`), who it goes to, and what `body_paragraphs` must establish before
generate_pdf.py is called. Never invent a fact (account number, date, dollar amount) the
client/business owner has not supplied — use an explicit placeholder like
`[CONFIRM: original creditor name]` instead.

## 1. Initial bureau dispute

- **To:** The bureau (Experian/Equifax/TransUnion) — see `bureau-contacts.md`.
- **Citation:** FCRA §611 (1681i).
- **Must establish:** which specific item (creditor name, account number — last 4 only
  if that's what the client has, reported status), why it's inaccurate/unverifiable/
  outdated, and what correction is requested (correct or delete).
- **Enclosures:** copy of photo ID, copy of proof of address, any supporting document
  (statement, autopay confirmation, payoff letter) — list only what the client actually
  has.

## 2. Furnisher/creditor dispute

- **To:** The original creditor or data furnisher directly (in addition to, not instead
  of, the bureau dispute).
- **Citation:** FCRA §623 (1681s-2).
- **Must establish:** same inaccuracy, framed as a notice to the furnisher of its own
  independent duty to investigate and correct what it reports.

## 3. Debt validation request

- **To:** A debt collector/collection agency, within 30 days of their first contact.
- **Citation:** FDCPA §809 (1692g).
- **Must establish:** request for proof of the debt (original creditor, amount, chain of
  assignment) — it is a request for evidence, not a dispute of accuracy. Do not combine
  with a bureau dispute letter; send as its own letter.

## 4. Goodwill adjustment request

- **To:** Original creditor (not a collector; the creditor must still hold the account
  or have furnished the original late-payment history).
- **Citation:** none — this is a discretionary request, not a legal demand. Do not cite
  FCRA/FDCPA; frame as an appeal based on an otherwise-good payment history and a
  specific, named circumstance (job loss, medical event, etc.) if the client has
  disclosed one.
- **Must establish:** account tenure/payment history, the specific late item, and a
  concrete, non-fabricated reason if one exists. If no reason was given, omit the
  "circumstance" paragraph rather than inventing one.

## 5. Pay-for-delete negotiation

- **To:** Collection agency currently holding the debt.
- **Citation:** none — a negotiated settlement offer, not a legal right.
- **Must establish:** the specific amount the client is offering/able to pay, and the
  explicit request that the account be deleted (not just marked "paid") from the credit
  file in exchange. Flag to the business owner: collectors are not required to agree,
  and some bureaus' current data-furnisher agreements discourage "delete" language —
  set client expectations accordingly rather than promising it will work.

## 6. Follow-up / missed-deadline letter

- **To:** Whoever received the original letter (bureau or furnisher) after the 30/45-day
  window under FCRA §611 has passed with no response.
- **Citation:** FCRA §611 (1681i), citing the specific date the original dispute was
  sent/received and the statutory deadline that has now passed.
- **Must establish:** date of original letter, confirmation it was received if known
  (certified mail receipt), and a restated request for the original correction.

## 7. Client completion / status notification

- Not a legal letter — an informational update to the client. See
  `client-communications` skill for the email template and CROA-safe language rules
  (no guaranteed outcomes, no implication that unpaid-for services are complete).
