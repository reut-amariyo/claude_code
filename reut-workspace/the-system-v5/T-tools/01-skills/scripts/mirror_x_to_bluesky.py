#!/usr/bin/env python3
"""X -> Bluesky mirror helper.

Detects ORIGINAL agency X posts on @lior_pozin that have NOT yet been mirrored
to Bluesky, so Claude can write an adapted (non-identical) Bluesky version and
publish it via post_bluesky.py.

Two safety nets prevent duplicate Bluesky posts:
  1. State log keyed by tweet_id  -> never mirror the same X post twice
     (needed because the Bluesky version is REWRITTEN, so text won't match).
  2. Live Bluesky-twin check       -> skip any X post that already has a
     near-identical Bluesky post in the lookback window. This catches posts
     made via post_social.py (scout / Reut), which already hit both networks.

Commands:
    mirror_x_to_bluesky.py list-pending [--days N]   # (Metricool path) JSON array to mirror
    mirror_x_to_bluesky.py mark <tweet_id>           # record a tweet as mirrored
    mirror_x_to_bluesky.py is-mirrored <tweet_id>    # prints YES/NO (state-log check)
    mirror_x_to_bluesky.py bluesky-recent [--limit N]  # normalized recent Bluesky post
                                                       # texts (real-time, via atproto).
                                                       # Used to skip scout/post_social
                                                       # cross-posts already on Bluesky.
    mirror_x_to_bluesky.py bootstrap [--days N]      # mark ALL current X posts as
                                                     # mirrored (run once at setup
                                                     # so history isn't back-filled)

NOTE: list-pending/bootstrap read Metricool (METRICOOL_TOKEN). The live mirror now
detects posts by reading x.com via Chrome (Metricool lags 1-2 days and has no thread
metadata), so list-pending is a fallback only. bluesky-recent uses BSKY_HANDLE/
BSKY_APP_PASSWORD. source ~/.zshrc for all.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

METRICOOL_BASE_URL = "https://app.metricool.com/api"
METRICOOL_USER_ID = "4473461"
METRICOOL_BLOG_ID = "5775125"

REPO_ROOT = Path(__file__).resolve().parents[3]  # .../the-system-v5
STATE_FILE = REPO_ROOT / "O-output" / "bluesky-mirror-log.json"

DEFAULT_DAYS = 3
URL_RE = re.compile(r"https?://\S+")
WS_RE = re.compile(r"\s+")


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def _token() -> str:
    token = os.environ.get("METRICOOL_TOKEN")
    if not token:
        print("ERROR: Missing METRICOOL_TOKEN. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)
    return token


def _fetch(network: str, days: int) -> list[dict]:
    token = _token()
    now = datetime.now(timezone.utc)
    from_dt = now - timedelta(days=days)
    url = (
        f"{METRICOOL_BASE_URL}/v2/analytics/posts/{network}"
        f"?blogId={METRICOOL_BLOG_ID}&userId={METRICOOL_USER_ID}"
        f"&from={_iso(from_dt)}&to={_iso(now)}"
    )
    req = urllib.request.Request(url, headers={"X-Mc-Auth": token, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:500]
        print(f"Metricool FAILED ({e.code}) on {network}: {detail}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print(f"Metricool FAILED on {network}: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
    return body.get("data") or []


def _norm(text: str) -> str:
    """Normalize text for cross-network twin comparison."""
    text = URL_RE.sub("", text or "")
    text = WS_RE.sub(" ", text).strip().lower()
    return text


def _is_original(text: str) -> bool:
    """Skip retweets and pure replies; mirror only original posts."""
    t = (text or "").strip()
    if not t:
        return False
    if t.startswith("RT @"):
        return False
    if t.startswith("@"):  # reply that opens by mentioning someone
        return False
    return True


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"mirrored": {}}
    try:
        data = json.loads(STATE_FILE.read_text())
        data.setdefault("mirrored", {})
        return data
    except json.JSONDecodeError:
        return {"mirrored": {}}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2))


def list_pending(days: int) -> list[dict]:
    state = load_state()
    mirrored = state.get("mirrored", {})

    x_posts = _fetch("twitter", days)
    bsky_posts = _fetch("bluesky", days)
    bsky_norms = {_norm(p.get("text", "")) for p in bsky_posts}

    pending = []
    for p in x_posts:
        tid = p.get("tweetId")
        text = p.get("text") or ""
        if not tid:
            continue
        if tid in mirrored:
            continue
        if not _is_original(text):
            continue
        norm = _norm(text)
        if norm and norm in bsky_norms:
            # Already cross-posted to Bluesky (e.g. via post_social.py) -> skip,
            # and remember it so we never reconsider it.
            mirrored[tid] = {"mirrored_at": datetime.now(timezone.utc).isoformat(),
                             "reason": "already_on_bluesky"}
            continue
        created = (p.get("createdAt") or {}).get("dateTime")
        pending.append({
            "tweet_id": tid,
            "created_at": created,
            "text": text,
            "url": p.get("url"),
        })

    save_state(state)  # persist any auto-skips
    pending.sort(key=lambda r: r.get("created_at") or "")
    return pending


def mark(tweet_id: str, reason: str = "mirrored") -> None:
    state = load_state()
    state["mirrored"][tweet_id] = {
        "mirrored_at": datetime.now(timezone.utc).isoformat(),
        "reason": reason,
    }
    save_state(state)
    print(f"Marked {tweet_id} as {reason}.")


def bluesky_recent(limit: int) -> list[str]:
    """Return normalized text of recent Bluesky posts by the account (real-time).

    Used by the Chrome-based mirror to skip X posts that were cross-posted to
    Bluesky via post_social.py (scout / Reut) and therefore already exist there.
    """
    handle = os.environ.get("BSKY_HANDLE")
    pw = os.environ.get("BSKY_APP_PASSWORD")
    if not (handle and pw):
        print("ERROR: Missing BSKY_HANDLE / BSKY_APP_PASSWORD. Run: source ~/.zshrc",
              file=sys.stderr)
        sys.exit(1)
    from atproto import Client
    client = Client()
    client.login(handle, pw)
    out: list[str] = []
    cursor = None
    while len(out) < limit:
        resp = client.get_author_feed(actor=handle, cursor=cursor, limit=min(100, limit - len(out)))
        for item in resp.feed:
            rec = getattr(item.post, "record", None)
            text = getattr(rec, "text", "") if rec else ""
            n = _norm(text)
            if n:
                out.append(n)
        cursor = getattr(resp, "cursor", None)
        if not cursor:
            break
    return out[:limit]


def is_mirrored(tweet_id: str) -> bool:
    return tweet_id in load_state().get("mirrored", {})


def bootstrap(days: int) -> None:
    state = load_state()
    x_posts = _fetch("twitter", days)
    n = 0
    for p in x_posts:
        tid = p.get("tweetId")
        if tid and tid not in state["mirrored"]:
            state["mirrored"][tid] = {
                "mirrored_at": datetime.now(timezone.utc).isoformat(),
                "reason": "bootstrap",
            }
            n += 1
    save_state(state)
    print(f"Bootstrapped {n} existing X posts as already-handled "
          f"(last {days} days). Mirror will only act on NEW posts from now on.")


def main() -> None:
    parser = argparse.ArgumentParser(description="X -> Bluesky mirror helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list-pending")
    p_list.add_argument("--days", type=int, default=DEFAULT_DAYS)

    p_mark = sub.add_parser("mark")
    p_mark.add_argument("tweet_id")

    p_ism = sub.add_parser("is-mirrored")
    p_ism.add_argument("tweet_id")

    p_bsr = sub.add_parser("bluesky-recent")
    p_bsr.add_argument("--limit", type=int, default=50)

    p_boot = sub.add_parser("bootstrap")
    p_boot.add_argument("--days", type=int, default=30)

    args = parser.parse_args()

    if args.cmd == "list-pending":
        print(json.dumps(list_pending(args.days), ensure_ascii=False, indent=2))
    elif args.cmd == "mark":
        mark(args.tweet_id)
    elif args.cmd == "is-mirrored":
        print("YES" if is_mirrored(args.tweet_id) else "NO")
    elif args.cmd == "bluesky-recent":
        for t in bluesky_recent(args.limit):
            print(t)
    elif args.cmd == "bootstrap":
        bootstrap(args.days)


if __name__ == "__main__":
    main()
