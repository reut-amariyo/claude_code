# LinkedIn strategy change: followers become the KPI, impressions become a diagnostic

Decision taken by Reut, 2026-08-23. This document turns it into a measurable system.
Supersedes the exposure-first KPI that has driven LinkedIn work since May 2026.

---

## 1. The decision in one line

**From today, LinkedIn is judged on net new followers per month.** Impressions stay in the
report as a diagnostic input, not as a win condition.

---

## 2. Why this is the right call, in three numbers

**a. Reach and followers are already proven to be separate systems on this account.**

| Month | Posts* | Impressions | Net new followers | Followers per 1K imp |
|---|---|---|---|---|
| April 2026 | 8 | 49,353 | +922 | 18.7 |
| May 2026 | 13 | 292,705 | +1,100 | 3.8 |
| June 2026 | 7 | 51,839 | +1,009 | 19.5 |
| July 2026 | 21 | 71,776 | +821 | 11.4 |

Impressions moved 6x. Followers never left a 922-1,100 band. May's two viral posts bought
240,000 extra impressions and roughly 91 extra followers.

**b. The two months with the best conversion were the two lowest-reach months.**
April and June converted at 18.7 and 19.5 followers per 1K impressions. May, the record
reach month, converted at 3.8. Chasing reach did not just fail to add followers, it
coincided with the worst conversion we have on record. The plausible mechanism is that a
viral post distributes to a cold, off-ICP audience that sees one post and never follows.

**c. Optimising LinkedIn for reach was never rational at the OKR level.**
The Q3 reach KR is 7M views a month across all platforms. LinkedIn's share of that is
70K, which is **1%**. Instagram and Facebook carry that number. So moving LinkedIn off a
reach KPI costs the company OKR essentially nothing, while the follower KR it does carry
gets a system built for it for the first time.

*Post counts come from our own log, not a LinkedIn export, and June's 7 looks low.
Verify before this table is shown to Lior.

**The uncomfortable one worth noticing:** July ran three times June's post volume and
produced fewer followers. I first read that as "volume is not a follower lever".
**Corrected 2026-08-23 after Reut's challenge, see section 5A: that reading was wrong.**
July had the frequency and neither of the two things that make frequency work.

---

## 3. The new KPI stack

**North star:** net new followers per month.

**The decomposition that makes it steerable.** A follower is the product of three terms,
and until now we have measured only the first:

```
followers = impressions  ×  (profile visits / impressions)  ×  (follows / profile visits)
               reach            curiosity rate                    profile conversion
```

- If **curiosity rate** is the weak term, the posts travel but do not make anyone want to
  know who wrote them. That is a hook and topic problem.
- If **profile conversion** is the weak term, the posts do their job and the profile page
  loses the person. That is a headline, About and Featured problem, and it is the cheapest
  thing on this list to fix.

We cannot yet say which one is broken, because **monthly profile visits have never been
pulled**. That single number is now blocking, not merely missing.

**Reference shape from Instagram**, where we do have all three terms: curiosity rate runs
1.45-1.60% of views and profile conversion runs 13-37% of visits. LinkedIn will differ,
but it gives us an order of magnitude to react to.

**Per-post attribution.** LinkedIn will not tell us followers per post, so we build it:
take the daily new-follower series from Analytics and join it to the publish calendar.
Over 8-20 posts a month that produces a ranking, which is what we actually need.

**The new win condition, replacing "10,000+ impressions":**
**a post that produces 150+ net followers in the 48 hours after publishing.**
This threshold is a first estimate against a ~963/month baseline and must be recalibrated
after one full month of daily-delta data. Treat it as provisional until then.

---

## 4. Targets

**Baseline:** 963 net new followers per month, four-month average, band 821-1,100.
Total 11,607 at end of July.

**Q3 stays as written.** The existing KR is 10.8K → 13.5K by 30 September, and current
pace reaches it without any change. Leave it. Use **September as the instrumentation
month**: build the measurement, pull the missing history, establish the decomposition
baseline. Changing a KR five weeks before quarter end buys nothing.

**Q4 2026, the first quarter actually run on this KPI:**

