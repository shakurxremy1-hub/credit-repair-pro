#!/usr/bin/env python3
"""Render a dispute/negotiation letter (JSON) into a professional business-letter PDF.

Usage:
    python generate_pdf.py --data letter.json --output output.pdf [--config ../../../config.yml]

letter.json schema:
{
  "sender": {"name": "...", "address": "...", "phone": "...", "email": "..."},   # optional, falls back to config.yml business block
  "date": "October 28, 2026",
  "recipient": {"name": "...", "address": "..."},
  "reference_number": "Account #: ****1234",   # optional
  "subject": "Formal Dispute of Inaccurate Information",
  "salutation": "To Whom It May Concern:",
  "body_paragraphs": ["paragraph one...", "paragraph two..."],
  "enclosures": ["Copy of driver's license", "Copy of utility bill"],   # optional
  "signature_name": "Jane Doe"
}
"""
import argparse
import json
import sys
from pathlib import Path

import yaml
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.enums import TA_LEFT


def load_config(config_path):
    if config_path and Path(config_path).exists():
        with open(config_path) as f:
            return yaml.safe_load(f) or {}
    return {}


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="LetterBody", parent=styles["Normal"],
                               fontName="Helvetica", fontSize=11, leading=15,
                               spaceAfter=10, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="LetterSmall", parent=styles["Normal"],
                               fontName="Helvetica", fontSize=9, leading=12))
    styles.add(ParagraphStyle(name="LetterSubject", parent=styles["Normal"],
                               fontName="Helvetica-Bold", fontSize=11, leading=15,
                               spaceAfter=10))
    return styles


def render(data, config, output_path):
    styles = build_styles()
    business = config.get("business", {})
    sender = data.get("sender") or {
        "name": business.get("name", ""),
        "address": business.get("address", ""),
        "phone": business.get("phone", ""),
        "email": business.get("contact_email", ""),
    }

    doc = SimpleDocTemplate(
        str(output_path), pagesize=LETTER,
        topMargin=1 * inch, bottomMargin=1 * inch,
        leftMargin=1 * inch, rightMargin=1 * inch,
    )

    flow = []

    logo_path = business.get("logo_path")
    if logo_path and Path(logo_path).exists():
        flow.append(Image(logo_path, width=1.5 * inch, height=0.75 * inch))
        flow.append(Spacer(1, 12))

    sender_lines = [sender.get("name", ""), sender.get("address", ""),
                     sender.get("phone", ""), sender.get("email", "")]
    flow.append(Paragraph("<br/>".join(l for l in sender_lines if l), styles["LetterSmall"]))
    flow.append(Spacer(1, 18))

    flow.append(Paragraph(data.get("date", ""), styles["LetterBody"]))
    flow.append(Spacer(1, 6))

    recipient = data.get("recipient", {})
    recipient_lines = [recipient.get("name", ""), recipient.get("address", "")]
    flow.append(Paragraph("<br/>".join(l for l in recipient_lines if l), styles["LetterBody"]))

    if data.get("reference_number"):
        flow.append(Paragraph(data["reference_number"], styles["LetterBody"]))

    flow.append(Spacer(1, 6))

    if data.get("subject"):
        flow.append(Paragraph(f"RE: {data['subject']}", styles["LetterSubject"]))

    flow.append(Paragraph(data.get("salutation", "To Whom It May Concern:"), styles["LetterBody"]))

    for para in data.get("body_paragraphs", []):
        flow.append(Paragraph(para, styles["LetterBody"]))

    flow.append(Spacer(1, 18))
    flow.append(Paragraph("Sincerely,", styles["LetterBody"]))
    flow.append(Spacer(1, 24))
    flow.append(Paragraph(data.get("signature_name", sender.get("name", "")), styles["LetterBody"]))

    enclosures = data.get("enclosures") or []
    if enclosures:
        flow.append(Spacer(1, 12))
        enclosure_text = "Enclosures: " + "; ".join(enclosures)
        flow.append(Paragraph(enclosure_text, styles["LetterSmall"]))

    doc.build(flow)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", required=True, help="Path to letter JSON file")
    parser.add_argument("--output", required=True, help="Path to write the output PDF")
    parser.add_argument("--config", default=None, help="Path to config.yml (for business/letterhead defaults)")
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        print(f"error: data file not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    with open(data_path) as f:
        data = json.load(f)

    config = load_config(args.config)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    render(data, config, output_path)
    print(f"wrote {output_path}")


if __name__ == "__main__":
    main()
