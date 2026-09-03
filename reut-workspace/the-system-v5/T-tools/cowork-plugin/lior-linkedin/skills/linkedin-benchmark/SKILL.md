---
name: linkedin-benchmark
description: >
  This skill should be used when the user asks to "benchmark creators", "check if X is a good
  reference", "measure a LinkedIn account", "who should we copy", "is this account actually
  successful", or wants to evaluate LinkedIn creators as content models before copying them.
metadata:
  version: "0.1.0"
---

# LinkedIn creator benchmark

Measure a LinkedIn account before recommending it as a model. Never describe an account from
memory. Read it.

Read `${CLAUDE_PLUGIN_ROOT}/references/brand-core.md` and
`${CLAUDE_PLUGIN_ROOT}/references/creator-benchmark.md` first. The second file holds every
account already measured, so check it before re-scanning.

## The governing finding

**Follower count does not predict current performance. In our sample it inverted.** The three
largest accounts measured ran the three weakest engines. So never recommend an account on
follower count alone.

Filter on three things:
1. **Scale** proves they solved the follower problem once.
2. **Reactions per 100K followers** proves the method still works today.
3. **Mechanism legality** decides whether Lior can copy it at all.

## Procedure

1. Open `linkedin.com/in/<slug>/recent-activity/all/` in a logged-in browser. Scroll to load.
2. Extract the follower count from the left rail and, for the five most recent posts:
   author, character length, reactions, comments, reposts, whether the post carries media,
   and the first line as the hook.
3. Compute **reactions per 100K followers** as `avg reactions / (followers / 100000)`.
4. Read the actual post bodies. Classify the content: what lane is it in, and what is the
   engine, saves, comments, or a lead magnet.
5. Give a verdict in three parts:
   - **Take:** the specific mechanics that transfer.
   - **Dies at the door:** what violates the brand rules.
   - **Verdict:** model, craft-only, comment-target-only, or reject.

## Reference points measured 2026-08-23

Jasmin Alić 553 per 100K · Justin Welsh 319 · Greg Isenberg 173 · Sahil Bloom 116 ·
Hamna Aslam Kahn 97 · Ruben Hassid 78 · Chris Donnelly 53 · Steve Nouri 20 ·
Allie K. Miller 17 · Zain Kahn 6.

Anything above roughly 150 is a live engine. Below 30 is an account coasting on an audience
it acquired elsewhere.

## Two separate questions, never conflate them

- **Inspiration list** = who we copy structure from. Criterion: working engine plus a legal
  mechanism. Not role match.
- **Comment targets** = whose audience we borrow. Criterion: audience overlap, reach, and
  whether Lior has standing nobody else in the thread has.

An account can be excellent on one list and wrong on the other.

## Rules

- Read-only. Never react, follow, comment or click any engagement control.
- Five recent posts is a snapshot, not a trailing average. Say so in the verdict.
- Reactions per 100K cannot see saves, which is the metric we actually want and which is
  invisible on other people's posts. Say so.
- If a profile fails to load or is private, log it and move on. Never invent numbers.

## Without browser access

Ask the user to paste the profile headline, follower count, and the last five posts with
their engagement. The analysis works the same. Never estimate the numbers.
