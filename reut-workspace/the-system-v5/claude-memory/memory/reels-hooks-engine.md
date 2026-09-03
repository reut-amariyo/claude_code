---
name: reels-hooks-engine
description: "The /hooks skill — IG Reels hook engine that generates, scores, and learns from feedback"
metadata: 
  node_type: memory
  type: project
  originSessionId: dafc8060-2c67-403a-83c2-a4683a38ad2a
---

`/hooks` is a slash command that generates scroll-stopping IG Reels hooks for Lior. Built 2026-06-04 because invented one-at-a-time hooks were too weak.

**How it works:** generates 15-20 candidates across 8 proven viral formulas → scores each 1-5 on a 5-axis rubric (scroll-stop, curiosity gap, specificity, voice fit, 3-sec comprehension) → shows only the top 5 (18+/25) → logs Reut's loved/rejected verdicts so the next batch is sharper.

**Files:**
- Command: `.claude/commands/hooks.md`
- Swipe library (formulas, Lior asset bank, rubric, bans): `T-tools/01-skills/reels-hook-swipe-file.md`
- Feedback log (the learning loop): `O-output/reels-hooks-feedback-log.md`

The feedback loop is the point: winning hooks get promoted into the swipe file, rejected patterns get avoided. Without logging reactions, it stays static. Always log Reut's reaction after presenting hooks.

Related: [[favorite-hooks]], [[linkedin-hooks-library]]
