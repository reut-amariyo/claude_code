---
name: linkedin-followers
description: >
  This skill should be used when the user asks for the "monthly LinkedIn report", "how are we
  doing on followers", "follower growth", "did the post work", "KPI update", or wants to
  measure LinkedIn performance against the follower target.
metadata:
  version: "0.1.0"
---

# LinkedIn follower reporting

Read `${CLAUDE_PLUGIN_ROOT}/references/kpi.md`.

**The headline metric is net new followers per month.** Impressions are a diagnostic row,
never the headline.

## The monthly report

Report the three-term decomposition, not a single number:

```
followers = impressions × (profile visits / impressions) × (follows / profile visits)
               reach            curiosity rate                profile conversion
```

- If **curiosity rate** is weak, posts travel but nobody wants to know who wrote them. That
  is a hook and topic problem.
- If **profile conversion** is weak, the profile page loses the person. That is a headline,
  About and Featured problem, and it is the cheapest thing to fix.

## What to pull

| Cadence | What | Where |
|---|---|---|
| Weekly, Monday | Daily new-follower series for the past 7 days, joined to posts published | Analytics → Audience, daily view |
| Monthly | Net new followers, profile visits, impressions, post count, saves per post | Creator Analytics, custom range |
| Backfill, still missing | Monthly profile visits, April 2026 onward | Analytics → Profile viewers, one custom range per month |

**Monthly profile visits have never been pulled.** Until they exist, the middle of the funnel
cannot be diagnosed. Say this every time it is still missing.

## Per-post attribution

LinkedIn does not report followers per post. Build it: take the daily new-follower series and
join it to the publish calendar. Over 8 to 20 posts a month that produces a ranking.

Win condition: **150+ net followers in the 48 hours after publishing.** Provisional until one
month of real attribution recalibrates it.

## Reporting discipline

- Never report a 10K+ impression post as a win in its own right.
- Never use the "reach record" framing. May 2026 was the worst conversion month on record.
- Frequency is a lever, but only behind a repeating format and a consistent topic. July ran
  three times June's volume and produced fewer followers because the posts were scattered.
- Log saves per post. That is the metric the current strategy is optimizing and we only
  started tracking it in 2026-08.
