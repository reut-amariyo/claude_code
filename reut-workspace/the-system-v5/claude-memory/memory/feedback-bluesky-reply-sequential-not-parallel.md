---
name: feedback-bluesky-reply-sequential-not-parallel
description: "scout-reply Bluesky task — find then reply must be sequential, never fabricate uri/cid"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0e735694-4f51-40f5-8f17-0dd1455be2b5
---

The scout-reply (Bluesky and X) flow is strictly sequential: run `find_reply_target_*.py` FIRST, read its actual `uri` and `cid` from the JSON output, THEN write and post the reply with those exact values.

**Why:** On 2026-05-29 I ran the find script and the reply script in the same parallel tool block, passing a fabricated uri/cid I had invented before the find output returned. The reply posted to a non-existent parent (Bluesky's createRecord does not validate parent existence), producing an orphaned, off-topic post on Lior's account that had to be deleted via `com.atproto.repo.deleteRecord`.

**How to apply:** Never call find and reply in one batch. Never invent or reuse a uri/cid from memory/prior context. Copy uri+cid verbatim from THIS run's find output, and the reply text must match the post THIS run's find script returned. The reply script env vars are `BSKY_HANDLE` / `BSKY_APP_PASSWORD` (NOT `BLUESKY_*`) — use these for any manual deleteRecord cleanup. See [[project-x-reply-pipeline-whitelist-collapse]].
