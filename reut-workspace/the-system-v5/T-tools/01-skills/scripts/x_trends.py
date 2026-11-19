#!/usr/bin/env python3
"""Find the most-engaged X posts of the last N hours for one audience, via Grok x_search.

Used by the daily-trends scheduled task, X section (audience = buyers for AvatarFactory:
AI influencers, AI UGC, AI avatars, faceless content, making money with AI video).

Usage:  source ~/.zshrc && python3 x_trends.py [--hours 24] [--limit 10] [--topic "..."]
Output: JSON array on stdout: [{url, author, followers, posted_at, likes, reposts,
        replies, views, text, why_trending}]
"""

import argparse
import json
import os
import re
import sys

import requests

GROK_URL = "https://api.x.ai/v1/responses"
GROK_MODEL = "grok-4-fast-non-reasoning"

DEFAULT_TOPIC = (
    "AI influencers, AI UGC ads, AI avatars and AI clones, faceless AI content, "
    "AI video generators such as HeyGen, Higgsfield, Veo, Sora, Kling, Arcads, Captions, "
    "and making money online with AI-generated video. US-based or English-language accounts."
)

PROMPT = """Use x_search to find the {limit} most-engaged original X posts (not replies, not reposts)
published in the last {hours} hours about: {topic}

Rank by real engagement: likes + 3x replies + 2x reposts, and prefer posts that clearly beat the
author's usual numbers. Skip giveaways, crypto, NSFW, engagement-bait "comment X to get Y" posts
and bot accounts. Only include posts you actually found with x_search; never invent a post,
URL or number. If you find fewer than {limit}, return fewer.

Return ONLY a JSON array, no prose, each item:
{{"url": "https://x.com/<handle>/status/<id>", "author": "@handle", "followers": int or null,
"posted_at": "ISO date", "likes": int, "reposts": int, "replies": int, "views": int or null,
"text": "full post text", "why_trending": "one short line"}}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--topic", default=DEFAULT_TOPIC)
    a = ap.parse_args()

    key = os.environ.get("XAI_API_KEY")
    if not key:
        sys.exit("ERROR: XAI_API_KEY not set. Run: source ~/.zshrc")

    payload = {
        "model": GROK_MODEL,
        "stream": False,
        "input": [{"role": "user", "content": PROMPT.format(limit=a.limit, hours=a.hours, topic=a.topic)}],
        "tools": [{"type": "x_search"}],
    }
    try:
        r = requests.post(GROK_URL, headers={"Authorization": f"Bearer {key}"}, json=payload, timeout=300)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        sys.exit(f"ERROR: Grok request failed: {e}")

    text = ""
    for item in r.json().get("output", []):
        if item.get("type") == "message":
            for c in item.get("content", []):
                if c.get("type") == "output_text":
                    text += c.get("text", "")
    m = re.search(r"\[.*\]", text, re.S)
    if not m:
        sys.exit(f"ERROR: no JSON array in Grok reply:\n{text[:1000]}")
    try:
        posts = json.loads(m.group(0))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: bad JSON from Grok ({e}):\n{m.group(0)[:1000]}")
    posts = [p for p in posts if re.match(r"https://(x|twitter)\.com/\w+/status/\d+", str(p.get("url", "")))]
    print(json.dumps(posts, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
