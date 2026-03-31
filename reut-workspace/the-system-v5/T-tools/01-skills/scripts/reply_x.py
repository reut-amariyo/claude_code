#!/usr/bin/env python3
"""Reply to a specific tweet on X (@lior_pozin).

Usage: reply_x.py <tweet_id> "reply text here"
Logs replied tweet IDs to ~/.scout-replies-log.json for deduplication.
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime, timedelta

LOG_FILE = Path.home() / ".scout-replies-log.json"


def load_log():
    if not LOG_FILE.exists():
        return []
    try:
        return json.loads(LOG_FILE.read_text())
    except json.JSONDecodeError:
        return []


def save_log(entries):
    # Prune entries older than 7 days
    cutoff = (datetime.now() - timedelta(days=7)).isoformat()
    entries = [e for e in entries if e.get("replied_at", "") > cutoff]
    LOG_FILE.write_text(json.dumps(entries, indent=2))


def main():
    if len(sys.argv) < 3:
        print('Usage: reply_x.py <tweet_id> "reply text"', file=sys.stderr)
        sys.exit(1)

    tweet_id = sys.argv[1]
    reply_text = sys.argv[2]

    if len(reply_text) > 280:
        print(f"WARNING: Reply is {len(reply_text)} chars (X limit is 280).", file=sys.stderr)

    required = ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        print(f"ERROR: Missing env vars: {', '.join(missing)}. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    import tweepy

    client = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
    )

    try:
        result = client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet_id)
        reply_id = result.data["id"]
        print(f"REPLY SUCCESS: https://x.com/lior_pozin/status/{reply_id}")
    except Exception as e:
        error_msg = str(e)
        print(f"REPLY FAILED: {type(e).__name__}: {error_msg}", file=sys.stderr)
        # Log failed tweets too so we skip them next time
        log = load_log()
        log.append({"tweet_id": tweet_id, "replied_at": datetime.now().isoformat(), "status": "failed"})
        save_log(log)
        print(f"Logged failed tweet {tweet_id} to skip next time.")
        sys.exit(1)

    # Log the successful reply
    log = load_log()
    log.append({"tweet_id": tweet_id, "replied_at": datetime.now().isoformat(), "status": "success"})
    save_log(log)
    print(f"Logged tweet {tweet_id} to dedup log.")


if __name__ == "__main__":
    main()
