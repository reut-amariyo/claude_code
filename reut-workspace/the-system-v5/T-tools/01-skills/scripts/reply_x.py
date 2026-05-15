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
CANDIDATES_CACHE = Path.home() / ".scout-reply-candidates-cache.json"
BLOCKED_AUTHORS_FILE = Path.home() / ".scout-blocked-authors.json"

# Persistent reply log for x-analyst-weekly. Metricool does NOT track replies posted
# via this script, so this is the only source of truth for true reply volume/quality.
PERFORMANCE_LOG = (
    Path(__file__).resolve().parents[3] / "O-output" / "x-performance-log" / "replies.jsonl"
)


def lookup_author_from_cache(tweet_id):
    """Find the @handle for tweet_id in the find_reply_target.py candidates cache."""
    if not CANDIDATES_CACHE.exists():
        return None
    try:
        cache = json.loads(CANDIDATES_CACHE.read_text())
        for t in cache.get("candidates", []):
            if t.get("tweet_id") == tweet_id:
                return t.get("author")
    except (json.JSONDecodeError, KeyError):
        pass
    return None


def add_blocked_author(author, tweet_id, reason):
    """Append author to the blocked-authors file so find_reply_target.py skips them next run."""
    if not author:
        return
    handle = author.lower().lstrip("@")
    try:
        data = json.loads(BLOCKED_AUTHORS_FILE.read_text()) if BLOCKED_AUTHORS_FILE.exists() else {}
    except json.JSONDecodeError:
        data = {}
    data.setdefault("authors", [])
    data.setdefault("history", [])
    if handle not in {a.lower().lstrip("@") for a in data["authors"]}:
        data["authors"].append(handle)
    data["history"].append({
        "author": handle,
        "tweet_id": tweet_id,
        "blocked_at": datetime.now().isoformat(),
        "reason": reason,
    })
    BLOCKED_AUTHORS_FILE.write_text(json.dumps(data, indent=2))


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


def append_performance_log(record):
    PERFORMANCE_LOG.parent.mkdir(parents=True, exist_ok=True)
    with PERFORMANCE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


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

    now_iso = datetime.now().isoformat()
    try:
        result = client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet_id)
        reply_id = result.data["id"]
        print(f"REPLY SUCCESS: https://x.com/lior_pozin/status/{reply_id}")
    except Exception as e:
        error_msg = str(e)
        print(f"REPLY FAILED: {type(e).__name__}: {error_msg}", file=sys.stderr)
        # Log failed tweets too so we skip them next time. Capture the error so we can
        # diagnose later — the 29 historical "failed" entries were unanalyzable without it.
        log = load_log()
        log.append({
            "tweet_id": tweet_id,
            "replied_at": now_iso,
            "status": "failed",
            "error_type": type(e).__name__,
            "error_message": error_msg[:500],
        })
        save_log(log)
        append_performance_log({
            "replied_at": now_iso,
            "status": "failed",
            "tweet_id": tweet_id,
            "original_url": f"https://x.com/i/status/{tweet_id}",
            "reply_text": reply_text,
            "error_type": type(e).__name__,
            "error_message": error_msg[:500],
        })
        print(f"Logged failed tweet {tweet_id} to skip next time.")

        # If this was a 403 reply-restriction, block the author for future runs.
        # Closes the loop: every restricted-reply author teaches the scout to skip them.
        if "403" in error_msg or "Forbidden" in error_msg:
            author = lookup_author_from_cache(tweet_id)
            if author:
                add_blocked_author(author, tweet_id, "403 reply-restricted")
                print(f"Blocked author {author} from future scout runs.")
            else:
                print(f"WARNING: could not resolve author for {tweet_id} from cache — not blocked.",
                      file=sys.stderr)
        sys.exit(1)

    # Log the successful reply (dedup log + persistent performance log)
    log = load_log()
    log.append({"tweet_id": tweet_id, "replied_at": now_iso, "status": "success"})
    save_log(log)
    append_performance_log({
        "replied_at": now_iso,
        "status": "success",
        "tweet_id": tweet_id,
        "original_url": f"https://x.com/i/status/{tweet_id}",
        "reply_id": str(reply_id),
        "reply_url": f"https://x.com/lior_pozin/status/{reply_id}",
        "reply_text": reply_text,
    })
    print(f"Logged tweet {tweet_id} to dedup log.")
    print(f"Logged reply to performance log: {PERFORMANCE_LOG}")


if __name__ == "__main__":
    main()