| Month | Net new followers | Total |
|---|---|---|
| October | 1,400 | ~14,900 |
| November | 1,800 | ~16,700 |
| December | 2,200 | ~18,900 |

That is a 2.3x exit run-rate against baseline, and it is the number the conversion levers
should be sized against.

**The honest long-range answer on 100K, which Lior should hear from us before he asks:**

| Scenario | Monthly pace | 100K arrives |
|---|---|---|
| Do nothing | 963 | 2034 |
| Q4 plan holds and 2027 averages 2,750 | 2,750 | mid-2029 |
| To land end of 2027 | ~3,700 sustained from now | not credible organically |

100K organically is a 2029 date. Landing it sooner needs either paid follower campaigns,
which are the only lever that buys followers at a known price, or the structural lever
below.

**The biggest untested structural lever: the Instagram port.** There are 100,000+
Instagram followers and 11,607 on LinkedIn. Deliberately converting 2% per quarter is
2,000 followers a quarter, roughly +70% on the current organic pace, from an audience that
already chose Lior once. It has never been run as a campaign. It should be the first thing
we test in Q4.

---

## 5. What changes in how we work

### a. The Top 13 playbook gets a KPI amendment, not a rewrite

The playbook's stated KPI is "Exposure / impressions, threshold 10,000+. Not
engagement-rate, not reactions, not comments." That top line is now wrong. The ten
archetypes stay valid; their **ranking inverts**:

| Archetype | Best evidence | Under exposure KPI | Under follower KPI |
|---|---|---|---|
| 4 — Industry Release Decode | 142,818 imp @ 0.16% ER; 93K tutorial @ 0.09% ER | champion | **reach play, budgeted** |
| 8 — Personal milestone | 17,970 imp @ 1.16% ER | mid | **promoted** |
| 9 — Market empathy | 13,256 imp @ 1.95% ER | lowest reach | **promoted to first** |

Stated honestly: engagement rate is a **proxy**, not follower rate. This re-ranking is the
best inference available from the data we hold, and it is a hypothesis to be confirmed or
killed within one month of daily-delta attribution. If the data contradicts it, the data wins.

### b. The pre-publish gate gets one new mandatory question

> **Why would a stranger who has never heard of Lior press Follow after reading this?**

If the honest answer is "they would not, but it will travel", the post is a reach play and
must fit inside the monthly reach budget below. It does not get published by default any more.

### c. Monthly post mix becomes a budget

- **60% conversion posts** — personal artifact, real past failure, operator confession,
  market empathy. The formats that make a stranger want the person, not the information.
- **30% authority posts** on the chosen niche, to train the interest-graph classifier.
- **10% reach plays** — roughly one Archetype 4 newsjack a month. Kept because on-lane
  reach still feeds the top of the funnel, but capped rather than defaulted to.

### d. ~~Volume stops being a lever~~ — SUPERSEDED 2026-08-23, see section 5A

Original text, kept for history: "Pending verification of the post counts, publish fewer and
better. July's 21 posts underperformed June's 7 on the only metric that now counts."

This was wrong. Outside data says frequency is one of the strongest follower levers on the
platform. What July actually proves is narrower and more useful. See 5A.

### e. The commenting program moves from tactic to channel

It is the only lever that puts Lior in front of a pre-qualified audience instead of a cold
one, which is precisely the term the decomposition says is broken. The 8-name alert tier
and the routine are in
`O-output/linkedin-growth-people-and-niches-2026-08-23.md`.

### f. The profile rewrite becomes blocking, not optional

It is the third term of the equation and an input to the classifier. Nothing else on this
list can be measured cleanly until the landing page stops leaking.

---

## 5A. The wide view — added 2026-08-23 after Reut's challenge

**The challenge, and why it lands.** Everything in sections 2-5 is derived from Lior's own
account: four months, roughly 50 posts, one voice, one posting rhythm. That data can only
describe variance *inside what we already do*. It is structurally incapable of evaluating a
strategy we have never run. Reut's correction was to look at the accounts that actually have
the followers we want and ask what they share. That is the right instrument, and it changes
two of my conclusions.

### What the large accounts have in common

