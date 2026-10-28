# Legal Grounding for Dispute & Negotiation Letters

Reference citations to use in letters and to sanity-check that a letter has a real legal
basis. This is not legal advice; the business owner is responsible for compliance with
federal and state law, including engaging their own counsel.

## FCRA (Fair Credit Reporting Act), 15 U.S.C. §1681 et seq.

- **§611 (1681i) — Dispute investigation.** A consumer may dispute inaccurate or
  incomplete information directly with the bureau. The bureau must investigate within
  30 days (45 if the consumer supplies more information during the window) and remove
  or correct anything it cannot verify as accurate.
- **§609 (1681g) — Disclosure to consumers.** Basis for requesting the bureau's full
  file and the sources it used.
- **§623 (1681s-2) — Furnisher responsibilities.** Furnishers (the original creditor
  or collector that reported the item) have their own duty to investigate once notified
  of a dispute by the bureau, and may not re-report an item without noting it as
  disputed. Use this citation in letters sent to the furnisher/creditor itself, not just
  the bureau.

## FDCPA (Fair Debt Collection Practices Act), 15 U.S.C. §1692 et seq.

- **§809 (1692g) — Validation of debts.** Within 30 days of a debt collector's initial
  communication, a consumer can demand validation (proof the debt is owed, to whom, and
  the amount). Use for debt-validation letters to collection agencies — this is a
  distinct letter type from a bureau dispute and should cite §1692g, not §1681i.
- **§805 (1692c) — Communication restrictions.** Relevant if a client wants
  communications with a collector to go only through the business, or stopped
  entirely (cease-and-desist), and in hardship-based goodwill asks.

## CROA (Credit Repair Organizations Act), 15 U.S.C. §1679 et seq.

Applies to businesses that sell credit-repair services to consumers for a fee — i.e.
most users of this plugin. Before drafting a `CLIENT_COMPLETION` or engagement-adjacent
message, confirm the business's own paperwork satisfies CROA; this plugin does not
generate the CROA contract itself, but the completion email should not contradict it.
Key points to never contradict in generated copy:

- **No fees before services are fully performed** (§1679b(b)). Follow-up/status copy
  should describe work actually completed, never imply payment was collected for
  services that were promised but not yet performed.
- **3-day right to cancel** (§1679e). Any client-facing contract reference should not
  imply the cancellation window has closed sooner than 3 business days after signing.
- **No guaranteed outcomes.** Never state or imply a specific credit-score increase, a
  guaranteed removal, or a guaranteed timeline. Use "may," "requested," "disputed" —
  never "will be removed" or "will raise your score."
- Many states have their own Credit Services Organization Act with additional bonding,
  licensing, or disclosure requirements (surety bond, registration, specific contract
  language) that are stricter than federal CROA. The business owner should confirm
  their state's requirements; this skill does not track state-by-state variance.

## What NOT to generate

- A dispute letter for an item the client has confirmed is accurate, filed solely to
  exploit the 30-day investigation window ("dispute everything" / "stall tactic"). This
  is the core mechanism behind illegal credit-repair schemes and exposes the business to
  FTC/CFPB action. Only draft a dispute when there is an articulable basis: factual
  inaccuracy, unverifiable information, outdated item past the 7-year (10-year for
  bankruptcy) reporting window, mixed file / identity error, or a procedural violation by
  the furnisher or bureau.
- Any letter built around a synthetic identity, a "CPN" (credit privacy/profile number)
  presented as an EIN-based alternative identity, or file segregation — these are
  consumer-fraud schemes, not legitimate dispute tools. Refuse and flag if a request
  points this direction.
- Language promising a specific score increase, guaranteed deletion, or a guaranteed
  timeline.
