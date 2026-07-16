#!/usr/bin/env python3
"""
demand_radar.py — Multi-source "what's heating up for Lior's audience" scanner.

Goal: surface the topics with real DEMAND right now (and why), so Lior can ride
them while they're hot. Built for virality, not e-commerce ops.

Sources:
  - Hacker News (Algolia API) — FREE, no auth, works immediately. Strong signal
    for what founders + AI builders are actually arguing about.
  - Reddit via Apify (OPTIONAL, paid pay-as-you-go) — only if APIFY_TOKEN is set.
    Reddit's own API self-service was closed (Responsible Builder Policy 2026-06-05)
    and reddit.com is blocked from scraping/WebSearch/Chrome here, so a 3rd-party
    data provider (Apify) is the practical paid unlock. See setup note below.

Cross-source recurrence is the strongest demand signal: a topic that shows up on
BOTH HN and Reddit is hotter than one that shows up on only one.

Reddit via Apify — setup (one time, if you want Reddit in the mix):
  1. Sign up at https://apify.com (free tier + pay-per-use, ~cents per run)
  2. Settings -> Integrations -> API token
  3. Add to ~/.zshrc:  export APIFY_TOKEN="apify_api_..."
  4. `source ~/.zshrc`
  The actor + input may need a one-time tweak on first run (Apify actors vary);
  the script prints the raw error so you can adjust ACTOR / input if needed.

Usage:
  python3 demand_radar.py                 # HN (+ Reddit if APIFY_TOKEN set)
  python3 demand_radar.py --days 3
  python3 demand_radar.py --json
"""

import os
import re
import sys
import json
import time
import argparse
import urllib.parse
import urllib.request

# Lior's lane (e-commerce intentionally dropped per Reut, 2026-06-27).
LANE_KEYWORDS = [
    "ai", "agent", "llm", "gpt", "claude", "openai", "anthropic", "deepseek",
    "gemini", "model", "inference", "token", "prompt", "coding", "open source",
    "open-source", "startup", "founder", "saas", "micro saas", "bootstrapped",
    "vc", "venture", "funding", "valuation", "ipo", "acqui", "exit", "pricing",
    "churn", "mrr", "arr", "cac", "ltv", "growth", "scaling", "moat",
    "distribution", "burnout", "bubble", "layoff", "automation",
]

# Subreddits for the Apify path (no e-commerce).
REDDIT_SUBS = [
    "SaaS", "startups", "Entrepreneur", "indiehackers", "microsaas",
    "OpenAI", "ClaudeAI", "LocalLLaMA", "AI_Agents", "artificial",
    "singularity", "venturecapital",
]

HN_SEARCH = "https://hn.algolia.com/api/v1/search"
HN_BYDATE = "https://hn.algolia.com/api/v1/search_by_date"
APIFY_ACTOR = "trudax~reddit-scraper-lite"  # adjust if your token uses another actor
UA = "lior-demand-radar/1.0"


def _get(url):
    r = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(r, timeout=30) as resp:
        return json.loads(resp.read().decode())


def in_lane(title):
    t = (title or "").lower()
    # word-boundary match so short keys (ai, vc) don't hit "brain"/"trails".
    return [k for k in LANE_KEYWORDS if re.search(r"\b" + re.escape(k) + r"\b", t)]


def fetch_hn(days):
    """HN: front page + recent stories, filtered to lane, scored by debate."""
    items = {}
    # 1) current front page
    try:
        for h in _get(HN_SEARCH + "?tags=front_page&hitsPerPage=40").get("hits", []):
            items[h["objectID"]] = h
    except Exception as e:
        sys.stderr.write(f"[warn] HN front_page: {e}\n")
    # 2) recent stories
    ts = int(time.time() - days * 86400)
    q = HN_BYDATE + "?" + urllib.parse.urlencode({
        "tags": "story",
        "numericFilters": f"created_at_i>{ts}",
        "hitsPerPage": 200,
    })
    try:
        for h in _get(q).get("hits", []):
            items.setdefault(h["objectID"], h)
    except Exception as e:
        sys.stderr.write(f"[warn] HN by_date: {e}\n")

    out = []
    for h in items.values():
        hits = in_lane(h.get("title"))
        if not hits:
            continue
        pts = h.get("points") or 0
        cmts = h.get("num_comments") or 0
        age_h = max(1.0, (time.time() - (h.get("created_at_i") or time.time())) / 3600)
        recency = 1.0 if age_h <= 24 else (0.6 if age_h <= 72 else 0.3)
        score = round((cmts * 2 + pts) * (1 + 0.3 * len(hits)) * recency, 1)
        out.append({
            "source": "HN", "title": h.get("title", ""),
            "points": pts, "comments": cmts, "age_h": round(age_h),
            "url": f"https://news.ycombinator.com/item?id={h['objectID']}",
            "matched": hits, "score": score,
        })
    return out


def fetch_reddit_apify(days):
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        return []
    start_urls = [{"url": f"https://www.reddit.com/r/{s}/top/?t=week"} for s in REDDIT_SUBS]
    payload = json.dumps({
        "startUrls": start_urls,
        "maxItems": 120,
        "sort": "top",
        "time": "week",
        "skipComments": True,
    }).encode()
    url = (f"https://api.apify.com/v2/acts/{APIFY_ACTOR}/run-sync-get-dataset-items"
           f"?token={token}")
    try:
        r = urllib.request.Request(url, data=payload,
                                   headers={"User-Agent": UA, "Content-Type": "application/json"})
        with urllib.request.urlopen(r, timeout=180) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        sys.stderr.write(f"[warn] Apify/Reddit failed ({e}). Adjust ACTOR/input if needed.\n")
        return []

    out = []
    for p in data:
        title = p.get("title") or p.get("text") or ""
        ups = p.get("upVotes") or p.get("ups") or p.get("score") or 0
        cmts = p.get("numberOfComments") or p.get("num_comments") or 0
        hits = in_lane(title)
        if not hits:
            continue
        score = round((cmts * 3 + ups) * (1 + 0.3 * len(hits)), 1)
        out.append({
            "source": "Reddit", "title": title[:120],
            "points": ups, "comments": cmts, "age_h": None,
            "url": p.get("url") or p.get("link") or "",
            "matched": hits, "score": score,
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=4)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    pool = fetch_hn(args.days) + fetch_reddit_apify(args.days)
    pool.sort(key=lambda x: x["score"], reverse=True)
    pool = pool[: args.top]

    if args.json:
        print(json.dumps(pool, indent=2))
        return

    has_reddit = any(p["source"] == "Reddit" for p in pool)
    print(f"Demand Radar — HN{' + Reddit(Apify)' if has_reddit else ' only (set APIFY_TOKEN for Reddit)'} "
          f"— last {args.days}d — {len(pool)} signals (comments weighted = debate)\n")
    for i, p in enumerate(pool, 1):
        age = f"{p['age_h']}h" if p["age_h"] is not None else "~wk"
        print(f"{i:>2}. [{p['score']:>7}] {p['source']:<6} {p['points']}up/{p['comments']}c/{age}")
        print(f"    {p['title']}")
        print(f"    {p['url']}")
        print()


if __name__ == "__main__":
    main()
