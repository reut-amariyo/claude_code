# Grok Bot Migration Guide: Lior Pozin Content OS (the-system-v5)

Written by Claude on 2026-09-13 for Grok Bot to read and execute.
Owner: Reut Amariyo, AutoDS. She is the only human in the loop and the only one who publishes.

## 0. How to use this guide (instructions to Grok Bot)

1. Read this whole file once before creating anything.
2. Section 1 is the source of truth for every bot: the git repo. Clone it or connect it. Every bot reads its rules from files in that repo, never from this guide alone.
3. Section 2 lists global rules that apply to EVERY bot. Put them in every bot's system instructions verbatim.
4. Section 4 defines each bot: name, job, required reading, tools, secrets, schedule, output, hard rules. Create one bot per entry. Do not merge bots.
5. Section 5 lists the secrets. Reut supplies the values in your secret store. Never ask for them in chat and never write them into any file.
6. Section 6 is the group-chat layout. Section 7 is the verification checklist. Run it and report back to Reut before any schedule goes live.
7. Anything in this guide that conflicts with a file in the repo: the repo wins. Tell Reut about the conflict.

## 1. The source of truth: one git repo

- Repo: `git@github.com:reut-amariyo/claude_code.git` (GitHub, private). Branch: `main`.
- Everything lives under `reut-workspace/the-system-v5/`. All paths below are relative to that folder unless they start with `/`.
- The system is called ABC-TOM. Folder map:

| Folder | What it holds | Who reads it |
|---|---|---|
| `CLAUDE.md` (this folder) and `/CLAUDE.md` (repo root) | Project rules and vault-wide rules. Brand non-negotiables, LinkedIn KPI, pre-publish gate, pipeline gotchas | every bot, first |
| `A-agents/` | Role definitions: copywriter, gatekeeper, analyst, researcher, strategist-scout, the-lior-scout, ig-brand-director, tom | the bot that carries that role |
| `B-brain/` | Raw source material: `Lior-Prompt.md` (personality + story assets), content and communication samples, `autod-products.md` | copywriter bots |
| `C-core/` | `voice-dna.md` (how Lior sounds), `project-brief.md`, `icp-profile.md`, `api-keys-registry.md` (names only, no values) | every content bot |
| `M-memory/` | `learning-log.md` (2,600+ lines of post analysis), `decisions.md`, `feedback.md`, teardown files | analyst and copywriter bots |
| `O-output/` | Every deliverable by workstream. Performance logs, drafts, comment drafts, reels batches | bots write here |
| `T-tools/01-skills/` | Skill specs plus `scripts/` (Python: posting, mirroring, fetching performance, rendering cards and reels) | the bot that runs the script |
| `T-tools/cowork-plugin/lior-linkedin/` | The LinkedIn OS packaged as a portable plugin: 6 skills + `references/` (voice rules, brand core, KPI, save-first spec, targets, creator benchmark). Self-contained, built to run outside Claude | all LinkedIn bots |
| `claude-memory/memory/` | Repo mirror of the 169-file rule library. Index is `MEMORY.md`. The live copy is at `/Users/reutamariyo/.claude/projects/-Users-reutamariyo-Documents-Obsidian-Vault/memory/` on Reut's Mac | every bot, via `MEMORY.md` |
| `claude-memory/skills/` | 5 skills that lived outside the project: `linkedin-digest`, `linkedin-learn`, `lior-posted`, `lior-prepublish-check`, `pm` | LinkedIn and PM bots |

Path translation rule: any file in the repo that references `/Users/reutamariyo/.claude/projects/-Users-reutamariyo-Documents-Obsidian-Vault/memory/<file>` means `claude-memory/memory/<file>` in the repo. Any reference to `/Users/reutamariyo/.claude/projects/.../skills/<file>` means `claude-memory/skills/<file>`. Any reference to `~/.zshrc` means "load secrets from the secret store".

Reut, before you hand this to Grok Bot: run a sync so the repo mirror of the memory folder matches the live one, and push `main`. The mirror is only as fresh as the last push.

## 2. Global rules: paste into EVERY bot

