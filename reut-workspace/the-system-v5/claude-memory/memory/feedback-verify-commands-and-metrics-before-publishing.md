---
name: feedback-verify-commands-and-metrics-before-publishing
description: Never publish a command, path, or benchmark number in Lior content on the donor's authority alone — verify against primary source. Two real errors caught this way on 2026-09-07.
metadata:
  type: feedback
---

2026-09-07. Building a how-to post from Charlie Hills' migration article. Two errors would have
shipped if the donor had been trusted:

- **I invented `/migrate-to-codex` as the way to run the skill.** The real invocation is an
  environment variable pointing at a Python script. Hills never publishes a run command, which is
  exactly why I should have checked instead of filling the gap. Source of truth was the skill's own
  SKILL.md in openai/skills.
- **The donor's reason for the backup step was wrong.** He wrote that the skill "rewrites that file
  from scratch." The skill's documentation says it preserves existing entries. The advice survived,
  the reasoning had to change.

A third, on the graphic: **"35 points, 2%" is an invalid operation on an Elo rating.** Elo is an
interval scale, so dividing two ratings means nothing. The correct reading is a win probability,
1 / (1 + 10^(-gap/400)), which for 35 points is about 55 wins in 100. Reut replaced the label.

**Why:** a how-to post is audited by its readers within hours, and the whole argument of this
particular post was that other people had framed a chart dishonestly. One wrong path in the body
would have become the entire comment thread.

**How to apply:** before any Lior post containing a command, a file path, a benchmark number or a
statistic, open the primary source. The donor post is a structure, never a fact-checker. State in
the delivery file which facts were verified and against what.

Related: [[lior-post-claude-to-codex-migration]], [[feedback-build-on-proven-structures]].
