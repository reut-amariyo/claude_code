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
WHITELIST_FILE = Path.home() / ".scout-reply-whitelist.json"


def load_whitelist():
    """Return set of lowercased curated open-reply handles, or empty set."""
    if not WHITELIST_FILE.exists():
        return set()
    try:
        data = json.loads(WHITELIST_FILE.read_text())
        return {h.lower().lstrip("@") for h in data.get("handles", [])}
    except (json.JSONDecodeError, KeyError):
        return set()

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
    # Never block a curated open-reply account. A transient 403 must not erode the
    # whitelist (see [[x-reply-pipeline-whitelist-collapse]], 2026-05-20).
    if handle in load_whitelist():
        print(f"NOTE: {author} is whitelisted — 403 ignored, not blocking.", file=sys.stderr)
        return
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
        # Resolve the author up front so per-handle outcomes can be aggregated later
        # (whitelist pruning — see reply_whitelist_stats.py). is_403 distinguishes a
        # reply-restriction (a fact about the handle) from a transient/other error.
        author = lookup_author_from_cache(tweet_id)
        is_403 = "403" in error_msg or "Forbidden" in error_msg
        # ACCOUNT-LEVEL restriction (NOT the target's fault). Verified 2026-05-23:
        # @lior_pozin is in an X-imposed limited state — replies AND quotes to
        # strangers 403 with this wording even when the target's reply_settings is
        # "everyone" (write perms + Premium confirmed fine). It is X anti-spam on a
        # low-trust/automated account, not a per-author setting. So we must NOT block
        # the author for it. See [[x-reply-pipeline-whitelist-collapse]].
        account_restricted = (
            "not been mentioned or otherwise engaged" in error_msg
            or "not part of the conversation thread" in error_msg
        )
        if account_restricted:
            failure_kind = "account_reply_restricted"
        elif is_403:
            failure_kind = "403_reply_restricted"
        else:
            failure_kind = "other"
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
            "author": author,
            "failure_kind": failure_kind,
            "original_url": f"https://x.com/i/status/{tweet_id}",
            "reply_text": reply_text,
            "error_type": type(e).__name__,
            "error_message": error_msg[:500],
        })
        print(f"Logged failed tweet {tweet_id} to skip next time.")

        if account_restricted:
            # Loud, unambiguous signal so a human (or the scout) stops retrying. No
            # author is blocked — the restriction is on THIS account, not the target.
            print(
                "ACCOUNT REPLY-RESTRICTED: X is blocking this account's replies/quotes "
                "to non-engaged authors (anti-spam limited state). This is NOT fixable by "
                "retrying or by curating the whitelist. The scout-reply-x scheduled tasks "
                "are disabled for this reason; re-run reply_whitelist_stats.py or the live "
                "API test to check if the restriction has lifted before re-enabling.",
                file=sys.stderr,
            )
        elif is_403:
            # A genuine per-author/tweet 403 (different wording). Teach the scout to skip
            # that author next time. (Whitelisted handles are exempted in add_blocked_author.)
            if author:
                add_blocked_author(author, tweet_id, "403 reply-restricted")
                print(f"Blocked author {author} from future scout runs.")
            else:
                print(f"WARNING: could not resolve author for {tweet_id} from cache — not blocked.",
                      file=sys.stderr)
        sys.exit(1)

    # Log the successful reply (dedup log + persistent performance log)
    author = lookup_author_from_cache(tweet_id)
    log = load_log()
    log.append({"tweet_id": tweet_id, "replied_at": now_iso, "status": "success"})
    save_log(log)
    append_performance_log({
        "replied_at": now_iso,
        "status": "success",
        "tweet_id": tweet_id,
        "author": author,
        "original_url": f"https://x.com/i/status/{tweet_id}",
        "reply_id": str(reply_id),
        "reply_url": f"https://x.com/lior_pozin/status/{reply_id}",
        "reply_text": reply_text,
    })
    print(f"Logged tweet {tweet_id} to dedup log.")
    print(f"Logged reply to performance log: {PERFORMANCE_LOG}")


if __name__ == "__main__":
    main()
