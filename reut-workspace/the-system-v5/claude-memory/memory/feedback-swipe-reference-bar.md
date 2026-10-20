---
name: feedback-swipe-reference-bar
description: Reut 2026-09-20 on the swipe engine's first report - a reference must be text-carried, a clear outlier for that specific creator AND strong in absolute numbers, on a CEO-level topic; zero references beats padding
metadata:
  type: feedback
---

Reut's review of the first swipe report (2026-09-20) rejected 4 of 5 picks:
- Sinek, Partaker: "רק תמונה בלי טקסט", image-only posts are never references.
- Denk: off-topic (comp/hiring mechanics), BUT she liked the framing: "משהו שביצע טוב אצל
  בן אדם ספציפי זה חזק יותר מאשר סתם פוסט מוצלח". Outlier-vs-that-creator is the right lens.
- Donnelly, Matt Gray: "לא הרבה מעורבות", 598/231 and 379/300 on 1.26M and 920K followers
  is baseline for them, and LinkedIn-marketing is a CMO topic anyway.
- Alex Hormozi: barred outright, "אל תיתן לי את אלכס הורמוזי".

**Why:** she wants proof, not volume. A post that is merely big (Welsh at x1.0), merely
relative (Denk x7 on 992 likes), or merely on-topic is not evidence of a structure that works.

**How to apply:** the ★ bar in `scripts/harvest.py`: text 40+ words, xMedian ≥ 2,
1,000+ likes or 200+ comments, creator not barred, PLUS Claude's topic filter (CEO-level
AI / leadership / entrepreneurship; career, marketing/LinkedIn tactics, tool tips,
hiring/comp, robotics all fail). Only ★ rows become teardowns or go in the Hebrew top-5.
If none pass, say "no reference-grade post today" and stop. Zero is fine, padding is not.
Show likes per 10K followers next to xMedian, it exposes baseline posts from big accounts.
Applies to [[project-linkedin-swipe-engine]] and to any "find me a donor" request
under [[feedback-build-on-proven-structures]].

**Round 2 (2026-09-21), Reut rejected the whole 7-topic list:**
- "Trending" means the last 7 days. A 09-06 post shown on 09-21 ("מלפני שבועיים") is not trending.
- 🚫 Gary Vaynerchuk barred as a donor, same status as Hormozi ("אל תביא לי גארי וי"). `donor: red` in creators.json.
- She wants posts people SAVE, on AI: frameworks, lists, guides, first-party artifacts. Comment-only outliers
  (Roetzer 381 likes / 307 comments) are "לא הצליח": likes floor stands, comments alone never qualify.
- Culture / hiring / founder-story topics that pass the numbers still fail: the ask is AI, save-worthy, this week.
So the query is now: AI topic AND date ≤ 7 days AND save-shaped (list / framework / carousel / artifact)
AND x2 own median AND 1K+ likes. If the harvest has none, say so in one line; do not fill with adjacent topics.
