#!/usr/bin/env python3
"""Post text to X (@lior_pozin) and Bluesky (@liorpozin.bsky.social) via Metricool."""

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
    """Post to Metricool for X + Bluesky.

    Args:
        text: The post text.
        schedule_time: Optional ISO datetime string (e.g. "2026-03-31T16:00:00")
                       or "HH:MM" for today in Israel time.
                       If None, schedules 2 minutes from now.
    """
    token = os.environ.get("METRICOOL_TOKEN")
    if not token:
        print("ERROR: Missing METRICOOL_TOKEN env var. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    israel_tz = timezone(timedelta(hours=3))

    if schedule_time and "T" in schedule_time:
        date_str = schedule_time
    elif schedule_time and ":" in schedule_time:
        # "HH:MM" format - schedule for today at that time
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
            {"network": "twitter"},
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
            print(f"Metricool SUCCESS: Post scheduled for {date_str} (Israel time)")
            print(f"  -> X (@lior_pozin) + Bluesky (@liorpozin.bsky.social)")
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
        print('Usage: post_social.py "post text" [HH:MM or ISO datetime]', file=sys.stderr)
        sys.exit(1)

    post_text = sys.argv[1]
    schedule_time = sys.argv[2] if len(sys.argv) > 2 else None

    if len(post_text) > 500:
        print(
            f"ERROR: Post too long ({len(post_text)} chars). Max ~280 for X.",
            file=sys.stderr,
        )
        sys.exit(1)

    post_to_metricool(post_text, schedule_time)


if __name__ == "__main__":
    main()