Chris Donnelly went from roughly 20,000 to 1,000,000+ LinkedIn followers in about two years,
and reports 55,000 to 820,000 in 20 months. Rowan Cheung, Zain Kahn, Allie K. Miller and
Justin Welsh are all in the same shape. Looked at together, the shared mechanism is not the
topic and it is not the writing quality. It is this:

**A follow is a subscription decision, not a reaction.** Someone follows when they conclude
"there will be more of this, and I will miss something if I am not here." Every large account
manufactures that conclusion the same five ways:

1. **A signature series.** A recurring, recognisable format on a fixed rhythm. The format is
   the product. Welsh publishes one idea a day in an identical shape. Cheung and Kahn are
   daily AI briefings. The reader is not choosing a post, they are choosing a habit.
2. **The promise sits in the headline.** Zain Kahn's LinkedIn headline reads "Follow me to
   learn how you can leverage AI." Allie K. Miller's names her rank in AI business. These are
   subscription pitches, not job titles. The profile states what you get for following.
3. **Frequency high enough to form the habit.** Reported benchmarks: 3-5 posts a week is the
   band for individual creators; accounts posting 5x weekly are reported to grow around 12x
   faster than 1-2x weekly; consistent posting is credited with up to a 450% engagement lift
   over sporadic posting. Only about 3% of LinkedIn users post more than once a week, so the
   competition for a habit slot is thin.
4. **Renewable utility, not one-off narrative.** "Do not fall behind" is a need that returns
   every week. A great story is consumed once and does not create a reason to come back. This
   is Reut's core observation and it is the part our own data could never have shown us.
5. **Saveable artifacts.** Carousels, infographics, lists, roundups. Saves are also the
   strongest signal in the interest-graph ranking, so the format that builds the habit and the
   format the algorithm rewards are the same format.

### The reconciliation with July, which is the useful part

July ran 21 posts, about 4.8 a week, which is inside the optimal band. It still produced our
worst follower month. So frequency alone is clearly not sufficient, and I was wrong to read
that as frequency being irrelevant. The accurate statement:

> **Frequency without a repeating format and a consistent topic is noise. July had the volume
> and neither prerequisite.** 21 scattered posts do not train the algorithm's topic classifier,
> and they do not train a reader to expect anything. Average impressions per post collapsed
> from 7,406 in June to 3,418 in July, which is exactly what a confused classifier looks like.

We ran the volume experiment without the two things that make volume work, and then concluded
volume does not work. That conclusion has to be withdrawn.

### The second thing I got wrong: the guides

I argued against Yonatan's four guides a week using the 93K tutorial post's 0.09% engagement
rate. That compared two **one-off** posts, and the variable that actually separates the large
accounts from us is **recurrence**. A single tutorial cannot build a subscription habit by
definition, so its weak resonance says nothing about whether a named, recurring format would
work. My objection to the content type was over-extended. The objection that survives is
narrower and still real: an unnamed stream of generic AI guides is the Educator/Curator lane,
which fails the CEO relevance filter and is a lane where Cheung and Kahn beat us on speed and
staffing every single day.

### The thing that does not transfer

Chris Donnelly's own voice is described as conversational and motivational. That is the
Motivator archetype, explicitly banned for Lior, who is the Architect of Growth. Same
discipline as the structure-harvest work: **take the mechanism, never the voice.** The large
accounts are mostly media businesses. Lior is a CEO. Copying their payload turns him into a
worse version of them. Copying their mechanism with a payload only he can produce is the play.

### So what is the CEO-legal version of a recurring value promise?

The large accounts sell **curated information**. Lior can sell something they structurally
cannot: **access**. Nobody else publishing about AI and commerce is running a 250-person
commerce company while they write.

**Recommended signature series, the spine of the whole strategy:**

**"The operator's read on AI commerce"** — one fixed day every week. What changed this week in
AI and commerce, and what it actually means for anyone selling online, judged from inside the
company. Rowan Cheung reports the news. Lior delivers the verdict. The recurring promise is
"you will not fall behind on the one shift rewriting e-commerce," which is renewable by
definition. It is judgment, not tutorial, so it clears the CEO filter and the no-tool-tips
rule. It sits exactly on the agentic-commerce niche, so it also trains the classifier.

