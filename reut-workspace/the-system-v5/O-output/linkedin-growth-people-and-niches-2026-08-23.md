# LinkedIn follower engine — people list, comment targets, AI niches

Built 2026-08-23 for Reut, after the call with Yonatan Raveh.
Goal this document serves: **followers**, not impressions. Every recommendation below is
filtered against that one metric.

---

## 0. Where Yonatan is right, and the one place he needs correcting

**Right, and our data already proves it:**

- *"Go more personal — failures, challenges, how I got through it."* Our numbers agree.
  The highest engagement-rate posts Lior has ever published are the personal ones:
  the Israeli-tech-layoffs post at 1.95% ER and the exit-birthday post at 1.16%, versus
  0.16% on the record-reach Google post and 0.09% on the 93K tutorial post. On Instagram,
  one childhood photo post drove 57% of July's entire follower growth. Personal artifact
  is the proven follower converter on every channel we run.
- *"Half-niche inside AI, not AI in general."* This is now algorithmically enforced, not
  just editorially smart. LinkedIn's feed has been an interest graph since March 2026:
  it ranks by topic-embedding relevance and it reads the poster's profile text before it
  distributes anything. Off-lane posts do not just underperform, they mis-train the
  classifier for the next post.
- *"Comment early on a viral post, before it drowns."* Correct. In our own July creator
  scan, Steven Bartlett's top post carried 1,597 comments. A comment posted at hour six
  on that post is invisible. The window is the first 30-60 minutes.
- *"Keep a list of people and a list of topics."* That is exactly what sections 1-4 are.

**Where I would push back — the 4 guides a week.**

He is skeptical about the ability to produce them. I am skeptical about whether we should,
and for a harder reason: our data says guides are the wrong instrument for a follower goal.
The 93K "Anthropic MD→HTML workflow" post is the single best evidence we have on tutorial
content, and it converted at 0.09% engagement, the lowest of any winning post in the set.
Tutorials buy cold reach and debate comments. They do not buy affinity, and affinity is
what makes someone press Follow. Four guides a week would be four reach plays a week
against a conversion problem. Guides stay a monthly reach lever, in the insider-intel
framing only, never a weekly production line.

**The thing neither of us said out loud, and it is the real one.**

Impressions moved 6x this year. New followers stayed in a 922-1,100 per month band every
single month. That is not a content problem, it is a leak between *impression → profile
visit → follow*. Two of the three fixes are cheap and we have never done them:

1. **The profile itself is the landing page and it has never been rewritten for this.**
   Every follower decision happens there, and the interest-graph classifier reads it too.
   One rewrite of the headline and About against the chosen niche, one time, affects both.
2. **We still do not track LinkedIn monthly profile visits.** It is the only metric that
   tells us which half of the funnel leaks. Pull it before we start, so the commenting
   program below has a before-number.
3. Everything else in this document.

---

## 1. The 20 — who to study and steal structure from

Grouped by *what we take from them*. Follower counts are approximate and mostly
self-reported; treat as signal, not proof. Slugs marked ⚠️ need one click to confirm.

### Tier A — Operator-CEO twins (steal topic AND structure; closest role match)

| # | Who | Profile | Why them | What we take |
|---|---|---|---|---|
| 1 | **Will Ahmed** (Whoop) | linkedin.com/in/willahmed | Our own creator scan flagged him as the closest voice match to Lior: operator CEO, earned milestones, zero motivation-speak | Named-entity anchor stories (Ronaldo, FDA clearance, F1 Monaco) that reliably clear 2K reactions. Milestone-as-earned-outcome framing, which is exactly our no-imposter-syndrome rule executed well |
| 2 | **Micha Kaufman** (Fiverr CEO) | linkedin.com/in/michakaufman ⚠️ | The acquirer's CEO. Warm graph, overlapping audience, and he posts hard on AI and the future of work | Big-thesis posts from a public-company seat. Also our single best commenting target: relevance is automatic and the audience is exactly ours |
| 3 | **Harley Finkelstein** (Shopify) | linkedin.com/in/harleyf | Commerce authority with founder voice. Posted the Economist "entrepreneur's paradise" piece in our August scan | Third-party authority visuals, commerce-macro framing. 🛑 Partner guardrail: never criticize, never argue, only build on |
| 4 | **Aaron Levie** (Box CEO) | linkedin.com/in/boxaaron ⚠️ | The template for a SaaS CEO who comments on AI economics daily and stays credible | The one-paragraph AI-economics take. Short, opinionated, no tutorial, always from the operator seat |
| 5 | **Tyler Denk** (beehiiv) | linkedin.com/in/tyler-denk ⚠️ | Build-in-public operator. His "what's the worst part of our product?" post pulled 201 comments off 130 reactions | The vulnerable direct ask. Cheapest comment-storm mechanic we have seen, and it fits Lior's voice without violating anything |
| 6 | **Simon Beard** | linkedin.com/in/simonbeardck | Contrarian policy takes from an operator seat; his #1 post by far | Contrarian-newsjack structure where the operator seat is the licence to speak |

