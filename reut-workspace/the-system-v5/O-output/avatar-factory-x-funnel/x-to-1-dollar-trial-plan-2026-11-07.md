# AvatarFactory on X: post to $1 trial, A to Z

Built 2026-11-07 from the AvatarFactory Marketing Brief, Lior's X data and the X algorithm book.
Owner: Reut. Status: plan, nothing set up yet.

---

## 0. The one-line goal

Every AvatarFactory sale that starts on X can be traced back to the exact post, placement and creator that sent it, all the way to the $1 three-day trial and to the first paid month after it.

The North Star metric is **paid conversions from X per week**, meaning trial → Starter/Creator/Influencer. Trials are the leading indicator. Impressions only matter when they turn into trials.

---

## 1. Gates: settle these before anything goes live

| # | Gate | Why it blocks | Who decides |
|---|---|---|---|
| G1 | **How Lior's ownership shows up on X** | Selling a product from his account without disclosing that he owns it is an FTC "material connection" risk. It also reads as a hidden ad. The Sept 26 post said "We use Avatar Factory" with no disclosure. | Lior |
| G2 | **AvatarFactory's existing UTM standard** | The brief says every outside link already follows "our UTM standard". Use theirs; don't invent a parallel one. Section 3 is the fallback if none exists. | AF growth team |
| G3 | **UTMs survive all the way to the $1 payment** | If the UTM drops between avatarfactory.io and app.avatarfactory.io/register and checkout, the whole funnel goes blind after the click. Needs a dev check. | AF dev |
| G4 | **Analytics access for Reut** | You need read access to whatever records register + trial + paid: GA4 / Mixpanel / Amplitude / Stripe or the billing tool. | AF team |
| G5 | **Results from the Oct 21 launch** | 4 paid creators, $3,600. If their links carried no UTM, that money produced no learning. Get whatever data exists as the baseline. | Agency / AF |

**My recommendation on G1:** disclose it. Lior's strongest X asset is himself: the "I'm Lior" origin threads drove 96% of September follows. "The founder who sold AutoDS is building his next company, here is what it does" is a better story than a tool tip, and it removes the FTC risk. Hiding ownership forces generic tool-review content, which is the weakest format on his account. This reverses the 2026-10-21 rule, so it's Lior's call.

---

## 2. The funnel and what gets measured at each step

```
X post (impression)
  → engagement: reply / bookmark / profile click         [X analytics]
  → link click: reply 1 / bio / pinned / Article / DM    [short-link clicks]
  → landing page session                                  [GA4, utm_*]
  → register at app.avatarfactory.io/register             [app DB + utm stored on user]
  → $1 trial paid (15 credits, 3 days)                    [billing, utm in metadata]
  → first video rendered during the trial                 [app event: activation]
  → converts to paid plan on day 3                        [billing]
  → month 2 renewal                                       [billing]
```

| Stage | Metric | Source | Starting target |
|---|---|---|---|
| Reach | Impressions, out-of-network share | X analytics | No target yet; the account had a soft throttle in 2026 |
| Interest | Reply rate, profile-click rate, bookmark rate | X analytics | Reply 1.5%+, profile click 1-3%, bookmarks 0.5-2% (book benchmarks) |
| Click | Link clicks per post | Short-link tool | Baseline in week 1 |
| Landing | Sessions per utm_content | GA4 | Clicks vs sessions gap < 20%. A bigger gap means tracking loss |
| Register | Registrations per utm_content | App DB | Baseline |
| Trial | $1 trials per utm_content | Billing | Baseline |
| Activation | % of trials that render a video | App event | Ask AF for the current site-wide number |
| Paid | Trial → paid % and plan mix | Billing | Compare with AF's site-wide trial → paid |
| Value | Revenue per 1,000 impressions | Calculated | The number that decides whether X is worth it |

Don't set targets for the bottom half until you have one full week of real numbers. Invented targets get defended later as if they were data.

---

## 3. UTM standard (fallback if AF has none)

All lowercase, no spaces, hyphens inside values, underscores between parts.

