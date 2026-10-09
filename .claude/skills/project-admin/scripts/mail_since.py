#!/usr/bin/env python3
"""List new mail since a UTC time, and drafts, in all four mailboxes (SC-31).

Usage:  python3 -I mail_since.py 2026-10-08T16:25 [--no-drafts]

Prints one line per message: time (UTC) | sender | subject | message id, per mailbox, and the draft ids.
It lists only. Project mail is judged by what it is about (Charter-Rules 0c), then read one message at a
time with read_msg.py. info@ is the Composio account `anna-gmail`; the native Gmail tool reads the same box.
"""
import json, subprocess, sys

ACCOUNTS = ["anna-gmail", "anna-gmail-minda", "anna-gmail-ops", "anna-gmail-properties"]
LABEL = {"anna-gmail": "info@ (anna-gmail)", "anna-gmail-minda": "minda@", "anna-gmail-ops": "ops@",
         "anna-gmail-properties": "properties"}


def run(slug, account, payload):
    p = subprocess.run(["composio", "execute", slug, "--account", account, "-d", json.dumps(payload)],
                       capture_output=True, text=True)
    try:
        r = json.loads(p.stdout)
    except Exception:
        return None
    path = r.get("outputFilePath") or r.get("data", {}).get("outputFilePath")
    if path:
        try:
            r = json.load(open(path))
        except Exception:
            return None
    return r


def find(o, key):
    if isinstance(o, dict):
        if isinstance(o.get(key), list):
            return o[key]
        for v in o.values():
            x = find(v, key)
            if x is not None:
                return x
    return None


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    since = sys.argv[1]
    drafts = "--no-drafts" not in sys.argv
    day = since[:10].replace("-", "/")
    for a in ACCOUNTS:
        r = run("GMAIL_FETCH_EMAILS", a, {"query": f"after:{day} -in:draft", "max_results": 100})
        msgs = find(r, "messages") if r else None
        print(f"== {LABEL[a]}")
        if msgs is None:
            print("   FAILED to read (signed out? run `composio whoami`)")
            continue
        n = 0
        for m in sorted(msgs, key=lambda x: x.get("messageTimestamp") or ""):
            t = m.get("messageTimestamp") or ""
            if t >= since:
                n += 1
                print(f"   {t[5:16]} | {str(m.get('sender'))[:38]} | {str(m.get('subject'))[:70]} | {m.get('messageId')}")
        print(f"   new since {since}Z: {n}")
        if drafts:
            d = run("GMAIL_LIST_DRAFTS", a, {"max_results": 30})
            dl = find(d, "drafts") if d else None
            print("   drafts:", "FAILED" if dl is None else f"{len(dl)} {[x.get('id') for x in dl]}")


main()