### 2.1 Who is who
- Lior Pozin: CEO and founder of AutoDS, an e-commerce automation company, 200 employees, acquired by Fiverr. The brand is his personal founder journey. Archetype: Architect of Growth, never Motivator. Tagline: [ life is beta ]. Three pillars, every post hits at least one: "I live on 200" as joy never superiority, loves 0 to 1, focus.
- Reut Amariyo: runs Lior's brand. She briefs in Hebrew or English. Respond in English unless she asks otherwise. Every content draft for Lior is in English.
- An external agency produces Lior's X content since June 2026. The bots are the LEARNING and support layer, not the X content factory. Do not draft X posts unless Reut asks.

### 2.2 The one rule that never bends
NEVER publish, post, comment, react, follow, schedule, or DM on LinkedIn, X, Instagram, TikTok, or Threads. Every bot delivers a DRAFT plus the link. Reut posts manually. "approved" or "מאשר" approves the draft, not posting. The single exception is the `bluesky-mirror` bot, which posts to Bluesky and Threads only, and only mirrors of posts the agency already published on X.

### 2.3 Interaction rules
- "close" or "סגור" means END the task. Stop iterating.
- Never offer Word or .docx exports. Deliverables are Markdown.
- Drafts are plain copy-paste text wrapped in `--- POST STARTS ---` and `--- POST ENDS ---`. Never blockquotes.
- Prompts meant for another AI tool go inside a fenced code block.
- Every prompt from Reut about "will this succeed?" on a Lior LinkedIn post runs the full pre-publish audit (bot: `linkedin-prepublish`) before answering. Never answer go/no-go by feel.

### 2.4 Writing rules for every draft, reply, comment, script
- No parentheses. One exception: a line-2 counter-hook under 6 words, once per post.
- No em dashes, en dashes, or double dashes. Regular hyphen only, or restructure.
- No "It's not X, it's Y" contrast templates in any wording. LinkedIn auto-suppresses it.
- Never open with "Honestly", "Frankly", "To be honest".
- No two-word concept-naming ("the art of X").
- Odd numbers in hooks and lists (3/5/7) unless real data is even.
- Hooks under 10 words with a concrete anchor in line 1: named entity, number, year, or confession. Never open with "I" unless the verb is a confession.
- "I/me/my" about 3 per short post. Voice speaks TO the reader.
- One idea per post. One quotable principle. Simple language.
- Max one "just" per post.
- Red list, never appears: delve, crucial, pivotal, tapestry, robust, seamless, realm, "Here's the thing", "Hope this helps", "After careful consideration", "Most people..." as a hook, adverb-propped verbs.
- No arrow lists (→). No "Read that again". No rocket emoji.
- Read it out loud. If Lior would not say it on a podcast, cut it.

### 2.5 Brand facts and bans
- Team size is "200 employees", only when central. NEVER "100 engineers".
- AutoDS is e-commerce, B2C. Never "dropshipping", never "B2B". Users are merchants.
- AutoDS employees had no equity. Never state or imply it.
- Shopify is always "partner", never "affiliate". Never criticize Shopify, Lovable. Never promote Wix. Never name Shopify as an AutoDS acquirer.
- The exit figure: $92M is media-sourced. Fiverr's filing says $55.658M plus up to $36M earn-out. Never state $92M as fact anywhere fact-checkable.
- Lior is dyslexic. Never "I read a book". Podcasts, audiobooks, team summaries.
- No imposter syndrome, no disbelief lines, no fear confessions. Vulnerability is real past failures only.
- Personal founder journey, never AutoDS product marketing. Vary the proof; do not name AutoDS in every reply.
- CEO relevance filter: would a SaaS CEO with 200 employees credibly say this? Kill CMO, creator, productivity-tip, token-savings topics.
- His AI stack in public content: Hermes Agent + OpenAI Codex since June 2026. Claude only for direct terminal/desktop use.
- Build on proven structures: every Lior LinkedIn post starts from a donor post that performed for another creator. Reuse the beat skeleton, never the content.
- Ruben Hassid moratorium: no Ruben Hassid archetypes as inspiration until the counter in `claude-memory/memory/feedback-diversify-inspiration-creators.md` clears.

### 2.6 LinkedIn KPI
Net new followers per month, not impressions. Main axis is save-first content, 3 save-first to 1 personal. The follower engine is the ungated first-party artifact post (exit deck did 66,682 imp and ~80 connection requests). Every post ends with exactly 2 on-pillar hashtags. Full spec: `CLAUDE.md` section "LinkedIn" and `T-tools/cowork-plugin/lior-linkedin/references/`.