**Supporting slots:**
- **"From the 200"** — one real decision, number or thing that broke inside the company, and
  what he did about it. Access again, and it feeds the briefing with proof. Hits the "I live
  on 200" pillar directly. Needs a check on what is safe to share.
- **The artifact series** — the personal-artifact format that produced 57% of Instagram's July
  growth, run on LinkedIn as a series for the first time. This is the affinity layer. It makes
  people like him. It does not, on its own, make them subscribe.

### Revised working model

Sections 3, 4, 6 and 7 stand. The **theory of how followers arrive** changes:

| | Superseded | Revised |
|---|---|---|
| Primary follower engine | personal and vulnerability posts | **a signature series on a fixed rhythm** |
| Role of personal posts | the engine | the affinity layer around the engine |
| Frequency | publish fewer and better | **ramp to 3/week in September, 5/week in Q4** |
| Post mix | 60 conversion / 30 authority / 10 reach | **1 signature briefing + 2 niche authority + 1 personal artifact + 1 reactive, weekly** |
| Profile rewrite | hygiene, and a classifier input | **the subscription pitch. The headline states what you get for following** |

### What still needs proving

This section is built on outside benchmarks published by content-marketing vendors, who sell
posting tools and therefore have an interest in concluding that people should post more. The
direction is consistent across sources and the mechanism is coherent, but it is not audited
data. The honest next step is our own scan: take 8-10 accounts that actually grew, code their
recurring formats, cadence and headline promises, and check the pattern rather than trusting
the blogs. That study is worth running before the Q4 plan is locked.

---

## 6. The measurement routine

| Cadence | What | Where |
|---|---|---|
| **Backfill, this week** | Monthly profile visits, April through August | LinkedIn Analytics → Profile viewers, one custom range per month |
| **Backfill, this week** | Verified post counts, April through August | Creator Analytics → Posts tab |
| **Weekly, Monday** | Daily new-follower series for the past 7 days, joined to posts published | Analytics → Audience, daily view |
| **Monthly** | Net new followers, profile visits, impressions, post count → the three-term decomposition | Same, custom range |

The monthly deck headline changes from impressions to **net new followers**, with the
decomposition underneath and impressions demoted to a diagnostic row.

---

## 7. What we stop doing

- Stop reporting a 10K+ impression post as a win in its own right.
- Stop the "reach record" framing. May 2026 was our worst conversion month.
- ~~Stop scaling post volume as a growth lever.~~ **Withdrawn 2026-08-23.** Frequency is a
  lever, but only behind a repeating format and a consistent topic. Ramp to 3/week then 5/week.
- Stop treating profile visits as a nice-to-have. It is now the number that decides where
  we intervene.
- Do not add a stream of unnamed, generic AI guides. That is the Educator/Curator lane and
  Cheung and Kahn beat us on speed and staffing daily. **Revised 2026-08-23:** a *named,
  recurring, operator-judgment* series is the opposite of this and is now the recommended spine.

---

## 8. Needs Lior's sign-off

1. **The Q4 ladder**: 1,400 / 1,800 / 2,200. It is a 2.3x exit run-rate and it should be
   his number, not ours.
0. **The signature series and the cadence it commits him to.** A weekly fixed-slot format at
   3 to 5 posts a week is a real standing commitment on his calendar and on ours. It is the
   single biggest ask in this document and nothing else works without it.
2. **The 100K date.** He should hear that organic lands in 2029, and decide whether paid
   follower campaigns enter the conversation. That decision changes the entire Q4 plan and
   it cannot be made at our level.

---

## 9. Caveats

- Post counts are unverified and June's looks low. Every volume conclusion here is
  provisional until the Creator Analytics export confirms them.
- Engagement rate is standing in for follower rate throughout section 5a. It is the best
  proxy we hold, and it is still a proxy.
- The 150-follower win condition is an estimate against the current baseline and needs one
  month of real attribution data before it hardens into a gate.
- August numbers are not yet pulled, so every "current pace" figure runs through July.
