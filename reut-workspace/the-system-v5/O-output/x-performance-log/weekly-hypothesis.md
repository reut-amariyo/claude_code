# Weekly X Hypothesis — Week of 2026-06-01 (STOP CHASING ORIGINAL FORMATS — FIX REACH + RESTART REPLY ENGINE)

Generated: 2026-06-01 06:00
Approved by Reut: yes (2026-06-02)

## Context — the memoir pivot also failed, and the decision rule says escalate

Last week's hypothesis reverted to memoir with a decision rule for 2026-06-04:
- memoir avg > 100 → confirmed
- 50–100 → extend
- **≤ 50 → escalate (algorithm throttle may be deeper than format)**

**Result:** 11 new memoir/operator originals averaged **~17 imp**, only the dollar-bug story cleared 50 (60 imp). That is the ESCALATE branch. We now have two consecutive failed originals lanes at the same ceiling (take-driven ~22, memoir ~17). **The cause is upstream of copy.** No third content-format test this week.

**Second trigger fired too:** replies were supposed to hold 233.6 avg. Instead only **1 reply shipped in 4 days** (May 28–Jun 1), with no anchor/number. Per the decision rule, that's a reply-pipeline investigation, not a content miss.

So this week is not a content week. It's a **diagnose-and-unblock week.**

## Winning topic theme

For the few posts we DO ship: **AI cost / pricing operator takes + production-failure scenes** — the only two themes with proven traction.
- AI-pricing reply cluster (May 26) reached 201–981 imp: "80% cost cut" (@dee_bosa), "agent debt" (@gregisenberg), "2-week switching tax" (@BullTheoryio), "the AI bill is a vibe" (@edzitron).
- Production-failure original (dollar-bug, 60 imp, 2 replies) was the only original to draw real engagement.

These two themes go into REPLIES first (where they reach), originals second.

## Winning perspective

**Authoritative — Lior-specific anchor + concrete outcome number** (Rule 3). This is the ONLY perspective that has ever reached on this account, and it lives in replies. Storytelling memoir is demoted: it works as a texture, not a reach lever.

Why: every post above 200 imp this week was an anchor+number reply. Every memoir storytelling original (the perspective we bet on last week) sat at 10–60.

## Winning vehicle

**REPLY is the primary vehicle. Originals are secondary until reach is diagnosed.**

1. **Replies (priority): 3–5 lines, anchor + outcome number.** Direct response to OP → Lior-specific fact (AutoDS, 9 years, exact $/%) → sharper operator-verdict than the OP. Target high-traffic threads (1K+ likes / 50K+ views in last 12h).
2. **Originals (secondary): number + lived scene + one-line lesson** — the dollar-bug structure. Keep shipping but stop expecting them to be the growth lever.

## Style mix for next 5 posts

- 2 × story (production-failure / operator scene with a hard number — the dollar-bug structure)
- 1 × vulnerability (a genuine cost/mistake with the number attached)
- 1 × midas (a counterintuitive AutoDS win with the receipt)
- 1 × conviction or hot-take (AI pricing / cost — ONLY if it carries a Lior number, else drop)
- 0 × doc/framework (per archetype rule)
- 0 × memoir-as-reach-bet, 0 × prediction, 0 × "everyone says X" reframe

**But weight effort toward replies: minimum 5 anchor+number replies this week is the real deliverable.**

## The two interventions that actually matter this week

> **Canary checked 2026-06-01 → RESTRICTED (17 days running).** The reply engine is NOT a whitelist problem and is NOT code-fixable. @lior_pozin is in an account-level X restriction that 403s every API reply to a stranger. The May 26 replies that reached 200–981 imp were posted **manually via the web UI**. This corrects last week's "audit the whitelist" framing.

1. **🔴 Move replies to the manual channel — this is the only reply path that works.** Don't try to "restart" `reply_x.py`; it will 403 every time until X lifts the account flag. Instead: the pipeline DRAFTS 5–7 replies/week (anchor + outcome number, Rule 3) and surfaces open-reply mid-tier targets (non-verified, 50–800 likes, 3+ visible non-verified replies), and **Lior/Reut posts them by hand.** Hand-posted replies are the highest-reach content on the account, full stop. Do NOT re-run the canary off-schedule — the Sunday `x-reply-canary` already watches for the lift.
2. **🔴 Diagnose original reach suppression.** Originals are now the only API-writable channel, and they're capped at ~20 imp across two failed content pivots. Run ONE controlled test instead of another format A/B: post 1 original/day at a fixed peak time, with a manual early reply-seed, to test the "no first-hour engagement → algo buries it" hypothesis. AND stop the near-duplicate posting (same story reworded same-day) — on a 276-follower low-trust account it may be feeding the same anti-spam signal that triggered the reply restriction.

## What to avoid

1. **Near-duplicate / paraphrased posts** — this week the dollar-bug story ran twice in 24h and the "5 years no salary" story ran twice the same day. This is the #1 hygiene failure and a candidate cause of throttle. Scout-day must check the last 7 days for repeated STORIES, not just phrasing.
2. **A third original-format experiment.** Take-driven and memoir both failed at the same ceiling. Don't propose "let's try X format" — the lever is distribution.
3. **Memoir as a reach bet** — confirmed failed at ~17 imp avg.
4. **Prediction frames / "next 18 months" / "everyone says X"** — dead, multiple weeks.
5. **Seat-based pricing dying / SaaS dying** — beaten to death, single-digit-to-teens imp.
6. **Replies without a number or Lior anchor** — the one reply that shipped this week ("Ship fast, just start") was anchorless and got 20 imp. Rule 3 violation.
7. Em dashes, "not X it's Y," "I" hooks, Shopify criticism, crypto, politics, hardware, image-gen hype — voice rules unchanged.

## Measurement plan

- **Reply volume** is the headline metric: did we ship ≥5 anchor+number replies? (This week: 1.)
- **Reply avg impressions:** hold/beat 200+ (this week's new reply: 20).
- **Original reach test:** does a manually reply-seeded original beat the ~20 imp unseeded baseline? If yes → first-hour engagement is the throttle. If no → throttle is deeper (account-level / audience composition).
- Decision point: 2026-06-08.
  - If replies recover to 5+/week at 200+ avg → reply engine is the confirmed strategy, stop worrying about originals.
  - If the reply-seed test lifts originals above ~100 → first-hour seeding becomes a standing rule.
  - If both stay flat → escalate to Reut: the account may need a structural reset (posting account/audience review), not more content tuning.

## Reply pipeline status

**🔴 API reply path is dead — account-level X restriction, confirmed RESTRICTED 2026-06-01 (17 days).** This is NOT the whitelist and NOT code-fixable (full diagnosis: [[project-x-reply-pipeline-whitelist-collapse]]). The 15 `scout-reply-x` tasks are correctly disabled; the Sunday `x-reply-canary` watches for the lift and will auto-re-enable `-01/-02` only. **The only working reply channel is manual web-UI posting** (how the May 26 cluster reached 200–981 imp). Action this week: draft replies for Lior/Reut to post by hand — do not wait on the API path. Recovery of the API path depends on X lifting the flag + organic trust growth (only 276 followers), not on anything in this repo.
