# LinkedIn Viral Radar: Requirements Document

**Owner:** Reut Amariyo, LinkedIn content manager for CEOs and executives
**Audience:** the AI engineer building the system
**Version:** 1.0, 2026-09-24

---

## 1. What we are building

A web system that reads up to 100 LinkedIn profiles I choose, once a day. It finds the posts they published in the last 24 hours and shows me the top posts that went viral in my niche. I use them as inspiration when I write posts for the executives I manage.

The system only reads and ranks. It never writes, analyzes, or rewrites content for me. I want to open one page each morning and see what worked, with a link to each post.

**Phase 1 user:** one executive, Lior Pozin, founder of AutoDS.
**Future users:** me, Tal, and other executives. Each person gets their own profile list, niche and results. Build for multiple clients from day one, even though only one is live at launch.

---

## 2. Scope

### In scope
- Managing a list of up to 100 LinkedIn profiles per client
- A daily collection of every post those profiles published in the last 24 hours
- Scoring each post for virality and for relevance to the client's niche
- A web dashboard with at least 10 ranked posts per day, each linked to the original post
- A history of past days

### Out of scope, and never allowed
- Posting, liking, commenting, following, or sending messages on LinkedIn
- Logging in to LinkedIn with any real person's account, including mine or a client's. An account ban on an executive's profile is the worst outcome this project could have.
- AI teardowns, hook analysis, rewrite ideas, or content drafts. I do that part myself.

---

## 3. Core concepts

| Term | Meaning |
|---|---|
| Workspace | One client, for example "Lior". It holds a profile list, niche topics, a blocklist and settings. |
| Tracked profile | A LinkedIn person profile URL inside a workspace. |
| Niche topics | The topics this workspace cares about, for example AI, leadership, business, CEO / founder-led thought leadership. |
| Original post | A post the tracked person wrote. Reposts of someone else's content are excluded. |
| Creator median | The median engagement of that person's recent original posts. It is the baseline for "viral for them". |

---

## 4. Functional requirements

### 4.1 Workspaces and users
- **FR-1** Create, rename and archive workspaces.
- **FR-2** Dashboard login with email + password or Google sign-in. A few users at most. Every user can see every workspace in phase 1.
- **FR-3** Each workspace has its own profile list, niche topics, blocklist, run time and history. No data leaks between workspaces.

### 4.2 Profile list management
- **FR-4** Add profiles by pasting URLs, one per line, or by uploading a CSV. Remove or pause a profile from the dashboard.
- **FR-5** Validate every URL on import. Show name, headline, follower count and profile photo so I can confirm it is the right person.
- **FR-6** Flag profiles the system cannot read. Some creators hide their activity from logged-out viewers. In our pilot this was 11 of 103 profiles. Show them as "not readable" with the reason. Do not fail silently.
- **FR-7** Cap: 100 active profiles per workspace. The cap should be a setting, not hard-coded.
- **FR-8** Blocklist per workspace: creators whose posts are collected for baselines but never shown in the ranking.

### 4.3 Daily collection
- **FR-9** Run once a day per workspace at a configurable time. Default 08:00 Israel time.
- **FR-10** Collect every original post published by tracked profiles in the 24 hours before the run.
- **FR-11** For each post, store:
  - Post URL, which must open the post directly on LinkedIn
  - Creator name, profile URL, photo, follower count at collection time
  - Publish time and hours since publishing at collection time
  - Full post text
  - Format: text only, image, carousel / document with page count, video, poll, article, link
  - Likes / reactions, comments, reposts where the data source provides them
  - Media thumbnail
- **FR-12** Exclude reposts. Detect them by comparing the post's author to the tracked profile.
- **FR-13** Keep a rolling baseline per creator. The median engagement of their last 15 original posts that are at least 24 hours old. Backfill 15 posts per profile when a profile is first added, so the ranking works from day one.
- **FR-14** Handle partial failures. If 7 profiles fail, show the other 93 and list the failures on the dashboard. Retry transient errors automatically. Never retry "profile hidden" errors, since those are permanent.

### 4.4 Scoring

**Virality, relative to the creator.** This is the main signal. A post counts as viral when it beats that person's own normal, not when it comes from a big account.

    engagement = comments x 3 + likes x 1  [+ reposts x 4 if the source provides them]
    x_median   = engagement / creator median engagement
    viral      = engagement x min(x_median, 10)

- **FR-15** Age fairness. A post that is 4 hours old cannot be compared raw to one that is 22 hours old. Normalize by engagement per hour, or propose a better method and document it.
- **FR-16** Noise floor. The x_median multiplier only applies above a minimum absolute engagement, 100+ likes or 20+ comments by default. Without it, a post with 12 likes from a tiny account ranks as a 6x breakout.
- **FR-17** Outlier bar, configurable per workspace. Defaults: x_median ≥ 2 AND 1,000+ likes or 200+ comments. Posts that clear it get a visible "Breakout" badge.
- **FR-18** A creator needs at least 5 baseline posts before x_median is shown. Until then, show "new creator" and rank on absolute engagement only.
- Impressions are not used. They are not visible on other people's posts.

**Relevance to the niche**
- **FR-19** Score every post 0-100 for how well it matches the workspace's niche topics. Use an LLM classifier with the niche definitions as the prompt. The niche definitions are editable free text per workspace.
- **FR-20** Each workspace also has an exclusion list of topics, for example career advice, hiring tips, crypto, hardware. Posts matching an exclusion score 0.
- **FR-21** Text length floor. Posts with fewer than 40 words of text are tagged "image-only" and ranked below text posts by default. A photo with no text gives me nothing to learn from.

