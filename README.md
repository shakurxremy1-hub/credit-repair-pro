# credit-repair-pro

> **Built for Credit Repair Business Owners** — Automate your client workflow: generate dispute letters as PDFs, send them via email, and notify clients when their case is complete. All powered by Claude.

---

## What Is credit-repair-pro?

**credit-repair-pro** is a Claude plugin designed specifically for **credit repair business owners and professionals**. It automates the most time-consuming parts of running a credit repair service — analyzing client credit reports, drafting dispute letters as ready-to-send PDFs, emailing those documents directly to credit bureaus and creditors, and sending your clients a professional update message once everything is done.

Stop doing it manually. Let Claude handle the workflow while you focus on growing your business.

---

## Who Is This For?

- Credit repair business owners managing multiple clients
- Credit coaches and financial consultants
- Paralegals and consumer law professionals
- Anyone running a credit repair service who wants to automate client workflows

---

## Core Business Features

### 📄 PDF Dispute Letter Generation
Claude automatically drafts customized dispute letters for each client based on their credit report errors and exports them as **professional, ready-to-send PDF documents**. Each PDF includes:
- Client name and contact info
- Bureau-specific formatting (Experian, Equifax, TransUnion)
- Supporting argument language based on FCRA / FDCPA law
- Date, signature line, and reference numbers

### 📧 Automated Email Sending
Once dispute letters are drafted, credit-repair-pro sends them automatically:
- Emails dispute PDFs directly to the correct credit bureau(s)
- Emails creditors and collection agencies with negotiation letters
- Sends a copy to your client for their records
- Supports custom sender name and business email branding

### 💬 Client Completion Notifications
When a client's dispute round is complete, Claude automatically sends them a **professional status message** via email (or SMS if configured), letting them know:
- Which items were disputed and with which bureaus
- What to expect next and the timeline
- Any action they need to take on their end
- A summary of their dispute packet (PDF attached)

---

## Installation

