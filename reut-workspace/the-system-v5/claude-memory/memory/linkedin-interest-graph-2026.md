---
name: linkedin-interest-graph-2026
description: "LinkedIn feed rebuilt as an interest graph (verified via LinkedIn Engineering blog, Mar 2026) — topic classification beats follower count; changes how to read Lior's reach data"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1b545fdc-6ee0-4322-847a-966594e6d921
  modified: 2026-08-04T07:37:03.058Z
---

# LinkedIn is now an interest graph, not a social graph (2026)

**Verified fact** (LinkedIn Engineering blog, Hristo Danchev, 2026-03-12): the feed ranks by LLM-embedding topic relevance, not network. Signals: dwell time, saves, comments, sequential engagement history (1,000+ interactions per user), and the poster's PROFILE text. Rolled out through 2025-26; explains the industry-wide reach drops.

**Why:** Reut shared Devin Reed's "New Rules of LinkedIn" (2026-08-03) with "תלמד מזה". LinkedIn is a Q3 under-target platform; this changes how to interpret its performance data.

**How to apply:**
- Low reach on an off-pillar post = topic-mismatch signal from the classifier, not just throttle or bad content. Read the performance log through this lens.
- Off-pillar posts have compounding cost: they mis-train the classifier. The [[feedback-ceo-relevance-filter]] is now algorithmically enforced.
- Profile headline/About are read by the graph before any post distributes — keyword-align them to the pillars (one-time audit, flagged to Reut).
- Draft for saves/dwell (knowledge density), mirror of [[x-bookmark-weighted-scoring]]. Substantive commenting is now distribution (manual posting only).
- Reed's derived "7 rules" are hypothesis-tier like [[linkedin-q1-2026-trends]] — Lior's analyst data still overrides (his rule 6 "length doesn't matter" conflicts with our char rules; not adopted).

Full analysis: the-system-v5/M-memory/linkedin-interest-graph-shift-analysis-2026-08-04.md
