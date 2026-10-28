#!/usr/bin/env python3
"""Send an email (optionally with attachments) via the SMTP account in config.yml.

Usage:
    python send_email.py --config ../../../config.yml --to recipient@example.com \
        --subject "Subject line" --body body.txt [--attach file1.pdf --attach file2.pdf] \
        [--cc other@example.com] [--dry-run]

--dry-run prints the fully composed message (recipients, subject, attachments) without
sending or touching the network. Always run with --dry-run first and show the result to
the business owner before sending to a bureau, creditor, or client.
"""
import argparse
import smtplib
import ssl
import sys
from email.message import EmailMessage
from pathlib import Path

import yaml


def load_smtp_config(config_path):
    path = Path(config_path)
    if not path.exists():
        print(f"error: config file not found: {path}\n"
              f"Copy config.example.yml to config.yml and fill in SMTP credentials first.",
              file=sys.stderr)
        sys.exit(1)
    with open(path) as f:
        config = yaml.safe_load(f) or {}
    smtp = config.get("smtp")
    if not smtp:
        print("error: config.yml has no 'smtp' section", file=sys.stderr)
        sys.exit(1)
    return smtp


def build_message(smtp_cfg, to_addrs, cc_addrs, subject, body_text, attachments):
    msg = EmailMessage()
    from_name = smtp_cfg.get("from_name", "")
    from_email = smtp_cfg.get("from_email") or smtp_cfg["username"]
    msg["From"] = f"{from_name} <{from_email}>" if from_name else from_email
    msg["To"] = ", ".join(to_addrs)
    if cc_addrs:
        msg["Cc"] = ", ".join(cc_addrs)
    msg["Subject"] = subject
    msg.set_content(body_text)

    for attachment_path in attachments:
        path = Path(attachment_path)
        if not path.exists():
            print(f"error: attachment not found: {path}", file=sys.stderr)
            sys.exit(1)
        data = path.read_bytes()
        maintype, subtype = ("application", "pdf") if path.suffix.lower() == ".pdf" else ("application", "octet-stream")
        msg.add_attachment(data, maintype=maintype, subtype=subtype, filename=path.name)

    return msg


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, help="Path to config.yml")
    parser.add_argument("--to", action="append", required=True, help="Recipient email (repeatable)")
    parser.add_argument("--cc", action="append", default=[], help="CC email (repeatable)")
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body", required=True, help="Path to a text file containing the email body")
    parser.add_argument("--attach", action="append", default=[], help="Path to a file to attach (repeatable)")
    parser.add_argument("--dry-run", action="store_true",
                         help="Compose and print the message without sending")
    args = parser.parse_args()

    body_path = Path(args.body)
    if not body_path.exists():
        print(f"error: body file not found: {body_path}", file=sys.stderr)
        sys.exit(1)
    body_text = body_path.read_text()

    smtp_cfg = load_smtp_config(args.config)
    msg = build_message(smtp_cfg, args.to, args.cc, args.subject, body_text, args.attach)

    if args.dry_run:
        print("--- DRY RUN: message would be sent as follows ---")
        print(f"From: {msg['From']}")
        print(f"To: {msg['To']}")
        if msg.get("Cc"):
            print(f"Cc: {msg['Cc']}")
        print(f"Subject: {msg['Subject']}")
        print(f"Attachments: {args.attach or 'none'}")
        print("--- Body ---")
        print(body_text)
        print("--- END DRY RUN (nothing was sent) ---")
        return

    host = smtp_cfg["host"]
    port = smtp_cfg.get("port", 587)
    username = smtp_cfg["username"]
    password = smtp_cfg["password"]
    use_tls = smtp_cfg.get("use_tls", True)

    all_recipients = args.to + args.cc
    with smtplib.SMTP(host, port) as server:
        if use_tls:
            server.starttls(context=ssl.create_default_context())
        server.login(username, password)
        server.send_message(msg, to_addrs=all_recipients)

    print(f"sent to {', '.join(all_recipients)}")


if __name__ == "__main__":
    main()
