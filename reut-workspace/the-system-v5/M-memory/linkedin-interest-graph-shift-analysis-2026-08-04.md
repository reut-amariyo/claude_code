# LinkedIn Interest-Graph Shift — Analysis (2026-08-04)

**Source:** Devin Reed, "The New Rules of LinkedIn" (LinkedIn article, 2026-08-03), shared by Reut with "תלמד מזה".
**Primary source verified:** LinkedIn Engineering blog, "Engineering the next generation of LinkedIn's Feed", Hristo Danchev, 2026-03-12.
https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed

---

## What is FACT (verified against LinkedIn's own blog)

- The feed was rebuilt from a **social graph** (who follows you) to an **interest graph** (who cares about this topic). LLM-powered embeddings semantically classify every post and match it to reader interests, including people who don't follow you.
- Ranking signals confirmed by LinkedIn: reads, likes, comments, returns, scroll-past, **dwell time** ("long dwells"), profile data (industry, experience, skills, geography), and **sequential engagement patterns** — the model reads 1,000+ of a user's historical interactions through a transformer to predict what they care about.
- Rollout started in 2025, refined through early 2026, publicly explained only March 2026. The industry-wide reach drops of the past year are this system, not individual account decay.

## What is INTERPRETATION (Reed's 7 rules — hypothesis tier)

Same trust tier as the Q1 2026 trends memo: tiebreaker when Lior's own data is silent, never an override of Lior's analyst data.

| Reed's rule | vs. our existing rules | Verdict |
|---|---|---|
| 1. Followers aren't the moat, topic is | Corroborates Q1-2026 Trend 1 (10-25k creators catching up) | Adopt as lens |
| 2. Profile is the first thing the graph reads | NEW — nothing in our system covers profile-as-classifier | **New action** |
| 3. Pick 2-3 pillars, hammer 90 days | Matches the three brand pillars + one-idea-per-post | Already compliant, now with a mechanical reason |
| 4. Write for saves, not reactions | Mirrors X bookmark-weighted scoring (×3). LinkedIn analytics doesn't expose saves per post, so proxy = dwell-heavy "knowledge density" formats | Adopt as drafting lens |
| 5. Comments are training data; 5-10 real comments/day | Extends our engagement-gap rule; commenting becomes distribution, not just courtesy | **New action** (manual only — never auto-post) |
| 6. Post length doesn't matter, provocation does | CONFLICTS with our 750-1,200 char rule and Q1 trend's 1,250-3,000. Keep Lior's data as ground truth | Do not adopt |
| 7. 90-day consistency game | Standard advice, but now mechanically justified (classification takes 2-3 months) | Note |

Also corroborated: "use keywords, not your coined terms" independently confirms our anti-AI ban on concept-naming and renamed phenomena.

Caveat: the article's final section is a lead magnet funnel for Reed's templates. The algorithm analysis is sound; the templates pitch is marketing, not data.

## What this reframes for Lior

1. **Reach drops are a topic signal, not only throttle or content failure.** Under the new system, 3K impressions on a 30K+ follower base means "the graph thinks only 3K of them care about this topic." When reading the LinkedIn performance log, low reach on an off-pillar post now has a mechanical explanation. This is also a possible confound in the April 2026 failure wave (10 of 12) — the gate-skipping diagnosis stands, but the algorithm rollout was happening under it.
2. **Off-pillar posts now have a compounding cost.** Every CMO-lane or wellness-lane post doesn't just underperform — it teaches the classifier the wrong thing about Lior. The CEO relevance filter is now algorithmically enforced, not just brand hygiene.
3. **Follower-count comparisons to mega-accounts are obsolete.** Lior's band competes on topic authority, not list size.

## Actions (for Reut to decide / route to agency)

1. **Profile audit (one-time, highest leverage):** Lior's headline, About, and experience section should carry the searchable keywords of his pillars — SaaS founder, e-commerce automation, bootstrapped, 0→1, exit — not clever phrasing. The graph reads the profile before distributing any post.
2. **90-day pillar lock:** every LinkedIn post maps to one of the three pillars; no dabbling until classification settles. Audit recent agency posts for pillar drift.
3. **Commenting as channel:** 5-10 substantive comments/day on target SaaS/founder accounts, drafted here, posted manually by Reut/Lior per the never-auto-post rule.
4. **Draft for dwell:** favor knowledge-density posts (playbook archetypes with keep-forever value) over applause-bait; the engagement-gap close now also buys comment signal.

## Hierarchy placement

1. Lior's own analyst data — GROUND TRUTH
2. Voice/persona rules
3. Posting mechanics
4. **Interest-graph mechanics (the verified FACT section above) — platform ground truth, sits beside mechanics**
5. Reed's 7 rules + Q1 2026 trends — hypothesis/tiebreaker tier
