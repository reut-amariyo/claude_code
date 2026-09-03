---
name: project-bluesky-reply-dedup-log-drops-entries
description: "Bluesky scout-reply dedup log silently drops already-replied entries, re-surfacing old posts (double-reply risk)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 27b65b93-8c5b-40d7-9e2e-bf871004b752
---

The Bluesky scout-reply dedup log `~/.scout-replies-bluesky-log.json` is unreliable: entries for already-replied posts vanish over time. Observed 2026-06-14 during `scout-reply-09` — the log shrank 61→56 entries mid-run and a post replied to on 2026-06-06 (@edzitron.com `3mnkkzjscx224`, three "success" records) disappeared entirely. Some concurrent process (likely a sibling scout-reply slot or a buggy dedup pass) rewrites the file and removes records.

Consequence: `find_reply_target_bluesky.py` keeps returning posts that were already replied to (it only excludes URIs still present in the log). It also returns off-topic gaming posts (e.g. @duckaislop "Steam disclosure" game launches) and the script just picks the single top-liked candidate, so a stale/off-topic top result blocks everything.

**Why:** trusting the dedup log blindly risks violating Lior's hard rule "never reply twice to the same post" ([[feedback-linkedin-comments-manual-posting]] reply rules).

**How to apply:** when running the Bluesky scout-reply task, don't rely on the script's single pick. Pull the full candidate pool across all queries, exclude the union of every URI you've seen logged this session (not just the current file), drop gaming/off-topic, and pick a genuinely fresh SaaS/AI/founder post. On 2026-06-14 I bypassed the bug this way and replied to @sanity.io's AI-first-engineering post. Recurred 2026-06-27 (`scout-reply-04`): @duckaislop "Escape the Grind / SetForMoney Studios. Steam disclosure" was again the deterministic top pick (13 likes) and returned identically on two runs; bypassed via full-pool pull and replied to @edzitron.com's "AI has no real ROI" post instead. Related: [[feedback-bluesky-reply-sequential-not-parallel]], [[project-x-reply-pipeline-whitelist-collapse]].
