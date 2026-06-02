#!/usr/bin/env python3
"""Canary: is @lior_pozin still reply-restricted on X?

Background (2026-05-23): X put the account in a limited state that 403s every
API reply/quote to a stranger's post (even "everyone" tweets), while original
posts still work. See [[x-reply-pipeline-whitelist-collapse]]. The 15
scout-reply-x scheduled tasks were disabled because they only produced 403s.

This script posts ONE real reply to a live "everyone" tweet and deletes it
immediately, to detect the moment the restriction lifts. It is the only reliable
signal — the restriction is account-level and can't be inferred from read calls.

Output: prints exactly one STATUS line and writes ~/.scout-x-reply-canary-status.json.
Exit codes:
    0  -> LIFTED         (a reply succeeded; restriction is gone)
    10 -> RESTRICTED     (still the account-level 403)
    20 -> INCONCLUSIVE   (no live target, missing creds, or unexpected error)

Safe: anything posted is deleted within ~1s. Never blocks authors, never edits
the whitelist/blocklist.
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

STATUS_FILE = Path.home() / ".scout-x-reply-canary-status.json"
REPLIES_LOG = Path(__file__).resolve().parents[3] / "O-output" / "x-performance-log" / "replies.jsonl"
TEST_TEXT = "Great point."


def write_status(status, detail="", target=None, posted_id=None):
    STATUS_FILE.write_text(json.dumps({
        "checked_at": datetime.now().isoformat(),
        "status": status,            # LIFTED | RESTRICTED | INCONCLUSIVE
        "detail": detail,
        "target_tweet": target,
        "posted_reply_id": posted_id,
    }, indent=2))


def candidate_target_ids():
    """Historical 403'd tweet_ids — known real tweets to probe. Newest-ish first."""
    ids = []
    if REPLIES_LOG.exists():
        for line in REPLIES_LOG.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if r.get("status") == "failed" and r.get("tweet_id"):
                ids.append(r["tweet_id"])
    # de-dupe, preserve order
    seen, out = set(), []
    for i in ids:
        if i not in seen:
            seen.add(i); out.append(i)
    return out


def main():
    creds = {k: os.environ.get(k) for k in
             ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]}
    if not all(creds.values()):
        print("STATUS: INCONCLUSIVE missing X_API_* env vars (source ~/.zshrc)")
        write_status("INCONCLUSIVE", "missing creds")
        sys.exit(20)

    try:
        import tweepy
        from requests_oauthlib import OAuth1Session
    except Exception as e:
        print(f"STATUS: INCONCLUSIVE import failed: {e}")
        write_status("INCONCLUSIVE", f"import failed: {e}")
        sys.exit(20)

    oauth = OAuth1Session(creds["X_API_KEY"], creds["X_API_SECRET"],
                          creds["X_ACCESS_TOKEN"], creds["X_ACCESS_TOKEN_SECRET"])
    client = tweepy.Client(
        consumer_key=creds["X_API_KEY"], consumer_secret=creds["X_API_SECRET"],
        access_token=creds["X_ACCESS_TOKEN"], access_token_secret=creds["X_ACCESS_TOKEN_SECRET"])

    # Find a still-live "everyone" target among historical tweets.
    target = None
    for tid in candidate_target_ids():
        try:
            r = oauth.get("https://api.twitter.com/2/tweets",
                          params={"ids": tid, "tweet.fields": "reply_settings"})
            if r.status_code == 200 and r.json().get("data"):
                if r.json()["data"][0].get("reply_settings") == "everyone":
                    target = tid
                    break
        except Exception:
            continue
    if not target:
        print("STATUS: INCONCLUSIVE no live 'everyone' target found")
        write_status("INCONCLUSIVE", "no live target")
        sys.exit(20)

    # The actual test: attempt one reply.
    posted_id = None
    try:
        res = client.create_tweet(text=TEST_TEXT, in_reply_to_tweet_id=target)
        posted_id = res.data["id"]
    except Exception as e:
        msg = str(e)
        restricted = ("not been mentioned or otherwise engaged" in msg
                      or "not part of the conversation thread" in msg)
        if restricted:
            print("STATUS: RESTRICTED account-level reply block still active")
            write_status("RESTRICTED", msg[:300], target=target)
            sys.exit(10)
        print(f"STATUS: INCONCLUSIVE unexpected error: {type(e).__name__}: {msg[:200]}")
        write_status("INCONCLUSIVE", f"{type(e).__name__}: {msg[:200]}", target=target)
        sys.exit(20)

    # Success → restriction lifted. Clean up the test reply immediately.
    deleted = False
    try:
        time.sleep(1)
        dr = client.delete_tweet(posted_id)
        deleted = bool(getattr(dr, "data", {}) and dr.data.get("deleted"))
    except Exception as e:
        print(f"WARNING: posted {posted_id} but delete failed — delete manually: {e}",
              file=sys.stderr)
    print(f"STATUS: LIFTED reply succeeded (id {posted_id}, deleted={deleted})")
    write_status("LIFTED", f"deleted={deleted}", target=target, posted_id=posted_id)
    sys.exit(0)


if __name__ == "__main__":
    main()
