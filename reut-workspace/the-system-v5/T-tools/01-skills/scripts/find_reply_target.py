#!/usr/bin/env python3
"""Find a high-engagement tech/SaaS tweet to reply to via Grok API.

Returns JSON: {"tweet_id": "...", "author": "@...", "content": "...", "engagement": "..."}
Skips tweets already in ~/.scout-replies-log.json to avoid duplicates.
"""

import requests
import os
import sys
import json
from pathlib import Path

LOG_FILE = Path.home() / ".scout-replies-log.json"


def load_replied_ids():
    if not LOG_FILE.exists():
        return set()
    try:
        entries = json.loads(LOG_FILE.read_text())
        return {e["tweet_id"] for e in entries}
    except (json.JSONDecodeError, KeyError):
        return set()


def main():
    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        print("ERROR: XAI_API_KEY not set. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    replied_ids = load_replied_ids()

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
                    "Find the 10 most popular and engaging tech, AI, and SaaS tweets from today "
                    "that have OPEN REPLIES (everyone can reply). Look for tweets with many reply comments, "
                    "which indicates replies are open to everyone. "
                    "SKIP tweets that restrict who can reply. "
                    "SKIP promotional/sponsored posts, product ads, affiliate links, and engagement bait (follow+RT+comment giveaways). "
                    "For EACH tweet, provide ALL of the following on separate lines:\n"
                    "TWEET_ID: <the numeric tweet ID>\n"
                    "AUTHOR: <@handle>\n"
                    "CONTENT: <what they said, one line>\n"
                    "ENGAGEMENT: <likes, views, replies count>\n"
                    "---\n"
                    "Focus on posts with real conversation happening and many replies. English only. "
                    "Skip political posts, consumer AI hype, and drama threads. "
                    "Focus on: SaaS, AI tools, startup scaling, pricing, founder journey, developer tools."
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

    # Pick first tweet not already replied to
    for tweet in tweets:
        tid = tweet["tweet_id"]
        if tid not in replied_ids:
            print(json.dumps(tweet))
            return

    print("ERROR: All found tweets already replied to.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
