#!/usr/bin/env python3
"""Find a high-engagement tech/SaaS tweet to reply to via Grok API.

Returns JSON: {"tweet_id": "...", "author": "@...", "content": "...", "engagement": "..."}
Skips tweets already in ~/.scout-replies-log.json to avoid duplicates.
"""

import re
import requests
import os
import sys
import json
import time
from pathlib import Path

LOG_FILE = Path.home() / ".scout-replies-log.json"
CACHE_FILE = Path.home() / ".scout-reply-candidates-cache.json"
BLOCKED_AUTHORS_FILE = Path.home() / ".scout-blocked-authors.json"
CACHE_TTL_SECONDS = 20 * 60

# Handles matching these patterns almost always have reply restrictions
# (brand accounts, automated news bots, official channels). Case-insensitive.
SUSPICIOUS_HANDLE_PATTERNS = [
    re.compile(r"(?i)(AI|News|Bot|Official|HQ|Media|Daily|Watch|Wire|Brief)$"),
    re.compile(r"(?i)_official\b"),
    re.compile(r"(?i)\bteam_"),
    re.compile(r"\d{3,}$"),  # numeric suffix like user12345
]


def load_blocked_authors():
    if not BLOCKED_AUTHORS_FILE.exists():
        return set()
    try:
        entries = json.loads(BLOCKED_AUTHORS_FILE.read_text())
        return {a.lower().lstrip("@") for a in entries.get("authors", [])}
    except (json.JSONDecodeError, KeyError):
        return set()


def is_suspicious_handle(author):
    handle = author.lstrip("@")
    return any(p.search(handle) for p in SUSPICIOUS_HANDLE_PATTERNS)


def load_replied_ids():
    if not LOG_FILE.exists():
        return set()
    try:
        entries = json.loads(LOG_FILE.read_text())
        return {e["tweet_id"] for e in entries}
    except (json.JSONDecodeError, KeyError):
        return set()


def load_cache():
    """Return (candidates, consumed_ids) from a fresh cache, or (None, set())."""
    if not CACHE_FILE.exists():
        return None, set()
    try:
        cache = json.loads(CACHE_FILE.read_text())
        age = time.time() - cache["created_ts"]
        if age > CACHE_TTL_SECONDS:
            return None, set()
        return cache["candidates"], set(cache.get("consumed", []))
    except (json.JSONDecodeError, KeyError, TypeError):
        return None, set()


def save_cache(candidates, consumed):
    payload = {
        "created_ts": time.time(),
        "candidates": candidates,
        "consumed": sorted(consumed),
    }
    tmp = CACHE_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload))
    tmp.replace(CACHE_FILE)


def mark_consumed(tweet_id):
    if not CACHE_FILE.exists():
        return
    try:
        cache = json.loads(CACHE_FILE.read_text())
        consumed = set(cache.get("consumed", []))
        consumed.add(tweet_id)
        cache["consumed"] = sorted(consumed)
        tmp = CACHE_FILE.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(cache))
        tmp.replace(CACHE_FILE)
    except (json.JSONDecodeError, KeyError):
        pass


def serve(candidate):
    """Mark a candidate as consumed and emit it to stdout."""
    mark_consumed(candidate["tweet_id"])
    print(json.dumps(candidate))


