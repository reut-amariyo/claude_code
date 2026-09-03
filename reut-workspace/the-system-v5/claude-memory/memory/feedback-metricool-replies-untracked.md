---
name: Metricool doesn't track X replies
description: When auditing X reply volume, don't infer from Metricool's posts.jsonl — it doesn't log replies posted via reply_x.py
type: feedback
originSessionId: a571877e-534b-47fa-b560-808044856001
---
Metricool's `posts.jsonl` log does NOT capture replies posted via `T-tools/01-skills/scripts/reply_x.py`. Replies go directly to X via the X API, bypassing Metricool entirely. The fetcher (`fetch_post_performance.py`) only sees originals + the rare reply that was scheduled through Metricool.

**Why:** The reply pipeline uses a different code path. Replies are time-sensitive and need to ship immediately on the trending post — they don't go through Metricool's scheduling layer.

**How to apply:** Never claim the "reply pipeline is broken" or "scout-reply-x tasks are failing" based solely on absent Metricool log entries. To audit actual reply volume, check Lior's X profile directly, or add explicit logging to `reply_x.py`. Reut confirmed this on 2026-05-06 after I incorrectly flagged the reply pipeline as broken in the weekly analyst output.
