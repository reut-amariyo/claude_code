#!/usr/bin/env python3
"""Fetch X (Twitter) post performance for @lior_pozin from Metricool analytics.

Writes/updates an append-only JSONL log at
`O-output/x-performance-log/posts.jsonl`. Each post is upserted by tweetId so
repeated runs keep metrics fresh without duplicating rows.

Usage:
    fetch_post_performance.py              # default: last 2 days
    fetch_post_performance.py --days 7     # last 7 days
    fetch_post_performance.py --days 60    # backfill
    fetch_post_performance.py --days 7 --summary   # also print a text summary
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

METRICOOL_BASE_URL = "https://app.metricool.com/api"
METRICOOL_USER_ID = "4473461"
METRICOOL_BLOG_ID = "5775125"

REPO_ROOT = Path(__file__).resolve().parents[3]  # .../the-system-v5
LOG_DIR = REPO_ROOT / "O-output" / "x-performance-log"
LOG_FILE = LOG_DIR / "posts.jsonl"


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def fetch_twitter_posts(days: int) -> list[dict]:
    token = os.environ.get("METRICOOL_TOKEN")
    if not token:
        print("ERROR: Missing METRICOOL_TOKEN. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    now = datetime.now(timezone.utc)
    from_dt = now - timedelta(days=days)

    url = (
        f"{METRICOOL_BASE_URL}/v2/analytics/posts/twitter"
        f"?blogId={METRICOOL_BLOG_ID}&userId={METRICOOL_USER_ID}"
        f"&from={_iso(from_dt)}&to={_iso(now)}"
    )

    req = urllib.request.Request(
        url,
        headers={"X-Mc-Auth": token, "Accept": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:500]
        print(f"Metricool FAILED ({e.code}): {detail}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print(f"Metricool FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)

    return body.get("data") or []


def normalize(post: dict) -> dict:
    """Flatten Metricool's record into a stable row."""
    created = (post.get("createdAt") or {}).get("dateTime")
    return {
        "tweet_id": post.get("tweetId"),
        "created_at": created,
        "text": post.get("text") or "",
        "url": post.get("url"),
        "impressions": post.get("totalImpressions") or 0,
        "likes": post.get("totalLikes") or 0,
        "retweets": post.get("totalRetweets") or 0,
        "replies": post.get("totalReplies") or 0,
        "quotes": post.get("totalQuotes") or 0,
        "link_clicks": post.get("totalLinkClicks") or 0,
        "profile_clicks": post.get("totalProfileClicks") or 0,
        "video_views": post.get("totalVideoViews") or 0,
        "engagement": post.get("totalEngagement") or 0.0,
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }


def upsert_log(rows: list[dict]) -> tuple[int, int]:
    """Merge rows into posts.jsonl by tweet_id. Returns (new, updated)."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    existing: dict[str, dict] = {}
    if LOG_FILE.exists():
        with LOG_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    if rec.get("tweet_id"):
                        existing[rec["tweet_id"]] = rec
                except json.JSONDecodeError:
                    continue

    new_count = 0
    updated_count = 0
    for row in rows:
        tid = row.get("tweet_id")
        if not tid:
            continue
        if tid in existing:
            # Preserve first_seen timestamp if present
            row["first_seen"] = existing[tid].get("first_seen") or existing[tid].get("last_updated")
            updated_count += 1
        else:
            row["first_seen"] = row["last_updated"]
            new_count += 1
        existing[tid] = row

    # Sort by created_at descending for readability
    ordered = sorted(
        existing.values(),
        key=lambda r: r.get("created_at") or "",
        reverse=True,
    )
    with LOG_FILE.open("w", encoding="utf-8") as f:
        for rec in ordered:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    return new_count, updated_count


def print_summary(rows: list[dict]) -> None:
    if not rows:
        print("No posts in window.")
        return
    sorted_rows = sorted(rows, key=lambda r: r.get("impressions") or 0, reverse=True)
    total_imp = sum(r.get("impressions") or 0 for r in rows)
    total_eng = sum(r.get("engagement") or 0 for r in rows)
    print(f"\n{len(rows)} posts | total impressions={total_imp} | total engagement={total_eng:.1f}")
    print("\nTop 5 by impressions:")
    for r in sorted_rows[:5]:
        text = (r.get("text") or "").replace("\n", " ")[:90]
        print(
            f"  {r.get('created_at','?')[:16]}  "
            f"imp={r.get('impressions',0):>5}  "
            f"likes={r.get('likes',0):>3}  "
            f"rep={r.get('replies',0):>3}  "
            f"rt={r.get('retweets',0):>3}  "
            f"| {text}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=2, help="Lookback window in days (default 2)")
    parser.add_argument("--summary", action="store_true", help="Print a text summary of the window")
    args = parser.parse_args()

    raw = fetch_twitter_posts(days=args.days)
    rows = [normalize(p) for p in raw if p.get("tweetId")]
    new_count, updated_count = upsert_log(rows)

    print(
        f"Metricool: fetched {len(rows)} posts over last {args.days}d "
        f"| {new_count} new, {updated_count} updated -> {LOG_FILE}"
    )

    if args.summary:
        print_summary(rows)


if __name__ == "__main__":
    main()