This is a [Claude Code](https://claude.com/claude-code) plugin — it runs locally through
the Claude Code CLI, not through claude.ai's web Integrations panel.

### Requirements
- [Claude Code](https://claude.com/claude-code) installed
- Python 3.9+ with `pip install -r skills/dispute-letter-generator/scripts/requirements.txt -r skills/client-communications/scripts/requirements.txt`
  (or a venv — recommended)
- SMTP email credentials (Gmail/Outlook app password, or custom business email) for
  sending automated emails

### Steps to Install

1. **Clone this repo** (or add it as a plugin source):
   ```
   git clone https://github.com/nmdzaza/credit-repair-pro.git
   ```
2. **Install it as a local plugin** — from within Claude Code:
   ```
   /plugin marketplace add /path/to/credit-repair-pro
   /plugin install credit-repair-pro
   ```
   (or run Claude Code with `--plugin-dir /path/to/credit-repair-pro` while developing)
3. **Configure your business settings**
   - Copy `config.example.yml` to `config.yml` at the repo root
   - Fill in your business name/address, SMTP credentials, and (optionally) a logo path
   - `config.yml` is gitignored — it holds real credentials and must never be committed
4. **Install the Python dependencies** listed above into whatever Python environment
   Claude Code will invoke the skill scripts with.
5. **Use it** — once enabled, Claude Code loads `dispute-letter-generator` and
   `client-communications` automatically when a matching request comes in (see
   **How to Use** below).

---

## How to Use credit-repair-pro (Business Workflow)

### Step 1 — Add a Client
```
"Add a new client: [Client Name], email: [client@email.com]"
```
Claude creates a client profile and stores their information for the session.

---

### Step 2 — Upload or Paste the Client's Credit Report
```
"Here is my client's credit report: [paste report text or upload file]"
```
Claude analyzes the report from all three bureaus and identifies all disputable items — late payments, collections, errors, outdated accounts, and more.

---

### Step 3 — Generate Dispute Letters as PDFs
```
"Draft dispute letters for all errors found and export them as PDFs"
```
Claude creates bureau-specific dispute letters for each error, formatted professionally and exported as PDF files ready for sending.

---

### Step 4 — Mail the Bureau Copy, Email the Rest
```
"Send the dispute letters to the appropriate credit bureaus and creditors"
```
Bureaus process disputes by mail (ideally certified, for a timestamped FCRA §611 clock), not email — none of the three publish a general dispute inbox. Claude prepares the bureau PDFs for you to print and mail, and emails anything that *does* go by email: creditor/collector correspondence that accepts it, and the client's own copy — using your business email as the sender.

---

### Step 5 — Follow Up on Open Disputes
```
"Check follow-up status for [Client Name] and send reminder letters if needed"
```
Bureaus have **30 days** to respond. Claude tracks timelines and automatically drafts follow-up letters for any disputes that haven't received a response.

---

### Step 6 — Negotiate with Creditors on Behalf of Client
```
"Draft a pay-for-delete letter to [Creditor Name] for [Client Name]"
```
Claude drafts goodwill letters, pay-for-delete requests, and debt validation letters as PDFs and emails them directly to creditors.

---

### Step 7 — Notify the Client When Complete
```
"Send [Client Name] a completion message summarizing what was done"
```
Claude sends your client a **professional completion notification email** that includes:
- A full summary of all disputes filed
- The attached PDF dispute packet
- Next steps and expected timeline
- Your business contact info for follow-up questions

---

### Step 8 — Build Client's Credit Going Forward
```
"Give [Client Name] a personalized credit-building plan"
```
Claude creates a tailored plan covering secured cards, credit-builder loans, utilization targets, and payment scheduling — which can also be emailed to the client as a PDF guide.

---

## Example Business Commands

| What You Want | What to Say to Claude |
|---|---|
| Add a new client | "Add client: Jane Doe, jane@email.com" |
| Analyze credit report | "Analyze this credit report and find all disputable items" |
| Generate all dispute PDFs | "Draft dispute letters for all errors and export as PDFs" |
| Prep bureau mailings | "Generate dispute PDFs for all three credit bureaus" |
| Email creditor | "Send a pay-for-delete letter to Capital One for Jane" |
| Notify client | "Send Jane a completion email with the dispute summary" |
| Follow up | "Send follow-up letters for any disputes older than 30 days" |
| Build credit plan | "Email Jane a personalized credit-building plan as a PDF" |

---

## Email & PDF Configuration

Copy `config.example.yml` to `config.yml` at the repo root and fill it in — business
letterhead info, SMTP credentials, and the (usually blank, by design) bureau
dispute-email fields. `config.yml` is gitignored; never commit it.

```yaml
business:
  name: "Your Credit Repair Business LLC"
  contact_email: "you@yourbusiness.com"
  phone: "(555) 555-5555"
  address: "123 Main St, Suite 100, Your City, ST 00000"
  logo_path: ""

smtp:
  host: "smtp.gmail.com"
  port: 587
  username: "you@yourbusiness.com"
  password: "your_app_password"
  use_tls: true
  from_name: "Your Credit Repair Business LLC"
  from_email: "you@yourbusiness.com"
```

See `skills/dispute-letter-generator/SKILL.md` and
`skills/client-communications/SKILL.md` for how each piece gets used.

---

## Disclaimer

credit-repair-pro is an informational and automation tool for business use. It is **not**
a substitute for professional legal advice. All dispute letters are based on publicly
available consumer protection laws (FCRA, FDCPA) — see
`skills/dispute-letter-generator/references/legal-citations.md` for the specific
citations used and what the tool refuses to generate (disputes against confirmed-accurate
information, synthetic-identity/CPN schemes, guaranteed-outcome language). Credit-repair
businesses are generally subject to the federal Credit Repair Organizations Act (CROA)
and often a stricter state-level credit-services-organization law — business owners are
responsible for their own CROA/state compliance, reviewing every document before it goes
out, and their own licensing/bonding requirements. Results may vary per client.

---

## Project Structure

```
credit-repair-pro/
├── .claude-plugin/plugin.json          # Plugin manifest
├── config.example.yml                  # Copy to config.yml (gitignored) and fill in
├── skills/
│   ├── dispute-letter-generator/       # Draft letters, render to PDF
│   │   ├── SKILL.md
│   │   ├── scripts/generate_pdf.py
│   │   └── references/                # bureau-contacts, legal-citations, letter-playbook
│   └── client-communications/          # Send email (dry-run first, always)
│       ├── SKILL.md
│       ├── scripts/send_email.py
│       └── references/email-templates.md
```

---

## Contributing

Got ideas or improvements? Pull requests are welcome!

1. Fork this repository
2. Create your feature branch: `git checkout -b feature/my-improvement`
3. Commit your changes: `git commit -m "Add my improvement"`
4. Push to the branch: `git push origin feature/my-improvement`
5. Open a Pull Request

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Support

If this plugin is helping your business, please **star this repo** so other credit repair professionals can find it!
