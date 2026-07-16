#!/usr/bin/env python3
"""Schedule a Bluesky-ONLY post via Metricool (@liorpozin.bsky.social).

Unlike post_social.py (which targets X + Bluesky), this targets Bluesky only —
used by the X->Bluesky mirror so it never re-posts to X.

Usage: post_bluesky_metricool.py "post text" "2026-06-14T15:15:00"
The schedule_time is ISO local (Asia/Jerusalem). If omitted, +2 min from now.
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


def post_to_metricool(text, schedule_time=None):
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
        "autoPublish": True,
        "descendants": [],
        "draft": False,
        "media": [],
        "mediaAltText": [],
        "providers": [
            {"network": "bluesky"},
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
            print(f"Metricool SUCCESS (Bluesky only): scheduled for {date_str} (Israel time)")
            print(f"  -> Bluesky (@liorpozin.bsky.social)")
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
    if len(sys.argv) < 2:
        print('Usage: post_bluesky_metricool.py "post text" [ISO datetime or HH:MM]', file=sys.stderr)
        sys.exit(1)

    post_text = sys.argv[1]
    schedule_time = sys.argv[2] if len(sys.argv) > 2 else None

    if len(post_text) > 300:
        print(
            f"ERROR: Post too long ({len(post_text)} chars). Max 300 for Bluesky.",
            file=sys.stderr,
        )
        sys.exit(1)

    post_to_metricool(post_text, schedule_time)


if __name__ == "__main__":
    main()
