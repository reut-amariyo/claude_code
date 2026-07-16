#!/usr/bin/env python3
"""Schedule a Threads-ONLY post via Metricool (@lior on Threads).

Twin of post_bluesky_metricool.py. Used by the X -> Bluesky/Threads mirror to
publish a refreshed (non-identical) version of an agency X post to Threads.
Metricool already holds the Threads connection for the "Lior Pozin" blog, so no
Meta Graph API token is needed.

Usage:
    post_threads_metricool.py "post text" ["2026-06-23T15:15:00" | "HH:MM"] [--draft]

- schedule_time is ISO local (Asia/Jerusalem). If omitted, +2 min from now.
- --draft creates a Metricool draft instead of publishing (for safe testing).
"""

import sys
import os
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

METRICOOL_BASE_URL = "https://app.metricool.com/api"
METRICOOL_USER_ID = "4473461"
METRICOOL_BLOG_ID = "5775125"

THREADS_MAX_CHARS = 500


def post_to_metricool(text, schedule_time=None, draft=False):
    token = os.environ.get("METRICOOL_TOKEN")
    if not token:
        print("ERROR: Missing METRICOOL_TOKEN env var. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    israel_tz = timezone(timedelta(hours=3))

    if schedule_time and "T" in schedule_time:
        date_str = schedule_time
    elif schedule_time and ":" in schedule_time:
        hour, minute = map(int, schedule_time.split(":"))
        now = datetime.now(israel_tz)
        publish_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        date_str = publish_time.strftime("%Y-%m-%dT%H:%M:%S")
    else:
        publish_time = datetime.now(israel_tz) + timedelta(minutes=2)
        date_str = publish_time.strftime("%Y-%m-%dT%H:%M:%S")

    payload = {
        "autoPublish": not draft,
        "descendants": [],
        "draft": draft,
        "media": [],
        "mediaAltText": [],
        "providers": [
            {"network": "threads"},
        ],
        "publicationDate": {
            "dateTime": date_str,
            "timezone": "Asia/Jerusalem",
        },
        "shortener": False,
        "smartLinkData": {"ids": []},
        "text": text,
    }

    url = (
        f"{METRICOOL_BASE_URL}/v2/scheduler/posts"
        f"?blogId={METRICOOL_BLOG_ID}&userId={METRICOOL_USER_ID}"
    )

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "X-Mc-Auth": token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            kind = "DRAFT created" if draft else f"scheduled for {date_str} (Israel time)"
            print(f"Metricool SUCCESS (Threads only): {kind}")
            print(f"  -> Threads (@lior)")
            if isinstance(body, dict) and body.get("id"):
                print(f"  -> Post ID: {body['id']}")
            return body
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print(f"Metricool FAILED ({e.code}): {error_body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Metricool FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    args = [a for a in sys.argv[1:]]
    draft = "--draft" in args
    args = [a for a in args if a != "--draft"]

    if not args:
        print('Usage: post_threads_metricool.py "post text" [ISO datetime or HH:MM] [--draft]', file=sys.stderr)
        sys.exit(1)

    post_text = args[0]
    schedule_time = args[1] if len(args) > 1 else None

    if len(post_text) > THREADS_MAX_CHARS:
        print(
            f"ERROR: Post too long ({len(post_text)} chars). Max {THREADS_MAX_CHARS} for Threads.",
            file=sys.stderr,
        )
        sys.exit(1)

    post_to_metricool(post_text, schedule_time, draft=draft)


if __name__ == "__main__":
    main()
