# August 2026 Review — Raw Data (Month 2 of Q3)

_Built 2026-09-08. Completes the offsite deck of 2026-09-02, which covered Instagram,
Facebook and TikTok only. LinkedIn and X are added here from primary sources._

**Sources**
- LinkedIn: `AggregateAnalytics_Lior Pozin_2026-08-01_2026-08-31.xlsx`, LinkedIn's own export, provided by Reut 2026-09-08. Plus the Follower-growth and Top-demographics screens.
- X: `account_overview_analytics (5).csv`, X Account Analytics daily export 1-31 Aug, provided by Reut 2026-09-08. Per-post data pulled from Metricool 2026-09-08 into `O-output/x-performance-log/posts.jsonl` (110-day backfill).
- Instagram, Facebook, TikTok: the offsite pack of 2026-09-02 (`O-output/offsite-2026-09-02/`), sourced from the IG app, Facebook Professional Dashboard and TikTok Studio.
- Per-post LinkedIn detail: `claude-memory/memory/lior-performance-log.md`.

## OKR reference (Q3 targets = September run-rate)

| Platform | June baseline | Sep target views/mo | Followers Jun 30 | Followers target |
|---|---|---|---|---|
| Instagram | 2.44M | 2.6M | 71K | 95K |
| Facebook | 3.25M | 4M | 71.9K | 96K |
| LinkedIn | 52K | 70K | 10.8K | 13.5K |
| TikTok | 316K | 350K | 12K | — |
| X | 21K | 40K | — | — |
| **Total** | **6.1M** | **7M+** | **~166K** | **~202K+** |

---

## LinkedIn — August 2026 (exact calendar month, LinkedIn export)

| Metric | August | July | Change |
|---|---|---|---|
| Impressions | **144,796** | 71,776 | **+102%** |
| Members reached | **69,295** | 24,764 | **+180%** |
| Engagements | **4,675** | 1,970 | **+137%** |
| Engagement rate | **3.23%** | 2.74% | +18% |
| New followers (gross) | **1,728** | 1,061 | **+63%** |
| Total followers (Aug 31) | **12,980** | 11,607 | **+1,373 net** |
| Followers per 1K impressions | **11.9** | 14.8 | -20% |

**Daily shape.** The month has one spine: Aug 25 (18,295 imp / 898 eng), Aug 26 (41,195 / 1,613),
Aug 27 (10,049 / 317). Those three days are **48% of the month's impressions and 40% of its new
followers**, 685 of 1,728. Second wave Aug 12-13 (8,967 + 5,604). Floor day 594.

**Top posts by impressions (LinkedIn export):**
1. **70,922** — 8/25 "Sold my business to Fiverr for $92M with this 47-slide deck" (ungated exit deck) — also #1 by engagement, 2,906
2. 11,436 — 8/5 "At 28, I sold my business to Fiverr / 7 things I wish someone had told me"
3. 9,860 — 8/16 "This role is probably not for you. Top 0.1%" (hiring, negative-filter hook)
4. 8,383 — 8/12 "Galit finished dental school this week"
5. 8,373 — 8/11 "Anthropic just dropped invisible watermarks into Claude"
6. 6,503 — 8/26 "There's a reason Claude keeps giving you mid output"
7. 4,962 — 8/18 "100K followers on Instagram this week"
8. 4,603 — 8/6 "Here's the secret behind Shopify's 18% jump"

Bottom of the month, for the record: 8/20 founder stations 1,104, 8/27 SaaS steps 1,450,
8/17 watermark explainer 1,456, 8/10 Jim Rohn 695.

**The follower-conversion finding.** May did 292,705 impressions and produced 1,100 followers,
0.38% of impressions. August did **half of May's reach and produced 57% more followers**, 1.19%
of impressions. Four months sat inside a 922-1,100 net band no matter what reach did. August is
the first break in that band and it came from one post type.

**Audience demographics (followers, Aug):** Founder 12% + Co-Founder 10% + CEO 7% + Owner 1%
= **30% founders/CEOs by title**, unchanged from July. Seniority: Senior 25%, CXO 21%, Owner 13%,
Director 8%. Company size 2-50 = **46%**. Locations: Tel Aviv-Yafo 10%, NYC 5%, Miami 3%,
SF Bay 2%, London 2%. Top company: Shopify 1%.

**Content demographics, who the posts actually reached in August:** Senior 27%, Entry 24%,
CXO 10%. Founder 8%, Software Engineer 5%. NYC 6%, Tel Aviv 6%, SF Bay 3%, London 3%.
The reached audience is more junior and more technical than the follower base, which is what
a month carried by an AI-topic and a viral artifact post looks like.

**vs OKR (Sep targets: 70K impressions, 13.5K followers)**
- Impressions **144,796 = 207% of the September target**, in month 2.
- Followers **12,980 = 96% of the 13.5K target**, needs +520 in September to land it. On the August rate that is comfortable, on the four-month rate it is exactly on the line.