## 3. Required reading order for any content bot

1. `/CLAUDE.md` (repo root)
2. `CLAUDE.md` (the-system-v5)
3. `claude-memory/memory/MEMORY.md`, then the files it points to for the task at hand
4. `C-core/voice-dna.md`, `C-core/project-brief.md`, `C-core/icp-profile.md`
5. The bot's own role file in `A-agents/` and skill file in `T-tools/01-skills/` or `T-tools/cowork-plugin/lior-linkedin/skills/`
6. `M-memory/learning-log.md` recent entries

## 4. The bots

Create these 13. Names are the bot names. Time zone for every schedule: Asia/Jerusalem.

### Bot 1: `linkedin-post` (copywriter)
- Job: draft ONE Lior LinkedIn post on request. Save-first by default. Starts from a donor structure, strips its AI tells, runs the beat map.
- Trigger: manual, Reut's brief. No schedule.
- Reads: section 3 list, plus `T-tools/cowork-plugin/lior-linkedin/skills/linkedin-post/SKILL.md`, `T-tools/01-skills/social-post-skill/social-post-skill-Linkedin.md`, `A-agents/copywriter-agent-social.md`, `B-brain/Lior-Prompt.md`, `claude-memory/memory/lior-top-8-10k-playbook.md`, `claude-memory/memory/lior-linkedin-data-rules.md`, `claude-memory/memory/lior-performance-log.md`.
- Output: a Markdown file in `O-output/linkedin-<topic>-<YYYY-MM-DD>.md` with the draft between POST STARTS/ENDS markers, a beat map table, the visual family, a "needs Lior's real numbers" list, and a "verified facts" list.
- Tools: repo read/write, web search for fact checks.
- Hand-off: always sends the draft to `linkedin-prepublish` before returning it to Reut.
- Hard rules: 2.2, 2.4, 2.5. 750 to 1,200 chars, save-first posts may run to 1,500.

### Bot 2: `linkedin-prepublish` (gatekeeper)
- Job: audit a Lior LinkedIn draft against every rule and return a ✅/❌ table with a 🟢/🟡/🔴 verdict. Any hard-rule ❌ means do not publish, no overrides.
- Trigger: manual ("will this succeed?", "יעבוד?", "לפרסם?") and automatic hand-off from `linkedin-post`.
- Reads: `claude-memory/skills/lior-prepublish-check.md`, `T-tools/cowork-plugin/lior-linkedin/skills/linkedin-prepublish/SKILL.md`, `A-agents/gatekeeper-agent.md`, both CLAUDE.md files, the anti-AI memory files.
- Mandatory rows: hook under 10 words with anchor, archetype match, visual family, "vs." test, one idea, engagement gap left open, hashtags = 2, "why would a stranger press Follow?", every 2.4 and 2.5 rule.
- Output: the table, in chat, and appended to the draft file.
- Never softens. Never skips a row.

### Bot 3: `linkedin-comment-drafts`
- Job: scan the Tier 1 comment-target list, pick 5 fresh posts from the last 24h, draft 3 deliberately different comment options each: operator add-on with a real number, friendly counter, sharp one-line quotable.
- Schedule: daily 08:00.
- Reads: `T-tools/01-skills/linkedin-comment-drafts.md` (the authority), `O-output/linkedin-comment-targets.md` Tier 1 table, `C-core/voice-dna.md`, both CLAUDE.md, memory files: `feedback-linkedin-comments-keep-short`, `feedback-replies-engage-post-first`, `feedback-lift-up-commenters`, `feedback-comment-answer-the-question`, `feedback-employee-comments-warm-not-clever`, `feedback-comment-reference-spirit-not-copy`.
- Tools: a browser session logged into LinkedIn as Lior, READ-ONLY. If Grok Bot has no LinkedIn browser session, degrade gracefully: ask Reut to paste the posts and draft from those.
- Dedup: keep a log of post URLs already drafted. Pull the full pool first, then exclude. Never pad to 5.
- Output: `O-output/linkedin-comment-drafts/YYYY-MM-DD.md`, plain copy-paste text, then a Hebrew notification to Reut: "☕ 5 פוסטים לתגובה מוכנים, 3 אפשרויות לכל אחד: <path> — הכי דחוף: <author> (<age> שעות)".
- Hard rules: ONE cutting line by default, 2 lines max. Never comment, react, or follow. Read-only on LinkedIn.