| Param | Value | Example |
|---|---|---|
| utm_source | `x` | `x` |
| utm_medium | where the link sits: `organic-post` / `reply` / `bio` / `pinned` / `article` / `dm` / `creator` | `reply` |
| utm_campaign | `af-x-lior-2026-11` (one per month or per launch) | `af-x-lior-2026-11` |
| utm_content | `<date>_<post-slug>` or `<creator-handle>_<date>` | `1110_origin-ai-influencer` |
| utm_term | format or angle being tested: `video-demo` / `thread` / `article` / `proof` / `build-in-public` | `video-demo` |

Example link for reply 1 under a demo video posted Nov 10:

```
https://app.avatarfactory.io/register?utm_source=x&utm_medium=reply&utm_campaign=af-x-lior-2026-11&utm_content=1110_copy-reel-demo&utm_term=video-demo
```

Rules:
1. **One row per link in a UTM sheet.** Columns: date, post URL, placement, full UTM link, short link, owner. Nobody types UTMs by hand in X.
2. **Wrap every link in a branded short link.** Use something like Dub or Bitly with a custom domain. It preserves the UTM, looks clean on X, and counts clicks on its own, so you can see how many clickers get lost before GA4.
3. **The bio link and pinned post get their own permanent UTMs** (`utm_medium=bio`, `utm_medium=pinned`). They will quietly carry a large share of conversions.
4. **Creators:** each creator gets their own `utm_content=<handle>`. Better still, use the AF affiliate link (50% lifetime, built-in dashboard), which tracks itself and pays for performance instead of a flat fee.
5. **Destination:** the brief's approved destination is `app.avatarfactory.io/register`. For cold traffic, test a landing page on avatarfactory.io against going straight to register. Internal links between AF pages never carry UTMs; that rule comes from the brief.

---

## 4. Technical setup checklist for the AF dev team

Send this to whoever owns the AF site and app.

1. **Capture UTMs on first landing** on avatarfactory.io and app.avatarfactory.io. Store them first-party, in a cookie on `.avatarfactory.io` plus localStorage, so they survive the move between subdomains.
2. **Save UTMs on the user record at registration**, both first-touch and last-touch.
3. **Pass UTMs into billing metadata** when the $1 trial is charged. This is the step that connects post → money.
4. **Fire 4 events** with UTM attached: `sign_up`, `trial_started`, `first_video_rendered`, `subscription_converted`.
5. **Add a "How did you hear about us?" field** at register, with options including "Lior Pozin on X". X's in-app browser often loses attribution when people come back later in Safari or Chrome. Self-reported attribution catches what UTMs miss.
6. **Test it end to end before launch.** Reut clicks a tagged link from the X app on a phone, registers, pays the $1 trial herself, then checks that the UTM appears on the user record and in billing. Run the test in the X in-app browser, not on desktop.
7. Optional: the X Pixel / conversion events on register and trial. These only matter if paid X promotion comes later.

---

## 5. The measurement platform: the vendor in the intro email

The email offers "tracking where every signup and demo comes from organically". That's useful, but **it does not replace steps 1-6 above**. Any tool still needs the UTM + billing connection to see the $1 trial and the day-3 conversion.

Take the call. Questions to ask:

1. Can it attribute **individual organic X posts**, not only "X" as a channel?
2. How does it handle **X's in-app browser** and the later return visit in Safari or Chrome?
3. Does it connect to **billing**, so it sees the $1 trial *and* trial → paid, not just signups?
4. Does it combine **self-reported attribution** with click data?
5. What install does it need from AF dev, and how long until first data?
6. Price, contract length, and whether there's a pilot before a commitment.
7. Can you see a live example built on an X-heavy B2C product?

Their slots: Friday 3pm EST has passed. **Monday Nov 9, 2pm EST = 21:00 Israel time.**

Decision rule: if the tool can tie posts → trials → paid with less dev work than section 4, buy it. If it only tracks signups, section 4 + GA4 + the UTM sheet is enough for v1.

---

## 6. Content strategy on X

### Where the link goes
- **Never in the post body.** Body links get near-zero reach on X. The post stands alone; the tagged short link goes in **reply 1** or in the final tweet of a thread.
- **Native video** is the strongest format: upload demos directly, with captions. Never link out to YouTube.
- **X Articles** for the long version, like the Oct 21 article, with the tagged link inside the Article.
- **Bio + pinned post** always point to the trial with permanent UTMs.

### Three content lanes, no more
Keep the topic tight so X knows who to show the account to.

