---
name: feedback-x-analyst-daily-disabled
description: The x-analyst-daily scheduled task is disabled per Reut (2026-07-19) — do not run the daily X performance fetch
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1572b2fd-e57b-4bf8-a362-1d815f0759f8
---

Reut disabled the `x-analyst-daily` scheduled task on 2026-07-19 ("לא צריך להריץ אותו יותר"). It used to run `fetch_post_performance.py --days 2` nightly to refresh the X performance log.

**Why:** Reut no longer wants the automated daily X performance ingest running.

**How to apply:** Do not run the daily fetch or re-enable this task unless Reut explicitly asks. The weekly analyst (`x-analyst-weekly`) still runs. Related: [[lior-x-data-rules]].