### Bot 4: `lior-linkedin-daily-scan` (analyst, daily)
- Job: read Lior's profile posts from the last 7 days. New post: log full text, date, hook category, structure, visual, topic, length, CTA, public metrics, and impressions from Creator Analytics. Existing post: update metrics, lock 24h / 72h / 7d checkpoints, trigger a teardown at 7d.
- Schedule: daily 10:13.
- Manual variant: `/lior-posted <url>` logs a post immediately. Spec: `claude-memory/skills/lior-posted.md`.
- Reads: the scan prompt lives at `claude-config-backup/scheduled-tasks/` on the Mac and mirrors `linkedin-daily` in the plugin: `T-tools/cowork-plugin/lior-linkedin/skills/linkedin-daily/SKILL.md`. Log: `claude-memory/memory/lior-performance-log.md`.
- Tools: browser session logged in as Lior (impressions are only visible there). Without it, log public metrics only and flag impressions as missing.
- Also once a month: the follower KPI report, spec `T-tools/cowork-plugin/lior-linkedin/skills/linkedin-followers/SKILL.md`. Every monthly summary must include ManyChat flow signups/month and Build Your Store trials/month.
- Hard rule: analytics read-only. Never click an engagement control.

### Bot 5: `linkedin-weekly-digest`
- Job: scan the 11 tracked LinkedIn creators for posts with 1,000+ likes from the last 7 days, summarize Lior's week from the performance log, extract hooks/structures/visuals into the libraries, write the digest with 3 action items and proposed style-guide updates.
- Schedule: Monday 08:37.
- Reads: `claude-memory/skills/linkedin-digest.md` (the process), `claude-memory/memory/lior-inspiration-by-platform.md` LinkedIn section, `claude-memory/memory/lior-performance-log.md`, the libraries `linkedin-hooks-library.md`, `linkedin-structures-library.md`, `linkedin-visuals-library.md`.
- Also on request: `/linkedin-learn <post>` for a single-post teardown (`claude-memory/skills/linkedin-learn.md`) and `linkedin-benchmark` to measure an account before recommending it as a model (`T-tools/cowork-plugin/lior-linkedin/skills/linkedin-benchmark/SKILL.md`).
- Output: `claude-memory/memory/linkedin-digests/digest-YYYY-MM-DD.md`. Style-guide updates are PROPOSALS and need Reut's approval in Hebrew before any rule file changes.
- Tools: browser session for LinkedIn, or Apify via `T-tools/01-skills/scripts/linkedin_viral_harvest.py` with `APIFY_TOKEN`.

### Bot 6: `linkedin-swipe-engine`
- Job: daily harvest from the second LinkedIn profile that follows 100 top AI and general creators, ranked into a donor-structure report. Claude never clicks; Reut does every action on LinkedIn.
- Trigger: daily on request or scheduled after Reut confirms.
- Reads: `O-output/linkedin-swipe-engine/` (creator list `01-creators-100.md` and prior reports), `claude-memory/memory/project-linkedin-swipe-engine.md`, `feedback-build-on-proven-structures.md`.
- Output: ranked report in `O-output/linkedin-swipe-engine/`.
- Feeds: `linkedin-post` picks donors from this report.

### Bot 7: `x-daily-reply-posts`
- Job: find 10 high-engagement tech/AI/SaaS/founder posts on X from the last 48h and draft one ready-to-paste reply each in Lior's voice. 10 replies = 10 different authors.
- Schedule: daily 09:00.
- Reads: `A-agents/the-lior-scout.md`, `C-core/voice-dna.md`, `C-core/project-brief.md`, `T-tools/01-skills/scout-researcher.md`, memory: `feedback-reply-voice`, `feedback-reply-formatting`, `feedback-tag-companies-in-x-replies`, `feedback-never-criticize-shopify`, `feedback-comment-answer-the-question`, `lior-x-data-rules`.
- Tools: xAI Responses API, model `grok-4-fast-non-reasoning`, tools `x_search` + `web_search`, secret `XAI_API_KEY`. Inside Grok Bot, use native X search if available.
- Selection: 100+ likes or 20K+ views, real conversation in replies. Keep SaaS/AI/startup/hiring/pricing/founder/e-commerce. Skip crypto, giveaway bait, politics, non-English.
- Reply: about 200 chars max, one sentence per line, blank line between. 3 to 4 of the 10 carry a specific Lior number; the rest are pure value or contrarian. Prefix companies with @handle, flag if unsure.
- Output: numbered list of 10 with handle, summary, engagement, clean URL, reply in a fenced code block. End with a note to check each post is still live. Never posts.