---

## X — August 2026 (exact calendar month, X Account Analytics export)

| Metric | August | July | Change |
|---|---|---|---|
| Impressions | **324,235** | 93,400 | **+247%** |
| Engagements | **9,357** | 1,700 | **+450%** |
| Engagement rate | **2.89%** | 1.8% | +61% |
| Likes | **3,992** | 646 | +518% |
| Bookmarks | **3,663** | 397 | **+822%** |
| Reposts | 263 | 177 | +49% |
| Replies | 78 | 63 | +24% |
| Shares | 136 | 20 | +580% |
| Profile visits | **1,225** | 472 | +160% |
| New follows | **867** | ~150-200 | ~+4x |
| Unfollows | 22 | — | — |
| **Net follows** | **+845** | ~+150-200 | — |
| Posts created (X count) | 23 | 24 | -4% |

Metricool logs 47 items for August; the gap against X's 23 is thread parts and the two
"Follow @lior_pozin" cards. Impressions per post on X's count: **14,097 vs July's 3,890, 3.6x.**

**Daily shape, and the split that matters.**

| Day | Impressions | % of month | New follows | % of month |
|---|---|---|---|---|
| Aug 20 | 120,567 | 37% | 24 | 3% |
| Aug 19 | 107,547 | 33% | 27 | 3% |
| Aug 16 | 39,486 | 12% | **489** | **56%** |
| Aug 17 | 15,430 | 5% | **195** | **22%** |
| Aug 15 | 7,926 | 2% | 64 | 7% |

**Aug 19-20 is the "Someone on Reddit just LEAKED…" post: 219,123 impressions, 3,185 likes,
and 51 followers across both days.** 70% of the month's reach bought 6% of the month's follows.

**Aug 15-17 is the "The kid nobody would have bet on" personal-timeline thread: 58,103
impressions, 1,179 profile clicks, and 748 followers across three days.** 19% of the reach
bought 85% of the follows.

**Top posts (Metricool, by impressions):**
1. 219,123 — 8/19 "Someone on Reddit just LEAKED the exact step-by-step process…" (3,185 likes, 223 reposts, 84 profile clicks)
2. 58,103 — 8/15 "The kid nobody would have bet on" (154 likes, **1,179 profile clicks**)
3. 9,095 — 8/19 "Follow @lior_pozin if you want raw lessons…" (follow card)
4. 5,017 — 8/27 "I met my wife when I was working 16-hour days"
5. 2,224 — 8/14 "At 21, I lost the only business I had"

**Follower total.** X's export gives daily follows and unfollows, not a running total. July closed
at 487 confirmed on Aug 4, so August closes at **~1,330, derived**. Confirm from the X app profile
before this goes to Lior.

**vs OKR (Sep target 40K impressions)**
- **324,235 = 810% of the September target.** The platform that missed its Q2 OKR at 54% is now the biggest overshoot in the family, two months running.

---

## Instagram — August 2026 (offsite pack, 2026-09-02)

| Metric | August | July | Change |
|---|---|---|---|
| Views | **3,331,989** | 4,100,000 | -19% |
| Viewers | 1,271,908 | — | — |
| Content published | **161** | 114 | +41% |
| Avg views per piece | **20,696** | 35,965 | **-42%** |
| Profile visits | 64,241 | 65,463 | flat |
| Gross follows | 11,600 | 26,300 | -56% |
| **Net followers** | **+8,976** | +24,354 | -63% |
| Bio link taps | 964 | 750 | +29% |
| Total followers (Aug 31) | **104,659** | 95,635 | crossed 100K on Aug 16 |

**The artifact finding, already in the offsite deck.** Five giveaway posts out of 161 produced
**45% of the month's new followers**: "Comment CEO" 10-startups list 3,200 follows and 332K views,
"Comment EXIT" exit deck 1,400 follows. The 10-startups list was run four times: 3,200, then 267,
then 207. It decays 94% by the fourth run. Format proven, supply short.

## Facebook — August 2026

| Metric | August | July | Change |
|---|---|---|---|
| Views | **107,426** | 3,181,303 | **-94%** |
| Interactions | 1,521 | ~108,000 | -98.6% |
| Net followers | **-290** | +14,400 | — |
| Total followers | ~84,000 | — | vs 96K Q3 target |

Facebook alone is **102% of the brand's total July-to-August view drop.** Reels fell from 96.9%
of Facebook traffic to 63.3% while photo posts rose to 34.4%. Publishing was heavy Aug 5-12,
five to nine pieces a day, and those days made five to eight thousand views each against a July
daily average near 103,000. The read stays: distribution first, supply second. Still unpulled:
Facebook post count August vs July, and views per post for each. That one number settles it.

## TikTok — August 2026

