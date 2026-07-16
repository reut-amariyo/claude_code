#!/usr/bin/env python3
"""Post to Bluesky (@liorpozin.bsky.social) via AT Protocol — single post or thread.

Posts IMMEDIATELY (not scheduled). Used by the X->Bluesky mirror so agency X
posts get an adapted Bluesky version. Supports native Bluesky threads so that
long X posts (>300 chars) can be split across linked posts without losing
content.

Usage:
    post_bluesky.py "single post text"                 # one post
    post_bluesky.py "part 1 text" "part 2 text" ...    # a thread (each <=300)

Each argument is one post in the thread, in order. Every part must be <=300
characters (Bluesky's hard limit). The caller (Claude) decides whether to
condense into one part or split into a thread.

Requires env: BSKY_HANDLE, BSKY_APP_PASSWORD (source ~/.zshrc).
"""

import sys
import os

BLUESKY_LIMIT = 300


def main():
    parts = [a for a in sys.argv[1:]]
    if not parts:
        print('Usage: post_bluesky.py "post text" ["part 2" ...]', file=sys.stderr)
        sys.exit(1)

    # Validate every part up front so we never post a half thread.
    too_long = [(i + 1, len(p)) for i, p in enumerate(parts) if len(p) > BLUESKY_LIMIT]
    if too_long:
        for idx, n in too_long:
            print(f"ERROR: thread part {idx} is {n} chars (Bluesky limit is {BLUESKY_LIMIT}).",
                  file=sys.stderr)
        print("Re-split so each part is <=300 chars, then retry.", file=sys.stderr)
        sys.exit(1)

    required = ["BSKY_HANDLE", "BSKY_APP_PASSWORD"]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        print(f"ERROR: Missing env vars: {', '.join(missing)}. Run: source ~/.zshrc",
              file=sys.stderr)
        sys.exit(1)

    from atproto import Client, models

    client = Client()
    client.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_APP_PASSWORD"])

    try:
        # First post = thread root.
        root = client.send_post(text=parts[0])
        print(f"Bluesky SUCCESS (1/{len(parts)}): {root.uri}")

        root_ref = models.ComAtprotoRepoStrongRef.Main(uri=root.uri, cid=root.cid)
        parent_ref = root_ref

        # Remaining parts chain as replies: root stays fixed, parent advances.
        for i, text in enumerate(parts[1:], start=2):
            reply_ref = models.AppBskyFeedPost.ReplyRef(parent=parent_ref, root=root_ref)
            res = client.send_post(text=text, reply_to=reply_ref)
            print(f"Bluesky SUCCESS ({i}/{len(parts)}): {res.uri}")
            parent_ref = models.ComAtprotoRepoStrongRef.Main(uri=res.uri, cid=res.cid)

        if len(parts) == 1:
            print("  -> Posted single post to Bluesky (@liorpozin.bsky.social)")
        else:
            print(f"  -> Posted {len(parts)}-post thread to Bluesky (@liorpozin.bsky.social)")
    except Exception as e:  # noqa: BLE001
        print(f"Bluesky FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