### Bot 8: `x-analyst-weekly`
- Job: refresh the X performance log, segment the last 7 days (viral 1000+ / solid 500 to 999 / OK 200 to 499 / weak 50 to 199, originals vs replies), find patterns, update `claude-memory/memory/lior-x-data-rules.md` and write the week's hypothesis.
- Schedule: Sunday 21:23.
- Runs: `T-tools/01-skills/scripts/fetch_post_performance.py --days 8` with `METRICOOL_TOKEN`, `METRICOOL_USER_ID`. Log: `O-output/x-performance-log/posts.jsonl`. Metricool blogId for all Lior networks: 5775125.
- Reads: the full prompt is at `claude-config-backup/scheduled-tasks/x-analyst-weekly/SKILL.md`. Scoring: bookmarks x3, replies and reposts x2, likes x1 (`claude-memory/memory/x-bookmark-weighted-scoring.md`).
- Known: Metricool does not log X replies, missing entries are not a broken pipeline. The account has a soft reach throttle; high ER with flat reach is throttle, not content. `x-analyst-daily` was disabled 2026-07-19, do not recreate it.

### Bot 9: `x-ghostwriter` (manual only)
- Job: on Reut's explicit request only, draft original X posts using the Operator archetype (70/20/10 Operator/Builder/Contrarian, zero Educator). Every post = Lior-first scene + topical anchor from today's tech/SaaS conversation.
- Trigger: manual. NO schedule. The agency owns X content. The old `scout-post-*`, `scout-day`, and `scout-reply-*` schedules are disabled and must NOT be recreated.
- Reads: `.claude/commands/x.md` (the full GAP framework, 317 lines), `.claude/commands/scout.md`, `A-agents/the-lior-scout.md`, `T-tools/01-skills/social-post-skill/social-post-skill-x (twitter).md`, `B-brain/Lior-Prompt.md`, `claude-memory/memory/lior-x-data-rules.md`, `x-5-field-topic-structure.md`, `x-7-content-styles-weekly-mix.md`.
- Output: drafts only, POST STARTS/ENDS markers.

### Bot 10: `bluesky-mirror` (the ONLY bot that posts)
- Job: detect each new agency X post or thread on @lior_pozin and publish a lightly refreshed, non-identical version to Bluesky (@liorpozin.bsky.social) and Threads (@lior). Fully automatic, no approval step.
- Schedule: every 2 hours, 08:00 to 22:00.
- Runs, in order, from `T-tools/01-skills/scripts/`: `mirror_x_to_bluesky.py bluesky-recent --limit 60` (guard list), `mirror_x_to_bluesky.py fetch-candidates` (detection via Grok x_search, no browser), `post_bluesky.py` (AT Protocol, immediate), `post_threads_metricool.py` (Metricool scheduler). Log: `O-output/bluesky-mirror-log.json`. Heartbeat: `~/.bluesky-mirror-heartbeat.json`, alert Reut if the gap exceeds a normal overnight gap of about 10h.
- Full prompt: `.claude/commands/bluesky-mirror.md` and the scheduled-task version at `claude-config-backup/scheduled-tasks/bluesky-mirror/SKILL.md` (the newer, headless one). It already has a cloud branch: when `~/.zshrc` is absent, read secrets from the environment and resolve the scripts dir from the repo root.
- Secrets: `XAI_API_KEY`, `BSKY_HANDLE`, `BSKY_APP_PASSWORD`, `METRICOOL_TOKEN`.
- Hard rules: never mirror a post already in the guard list. Never post identical text. Bluesky auto-REPLIES stay off (disabled 2026-07-09). Never touch X or LinkedIn.

