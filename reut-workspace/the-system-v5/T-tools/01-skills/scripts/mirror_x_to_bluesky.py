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
    mirror_x_to_bluesky.py fetch-candidates [--days N]  # PRIMARY detection. Grok
                                                       # x_search (XAI_API_KEY) reads
                                                       # @lior_pozin with NO Chrome/
                                                       # Mac-awake dependency, then
                                                       # runs the full dedup (state
                                                       # log + live Bluesky twin
                                                       # guard) and returns a
                                                       # mirror-ready JSON array.
                                                       # Exit 2 = detection down
                                                       # (credit/API), NOT "no posts".
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

GROK_URL = "https://api.x.ai/v1/responses"
GROK_MODEL = "grok-4-fast-non-reasoning"
X_HANDLE = "lior_pozin"
CANDIDATE_DAYS = 2  # only mirror today/yesterday, matching the Chrome flow

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


def _grok_fetch_x_posts(days: int) -> list[dict]:
    """Detect recent @lior_pozin posts via Grok x_search (no Chrome needed).

    Replaces the fragile Chrome scrape: Grok's x_search returns tweet_id, date,
    repost/reply flags and FULL verbatim text with no browser or Mac-awake
    dependency. Exits 2 on a credit/spend error so the caller can tell
    "detection is down" apart from "no new posts".
    """
    import requests  # local import: only this path needs it

    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        print("ERROR: Missing XAI_API_KEY. Run: source ~/.zshrc", file=sys.stderr)
        sys.exit(1)

    prompt = (
        f"Search X for the most recent original posts by @{X_HANDLE} from the "
        f"last {days} days.\n"
        "Include self-reply threads by the same author (treat each thread as ONE "
        "post: concatenate the author's consecutive self-replies in order into the "
        "TEXT). EXCLUDE reposts/retweets and replies to OTHER people's posts.\n"
        "Return the FULL verbatim text, never a summary, and never invent a post.\n"
        "For EACH post output exactly these lines, in this order:\n"
        "TWEET_ID: <numeric id of the root post>\n"
        "DATE: <ISO 8601 timestamp>\n"
        "IS_REPLY_TO_OTHERS: <yes/no>\n"
        "IS_REPOST: <yes/no>\n"
        "TEXT: <full verbatim text>\n"
        "---\n"
    )
    payload = {
        "model": GROK_MODEL,
        "stream": False,
        "input": [{"role": "user", "content": prompt}],
        "tools": [{"type": "x_search"}],
    }
    try:
        resp = requests.post(
            GROK_URL,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=payload,
            timeout=120,
        )
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        body = (getattr(resp, "text", "") or "").lower()
        status = getattr(resp, "status_code", None)
        if status == 403 and ("credit" in body or "spending limit" in body
                              or "used all available" in body):
            print("ERROR: xAI credits/spending limit exhausted — detection unavailable. "
                  "Top up at console.x.ai. NOT treating this as 'no new posts'.",
                  file=sys.stderr)
            sys.exit(2)
        print(f"ERROR: Grok API request failed: {e}", file=sys.stderr)
        sys.exit(2)
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Grok API request failed: {e}", file=sys.stderr)
        sys.exit(2)

    data = resp.json()
    raw = ""
    for item in data.get("output", []):
        if item.get("type") == "message":
            for c in item.get("content", []):
                if c.get("type") == "output_text":
                    raw += c.get("text", "")
    if not raw.strip():
        print("ERROR: Empty response from Grok x_search.", file=sys.stderr)
        sys.exit(2)

    posts: list[dict] = []
    for block in raw.split("\n---"):
        block = block.strip()
        if "TWEET_ID:" not in block or "TEXT:" not in block:
            continue
        tid_m = re.search(r"TWEET_ID:\s*(\d+)", block)
        if not tid_m:
            continue
        date_m = re.search(r"DATE:\s*(\S+)", block)
        rep_m = re.search(r"IS_REPLY_TO_OTHERS:\s*(\w+)", block, re.I)
        rpt_m = re.search(r"IS_REPOST:\s*(\w+)", block, re.I)
        text_m = re.search(r"TEXT:\s*(.*)", block, re.S)
        posts.append({
            "tweet_id": tid_m.group(1),
            "created_at": date_m.group(1) if date_m else None,
            "is_reply_to_others": bool(rep_m and rep_m.group(1).lower().startswith("y")),
            "is_repost": bool(rpt_m and rpt_m.group(1).lower().startswith("y")),
            "text": (text_m.group(1).strip() if text_m else ""),
        })
    return posts


def _within_days(iso: str | None, days: int) -> bool:
    if not iso:
        return True  # keep if undated; state-log + twin-guard still protect us
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return True
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt >= datetime.now(timezone.utc) - timedelta(days=days)


def fetch_candidates(days: int) -> list[dict]:
    """Return NEW original @lior_pozin posts that still need mirroring.

    Full detection+dedup in one call so the mirror skill no longer touches Chrome:
      Grok x_search -> drop reposts/other-replies/old -> state-log skip ->
      live Bluesky twin-guard (auto-marks twins) -> mirror-ready JSON.
    """
    state = load_state()
    mirrored = state.get("mirrored", {})

    raw_posts = _grok_fetch_x_posts(days)
    try:
        bsky_norms = set(bluesky_recent(60))
    except SystemExit:
        raise
    except Exception:  # noqa: BLE001
        bsky_norms = set()  # twin-guard is best-effort; state log is the hard gate

    pending: list[dict] = []
    seen_ids: set[str] = set()
    for p in raw_posts:
        tid = p.get("tweet_id")
        text = p.get("text") or ""
        if not tid or tid in seen_ids:
            continue
        seen_ids.add(tid)
        if p.get("is_repost") or p.get("is_reply_to_others"):
            continue
        if not _is_original(text):
            continue
        if not _within_days(p.get("created_at"), days):
            continue
        if tid in mirrored:
            continue
        norm = _norm(text)
        if norm and norm in bsky_norms:
            mirrored[tid] = {"mirrored_at": datetime.now(timezone.utc).isoformat(),
                             "reason": "already_on_bluesky"}
            continue
        pending.append({
            "tweet_id": tid,
            "created_at": p.get("created_at"),
            "text": text,
            "url": f"https://x.com/{X_HANDLE}/status/{tid}",
        })

    save_state(state)  # persist any twin auto-skips
    pending.sort(key=lambda r: r.get("created_at") or "")
    return pending


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

    p_fc = sub.add_parser("fetch-candidates")
    p_fc.add_argument("--days", type=int, default=CANDIDATE_DAYS)

    args = parser.parse_args()

    if args.cmd == "list-pending":
        print(json.dumps(list_pending(args.days), ensure_ascii=False, indent=2))
    elif args.cmd == "fetch-candidates":
        print(json.dumps(fetch_candidates(args.days), ensure_ascii=False, indent=2))
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
