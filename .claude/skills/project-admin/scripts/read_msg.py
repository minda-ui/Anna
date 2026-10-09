#!/usr/bin/env python3
"""Read one message by id, quoted history cut, attachment names listed (SC-31).

Usage:  python3 -I read_msg.py <account> <message_id> [<message_id> ...] [--chars 1200]

<account> is a Composio account: anna-gmail (info@), anna-gmail-minda, anna-gmail-ops, anna-gmail-properties.
A message id belongs to one mailbox (SC-24): use the account the id was listed under. Never loop over a
sender (SC-25): pass exact ids only. Attachment ids are printed in full (a shortened id fails with
'Invalid attachment token').
"""
import json, re, subprocess, sys


def main():
    args = sys.argv[1:]
    chars = 1200
    if "--chars" in args:
        i = args.index("--chars")
        chars = int(args[i + 1])
        del args[i:i + 2]
    if len(args) < 2:
        sys.exit(__doc__)
    account, ids = args[0], args[1:]
    for mid in ids:
        p = subprocess.run(["composio", "execute", "GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID", "--account", account,
                            "-d", json.dumps({"message_id": mid, "format": "full"})], capture_output=True, text=True)
        try:
            r = json.loads(p.stdout)
            path = r.get("outputFilePath") or r.get("data", {}).get("outputFilePath")
            d = json.load(open(path)) if path else r
            d = d.get("data", d)
        except Exception:
            print(f"=== {mid}: FAILED to read"); continue
        t = d.get("messageText") or ""
        t = re.split(r"\n(?:From:|-----Original|_{10,}|On .{5,80} wrote:|Sent from)", t)[0]
        t = re.sub(r"\n\s*\n+", "\n", t)
        print(f"=== {mid} | {str(d.get('messageTimestamp'))[:16]} | {str(d.get('sender'))[:40]} -> {str(d.get('to'))[:60]}"
              f" | cc {str(d.get('cc'))[:70]} | {str(d.get('subject'))[:70]}")
        for a in d.get("attachmentList", []) or []:
            fn = a.get("filename", "")
            if not fn.lower().startswith("image0") and fn.lower() not in ("image.png",):
                print(f"   attachment: {fn} | id {a.get('attachmentId')}")
        print(t[:chars])


main()
