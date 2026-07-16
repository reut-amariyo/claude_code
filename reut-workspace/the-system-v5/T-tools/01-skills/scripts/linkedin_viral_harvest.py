#!/usr/bin/env python3
"""
LinkedIn Viral Harvest — pull high-engagement LinkedIn posts via Apify and
keep the top slice, sorted by engagement.

Requires: APIFY_TOKEN env var (same setup as demand_radar.py):
  1. Sign up at https://apify.com (pay-per-use)
  2. Settings -> Integrations -> API token
  3. Add to ~/.zshrc:  export APIFY_TOKEN="apify_api_..."

Actor: harvestapi/linkedin-post-search (no cookies, ~17K users).
NOTE (same caveat as demand_radar.py): Apify actor input schemas vary and may
need a one-time tweak on first run. Run with --dry-run to print the input
without spending credits; if the run errors, open the actor page on Apify,
check its Input tab, and adjust build_actor_input() below.

Usage:
  python3 linkedin_viral_harvest.py "AI" "founder"            # default 100 posts/keyword, past week
  python3 linkedin_viral_harvest.py "AI" --max 200 --window month
  python3 linkedin_viral_harvest.py "AI" --top-pct 1          # keep top 1%
  python3 linkedin_viral_harvest.py "AI" --dry-run

Output: O-output/linkedin-viral-harvest/harvest-YYYY-MM-DD.md (report)
        O-output/linkedin-viral-harvest/harvest-YYYY-MM-DD.jsonl (raw, sorted)
"""

import argparse
import datetime
import json
import os
import pathlib
import sys
import urllib.request

APIFY_ACTOR = "harvestapi~linkedin-post-search"
OUT_DIR = pathlib.Path(__file__).resolve().parents[3] / "O-output" / "linkedin-viral-harvest"

# Engagement score mirrors the X bookmark-weighted idea, adapted to LinkedIn:
# reposts spread reach, comments signal depth, reactions are the base.
W_REACTIONS, W_COMMENTS, W_REPOSTS = 1, 2, 3


def build_actor_input(keywords, max_items, window):
    # harvestapi actors commonly accept searchQueries + maxItems + postedLimit.
    # Adjust here after first run if the actor rejects the input.
    return {
        "searchQueries": keywords,
        "maxItems": max_items,
        "postedLimit": window,  # "24h" | "week" | "month"
        "sortBy": "relevance",
    }


def run_actor(token, actor_input):
    url = (f"https://api.apify.com/v2/acts/{APIFY_ACTOR}/run-sync-get-dataset-items"
           f"?token={token}&timeout=300")
    req = urllib.request.Request(
        url,
        data=json.dumps(actor_input).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=320) as r:
        return json.load(r)


def norm_post(item):
    """Normalize one actor item. Field names differ between actors; probe
    common variants and keep the raw item for debugging."""
    def pick(*names, default=0):
        for n in names:
            v = item
            for part in n.split("."):
                v = v.get(part, None) if isinstance(v, dict) else None
                if v is None:
                    break
            if v is not None:
                return v
        return default

    reactions = int(pick("reactions", "likeCount", "numLikes", "engagement.likes", "socialContent.reactions", default=0) or 0)
    comments = int(pick("comments", "commentCount", "numComments", "engagement.comments", default=0) or 0)
    reposts = int(pick("reposts", "shareCount", "numShares", "engagement.shares", default=0) or 0)
    return {
        "author": pick("author.name", "authorName", "author", default="?"),
        "headline": pick("author.headline", "authorHeadline", default=""),
        "url": pick("url", "postUrl", "link", default=""),
        "date": pick("postedAt", "date", "postDate", default=""),
        "text": str(pick("text", "content", "postText", default=""))[:1200],
        "reactions": reactions,
        "comments": comments,
        "reposts": reposts,
        "score": reactions * W_REACTIONS + comments * W_COMMENTS + reposts * W_REPOSTS,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("keywords", nargs="+", help="search keywords, each runs as its own query")
    ap.add_argument("--max", type=int, default=100, help="max posts per keyword (default 100)")
    ap.add_argument("--window", default="week", choices=["24h", "week", "month"])
    ap.add_argument("--top-pct", type=float, default=5.0, help="keep top N%% by score (default 5)")
    ap.add_argument("--dry-run", action="store_true", help="print actor input and exit, no credits spent")
    args = ap.parse_args()

    actor_input = build_actor_input(args.keywords, args.max, args.window)
    if args.dry_run:
        print(json.dumps(actor_input, indent=2))
        return

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("APIFY_TOKEN not set. See header of this script for setup.")

    items = run_actor(token, actor_input)
    if not items:
        sys.exit("Actor returned 0 items — check the input schema on the actor's Apify page.")

    posts = [norm_post(i) for i in items]
    # Drop items where we failed to parse any engagement — schema mismatch guard.
    parsed = [p for p in posts if p["reactions"] or p["comments"]]
    if not parsed:
        print("WARNING: engagement fields not recognized. First raw item keys:")
        print(list(items[0].keys()))
        sys.exit(1)

    parsed.sort(key=lambda p: p["score"], reverse=True)
    keep = max(1, round(len(parsed) * args.top_pct / 100))
    top = parsed[:keep]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()
    jsonl_path = OUT_DIR / f"harvest-{today}.jsonl"
    with open(jsonl_path, "w") as f:
        for p in parsed:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    md_path = OUT_DIR / f"harvest-{today}.md"
    with open(md_path, "w") as f:
        f.write(f"# LinkedIn Viral Harvest — {today}\n\n")
        f.write(f"Keywords: {', '.join(args.keywords)} | window: {args.window} | "
                f"pool: {len(parsed)} posts | kept top {args.top_pct}% = {len(top)}\n\n")
        for i, p in enumerate(top, 1):
            hook = p["text"].split("\n")[0][:120]
            f.write(f"## {i}. {p['author']} — {p['reactions']:,} reactions / "
                    f"{p['comments']:,} comments / {p['reposts']:,} reposts\n")
            f.write(f"**Hook:** {hook}\n\n")
            f.write(f"**URL:** {p['url']}\n\n")
            f.write(f"> {p['text'][:600]}\n\n---\n\n")

    print(f"Pool {len(parsed)} posts -> top {len(top)} kept")
    print(f"Report: {md_path}")
    print(f"Raw:    {jsonl_path}")


if __name__ == "__main__":
    main()