### Tier B — AI-niche authorities (steal topic angles + borrowed reach; primary comment targets)

| # | Who | Profile | Why them | What we take |
|---|---|---|---|---|
| 7 | **Allie K. Miller** | linkedin.com/in/alliekmiller | ~2M followers, ranked #1 most-followed voice in AI business | How to make an AI topic land for a business audience without teaching a tool. Highest-value comment target in this tier |
| 8 | **Andrew Ng** | linkedin.com/in/andrewyng | Highest-authority AI voice on the platform; 2026 content is agentic workflows | Topic radar. Whatever Ng frames this month becomes LinkedIn's AI vocabulary next month |
| 9 | **Greg Isenberg** | linkedin.com/in/gisenberg | Closest match to Lior's 0→1 pillar. His "what_the_market_is_telling_us.md" post is the operational-artifact format that pulls outsized saves | The operational-artifact post: one concrete thing you actually run, shown, not explained |
| 10 | **Ruben Hassid** | linkedin.com/in/ruben-hassid | One of the highest-engagement AI creators on LinkedIn, and Israel-based | Pure mechanics: pacing, line breaks, how an AI post is packaged. 🛑 Voice and tool-tip topics die at the door |
| 11 | **Rowan Cheung** (The Rundown) | linkedin.com/in/rowancheung | ~2M newsletter; fastest AI news cycle on the platform | Day-1 timing. He is our early-warning system for what to newsjack, not someone to imitate |
| 12 | **Zain Kahn** (Superhuman AI) | linkedin.com/in/zainkahn | 1M+ subscriber AI newsletter | Same as Cheung: a news radar and a comment target, never a voice model |
| 13 | **Steve Nouri** | linkedin.com/in/stevenouri | ~2M followers, advises Nvidia / Oracle / Alteryx | Reach mechanics on AI topics at scale. Low priority as a model, high as a comment surface |

### Tier C — Craft layer (steal structure ONLY; their voice fails the CEO filter)

| # | Who | Profile | Why them | What we take |
|---|---|---|---|---|
| 14 | **Justin Welsh** | linkedin.com/in/justinwelsh | Owns the 5K-7.5K reaction band with one post a day | Mechanics only: sub-10-word hooks, one idea, open loop, daily consistency. 🛑 His self-reliance aphorism lane is the Motivator archetype, banned for Lior |
| 15 | **Jasmin Alić** | linkedin.com/in/alicjasmin | Ranked #1 LinkedIn expert by Favikon, Taplio and Aware; already on our advisor shortlist | Hook and copy craft at sentence level |
| 16 | **Amelia Sordell** | linkedin.com/in/ameliasordell | Founder-brand strategist, #1 Top Voice in personal branding; our recommended first advisor call | How a founder brand is built to serve the company, which is our exact brief |
| 17 | **Richard van der Blom** | linkedin.com/in/richardvanderblom | Publishes the annual Algorithm Insights report off 1.8M+ posts; already in contact | The only distribution advice on this list grounded in measured platform data |

### Tier D — Mega-reach story engines (steal hook + emotional architecture)