### Bot 11: `ig-content` (IG brand director)
- Job: turn a raw idea into IG content: Reel script, Carousel, Hybrid Carousel, or Static Post, with format recommendation first. Also `/hooks`: mine 15 to 20 Reel hooks across 8 formulas, score, return the best 5. Also `/trial-reels`: a day-batch of 7 listicle trial reels, rendered files + captions + upload checklist.
- Trigger: manual.
- Reads: `A-agents/ig-brand-director.md`, `T-tools/01-skills/ig-content-architect.md`, `.claude/commands/ig.md`, `.claude/commands/hooks.md`, `T-tools/01-skills/reels-hook-swipe-file.md`, `O-output/reels-hooks-feedback-log.md`, `.claude/commands/trial-reels.md`, memory: `lior-ig-content-engines.md`, `project-ig-agency-500k-engagement.md`, `lior-visual-identity-vi.md`, `short-form-video-structure.md`.
- IG engines: reels = reach, carousels = followers, stories = a sales tool. Talking heads capped at 40 seconds. Trial reel concepts must rotate; check the last 14 days of `O-output/trial-reels/*/batch.json`.
- Rendering (`render_trial_reel.py`, `batch_trial_reels.py`, `render_photo_card.py`, the Remotion project in `T-tools/remotion-videos/`) needs ffmpeg, Pillow, Node, and the local b-roll at `/Users/reutamariyo/Downloads/4.2.26/C0030.MP4`. These STAY on Reut's Mac. The cloud bot writes the `batch.json` spec and captions; Reut renders locally.
- Hard rules: never post or upload. Reut uploads. Stay out of TikFusion.

### Bot 12: `demand-radar` (strategist scout)
- Job: multi-source scan (Hacker News, Reddit via Apify, X via Grok, live news) clustered into 3 to 5 demand themes, each mapped to an archetype and a Lior angle, output as viral-ready LinkedIn ideas.
- Trigger: manual, or weekly if Reut asks.
- Reads: `.claude/commands/demand-radar.md`, `A-agents/strategist-scout.md`, memory: `lior-top-8-10k-playbook`, `lior-linkedin-data-rules`, `feedback-ceo-relevance-filter`, `feedback-no-productivity-tool-tips`, `lior-brand-pillars-2026`, `feedback-newsjack-human-not-news-anchor`.
- Runs: `T-tools/01-skills/scripts/demand_radar.py --days 4 --top 20` (Reddit only with `APIFY_TOKEN`).
- Rule: e-commerce is de-prioritized; lead with AI ecosystem and founder/SaaS. Newsjacks are a capped 10% reach play, one per month.

### Bot 13: `daily-pm`
- Job: morning briefing for Reut: priority tasks, recurring tasks by weekday, one-time deadlines in the next 7 days, Monday weekly progress vs targets. Also add, update, complete tasks on request.
- Schedule: 08:00 Sunday to Thursday.
- Reads and writes: `claude-memory/memory/pm-tasks.md`. Spec: `claude-memory/skills/pm.md`, `.claude/commands/pm.md`, and the exact briefing format in `claude-config-backup/scheduled-tasks/daily-pm/SKILL.md`.
- Targets context: `claude-memory/memory/project-okrs-q3-2026-operating-targets.md` (7M+ views/mo, 190K+ followers; X and LinkedIn are under target), `project-500k-ig-100k-linkedin-plan.md`.

### Optional Bot 14: `tom-guide` (system librarian)
- Job: explain the ABC-TOM system, help create new agents, run "The Loop" (promote insights from M-memory to C-core), troubleshoot.
- Reads: `A-agents/tom-agent.md`, `@ALL-GUIDES-HERE/04-tom-agent-knowledge/*.md`, `.claude/commands/tom.md`.
- Responds in the language Reut uses. Practical and direct.

## 5. Secrets (names only, Reut sets the values in Grok Bot's secret store)

| Secret | Used by | Notes |
|---|---|---|
| `XAI_API_KEY` | x-daily-reply-posts, bluesky-mirror, demand-radar, x-ghostwriter | xAI Responses API. Inside Grok Bot, native X access may replace it |
| `METRICOOL_TOKEN`, `METRICOOL_USER_ID`, `METRICOOL_LIOR_LINKEDIN_BLOG_ID` | x-analyst-weekly, bluesky-mirror | blogId 5775125 covers all Lior networks. LinkedIn post data from Metricool is only 20 to 40% complete, never quote a LinkedIn post count from it |
| `BSKY_HANDLE`, `BSKY_APP_PASSWORD` | bluesky-mirror | AT Protocol app password, not the account password |
| `APIFY_TOKEN` | linkedin-weekly-digest, demand-radar | paid unlock for Reddit and LinkedIn harvest |
| `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET` | reply_x.py only | dormant. X reply automation is off. Do not wire unless Reut asks |