def main():
    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        print("ERROR: XAI_API_KEY not set. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    replied_ids = load_replied_ids()

    # Cache-first: serve next unused candidate from the last fresh Grok batch
    # before spending another Grok call. The cache TTLs after 20min.
    cached, consumed = load_cache()
    if cached is not None:
        for t in cached:
            tid = t["tweet_id"]
            if tid in consumed or tid in replied_ids:
                continue
            serve(t)
            return
        print("INFO: cache exhausted, re-querying Grok.", file=sys.stderr)

    url = "https://api.x.ai/v1/responses"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "grok-4-fast-non-reasoning",
        "stream": False,
        "input": [
            {
                "role": "user",
                "content": (
                    "Find 10 on-brand tech/SaaS/AI/founder tweets from the last 24 hours that a SaaS "
                    "CEO could reply to. We are NOT looking for the most viral posts — viral tweets "
                    "from Premium/blue-check accounts almost always have reply-restriction turned on "
                    "(only verified or only-mentioned can reply), and our reply attempts fail with 403. "
                    "Instead, target the MID-TIER founder voice:\n"
                    "- Engagement range: 50–800 likes, 2K–100K views (NOT 5K+ likes, NOT 500K+ views).\n"
                    "- Author profile: real working founders, indie hackers, SaaS operators, "
                    "developer-tool builders, growth/marketing operators. NOT media accounts "
                    "(@unusual_whales, @TechCrunch, @TheRundownAI), NOT mega-creators (>100K followers), "
                    "NOT VCs broadcasting takes.\n"
                    "- ABSOLUTE RULE on verified accounts: do NOT return any tweet from a blue-check "
                    "verified account. No exceptions, no qualifiers, no 'unless their last 5 posts...'. "
                    "Verified founders almost always have replies restricted (verified-only or "
                    "mentioned-only), so reply attempts fail with 403. If you cannot confirm an "
                    "account is NOT verified, skip it. Prefer accounts with <50K followers and no "
                    "blue check.\n"
                    "- Reply signal: the post MUST already have at least 3 visible replies from "
                    "NON-verified accounts in the thread. If you can't confirm 3+ such replies exist, "
                    "skip the tweet entirely.\n"
                    "- Conversation type: a real opinion, observation, or question — not a 'comment to "
                    "apply' job ad, not 'drop what you're building', not 'follow+RT to win'.\n"
                    "Topics that fit: SaaS pricing, AI dev tools, startup scaling pain, founder "
                    "delegation, hiring engineers, dropshipping/e-commerce, pricing experiments, "
                    "developer workflow, agent orchestration, building in public.\n"
                    "HARD SKIPS: political posts, crypto/web3, consumer AI hype (Midjourney/Sora), "
                    "drama threads, hardware/robotics, podcast pitches, job ads.\n"
                    "English only. For EACH tweet, provide ALL of the following on separate lines:\n"
                    "TWEET_ID: <the numeric tweet ID>\n"
                    "AUTHOR: <@handle>\n"
                    "CONTENT: <what they said, one line>\n"
                    "ENGAGEMENT: <likes, views, replies count>\n"
                    "---\n"
                ),
            }
        ],
        "tools": [{"type": "x_search"}],
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Grok API request failed: {e}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    raw_text = ""
    for item in data.get("output", []):
        if item.get("type") == "message":
            for c in item.get("content", []):
                if c.get("type") == "output_text":
                    raw_text += c["text"]

    if not raw_text:
        print("ERROR: No output from Grok API.", file=sys.stderr)
        sys.exit(1)

    # Parse tweets from response
    tweets = []
    current = {}
    for line in raw_text.split("\n"):
        line = line.strip()
        if line.startswith("TWEET_ID:"):
            if current.get("tweet_id"):
                tweets.append(current)
            current = {"tweet_id": line.split(":", 1)[1].strip()}
        elif line.startswith("AUTHOR:"):
            current["author"] = line.split(":", 1)[1].strip()
        elif line.startswith("CONTENT:"):
            current["content"] = line.split(":", 1)[1].strip()
        elif line.startswith("ENGAGEMENT:"):
            current["engagement"] = line.split(":", 1)[1].strip()
    if current.get("tweet_id"):
        tweets.append(current)

    # Drop already-replied IDs early
    tweets = [t for t in tweets if t["tweet_id"] not in replied_ids]
    if not tweets:
        print("ERROR: All found tweets already replied to.", file=sys.stderr)
        sys.exit(1)

    # Python-side topic filter — Grok's prompt-level "skip drama/politics/crypto" leaks badly.
    # Drop candidates whose content matches any obvious-trash keyword. Case-insensitive
    # substring match on content + author. Lior Filter compatible (see memory rules).
    BANNED_TERMS = [
        # Crypto / memecoin / pump-and-dump
        "pumpfun", "$btc", "$eth", "$doge", "$sol", "memecoin", "rug pull", "moonshot",
        " btc ", " eth ", " sol ", "altcoin", "shitcoin", "to the moon",
        # Political / drama / celebrity
        "chud", "trump", "biden", "harris", "vance", "maga", "leftist", "rightwing",
        "right-wing", "left-wing", "antifa", "groyper", "kanye", "musk vs", "altman vs",
        # Engagement-bait / giveaway
        "rt to win", "follow + rt", "follow+rt", "comment 'roi'", "comment \"roi\"",
        "drop a 🚀", "drop a rocket", "tag a friend", "first 100 only", "free training",
        # Hardware/robotics (not Lior's lane)
        "humanoid robot", "tesla bot", "optimus", "boston dynamics",
        # Pure consumer AI hype
        "image gen war", "midjourney v", "dall-e ", "image generation",
    ]
    def is_trash(t):
        blob = (t.get("content","") + " " + t.get("author","")).lower()
        return any(term in blob for term in BANNED_TERMS)

    pre_filter_count = len(tweets)
    tweets = [t for t in tweets if not is_trash(t)]
    dropped = pre_filter_count - len(tweets)
    if dropped:
        print(f"INFO: dropped {dropped}/{pre_filter_count} candidates via topic filter.",
              file=sys.stderr)
    if not tweets:
        print("ERROR: All Grok candidates failed topic filter (politics/crypto/drama/bait).",
              file=sys.stderr)
        sys.exit(1)

    # Handle-pattern filter — catches branded/bot/news accounts that almost
    # always have reply restrictions. Grok prompt-level rule leaks badly.
    pre_handle_count = len(tweets)
    tweets = [t for t in tweets if not is_suspicious_handle(t.get("author", ""))]
    dropped_handles = pre_handle_count - len(tweets)
    if dropped_handles:
        print(f"INFO: dropped {dropped_handles}/{pre_handle_count} candidates via handle-pattern filter.",
              file=sys.stderr)

    # Blocked-authors filter — built from past 403 failures (see reply_x.py).
    # This is the closed-loop learning step: every 403 teaches the system to
    # avoid that author next time.
    blocked = load_blocked_authors()
    if blocked:
        pre_blocked_count = len(tweets)
        tweets = [t for t in tweets
                  if t.get("author", "").lower().lstrip("@") not in blocked]
        dropped_blocked = pre_blocked_count - len(tweets)
        if dropped_blocked:
            print(f"INFO: dropped {dropped_blocked}/{pre_blocked_count} candidates via blocked-authors list "
                  f"({len(blocked)} authors blocked).", file=sys.stderr)

    if not tweets:
        print("ERROR: All Grok candidates failed handle/blocked filter.", file=sys.stderr)
        sys.exit(1)

    # ENFORCE reply_settings == "everyone" via X API v2.
    # Grok's prompt-level "skip reply-restricted" is unreliable — 100% of 29 historical
    # reply attempts failed with 403 "Reply to this conversation is not allowed because
    # you have not been mentioned or otherwise engaged by the author". Verifying the
    # actual reply_settings field on the tweet is the only deterministic fix.
    x_creds = {k: os.environ.get(k) for k in
               ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]}
    if not all(x_creds.values()):
        # Without X creds we can't verify. Fall back to old behavior but warn loudly.
        print("WARNING: X_API_* env vars missing — cannot verify reply_settings. "
              "Returning unverified candidate (may 403 on reply).", file=sys.stderr)
        save_cache(tweets, set())
        serve(tweets[0])
        return

    try:
        import tweepy
        client = tweepy.Client(
            consumer_key=x_creds["X_API_KEY"],
            consumer_secret=x_creds["X_API_SECRET"],
            access_token=x_creds["X_ACCESS_TOKEN"],
            access_token_secret=x_creds["X_ACCESS_TOKEN_SECRET"],
        )
        # Batch-lookup up to 100 tweets per call. We have at most 10.
        ids = [t["tweet_id"] for t in tweets]
        resp = client.get_tweets(ids=ids, tweet_fields=["reply_settings"])
        settings_by_id = {}
        for t in (resp.data or []):
            settings_by_id[str(t.id)] = t.reply_settings or "everyone"
    except Exception as e:
        print(f"WARNING: reply_settings lookup failed ({type(e).__name__}: {e}). "
              "Returning unverified candidate.", file=sys.stderr)
        save_cache(tweets, set())
        serve(tweets[0])
        return

    # Filter to open-reply tweets only. Drop unknown IDs (hallucinated or deleted).
    open_tweets = [t for t in tweets
                   if settings_by_id.get(t["tweet_id"]) == "everyone"]

    if not open_tweets:
        # Surface why: how many were dropped vs missing
        restricted = sum(1 for t in tweets
                         if settings_by_id.get(t["tweet_id"]) not in (None, "everyone"))
        missing = sum(1 for t in tweets if t["tweet_id"] not in settings_by_id)
        print(f"ERROR: 0 candidates pass reply_settings filter. "
              f"Restricted: {restricted}, missing/deleted: {missing}, total: {len(tweets)}.",
              file=sys.stderr)
        sys.exit(1)

    save_cache(open_tweets, set())
    serve(open_tweets[0])


if __name__ == "__main__":
    main()
