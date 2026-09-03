---
name: X Workflow — Weekly Hypothesis BEFORE scout-day Drafts
description: x-analyst-weekly must output a data-backed hypothesis (winning topic + perspective + vehicle) BEFORE scout-day generates posts. Drafting cold is broken.
type: feedback
originSessionId: d1e3a08e-5052-4b9e-bfd6-a474226bc44b
---
Current state: scout-day generates 5 X posts cold each day with no week-level hypothesis driving them. This is the "open ChatGPT, take whatever comes out" failure mode the Wiz of Ecom system explicitly diagnoses.

**Fixed workflow:**

**Step 1 — Sunday: x-analyst-weekly outputs a hypothesis.** From the week's data, the analyst writes:
- This week's **winning topic theme** (e.g., "firing decisions," "AI replacing roles," "scaling team past 200")
- This week's **winning perspective** (e.g., BTS, contrarian, storytelling)
- This week's **winning vehicle** (e.g., story post, hot take, doc screenshot)
- This week's **winning style mix** (e.g., 2 story + 1 vulnerability + 1 midas + 1 hot take)

**Step 2 — Reut approves the hypothesis in Hebrew** (existing flow).

**Step 3 — scout-day reads the approved hypothesis** before generating each day's 5 posts. Every draft must justify itself against the hypothesis (topic / perspective / vehicle / style match).

**Step 4 — Friday: x-analyst checks** how many of the week's posts hit the hypothesis vs. drifted, and feeds that into next Sunday's hypothesis.

**Why:** Wiz of Ecom thread (2026-05-01) — the gap between agencies that work and agencies that don't is whether content is built off a weekly data-backed hypothesis or generated randomly. Without a hypothesis, scout-day is guessing. With one, every post compounds the previous week's learning.

**How to apply:**
- Update x-analyst-weekly skill to produce the hypothesis as a structured output (not just a rule refinement).
- Update scout-day skill to require reading the latest approved hypothesis as its first step. If no hypothesis exists, refuse to draft and ask Reut to run x-analyst-weekly first.
- Hypothesis lives in `reut-workspace/the-system-v5/O-output/x-performance-log/weekly-hypothesis.md` (latest only).
