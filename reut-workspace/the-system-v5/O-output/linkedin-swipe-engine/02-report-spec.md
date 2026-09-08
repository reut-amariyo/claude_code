# Report spec — how posts get ranked and torn down

Built 2026-09-06. This is the contract for what Claude produces from each harvest.

---

## The outlier bar (what Reut saves during the harvest)

Save a post if ANY of these is true:
- 500+ reactions
- 100+ comments
- 50+ reposts
- Visibly far above what that creator normally gets, even if under the numbers above

Reposts are the strongest single signal on LinkedIn. A post with 300 reactions and
60 reposts beats a post with 2,000 reactions and 4 reposts, every time.

## Weighted score

Borrowed from the X scoring model already in the vault, retuned for LinkedIn.

    score = (reposts x 4) + (comments x 2) + (reactions x 1)

Why this weighting:
- **Reposts x4** — someone put the post on their own feed. Highest-cost action, and
  the only one that buys new distribution outside the author's network.
- **Comments x2** — LinkedIn's dwell-and-reply signal, and the only metric that reliably
  correlates with follower gain, which is Lior's actual KPI.
- **Reactions x1** — cheapest action, most gameable.

Impressions are deliberately excluded. They are not visible on other people's posts,
and per [[feedback-linkedin-kpi-followers-not-impressions]] they are not the KPI anyway.

### Outlier multiplier

Where the creator's normal is known, the raw score gets multiplied:

    final = score x (this post / that creator's median post)

A 900-reaction post from someone who normally gets 3,000 is a FAILURE and ranks low.
A 400-reaction post from someone who normally gets 80 is a 5x outlier and ranks high,
because the delta is where the learning is. Median baselines get built over the first
3 weeks of running this and stored in `creator-baselines.md`.

---

## Report structure — `daily-reports/YYYY-MM-DD-report.md`

### 1. Header
Date, number of posts harvested, number of creators represented, top score.

### 2. The ranked table
Every harvested post, best to worst:

| Rank | Creator | Hook (first line) | React | Comm | Rep | Score | xMedian | Structure | Lior fit |
|---|---|---|---|---|---|---|---|---|---|

**Lior fit** is a 3-value flag:
- ✅ passes the CEO relevance filter, could be built as-is
- ⚠️ structure usable, topic needs a full swap
- ❌ off-limits (career content, AI tool tutorials, productivity tips, crypto/hardware,
  anything hitting [[feedback-no-productivity-tool-tips]] or [[feedback-ceo-relevance-filter]])

### 3. Donor teardowns — top 3 only
For each, a beat table per [[feedback-build-on-proven-structures]]:

| Beat | What the donor does | Lior equivalent |
|---|---|---|
| Hook shape | | |
| Counter-hook / line 2 | | |
| Stat placement | | |
| Item count and shape | | |
| Turn | | |
| Close | | |
| CTA | | |
| Visual family | | |

Plus: **AI tells to strip** — every "not X, it's Y", em dash, parenthetical, and red-list
word in the donor, listed so they never survive into the Lior version.
See [[linkedin-ai-slop-penalty]] and [[feedback-anti-ai-writing-rules]].

Plus: **Why would a stranger follow?** — the mandatory row from
[[feedback-linkedin-kpi-followers-not-impressions]]. If the donor has no answer,
it does not become a Lior post.

### 4. Pattern of the day
One paragraph. What repeated across the top 10 today that did not repeat yesterday.
Format shifts, hook shapes, a topic wave, a visual family. This is the compounding part
of the system, the daily rankings are disposable, this section is not.

### 5. Watch list
Any creator whose numbers moved sharply up or down. Feeds the monthly list maintenance.

### 6. Hebrew top-5 in chat
Not in the file. Five lines, each: creator, what the post did, why it is worth stealing.

---

## Weekly roll-up

Every Sunday, `daily-reports/YYYY-WW-weekly.md`:
- Top 10 of the week by score across all 7 days
- Which structures recurred, ranked by frequency
- The 3 donors queued for Lior posts that week
- Any creator to drop or add

## What does NOT go in the report

- No word-for-word reuse suggestions. Structure only.
- Posts from creators under an active donor moratorium get ranked and scored for data,
  and are explicitly marked "tracked, not usable" in the Lior fit column.
- No engagement-bait teardowns. If the post won purely on a comment gate or a
  giveaway hook, it gets a ❌ and one line saying why. The exit-deck evidence in
  [[lior-post-exit-deck-lead-magnet]] is clear that gates suppress reach.