| Metric | August | July | Change |
|---|---|---|---|
| Views | **1,391,919** | 858,333 | **+62%** |
| Videos | 41 | 25 | +64% |
| Avg views per video | 33,949 | 34,333 | flat |
| **Median video** | **4,318** | 1,877 | **+130%** |
| Top 3 share of month | 66% | 82% | -16pts |

The ceiling held and the floor rose. Followers and profile views still not pulled from the app.

---

## AUGUST TOTALS — all five platforms

| Platform | July views/imp | August views/imp | Change |
|---|---|---|---|
| Instagram | 4,100,000 | 3,331,989 | -18.7% |
| Facebook | 3,181,303 | 107,426 | **-96.6%** |
| TikTok | 858,333 | 1,391,919 | +62.2% |
| X | 93,400 | 324,235 | **+247%** |
| LinkedIn | 71,776 | 144,796 | **+102%** |
| **Total** | **8,304,812** | **5,300,365** | **-36.2%** |

**Facebook's drop is 3,073,877. The total drop is 3,004,447.** Every other platform combined
grew by 69,430 in the same month. The offsite deck put August at 4,831,334 because LinkedIn and
X were not in the room; the true figure is **5,300,365**, and the two missing platforms are the
two fastest-growing lines in the portfolio.

**Followers, end of August**

| Platform | Aug 31 | Net in August |
|---|---|---|
| Instagram | 104,659 | +8,976 |
| Facebook | ~84,000 | -290 |
| LinkedIn | 12,980 | +1,373 |
| X | ~1,330 derived | +845 |
| TikTok | not pulled | not pulled |
| **Total (excl. TikTok)** | **~202,969** | **+10,904** |

**vs Q3 KR1 (7M+ views/month, ~202K+ followers by September)**
- Views: **5.30M = 76% of target.** Facebook is 4M of that target and delivers 0.11M. Without Facebook's collapse the portfolio is above 8M.
- Followers: **~203K on four platforms already clears the ~202K target**, one month early, before TikTok is counted.

---

## Road to 500K Instagram and 100K LinkedIn

Baselines updated to Aug 31. Trailing-3 is the honest pace; single months on this account swing
too hard to plan from.

**Instagram, target 500,000**

| | Value |
|---|---|
| Now (Aug 31) | 104,659 |
| Gap | 395,341 |
| Net June / July / August | +4,740 / +24,354 / +8,976 |
| Trailing-3 average | **+12,690/mo** |
| Months at trailing-3 | **31** → ~April 2029 |
| Months at August alone | 44 → ~May 2030 |
| Months at July alone | 16 → ~January 2028 |
| To land in 12 months | +32,945/mo = **3.7x August** |
| To land in 24 months | +16,472/mo = **1.8x August** |

**LinkedIn, target 100,000**

| | Value |
|---|---|
| Now (Aug 31) | 12,980 |
| Gap | 87,020 |
| Net Apr / May / Jun / Jul / Aug | +922 / +1,100 / +1,009 / +821 / **+1,373** |
| Trailing-3 average | **+1,068/mo** |
| Months at trailing-3 | **82** → 2033 |
| Months at August alone | 63 → 2031 |
| To land in 12 months | +7,252/mo = **5.3x August** |
| To land in 24 months | +3,626/mo = **2.6x August** |

**What August changed in this math.** The August LinkedIn number is the first evidence that the
follower line responds to anything. It responded to one post: the ungated exit deck produced
roughly 590 incremental followers above the daily baseline in three days, about 43% of the month.
At that rate, 12 artifact posts a month lands the 12-month pace. We have two artifacts and we are
recycling them, so the binding constraint is supply, which is exactly what topic 2 of the offsite
concluded from Instagram data alone. Three platforms now say the same thing independently.

**The cross-platform rule August produced.** Reach and follows are separate buys.

| Post | Impressions | Followers |
|---|---|---|
| X, Reddit leak, Aug 19-20 | 226,670 | 51 |
| X, "kid nobody would bet on", Aug 15-17 | 58,103 | 748 |
| LinkedIn, exit deck, Aug 25-27 | 69,539 | ~590 incremental |
| IG, 10-startups list | 332,000 | 3,200 |

Volume and virality move the impressions line. First-party artifacts and personal-timeline
stories move the follower line. Both Instagram in July and every platform in August agree.

---

## Still missing before this is complete

1. **ManyChat flow signups per month and Build Your Store trials per month.** Standing requirement for every monthly pack. Still not instrumented.
2. **TikTok followers and profile views**, from TikTok Studio.
3. **X follower total**, from the app profile, to replace the derived ~1,330.
4. **Facebook post count August vs July**, plus views per post, to settle distribution against supply.
5. **LinkedIn monthly profile visits.** LinkedIn's export still does not carry it; it remains the highest-value missing number for diagnosing the 100K path.