| # | Who | Profile | Why them | What we take |
|---|---|---|---|---|
| 18 | **Steven Bartlett** | linkedin.com/in/stevenbartlett- ⚠️ | Biggest numbers in our entire scanned pool: 18.6K reactions on the hiring post, 5.9K on skill-stacking | The contrarian question post ("are we confusing how important AI is with how safe it is to invest in?") is the single most transferable format on this list for Lior |
| 19 | **Alex Hormozi** | linkedin.com/in/alexhormozi | Consistent 2.7-5.1K on origin-story and image-only posts | The immigrant-parents origin-story structure. Proof that a first-person story beats a framework |
| 20 | **Dan Martell** | linkedin.com/in/danmartell | The rehab-parking-lot letter did 549 reactions and 151 comments in 21 hours | The vulnerability-letter format: fastest comment velocity we have measured. 🛑 His activity page is not auto-scannable, so he is manual-only |

**Bench, if we need depth:** Codie Sanchez, Matt Gray, Lara Acosta, Matt Barker,
Guillermo Rauch, Roei Burstein, Gary Vaynerchuk.

---

## 2. Who to comment on — the alert list

Commenting is the only lever on this page that puts Lior in front of a *pre-qualified*
audience instead of a cold one. That is why it is the strongest follower play we have,
and why it deserves a routine rather than a habit.

### Selection rule (all four must be true)

1. Their audience is founders, operators, e-commerce or SaaS people — our ICP
2. The post is about AI, commerce, building, or running a company
3. The post is trending toward 500+ reactions, so an early comment gets carried with it
4. **Lior has operator standing to say something nobody else in that thread can say**

If rule 4 fails, skip it. A generic agreement comment costs us more than silence.

### Tier 1 — bell ON, comment within 30 minutes (8 names)

| Who | Why this one first |
|---|---|
| Micha Kaufman | Warm graph, perfect audience overlap, and Lior's seat in that story is unique |
| Harley Finkelstein | Commerce authority; Lior is one of the few commenters who runs a 250-person commerce company |
| Allie K. Miller | Biggest AI-business audience that is still a business audience, not an engineering one |
| Greg Isenberg | 0→1 and agent topics; his comment sections are full of founders |
| Aaron Levie | AI economics from a CEO seat; Lior's counter-example carries weight there |
| Will Ahmed | Operator-CEO peer; the comment reads as peer-to-peer, not fan-to-creator |
| Steven Bartlett | Largest reach on the list. Only comment when the post is AI or building, never on the wellness lane |
| Rowan Cheung | Fastest AI news; his post is usually the first place a story lands on LinkedIn |

### Tier 2 — opportunistic, no alert

Andrew Ng, Zain Kahn, Steve Nouri, Ruben Hassid, Tyler Denk, Simon Beard,
Dan Martell, Alex Hormozi, plus anything from our Israeli tech graph.

### Never comment

Motivation and self-reliance aphorisms · anything critical of Shopify, Lovable or Wix ·
crypto, hardware, robotics · AI safety, ethics and regulation debates · any thread where
the honest comment would be "I agree".

### The routine (this is what makes it work)

1. Turn on the **bell** for all 8 Tier-1 profiles, one time, five minutes of work.
2. Two check windows a day: **09:00 and 16:00 Israel time**, aligned to US morning posting.
3. Target **5 comments a day**, all from Tier 1, all inside the first 30-60 minutes.
   Skip a day rather than comment late or comment weakly.
4. Comment shape, per our existing rules: engage what the post actually says **first**,
   one cutting line, the quotable *is* the comment, two lines maximum. A real Lior number
   only when it fits naturally, never force-fitted.
5. 🛑 I draft, Reut posts. Comments are never auto-posted. Unchanged rule.
6. **Measurement:** profile visits and follower delta, weekly. Pull the profile-visits
   baseline before day one, otherwise we will not be able to prove this worked.

If you want it automated: I can extend the existing scan scripts to poll the 8 Tier-1
profiles for new posts and drop draft comments into a file for you to approve. Worth
knowing that scheduled tasks only fire when the Mac is awake with the app open, so it
would be a helper, not a guarantee.

---

## 3. Niches inside AI — beyond what Lior named

