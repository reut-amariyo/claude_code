# LinkedIn Swipe Engine — Setup Guide

Built 2026-09-06. Purpose: a dedicated LinkedIn profile whose feed is 100% top AI +
top general creators, so every day we harvest the best-performing posts and use their
structures as donors for Lior posts. See [[feedback-build-on-proven-structures]].

**Rule for this whole build: Reut does every click. Claude never logs in, never follows,
never posts, never installs anything. Claude produces copy-paste material only.**

---

## Known risk, stated once

LinkedIn's user agreement is one profile per person. A second account can be restricted,
and because it will share your device, browser fingerprint and IP with your main account,
a restriction can be linked back. You decided to proceed on 2026-09-06. The pacing below
is designed to keep the account looking like a normal new user, which is the main defence.

---

## STEP 1 — The email

Create a fresh Gmail. Do NOT use an autods.com address and do NOT alias your main Gmail
with +tags, LinkedIn treats those as the same mailbox.

Suggested handle patterns, pick one that reads like a real person:

    r.amariyo.research@gmail.com
    reut.a.studies@gmail.com
    reutamariyo.ai@gmail.com

Requirements:
- Set a recovery phone. LinkedIn phone-verifies most new accounts.
- Use a phone number that is NOT already attached to your main LinkedIn. If you only have
  one number, expect a verification challenge and be ready to solve it manually.
- Log the credentials in your password manager, not in this vault.

## STEP 2 — Create the profile (day 1, then stop)

Sign up at linkedin.com/signup from a normal browser window. Not incognito, not a VPN.
A VPN or incognito signup is one of the strongest restriction triggers.

Fill these on day 1 and then close the tab. Do not follow anyone yet.

**Name:** your real name. A fake name is what gets accounts permanently removed, and it
also breaks your ability to recover the account.

**Headline** — copy-paste, pick one:

Researching what actually performs on LinkedIn | AI content study

Content strategist | studying AI and founder-led content on LinkedIn

Building a research feed on AI, founders and what makes people stop scrolling

**About section** — copy-paste:

I study LinkedIn.

Specifically: what AI founders, operators and creators publish, and which of it actually
travels. I read a lot more than I post. Most days I am reading 50 to 100 posts and taking
notes on structure, hooks and formats.

This account is my reading account. If you build in AI, or you write well about building
anything, I am probably already following you.

**Location:** Israel
**Industry:** Marketing Services
**Photo:** upload a real photo of yourself. A blank avatar on a new account is a flag.
**Banner:** upload anything neutral. An empty banner is also a flag.

**Experience:** add one real entry. Blank experience on a new profile is the single
biggest restriction signal after no photo.

    Content Strategist
    Self-employed
    2024 - Present
    Studying and documenting what performs on LinkedIn, with a focus on AI and
    founder-led content.

**Education:** add your real school.

Then log out. Day 1 is done.

## STEP 3 — Warm-up week (days 2 to 8)

Do NOT follow 100 people on day one. That is the exact pattern LinkedIn's restriction
system looks for on a new account.

Each day, 8 to 12 minutes, in this order:

| Day | What to do |
|---|---|
| 2 | Log in. Scroll the default feed for 5 min. Like 3 posts. Follow **5** creators from Wave 1. |
| 3 | Scroll 5 min. Comment one real sentence on 1 post. Follow **8** from Wave 1. |
| 4 | Scroll. Like 5. Follow **10** from Wave 1. |
| 5 | Scroll. Comment on 1. Follow **12** from Wave 2. |
| 6 | Scroll. Like 5. Follow **12** from Wave 2. |
| 7 | Rest day. Log in, scroll 3 min, follow nobody. |
| 8 | Scroll. Follow **13** from Wave 2. |

Then 15 per day until the list is done, roughly day 12. Full list is in
`01-creators-100.md`, already split into waves.

**How to follow, and this matters:** use the LinkedIn search box, type the person's name,
open their profile, read for a few seconds, click Follow. Do not paste 100 URLs in a row.
Pasting URLs at machine speed is what gets flagged, not the follow count itself.

**Follow, do not connect.** Connection requests have a hard weekly cap and pending
invites hurt your account quality score. Follow has no such cap. Every name on the list
is a creator, so Follow is the correct button.

## STEP 4 — Kill the noise

Once a week for the first month, open the feed and use the three-dot menu on anything
that is not one of the 100:
- "Unfollow [name]" for accounts LinkedIn auto-followed you into during signup
- "Not interested" on job ads, LinkedIn News, and suggested content

Goal state: the feed is 100% the 100 creators. Takes about 3 weeks of pruning to settle.

## STEP 5 — AuthoredUp

You already have it. Install the extension in the same browser profile you use for
this account, and sign in to AuthoredUp with the new email if it asks.

What AuthoredUp gives us here:
- Inline engagement numbers on every post in the feed, so you can see at a glance
  which ones are outliers without opening each post
- Save posts to a collection, which becomes the swipe file
- Its analytics side is for your OWN posts only, so ignore that part for this account

What AuthoredUp does NOT do: track other creators overnight on its own. That means the
harvest is a short manual pass by you. See STEP 6.

Optional upgrade later: Taplio. Its post database tracks other creators' top posts
automatically and exports them, which would remove the manual pass. Do not connect
Taplio to the new LinkedIn account, use only its search/inspiration database, which
works without any account connection. Decide after a month of running this manually.

## STEP 6 — The daily harvest, your 5 minutes

Every morning, or at night, whichever suits you:

1. Open the new profile's feed, sorted by **Recent** (feed dropdown, top of the feed).
2. Scroll ~5 minutes. AuthoredUp shows the numbers inline.
3. Save anything that clears the outlier bar: **500+ reactions, or 100+ comments,
   or obviously above that creator's normal.**
4. Copy each saved post's TEXT and its NUMBERS into one file, then drop it in:

       reut-workspace/the-system-v5/O-output/linkedin-swipe-engine/inbox/

   Name it `YYYY-MM-DD-harvest.md`. Format does not need to be neat. Minimum per post:
   creator name, post URL, reactions, comments, reposts, and the full post text.

5. Tell me "harvest is in" and I produce the ranked report.

Target: 10 to 25 posts a day. Under 10 means the follow list needs more volume creators.

## STEP 7 — What I deliver

Every run I write `daily-reports/YYYY-MM-DD-report.md` containing:
- Every harvested post ranked best to worst by the weighted score in `02-report-spec.md`
- Engagement numbers and the creator's baseline, so we know what is a real outlier
- A one-line structure label per post
- Full donor beat-table for the top 3, ready to build a Lior post on
- Which of the top posts pass the CEO relevance filter and which do not

Plus a short Hebrew top-5 summary in chat.

## STEP 8 — Guardrails that still apply

- The new account never posts. It reads. If it starts posting, it needs a whole
  content strategy of its own and that is not this project.
- Nothing harvested gets copied word for word into a Lior post. Structure only.
  See [[feedback-build-on-proven-structures]] and [[feedback-comment-reference-spirit-not-copy]].
- Active donor moratoriums: Ruben Hassid until 20 non-Ruben posts ship,
  Amber Spears until 2026-10-29. Both stay ON the follow list for data. They are
  just barred as donor structures. See [[feedback-diversify-inspiration-creators]].
- Every donor gets stripped of AI tells before it becomes a Lior draft, especially
  "not X, it's Y". See [[linkedin-ai-slop-penalty]].
