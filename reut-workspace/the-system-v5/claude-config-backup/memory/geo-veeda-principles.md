---
name: GEO Optimization Principles (Veeda 2026)
description: GEO (Generative Engine Optimization) content principles from Veeda presentation - how to write content that gets cited by AI engines (ChatGPT, Gemini, Perplexity)
type: reference
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

## How to Apply
When writing any content for Lior/AutoDS (articles, website pages, landing pages):
1. Structure with clear heading hierarchy (H1→H2→H3)
2. Lead every paragraph with the hardest fact/data point
3. Use tables and bullet lists for 25-35% of content
4. Write in Wiki-Voice — factual, not promotional
5. Keep paragraphs under 150 words, documents 1,500-3,000 words
6. Include verifiable stats, percentages, named sources
7. Avoid empty marketing buzzwords