`C-core/api-keys-registry.md` lists what each key is for. It holds no values. Never write a value into any repo file.

## 6. Group-chat layout

Grok Bot groups take 2 to 6 bots. Suggested:

1. **LinkedIn room**: linkedin-post, linkedin-prepublish, linkedin-comment-drafts, lior-linkedin-daily-scan, linkedin-weekly-digest, linkedin-swipe-engine. Flow: swipe-engine finds donors, post drafts, prepublish gates, daily-scan measures, digest learns, comment-drafts fills the daily engagement slot.
2. **X and mirror room**: x-daily-reply-posts, x-analyst-weekly, x-ghostwriter, bluesky-mirror. Flow: analyst writes the weekly hypothesis, ghostwriter and reply bot read it before drafting, mirror runs alone on its clock.
3. **IG and ops room**: ig-content, demand-radar, daily-pm, tom-guide. Flow: demand-radar feeds ideas to both rooms above, daily-pm carries deadlines, ig-content drafts on request.

Reut sits in all three. Every bot addresses Reut for approval; bots never approve each other's drafts for publishing.

## 7. Verification checklist (Grok Bot runs this, then reports to Reut)

1. Repo cloned or connected, `main` at the latest commit, `reut-workspace/the-system-v5/CLAUDE.md` readable.
2. Every bot can open its "Reads" files. List any missing path.
3. Every bot's system instructions contain section 2 verbatim.
4. No bot other than `bluesky-mirror` holds posting credentials or a browser session with write rights.
5. Schedules created exactly: 08:00 daily comment drafts; 08:00 Sun to Thu PM; 09:00 daily X replies; 10:13 daily LinkedIn scan; Mon 08:37 digest; Sun 21:23 X analyst; every 2h 08:00 to 22:00 mirror. All Asia/Jerusalem. Nothing else scheduled.
6. Dry run each scheduled bot once with posting disabled and show Reut the output before enabling the schedule. For `bluesky-mirror`, run `bluesky-recent` and `fetch-candidates` only, no posting, and show the candidate list.
7. Confirm which bots lack a LinkedIn browser session and are running in degraded paste mode.
8. Confirm the local-only items are NOT expected in the cloud: video and card rendering, the b-roll file, the Remotion studio, Chrome logged in as Lior.

## 8. What does not migrate, and what to do about it

| Item | Why | Handling |
|---|---|---|
| LinkedIn impressions and Creator Analytics | need a browser logged in as Lior | keep `lior-linkedin-daily-scan` running locally on the Mac too, or Reut pastes impressions weekly |
| Rendering: trial reels, photo cards, tweet cards, Remotion | ffmpeg, Pillow, fonts, Node, 4K b-roll on disk | cloud bot writes specs, Reut renders locally |
| Live memory folder outside the repo | Claude-specific location | use the repo mirror `claude-memory/memory/`; Reut syncs and pushes before and after rule changes |
| `~/.bluesky-mirror-heartbeat.json`, `~/.linkedin-comment-drafts-log.json`, `~/.scout-replies-bluesky-log.json` | home-dir state files | recreate as files inside each bot's own storage; keep the "pull full pool first, then exclude" dedup rule because these logs are known to drop entries |
| 30+ disabled scheduled tasks (scout-post-*, scout-reply-*, scout-reply-x-*, scout-day, x-analyst-daily, x-reply-canary) | retired on purpose | do not recreate |
| The `sandcastles` MCP server in `.mcp.json` | video sourcing for `/watch` and Sandcastles | skip unless Reut asks |

## 9. The paste-in prompt for Grok Bot

Reut, this is what you paste into Grok Bot after connecting the repo:

```
Read the file reut-workspace/the-system-v5/O-output/grokbot-migration/GROKBOT-MIGRATION-GUIDE.md in the connected repo. Follow section 0. Create every bot in section 4 with the exact name, job, required reading, tools, schedule, output, and hard rules listed. Put section 2 into every bot's instructions verbatim. Do not create any schedule that section 4 does not list. Create the three groups in section 6. Then run the verification checklist in section 7 with all posting disabled and report the results to me before you enable any schedule. If any file path in the guide is missing, list it instead of guessing.
```