Lior named three: AI commerce, AI video, AI for efficiency in life. Here is how I would
sharpen those and what I would add. Ranked by follower potential, filtered by whether
Lior has standing nobody else in the thread has.

### 🥇 1. Agentic commerce — "what happens when the buyer is a bot"

Not "AI commerce" in general. The specific question of what breaks when the shopper is an
agent. This is the strongest lane available to him and it is barely occupied by anyone
with operating experience.

The 2026 facts that make it a live topic: Google launched a Universal Commerce Protocol at
NRF in January, ChatGPT Shopping is open to all US users with a million-plus Shopify
merchants connected and reportedly ~50M shopping queries a day, AI traffic to US retailers
grew 393% year over year in Adobe's Q1 2026 data, and AI-referred shoppers convert about
42% better than human ones.

Why Lior wins it: almost every voice discussing this is a consultant or a vendor. He runs a
250-person commerce automation company and can say what actually changed in his own funnel
this quarter. That is the one comment nobody else in the thread can leave.

Post shapes: Crisis Response (Archetype 1) when a protocol change hits AutoDS ·
Big-Brand Reversal (Archetype 2) on any retailer flipping its AI stance · Industry Release
Decode (Archetype 4) on every protocol announcement, which is also our highest-reach archetype.

### 🥈 2. Running a 250-person company on agents — AI-native org design

Headcount economics, what he stopped hiring for, what he refuses to automate, what broke
when he tried. This is identity content for other founders, which is why it converts to
follows rather than just likes. It sits directly on the "I live on 200" pillar and it rides
the "software is dead" wave that went viral on both platforms in August.

Guardrail: this is the lane where the no-arrogance and no-fear-confession rules matter
most. Wins are earned outcomes. Vulnerability is a past failure with what it cost.

### 🥉 3. AI and the exit — what an acquirer diligences now

Nearly untouched on LinkedIn, and Lior's $92M exit is a credential almost none of the AI
commentators have. What a buyer pays for when any feature can be rebuilt in a weekend.
Low volume, very high authority. One post a month, maximum.

### 4. AI video as the commerce creative layer

He already named AI video. The version where he wins is not tool commentary, it is
production reality: what an AI-generated product video actually does to conversion,
and what it costs. We have real data from the trial reels engine and the AI clone videos.
Everyone else in this niche is showing demos. He would be showing results.

### 5. The AI slop backlash and the authenticity premium

The "AI slop" story pulled ~72K likes on X in August and the authenticity-fatigue theme
appeared in our weekly scan twice. His angle is commerce-specific: what happens to a
product catalogue when every listing, image and review is generated. Only worth doing
with the commerce anchor. Without it, it is content-about-content and it fails the CEO
relevance filter.

### Lanes to stay out of

- **General AI news commentary.** Cheung and Kahn do it full-time and faster. We lose.
- **Prompt and tool tutorials as a weekly format.** 0.09% engagement. Reach without affinity.
- **Token and cost optimization.** Already banned, and correctly.
- **AI safety, ethics, regulation, training-data IP.** No operator standing, and the lane
  is a fight, not an audience.
- **"AI for life efficiency."** Of the three Lior named, this is the weak one. It is the
  most crowded niche on LinkedIn, it collapses into productivity tips, and it fails the
  CEO relevance filter. If we keep it, it survives only as *his* routine, told as a founder
  story, never as advice to the reader.

### The 90-day allocation I would run

Given that the classifier now learns from every post, spread is expensive. One lane needs
a clear majority:

- **70% agentic commerce** — the spine
- **20% AI-native org design** — the pillar content
- **10% everything else** — exit lens, AI video results, cultural moments

Plus one prerequisite: **rewrite the LinkedIn headline and About against lane #1 before the
first post ships.** The classifier reads it before it distributes anything, and it is also
the page every profile visitor lands on. It is the cheapest thing on this entire document
and it sits exactly where our funnel leaks.

---

## Caveats

- Follower counts and rankings above come from third-party trackers and self-reported
  figures. None are independently audited.
- Four profile slugs are marked ⚠️ and need one click to confirm before the bell goes on.
- Everything here is a hypothesis until the profile-visits baseline exists. Pull it first.
