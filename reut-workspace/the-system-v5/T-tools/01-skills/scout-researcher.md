# Skill: The Lior Scout Researcher (Data Gathering)

## Purpose
This skill defines exactly where and what to search when gathering intelligence for Lior's daily X posts. Focus strictly on AI in SaaS, builder tools, and industry friction.

## Execution: The Python Engine
Do not use external search MCPs. Instead, rely on local Python execution and the Grok API to gather data.

### Round 1: Broad X Search (Primary, Engagement-First)
Use the `XAI_API_KEY` environment variable to query the xAI **Responses API** (`https://api.x.ai/v1/responses`). Must use a **grok-4 family model** (e.g., `grok-4-fast-non-reasoning`) with `x_search` and `web_search` tools enabled.

**Use a simple, broad query. Do NOT over-constrain with specific handles.**
* Good query: `"What are the 5 most trendy and popular tech, SaaS tweets of today?"`
* Bad query: `"Top posts from @handle1 @handle2 @handle3 about AI in SaaS"` (too narrow, misses viral posts)

**Why:** The best content often comes from unexpected accounts. Locking onto specific handles causes you to miss high-engagement posts (500+ likes, 40K+ views) that Lior would actually react to.

### Round 2: Authority Check (Secondary, Optional)
If Round 1 didn't surface enough builder-specific content, run a second targeted query:
* `"What did @swyx, @patio11, @bentossell, @mattshumer_, @sama tweet about today?"`

### Round 3: RSS & Hacker News (Supporting Data)
* **RSS Feeds:** Fetch from TechCrunch, The Verge, OpenAI, and Hugging Face using `feedparser`.
* **Hacker News:** Pull top stories via the public API. Look for threads with high engagement (>50 comments).

## Ranking: Engagement First
Sort all gathered data by engagement (likes, views, comments) before applying the Lior Filter. High engagement signals real friction and real conversation. Low engagement posts are only worth including if they contain a genuinely novel insight.

## Core Data Sources (Reference List)
* **X Authority Accounts (for Round 2 if needed):** @alliekmiller, @patio11, @bentossell, @swyx, @mattshumer_, @sama, @rowancheung.
* **AI Companies:** OpenAI, Anthropic, Google DeepMind, Microsoft AI, Meta AI, Hugging Face, Cohere.
* **Builder Friction:** Hacker News and Hugging Face Daily Papers.
* **Wide Net Topics:** AI disrupting SaaS pricing, engineering scarcity, startup grind culture, vertical vs. generic SaaS, AI agent tooling, work/productivity shifts.

## The Hand-Off
1. Execute the data gathering (broad first, targeted second).
2. Rank by engagement. Filter ruthlessly. Discard consumer AI hype (e.g., generic ChatGPT wrappers). Keep only what affects SaaS economics, speed, or solves a builder's problem.
3. Pass the raw, filtered data directly to `A-agents/the-lior-scout.md` to format the final posts.