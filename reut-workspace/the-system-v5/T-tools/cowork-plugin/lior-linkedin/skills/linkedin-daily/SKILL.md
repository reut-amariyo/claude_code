---
name: linkedin-daily
description: >
  This skill should be used when the user asks for "today's post", "the daily harvest", "what
  should Lior post today", "scan the references", "one post for today", or wants a daily draft
  built from what is currently working on the reference accounts. Produces ONE draft, never posts.
metadata:
  version: "0.1.0"
---

# Daily harvest — one post from what is working right now

Run each morning. Scan the reference accounts, find what is actually outperforming today,
extract the structure, and draft **one** post for Lior.

One post. Not three options, not a menu. Pick the best idea and commit to it.

Read `${CLAUDE_PLUGIN_ROOT}/references/targets.md` for the reference list,
`${CLAUDE_PLUGIN_ROOT}/references/creator-benchmark.md` for each account's baseline, and
`${CLAUDE_PLUGIN_ROOT}/references/save-first-spec.md` for the format.

## Step 1 — Scan

For every account in the **inspiration list**, open
`linkedin.com/in/<slug>/recent-activity/all/` and collect posts from the last 48 hours:
hook, full body, character count, reactions, comments, reposts, media type.

Read-only. Never react, follow, comment or click anything.

## Step 2 — Find the outliers, not the top posts

Raw reactions are useless across accounts of different sizes. Score each post as a multiple
of **that creator's own baseline** from `creator-benchmark.md`:

```
outlier score = post reactions / (creator followers / 100000) / creator's baseline per 100K
```

A score above 1.5 means the post beat its author's own average. Those are the only posts
worth learning from. A 2,000-reaction post from someone who always gets 2,000 teaches nothing.

Take the top 3.

## Step 3 — Extract structure, never voice

For each of the 3, write the skeleton in beats. What is the hook shape, what is the artifact,
how does it close, what makes it saveable. Then split it:

- **Transfers:** the mechanics that are legal for Lior.
- **Dies at the door:** what violates the rules. Expect this to include the payload itself
  when the source is an AI-tips account.

This is the discipline: **take the mechanism, never the voice.** The reference accounts are
mostly creators and coaches. Lior is a CEO. Copying their payload makes him a worse version
of them. Copying their structure with a payload only he can produce is the play.

## Step 4 — Match to a Lior topic

Pick from the live lanes: agentic commerce first, then AI-native org design, then AI video as
commerce creative or the exit lens. The topic must be something Lior has operator standing on.

**If no structure fits a real topic today, say so and draft nothing.** A skipped day costs
nothing. A forced post trains the topic classifier wrong and burns a slot.

Honour the mix: **3 save-first : 1 personal.** Check the last few days in the log before
choosing, so the personal post lands roughly every fourth.

## Step 5 — Draft, gate, deliver

Draft with `linkedin-post`. Run `linkedin-prepublish` on it. Deliver:

1. **The draft**, wrapped in `--- POST STARTS ---` / `--- POST ENDS ---`, plain text.
2. **The source**: which post it learned from, whose, and its outlier score.
3. **The gate table** with the verdict.
4. **The visual** recommendation.

## Step 6 — Log it so the harvest compounds

Append the three extracted skeletons to the swipe file. A structure seen three or more times
across different accounts gets promoted to a confirmed pattern. This is the point of running
it daily: the reference set teaches a little every day and the library grows.

🛑 **Never publish.** One draft, delivered. Reut posts.
