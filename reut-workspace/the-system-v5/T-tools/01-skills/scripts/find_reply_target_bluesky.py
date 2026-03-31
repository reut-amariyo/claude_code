#!/usr/bin/env python3
"""Find a high-engagement tech/SaaS post on Bluesky to reply to.

Returns JSON: {"uri": "...", "cid": "...", "author": "@...", "content": "...", "engagement": "..."}
Skips posts already in ~/.scout-replies-bluesky-log.json to avoid duplicates.
"""

import os
import sys
import json
from pathlib import Path

LOG_FILE = Path.home() / ".scout-replies-bluesky-log.json"


def load_replied_uris():
    if not LOG_FILE.exists():
        return set()
    try:
        entries = json.loads(LOG_FILE.read_text())
        return {e["uri"] for e in entries}
    except (json.JSONDecodeError, KeyError):
        return set()


def main():
    handle = os.environ.get("BSKY_HANDLE")
    password = os.environ.get("BSKY_APP_PASSWORD")
    if not handle or not password:
        print("ERROR: BSKY_HANDLE or BSKY_APP_PASSWORD not set. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    from atproto import Client

    client = Client()
    client.login(handle, password)

    replied_uris = load_replied_uris()

    # Search for popular tech/SaaS posts
    queries = [
        "SaaS founder startup",
        "AI tools developers",
        "startup scaling pricing",
        "building in public SaaS",
        "AI coding software engineering",
    ]

    all_posts = []
    for query in queries:
        try:
            feed = client.app.bsky.feed.search_posts({"q": query, "limit": 10, "sort": "top"})
            for post in feed.posts:
                if post.uri not in replied_uris:
                    # Filter: English only, min engagement
                    text = post.record.text if post.record else ""
                    likes = post.like_count or 0
                    replies = post.reply_count or 0
                    # Skip non-English (basic heuristic)
                    if any(ord(c) > 0x2000 for c in text[:50]):
                        continue
                    # Skip very low engagement
                    if likes < 3:
                        continue
                    all_posts.append({
                        "uri": post.uri,
                        "cid": post.cid,
                        "author": f"@{post.author.handle}",
                        "content": text[:300],
                        "engagement": f"{likes} likes, {replies} replies",
                        "likes": likes,
                    })
        except Exception:
            continue

    if not all_posts:
        print("ERROR: No suitable Bluesky posts found.", file=sys.stderr)
        sys.exit(1)

    # Sort by likes, pick the best one
    all_posts.sort(key=lambda x: x["likes"], reverse=True)
    best = all_posts[0]
    del best["likes"]  # Remove sorting key
    print(json.dumps(best))


if __name__ == "__main__":
    main()