1. **Lior builds an AI influencer in public**: his own avatar, real numbers, what worked and what failed. This is the "only Lior" lane and the strongest fit with his origin-thread engine.
2. **Proof from the market**: AI influencer accounts making money, using approved claims only ("accounts like…", 50M+ videos analyzed, 1,389 avatars past 1M followers).
3. **The tool working, on screen**: a 20-40 second native screen recording of Copy Reel, the avatar wizard or Viral Reels, with the link in reply 1.

### Mix and volume
- **1 in 3 Lior posts at most carries the AF offer.** His account is a founder brand; if it turns into an ad feed, follows and reach drop for everything.
- **Volume stays modest.** The account was throttled in May 2026 at 100+ posts a month and recovered at about 33. Don't use the "2-5 posts a day" playbook here.
- **Post Tuesday-Thursday mornings US Eastern.** The AF buyer is US-heavy. Block 30-60 minutes after each post to answer replies: replies the author answers are the strongest ranking signal.

### Brief rules that apply to every X post (from AF)
- The order is always: **go viral → the whole stack → no face needed.** Never open with "all-in-one".
- Offer wording: "$1 three-day trial". **Never "free", "start free" or "no card required".** CTA: "Start your $1 trial".
- **Never promise auto-posting, scheduling, Campaign Studio or automation.** None of these are live. ⚠️ The Sept 26 post said "send it to the queue" and should not be repeated.
- No dollar-income promises in anything that might later be promoted as an ad. Organic posts can show real account examples with "accounts like".
- AF's own brand presenter is Kate Hollis. On Lior's account the face is Lior or his own avatar.

### Audience fit note
Lior's X audience is founders and e-commerce operators. AF's primary buyer is the 18-40 make-money-online side-hustler. The overlap is real, since AutoDS users are side-hustlers too, but not complete. Watch trial → paid by `utm_term`: if founder-angle posts bring trials that don't convert, shift toward lane 2 or 3, or move the offer to creators who own that audience.

---

## 7. Implementation timeline

**Week 0, gates (Nov 9-13)**
- [ ] Lior decides G1, how ownership is disclosed
- [ ] Get AF's UTM standard and analytics access (G2, G4)
- [ ] Send section 4 to AF dev; get a date for the end-to-end test (G3)
- [ ] Call with the measurement vendor, Mon Nov 9 21:00 Israel
- [ ] Pull whatever data exists from the Oct 21 creator launch (G5)

**Week 1, build (Nov 16-20)**
- [ ] UTM sheet created, short-link domain set up
- [ ] Bio link + pinned post updated with permanent UTMs
- [ ] End-to-end test passes on a phone in the X app
- [ ] Weekly dashboard set up, using the section 2 table as columns
- [ ] Agency briefed: link only in reply 1, content lanes, brief rules, disclosure line

**Weeks 2-5, 30-day sprint (Nov 23 - Dec 18)**
- [ ] About 3 AF posts a week inside the normal Lior mix, each with its own utm_content
- [ ] Every week, test one variable at a time: format (video vs thread vs Article), then lane, then destination (landing page vs register)
- [ ] Creators run on affiliate links or their own utm_content
- [ ] Weekly review every Sunday: which utm_content produced trials and which produced paid conversions

**Week 6, decide (Dec 21)**
- [ ] Revenue per 1,000 impressions, by lane and format
- [ ] Double down on the winning format, kill the bottom third
- [ ] Decide whether to buy the measurement tool, based on how much the setup missed

---

## 8. Weekly dashboard: one row per post

| Date | Post | Lane | Format | Impressions | Replies | Profile clicks | Link clicks | Sessions | Registers | $1 trials | Paid | Revenue |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Plus 3 fixed rows each week: bio, pinned, and each creator.

---

## 9. Open questions for the AF team / Lior

1. Is there an existing UTM standard document? Send it.
2. Which tools record register, trial and paid today: GA4, Mixpanel, Stripe, something else?
3. What is the current site-wide trial → paid rate and the average LTV? The agency asked for LTV. Without it, nobody can judge what an X trial is worth.
4. Did the 4 Oct 21 creators use tagged links? Any results?
5. Should AF have its own X account? The brief lists IG, TikTok and YouTube, but not X.
6. Is there a budget for affiliate-style creator deals instead of flat fees?
