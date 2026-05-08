#!/usr/bin/env python3
"""
Fetch Lior's LinkedIn post performance from Metricool and upsert into
O-output/linkedin-performance-log/posts.jsonl.

Credentials live in ~/.config/metricool/.env (chmod 600).
Run nightly via scheduled task `linkedin-analyst-daily`.

Usage:
    python3 fetch_linkedin_performance.py                  # last 30 days
    python3 fetch_linkedin_performance.py --days 90        # last 90 days
    python3 fetch_linkedin_performance.py --from 2026-01-01 --to 2026-05-03

Engagement on a post keeps growing for days after it's published, so this is an
upsert: existing postIds are overwritten with the latest metrics, new postIds
are appended. The file stays sorted by post creation time, newest first.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
LOG_PATH = REPO_ROOT / "O-output" / "linkedin-performance-log" / "posts.jsonl"
ENV_PATH = Path.home() / ".config" / "metricool" / ".env"
API_URL = "https://app.metricool.com/api/v2/analytics/posts/linkedin"


def load_env(path: Path) -> dict[str, str]:
    if not path.exists():
        sys.exit(f"Missing credentials file: {path}")
    out: dict[str, str] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        k, _, v = line.partition("=")
        out[k.strip()] = v.strip()
    return out


def fetch(token: str, user_id: str, blog_id: str, start: datetime, end: datetime) -> list[dict]:
    params = {
        "from": start.strftime("%Y-%m-%dT%H:%M:%S"),
        "to": end.strftime("%Y-%m-%dT%H:%M:%S"),
        "blogId": blog_id,
        "userId": user_id,
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"X-Mc-Auth": token})
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    posts = body.get("data", [])
    if not isinstance(posts, list):
        sys.exit(f"Unexpected API response shape: {body!r}")
    return posts


def load_existing(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    by_id: dict[str, dict] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        by_id[rec["postId"]] = rec
    return by_id


def write_log(path: Path, records: dict[str, dict]) -> None:
    def sort_key(r: dict) -> str:
        c = r.get("created", {})
        return c.get("dateTime", "") if isinstance(c, dict) else ""

    ordered = sorted(records.values(), key=sort_key, reverse=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for rec in ordered:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=30, help="Days back from today (ignored if --from/--to given)")
    parser.add_argument("--from", dest="start", help="Start date YYYY-MM-DD")
    parser.add_argument("--to", dest="end", help="End date YYYY-MM-DD")
    args = parser.parse_args()

    env = load_env(ENV_PATH)
    token = env.get("METRICOOL_API_TOKEN") or os.environ.get("METRICOOL_API_TOKEN")
    user_id = env.get("METRICOOL_USER_ID") or os.environ.get("METRICOOL_USER_ID")
    blog_id = env.get("METRICOOL_LIOR_LINKEDIN_BLOG_ID") or os.environ.get("METRICOOL_LIOR_LINKEDIN_BLOG_ID")
    if not (token and user_id and blog_id):
        sys.exit("Missing METRICOOL_API_TOKEN / METRICOOL_USER_ID / METRICOOL_LIOR_LINKEDIN_BLOG_ID in env")

    if args.start and args.end:
        start = datetime.fromisoformat(args.start)
        end = datetime.fromisoformat(args.end).replace(hour=23, minute=59, second=59)
    else:
        end = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)
        start = end - timedelta(days=args.days)

    posts = fetch(token, user_id, blog_id, start, end)
    existing = load_existing(LOG_PATH)
    new_count = 0
    updated_count = 0
    for p in posts:
        pid = p.get("postId")
        if not pid:
            continue
        p["_fetchedAt"] = datetime.utcnow().isoformat(timespec="seconds") + "Z"
        if pid in existing:
            updated_count += 1
        else:
            new_count += 1
        existing[pid] = p
    write_log(LOG_PATH, existing)

    print(f"Range: {start.date()} .. {end.date()}")
    print(f"Fetched: {len(posts)}  | New: {new_count}  | Updated: {updated_count}  | Total in log: {len(existing)}")
    print(f"Log: {LOG_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
