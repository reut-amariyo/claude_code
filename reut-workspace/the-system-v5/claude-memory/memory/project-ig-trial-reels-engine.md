---
name: project-ig-trial-reels-engine
description: "IG trial reels growth engine on @lior — listicle reels + \"comment X get the book\" lead magnets, scaling to 7/day; TikFusion rejected as spoofer"
metadata: 
  node_type: memory
  type: project
  originSessionId: 454d00cb-5070-47d9-8f84-695f5ad2c19c
---

As of 2026-07-05 Reut is scaling @lior's Instagram growth engine: **trial reels** (shown to non-followers) in the "10 startups that don't exist yet" listicle format, with a "Comment 'FOUNDER' and I'll DM you 200 startup ideas" lead-magnet CTA. Proven: 969 and 496 comments on the first two; the third repeat of the same concept decayed to 144 → scale needs concept variety, not duplicates. Target: 7 trial reels/day, automated.

Key facts:
- **TikFusion (tikfusion.com) rejected 2026-07-05**: it's a €199/mo video "spoofer" for evading IG duplicate detection, marketed to OnlyFans spam agencies. Never build around it — ban risk for the verified @lior account, and unnecessary since each reel carries a different list/book.
- **Metricool supports Trial Reel as a native content type** (most schedulers can't — trial toggle isn't in the public IG API). Plan: extend the existing Metricool API scripts (like post_bluesky_metricool.py) for IG trial reels.
- Pipeline design: lead-magnet library (keyword per book) → 7 daily Claude-generated listicle scripts → local ffmpeg template render → ManyChat comment→DM → performance log.
- **BUILT 2026-07-05**: `/trial-reels` skill (`.claude/commands/trial-reels.md`) + `render_trial_reel.py` + `batch_trial_reels.py` in `T-tools/01-skills/scripts/`. Renders 7 reels in ~35s from `batch.json`. First batch: `O-output/trial-reels/2026-07-06/`. Perf log: `O-output/trial-reels/performance-log.md`.
- **Reut's boundary: NEVER auto-post trial reels to Instagram.** Deliverable = MP4s + captions + checklist; she uploads manually. TikFusion: she bought it anyway to try (saves outputs to ~/Desktop, names them input_001.mp4); I stay out of its spoofing use entirely.
- B-roll: `/Users/reutamariyo/Downloads/4.2.26/C0030.MP4` — 32min 4K, Lior at podcast mic, crop_x_frac 0.62, avoid 0:00-0:30 and 21:00-24:30.
- Open: which comment-DM tool/keywords are live ("BUILD" assumed, unconfirmed), the actual "200 startup ideas" book file, new b-roll sources.
- Full plan: `the-system-v5/O-output/trial-reels-factory-plan.md`.

Related: [[project-lior-tasks-q2]] (IG is priority #1), [[reels-hooks-engine]], [[feedback-sandcastles-video-sourcing]]
