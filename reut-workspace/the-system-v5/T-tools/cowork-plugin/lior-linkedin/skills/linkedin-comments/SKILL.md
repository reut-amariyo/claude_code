---
name: linkedin-comments
description: >
  This skill should be used when the user asks to "draft comments", "who should Lior comment on
  today", "find posts to comment on", "daily comment drafts", or wants LinkedIn comment options
  in Lior's voice. Scans the target list, picks 5 fresh posts, drafts 3 options each. Never posts.
---

Draft LinkedIn comment options for Lior. Designed to run daily, first thing.

# 🛑 THE HARD RULE

**NEVER comment, react, follow, or click any engagement control on LinkedIn.**
This task is READ-ONLY on LinkedIn and WRITE-ONLY to a local file.
Reut posts every comment manually by copy-paste. There is no exception and no
"approved" state that changes this. If you find yourself about to click Comment, stop.

# Before starting (MANDATORY)

Read for voice and rules:
1. `${CLAUDE_PLUGIN_ROOT}/references/voice-rules.md`
2. `${CLAUDE_PLUGIN_ROOT}/references/brand-core.md`
3. `${CLAUDE_PLUGIN_ROOT}/references/brand-core.md`
4. The target list: `${CLAUDE_PLUGIN_ROOT}/references/targets.md`

# Step 1 — Scan the targets

Chrome is logged in as Lior. For each profile in the **Tier 1** table of the target list,
open `<profile-url>recent-activity/all/` and read the posts from the **last 24 hours**.

Collect for each post: author, post URL, full text, age in hours, reactions, comments.

Skip a profile that fails to load. Log it and move on. Never let one bad profile kill the run.

# Step 2 — Dedup

Read `<workspace>/.linkedin-comment-drafts-log.json`. It is a list of post URLs already suggested.
Exclude every URL already in it.

⚠️ Known gotcha from the Bluesky pipeline: a dedup log can silently drop entries. Pull the
FULL candidate pool first, then exclude, rather than trusting the log to be complete.

# Step 3 — Pick 5

Score each candidate on:
- **Freshness.** Under 3 hours old is ideal. The comment window is the first 30-60 minutes,
  and a post already past ~50 comments is a bad investment. Prefer young posts with velocity.
- **Fit.** AI, commerce, building, or running a company. Founders and operators in the replies.
- **Standing.** Does Lior have something to say that nobody else in that thread can say?
  This is the disqualifier. If the honest comment is "I agree", drop the post.

Apply the **Never comment** list from the target file. Then take the top 5.
If fewer than 5 qualify, deliver fewer. Never pad the list to hit the number.

# Step 4 — Draft 3 options per post

Three deliberately different angles so Reut has a real choice:

1. **The operator add-on** — a specific number or thing from inside the company that extends
   the author's point.
2. **The friendly counter** — challenge one part of it from experience. Never aggressive.
3. **The sharp line** — the quotable, no story attached.

## Comment rules, all mandatory

- **Engage what the post actually says FIRST.** Never open with Lior's story.
- **Credit the author's insight by name** before adding anything.
- **ONE cutting line by default. Two lines maximum.** The quotable IS the comment.
- If the post asks a question, **answer it genuinely**. No forced story.
- A real Lior story with a specific number when it **fits naturally**. Never force-fit one.
- English only.
- No parentheses. No em dashes or double dashes. No "It's not X, it's Y" in any wording.
- Never open with "Honestly", "Frankly", or "To be honest".
- Minimize "just", max one.
- Never arrogant. No flexing on team size or peers. No imposter syndrome, no fear confessions.
- "e-commerce" lowercase. "250 employees" only when central. **NEVER "100 engineers"**, the
  number is unverified and banned.
- Do not name AutoDS in every comment. Vary the proof.
- Never criticize Shopify, Lovable or Wix. Never name Shopify as a potential AutoDS buyer.
- Lior is dyslexic. Never "I read" or "I just finished a book". Podcasts, audiobooks, team summaries.
- Personal founder journey, never product marketing.

# Step 5 — Write the file

Write to:
`<workspace>/linkedin-comment-drafts/YYYY-MM-DD.md`

Format, plain copy-paste text, **never blockquotes**:

```
# LinkedIn comment drafts — YYYY-MM-DD

## 1. <Author> — <age>h — <reactions> reactions, <comments> comments
<post URL>

**What the post says:** <one line>
**Why Lior:** <one line, the standing>

--- OPTION A: operator add-on ---
<comment text>

--- OPTION B: friendly counter ---
<comment text>

--- OPTION C: sharp line ---
<comment text>
```

Then append the 5 post URLs to `<workspace>/.linkedin-comment-drafts-log.json`.

# Step 6 — Notify Reut, in Hebrew

"☕ 5 פוסטים לתגובה מוכנים, 3 אפשרויות לכל אחד: `O-output/linkedin-comment-drafts/YYYY-MM-DD.md`
הכי דחוף: <author> (<age> שעות)"

If the run found nothing worth commenting on, say so plainly rather than delivering weak drafts:
"☕ סרקתי, אין היום פוסט ששווה תגובה מליאור. עדיף לדלג מאשר להגיב חלש."

# Failure modes

- **Chrome not logged in / not available:** write the issue into today's draft file under
  "Scan issues" and notify Reut in Hebrew. Do not retry in a loop.
- **A profile's activity page is empty or private:** log it, skip it. Dan Martell's activity
  page is known to return 0 readable posts.
- **The Mac was asleep:** this task simply did not run. That is a missed slot, not a bug.
