#!/usr/bin/env python3
"""Reply to a specific Bluesky post (@liorpozin.bsky.social).

Usage: reply_bluesky.py <post_uri> <post_cid> "reply text here"
Logs replied post URIs to ~/.scout-replies-bluesky-log.json for deduplication.
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime, timedelta

LOG_FILE = Path.home() / ".scout-replies-bluesky-log.json"


def load_log():
    if not LOG_FILE.exists():
        return []
    try:
        return json.loads(LOG_FILE.read_text())
    except json.JSONDecodeError:
        return []


def save_log(entries):
    cutoff = (datetime.now() - timedelta(days=7)).isoformat()
    entries = [e for e in entries if e.get("replied_at", "") > cutoff]
    LOG_FILE.write_text(json.dumps(entries, indent=2))


def main():
    if len(sys.argv) < 4:
        print('Usage: reply_bluesky.py <post_uri> <post_cid> "reply text"', file=sys.stderr)
        sys.exit(1)

    post_uri = sys.argv[1]
    post_cid = sys.argv[2]
    reply_text = sys.argv[3]

    if len(reply_text) > 300:
        print(f"WARNING: Reply is {len(reply_text)} chars (Bluesky limit is 300).", file=sys.stderr)

    required = ["BSKY_HANDLE", "BSKY_APP_PASSWORD"]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        print(f"ERROR: Missing env vars: {', '.join(missing)}. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    from atproto import Client, models

    client = Client()
    client.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_APP_PASSWORD"])

    try:
        parent_ref = models.ComAtprotoRepoStrongRef.Main(uri=post_uri, cid=post_cid)
        reply_ref = models.AppBskyFeedPost.ReplyRef(parent=parent_ref, root=parent_ref)
        result = client.send_post(text=reply_text, reply_to=reply_ref)
        print(f"BLUESKY REPLY SUCCESS: {result.uri}")
    except Exception as e:
        print(f"BLUESKY REPLY FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        log = load_log()
        log.append({"uri": post_uri, "replied_at": datetime.now().isoformat(), "status": "failed"})
        save_log(log)
        sys.exit(1)

    log = load_log()
    log.append({"uri": post_uri, "replied_at": datetime.now().isoformat(), "status": "success"})
    save_log(log)
    print(f"Logged reply to dedup log.")


if __name__ == "__main__":
    main()
