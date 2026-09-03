---
name: geo-optimization-principles-veeda-2026
description: "GEO (Generative Engine Optimization) content principles from Veeda presentation - how to write content that gets cited by AI engines (ChatGPT, Gemini, Perplexity)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8a7363d9-b77f-4503-9663-f5c323e54701
---

## Core Shift: SEO → GEO
- Goal is no longer ranking in blue links — it's being **cited as the most authoritative source** in AI-generated answers
- KPI shifts from CTR/rankings to **Share of Model (SoM)** — brand's share of mentions in AI answers
- Brand mentions (0.664 correlation with AI visibility) beat backlinks (0.218 correlation)
- Organic traffic may drop 35%, but conversion quality jumps 5x due to AI pre-filtering

## Content Structure (GEO-SFE) — How Structure Determines Citation
- **Heading hierarchy**: 3-5 levels deep (models lose focus above 5, struggle below 3)
- **Paragraphs**: max 150-250 words, each chunk must be self-contained and logically complete
- **Tables & lists**: 25-35% of text — improves model extraction accuracy by 43%
- **Document length**: split content into 1,500-3,000 word pieces
- **Internal links density**: 0.15-0.20 — enables multi-step agent navigation without noise

## Writing Style — Fact-First & Wiki-Voice
- **Fact-First**: Place critical facts at the START of sentences and paragraphs (model attention peaks at sequence boundaries)
- **Fact Density**: Maximize verifiable data — stats, percentages, metrics. AI engines discard "marketing noise"
- **Wiki-Voice**: Objective, factual, neutral tone. Avoid empty adjectives like "revolutionary", "groundbreaking", "game-changing"
- **Hard data wins**: Models prefer sources with exact percentages, metrics, and verifiable claims over generic marketing copy

## Authority Building (E-E-A-T for AI)
- **Topic Authority** = highest ranking weight. Build deep, consistent coverage across topic clusters
- **Identified authors**: Content with named experts gets prioritized; anonymous/generic content gets marginalized
- **UGC & community**: Positive brand mentions on Reddit, Facebook etc. boost AI citation probability 4x
- **Digital PR > Link Building**: Brand mentions in authoritative contexts matter more than link profiles
- **Branded anchors** (0.527 correlation) beat general domain rating for RAG systems
- **Consensus mechanism**: AI models cross-reference sources to reduce hallucinations — be cited across multiple platforms

## Technical Infrastructure
- **llms.txt**: Machine-readable content file for AI agents (under 3,000 tokens, clean markdown, no JS/HTML clutter)
- **Nested Schema markup**: Article → Author → Organization hierarchy helps models understand authority
- **SSR (Server-Side Rendering)**: AI crawlers still struggle with JavaScript in 2026 — critical facts must be in initial HTML
- **Chunk optimization**: Content gets split into 200-300 word chunks for vector retrieval — each chunk must be independently meaningful

## AI Engine Differences (2026)
- **GPT-5.2**: 91-95% accuracy, leans on consensus sources (Wikipedia, Reddit), 2-4s response
- **Gemini 3.1**: 91% accuracy, strongly favors Google's search index, 1-2s response
- **Perplexity Pro**: 97% accuracy (complex queries), heavy reliance on citation authority, real-time retrieval
- **Copilot**: 88% accuracy, based on Bing, Office 365 integration focus

## Measurement
- **SoM (Share of Model)**: Brand's % of mentions in AI answers for a category — THE key metric
- **Citation rate**: How often a model cites your site as a source
- **Pipeline**: Prompts → Raw AI answers → NLP/NER analysis → Visual dashboard

## Google Search Profiles (launched ~Jun 2026) — ACTION ITEM for Lior
- Google's new **Search profile**: a claimable page inside Search that shows a creator's bio, links, and latest content. Appears in the Knowledge Panel, the **Google Discover** feed, and at a direct URL. Reinforces GEO/entity-based discovery + E-E-A-T — builds Lior as a recognized *entity*.
- **Eligibility**: 100K+ followers on ONE of Instagram / YouTube / X, OR 300K+ on TikTok; must be 18+. **US only** at launch (expanding later).
- **Claim at** `profile.google.com/claim` (or `creators.google/profile`). Sign in to the qualifying platform account → Google auto-verifies → customize avatar, bio, website, socials, pin featured content.
- **TODO**: confirm whether Lior clears 100K on any single platform; if yes, claim it. Passive traffic via Discover favors evergreen journey/story posts over news content. Blog: https://blog.google/products-and-platforms/products/search/a-new-profile-to-help-publishers-and-creators-highlight-their-work-on-search/

## How to Apply
When writing any content for Lior/AutoDS (articles, website pages, landing pages):
1. Structure with clear heading hierarchy (H1→H2→H3)
2. Lead every paragraph with the hardest fact/data point
3. Use tables and bullet lists for 25-35% of content
4. Write in Wiki-Voice — factual, not promotional
5. Keep paragraphs under 150 words, documents 1,500-3,000 words
6. Include verifiable stats, percentages, named sources
7. Avoid empty marketing buzzwords

## Update 2026-08-24 — ChatGPT now cites official sites over Reddit (source: Tom Orbach newsletter)

- Reddit fell from ~3.8% of everything ChatGPT cited to ~0.5% in one week, an 86% collapse, after
  ChatGPT changed retrieval to check official websites first. Reported figures, not our measurement.
- Consequence: the owned site is now the #1 thing that gets quoted. Three pages that earn citations:
  a pricing page with real numbers (AI cannot quote "Contact us"), a "[you] vs [competitor]" page
  (buyers ask AI to compare constantly and it quotes whoever wrote one), and an FAQ that answers
  each question in its FIRST sentence, in customer wording.
- Reddit still gets cited when a REAL employee under a real name answers inside big threads.
  Anonymous accounts do not. Reconciles with the UGC point above: it is identity, not the platform.
- Tool: is-agentic.com (Vercel) scores how readable a site is to AI agents out of 100 and lists
  fixes. Reference scores quoted: Stripe 80, openai.com 72, anthropic.com 62.
- Action for us: run lior-pozin.com / the Base44 site through is-agentic.com before the next site
  update, and check whether AutoDS has a real-numbers pricing page and comparison pages.
  See [[lior-website-base44]].

## Update 2026-09-01 — LinkedIn's own AI-search guide (Calcalist)

See [[linkedin-ai-search-citations-2026]]. Headline: 75% of LinkedIn's AI citations come from
individual member profiles, not company pages, and LinkedIn articles carry ~60% of those citations
versus ~40% for posts. Confirms the identity point above — it is a named human, not the brand
account, that gets quoted.
