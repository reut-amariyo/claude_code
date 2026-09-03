---
name: LinkedIn high-impressions low-engagement fix
description: The open-ending rule is a HYPOTHESIS, not proven — 2026-08-04 evidence audit found no correlation between ending type and impressions; directional-only effect on comments. Don't block a post on a closed ending.
type: feedback
originSessionId: 217754ec-1bf5-42a5-a048-d34cb043f1a3
modified: 2026-08-04T13:11:24.378Z
---
# Open endings: hypothesis, not law (downgraded 2026-08-04)

**Status change (2026-08-04, confirmed with Reut):** Reut challenged "does our playbook data PROVE open endings win?" An honest audit of the confirmed-win set answered NO. The rule below is downgraded from failure-pattern to directional hypothesis. In pre-publish audits, a closed ending is a ⚠️ note, never a blocker, and should not be pushed after Reut has chosen her ending.

**Why:** The evidence for the rule was a single data point; the winners themselves are mixed.

## The 2026-08-04 evidence audit

Supporting the rule (1 data point):
- "AI agents Paperclip" post: 10K imp, 12 likes, 0 comments, closed ending ("Humans aren't going anywhere"). Causation inferred, never A/B tested.

Mixed evidence from confirmed winners:
- Google Base44 (142K imp, all-time record): open close "Agree?" — but reach came from newsjack + tagging giants, not the ending
- Messi decode (10K+): question close, built for resonance
- Birthday listicle (17,970 imp, 198 likes, 1.16% ER — among the best resonance): FULLY CLOSED warm ending "Hope it saves you some (:" — directly contradicts "closed endings kill engagement"
- MD→HTML (93K imp, #2 all-time): closed strategic-insight ending, huge reach, lowest resonance 0.09% — but resonance driver was the debate-bait tutorial content, not the ending

## How to apply

- **Impressions (the playbook KPI): ending type shows NO proven effect.** Reach came from newsjacking, famous entities, and topic fit.
- **Comments: directional only.** Highest-comment posts had open/question closes, but the sample is small and confounded.
- In audits (S4 of `/lior-prepublish-check`): flag a closed ending as an observation with this file's nuance, offer a question-close option once, respect Reut's choice.
- **Open experiment:** the 2026-08-04 focus post ("Had a wealthy friend... Just focus.") shipped with a closed ending. Compare its comment count vs. the next comparable post with a question close, then update this file.

## Original analysis (2026, kept for context — now known to be over-claimed)

Pattern: high impressions + low likes + zero comments → suspected causes: (1) closed ending people nod and scroll past, (2) post gives the full answer leaving nothing to add, (3) balanced tone with no friction. Suggested fixes: genuine open question, leave one gap in the conclusion, "conversation starter" format over "article" format, sacrifice polish for provocation when the goal is comments.

Related: [[lior-top-8-10k-playbook]], [[feedback-mandatory-prepublish-check]].