**Final ranking**
- **FR-22** Final rank = virality x relevance. Posts below the relevance threshold, 60 by default, are excluded.
- **FR-23** Show at least 10 posts a day when that many exist. If fewer than 10 clear the outlier bar, still show 10, but only the qualifying ones get the Breakout badge. If fewer than 10 relevant posts exist, show what exists and say so. Never pad with off-topic posts.

### 4.5 Dashboard
- **FR-24** Default view: today's ranked list for the selected workspace.
- **FR-25** Each post card shows:
  - Rank and Breakout badge
  - Creator photo, name, follower count
  - Hours since publishing
  - First 3 lines of the post, with "show full text"
  - Format tag and thumbnail
  - Likes, comments, reposts, x_median, relevance score
  - **An "Open on LinkedIn" button that opens the original post in a new tab**
- **FR-26** Filters: niche topic, format, creator, Breakout only.
- **FR-27** Date picker to view any past day. Keep 12 months of history.
- **FR-28** Per-post actions: "Saved" and "Hide". These are internal only and never touch LinkedIn.
- **FR-29** A status line for each run: time, profiles read, profiles failed, posts collected.
- **FR-30** Works on desktop and mobile browsers.

### 4.6 Optional, phase 2
- A morning email or Slack message with the top 10 and a link to the dashboard
- A weekly view that ranks the week's breakouts

---

## 5. Non-functional requirements

- **NFR-1 Data source.** Use a third-party LinkedIn data provider that collects publicly visible data without our accounts, for example Bright Data or Apify. The engineer recommends one, with cost per month for 100 profiles daily plus the backfill.
- **NFR-2 Cost.** Give a monthly running-cost estimate before building: data provider, LLM calls, hosting. Show the cost at 1 workspace and at 5.
- **NFR-3 Reliability.** The daily run must happen whether or not anyone's computer is on. Cloud hosted, with an alert when a run fails.
- **NFR-4 Speed.** Results ready within 30 minutes of the scheduled run time.
- **NFR-5 Security.** API keys live in the hosting platform's secret store, never in code or the repo. The dashboard is behind login.
- **NFR-6 Ownership.** The code lives in a repository I own. Include a README that explains how to run, deploy and change settings, written for a non-engineer.

---

## 6. What we learned from our pilot

I ran a working prototype in September 2026 on Bright Data with 103 creators. The engineer should know these facts before choosing a design:

1. **About 11% of profiles hide their activity** from logged-out viewers and cannot be read by any scraper that does not log in. Often these are exactly the AI creators with the most saved content. Flag them in the UI, do not work around them with a login.
2. **About 33% of returned posts were reposts** of someone else's content. They must be filtered out, or they distort both the ranking and the baselines.
3. **Bright Data's LinkedIn posts dataset returned no repost counts.** It returned likes, comments, text, media, document page count, author followers and top comments. If repost counts matter, the engineer should find a source that has them, or drop them from the formula.
4. **There is no keyword discovery for LinkedIn posts** on that provider. You can only collect from profile URLs you name. "Trending in AI" is therefore limited to the profile list. That is acceptable for this project.
5. **Collection jobs took 2-6 minutes** and sometimes returned "still building" before they were done. Poll with retries.
6. **Post text can contain unusual line-separator characters**, for example U+2028. Parse carefully.
7. **Big accounts produce baseline posts that look big.** A post with 600 likes from a creator with 1.2M followers is a normal day for them. That is why relative scoring matters. Show likes per 10K followers on the card as a sanity check.
8. **Posts under 7 days old are "trending"**. Anything older is not. The 24-hour window is the product. The history view is for reference only.

The prototype code, a Python script with its scoring logic, is available on request as a reference.

---

## 7. Phase 1 workspace setup: Lior

- **Niche topics:** AI, leadership, business, CEO and founder-led thought leadership, entrepreneurship, e-commerce at the executive level
- **Exclusions:** career advice, job search, LinkedIn/marketing tactics, AI tool tutorials, productivity tips, hiring and compensation mechanics, crypto, hardware / robotics
- **Blocklist:** Alex Hormozi, Gary Vaynerchuk, Ruben Hassid, Amber Spears
- **Profiles:** I will provide the list of 100 URLs as a CSV at kickoff.

---

## 8. Milestones and acceptance

| # | Milestone | Done when |
|---|---|---|
| 1 | Plan + cost estimate | Engineer delivers stack, data provider choice, monthly cost, timeline. I approve before any build. |
| 2 | Collection + storage | 100 profiles backfilled, daily run stores posts, reposts excluded, hidden profiles flagged. |
| 3 | Scoring | Virality and relevance scores for one day of data. I review the top 20 and agree they make sense. |
| 4 | Dashboard | All of section 4.5 live behind login, on desktop and mobile. |
| 5 | Two-week burn-in | 14 consecutive daily runs with no manual fixes. At least 10 ranked posts each day when that many exist. Every "Open on LinkedIn" link works. |
| 6 | Second workspace | I create a second workspace from the dashboard, with no engineer help, and it runs the next day. |

**Final acceptance:** I open the dashboard at 08:30, pick a workspace, and within one minute click through to a relevant, verifiably viral post from the last 24 hours.

---

## 9. Questions for the engineer to answer in the plan

1. Which data provider do you recommend, and what does 100 profiles a day cost?
2. Which stack and hosting do you propose, and why?
3. How will you handle age fairness for posts of different ages in FR-15?
4. Which LLM will you use for relevance scoring, and what is the cost per day?
5. What breaks when we go from 1 workspace to 10, and what would that cost?
