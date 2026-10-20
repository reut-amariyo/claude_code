#!/usr/bin/env python3
"""Prune Lior's Bluesky account (@liorpozin.bsky.social): delete posts with no replies.

Two-step, never deletes on a scan:
    bluesky_prune.py scan                 # dry run: writes O-output/bluesky-prune-scan.json + prints summary
    bluesky_prune.py delete               # deletes every URI marked delete=true in the scan file
    bluesky_prune.py delete --keep-liked  # same, but spare posts that got >=1 like or repost

A post is marked for deletion when its reply count is 0. Reply count comes
from the live app.bsky.feed.getPosts hydration, so self-replies inside a
thread DO count as replies for the parent; a thread root is therefore kept
only if the thread has at least one reply, which is what we want visually.

Requires env: BSKY_HANDLE, BSKY_APP_PASSWORD (source ~/.zshrc).
"""

import json
import os
import sys
import time
from pathlib import Path

from atproto import Client

SCAN_FILE = Path(__file__).resolve().parents[3] / "O-output" / "bluesky-prune-scan.json"
BATCH = 25


def login():
    for k in ("BSKY_HANDLE", "BSKY_APP_PASSWORD"):
        if not os.environ.get(k):
            sys.exit(f"ERROR: missing env {k}. Run: source ~/.zshrc")
    c = Client()
    c.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_APP_PASSWORD"])
    return c


def list_all_post_uris(client):
    """Every app.bsky.feed.post record in the repo, oldest -> newest."""
    did = client.me.did
    uris, cursor = [], None
    while True:
        res = client.com.atproto.repo.list_records({
            "repo": did, "collection": "app.bsky.feed.post", "limit": 100, "cursor": cursor,
        })
        for rec in res.records:
            v = rec.value
            reply = getattr(v, "reply", None)
            uris.append({
                "uri": rec.uri,
                "created_at": getattr(v, "created_at", None),
                "text": getattr(v, "text", "") or "",
                "is_reply": reply is not None,
                "parent_uri": reply.parent.uri if reply else None,
                "root_uri": reply.root.uri if reply else None,
            })
        cursor = res.cursor
        if not cursor:
            break
    return uris


def hydrate(client, records):
    """Attach like/repost/reply counts via getPosts, 25 at a time."""
    by_uri = {r["uri"]: r for r in records}
    all_uris = list(by_uri)
    for i in range(0, len(all_uris), BATCH):
        chunk = all_uris[i:i + BATCH]
        res = client.app.bsky.feed.get_posts({"uris": chunk})
        for p in res.posts:
            r = by_uri[p.uri]
            r["replies"] = p.reply_count or 0
            r["likes"] = p.like_count or 0
            r["reposts"] = p.repost_count or 0
            r["quotes"] = getattr(p, "quote_count", 0) or 0
        time.sleep(0.2)
    for r in records:
        r.setdefault("replies", 0); r.setdefault("likes", 0)
        r.setdefault("reposts", 0); r.setdefault("quotes", 0)
    return records


def scan():
    client = login()
    me_did = client.me.did
    records = hydrate(client, list_all_post_uris(client))
    for r in records:
        # replies to OTHER people's posts (reply_bluesky.py output) vs own-thread continuations
        r["reply_to_self"] = bool(r["is_reply"] and r["parent_uri"] and f"at://{me_did}/" in r["parent_uri"])
        r["reply_to_other"] = bool(r["is_reply"] and not r["reply_to_self"])
        r["delete"] = r["replies"] == 0

    SCAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    SCAN_FILE.write_text(json.dumps(records, indent=1, ensure_ascii=False))

    n = len(records)
    top = [r for r in records if not r["is_reply"]]
    to_self = [r for r in records if r["reply_to_self"]]
    to_other = [r for r in records if r["reply_to_other"]]
    dele = [r for r in records if r["delete"]]
    keep = [r for r in records if not r["delete"]]
    liked_but_no_reply = [r for r in dele if r["likes"] + r["reposts"] + r["quotes"] > 0]

    print(f"Total post records: {n}")
    print(f"  top-level posts:            {len(top)}")
    print(f"  own-thread continuations:   {len(to_self)}")
    print(f"  replies to other accounts:  {len(to_other)}")
    print()
    print(f"WOULD DELETE (0 replies):     {len(dele)}")
    print(f"  of which have likes/reposts: {len(liked_but_no_reply)}")
    print(f"WOULD KEEP (>=1 reply):       {len(keep)}")
    print()
    print("Posts that would be KEPT:")
    for r in sorted(keep, key=lambda x: -x["replies"]):
        print(f"  replies={r['replies']:>2} likes={r['likes']:>2}  {r['created_at'][:10]}  {r['text'][:80]!r}")
    print()
    print("Top liked posts that would still be DELETED (no replies):")
    for r in sorted(liked_but_no_reply, key=lambda x: -(x["likes"] + x["reposts"]))[:15]:
        print(f"  likes={r['likes']:>2} rt={r['reposts']}  {r['created_at'][:10]}  {r['text'][:80]!r}")
    print(f"\nScan written to {SCAN_FILE}")


def delete(keep_liked=False):
    if not SCAN_FILE.exists():
        sys.exit("No scan file. Run `bluesky_prune.py scan` first.")
    records = json.loads(SCAN_FILE.read_text())
    targets = [r for r in records if r["delete"]]
    if keep_liked:
        targets = [r for r in targets if r["likes"] + r["reposts"] + r["quotes"] == 0]
    print(f"Deleting {len(targets)} posts...")
    client = login()
    did = client.me.did
    done, failed = 0, []
    # newest first so thread children go before their roots
    for r in sorted(targets, key=lambda x: x["created_at"] or "", reverse=True):
        rkey = r["uri"].rsplit("/", 1)[-1]
        try:
            client.com.atproto.repo.delete_record({
                "repo": did, "collection": "app.bsky.feed.post", "rkey": rkey,
            })
            done += 1
            if done % 25 == 0:
                print(f"  {done}/{len(targets)}")
            time.sleep(0.15)
        except Exception as e:  # noqa: BLE001
            failed.append((r["uri"], str(e)[:120]))
    print(f"Deleted {done}. Failed {len(failed)}.")
    for u, e in failed:
        print(f"  FAIL {u}: {e}")
    log = SCAN_FILE.with_name("bluesky-prune-deleted.json")
    log.write_text(json.dumps(targets, indent=1, ensure_ascii=False))
    print(f"Deleted list archived at {log}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] not in ("scan", "delete"):
        sys.exit(__doc__)
    if args[0] == "scan":
        scan()
    else:
        delete(keep_liked="--keep-liked" in args)
