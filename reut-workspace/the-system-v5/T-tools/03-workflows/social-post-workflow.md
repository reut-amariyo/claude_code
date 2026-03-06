# Social Post Workflow

> A collaborative workflow between the Copywriter and the Gatekeeper for creating a social media post.

---

## Process Overview

```
[Strategist] Scans trends and creates the Narrative Brief
          ↓
[Copywriter] Reads Brief, asks for platform, and writes first draft
          ↓
[Gatekeeper] Reviews and approves / requests changes
          ↓
[You] Publish the post (e.g., via Metricool)
          ↓
[Analyst] Pulls numbers, tells the "Story," and updates Memory
          
```

---

## Step 1: Preparation

### Before Starting

**All agents** must read:

- `C-core/project-brief.md` - Who you are and what you do.
    
- `C-core/voice-dna.md` - How your brand sounds.
    
- `C-core/icp-profile.md` - Who your target audience is.
    
- `M-memory/learning-log.md` - What we learned from previous rounds.

### Project Setup

Create a new folder in `O-output/` with a clear name. The folder will be populated in this order:

```
O-output/
└── 01-social-post-[topic]/
    ├── strategist-brief.md    ← Strategist's trend & angle report
    ├── copywriter-draft.md    ← Copywriter's version (v1, v2...)
    ├── gatekeeper-review.md   ← Gatekeeper's review & approval
    ├── final-post.md          ← Final version, ready to publish
    └── analyst-report.md      ← Performance story (added after 48h)
```

---
## Step 2: Strategic Briefing

### What the Strategist Does

1. **Environmental Scan** - Uses search tools to find relevant e-commerce trends, industry news, or "messes."
    
2. **Aligns with Brand** - Ensures the topic fits Lior's values and expertise.
    
3. **Creates Brief** - Defines the "Angle" and provides specific data or numbers so the Copywriter isn't guessing.
    

### File Format: `strategist-brief.md`

Markdown

```
# Strategic Brief: [Topic Name]

**Trend:** [Summary of news/event]
**Target Audience:** [From ICP profile]
**The Angle:** [Lior's specific take/perspective]
**Key Data/Fact:** [The specific number or detail to include for proof]
```

---

## Step 3: Copywriter Creates a Draft

### What the Copywriter Does

1. **Reads Strategist Brief** - Understands the core message and the "Angle."
    
2. **Reads C-core documents** - Refreshes on voice and audience patterns.
    
3. **Ask Platform** - Asks you which platform this is for (LinkedIn, X, TikTok, etc.).

4. If LinkedIn: Read `T-tools/01-skills/social-post-skill/social-post-skill-Linkedin.md`.
    
5. **Writes first draft** - Follows `T-tools/` for the correct format and platform-specific skill set.
    

### File Format: `copywriter-draft.md`

Markdown

```
# Social Post: [Topic Name]

**Date:** [Date]
**Version:** v1
**Platform:** [Platform Name]

---

## The Post
[Post text here]

---

## Copywriter Notes
- **Hook Choice:** [Why I chose this hook type]
- **Brief Alignment:** [How I integrated the Strategist's angle]
- **Voice Patterns:** [Which of Lior's signature patterns were used]
```

---


## Step 4: Gatekeeper Reviews

### What the Gatekeeper Does

1. **First read** - Gut reaction within 5 seconds
2. **Check against standards** - Voice DNA, ICP alignment, platform fit
3. **Decision** - Approved / Revisions Needed / Escalate

### File Format: `gatekeeper-review.md`

```markdown
# Gatekeeper Review: [Topic Name]

**Date:** [Date]
**Version reviewed:** v1

---

## Status: [APPROVED / REVISIONS NEEDED / ESCALATE]

---

## What Works Well
- [Strength 1]
- [Strength 2]

## What Needs Improvement
1. **[Issue 1]** - [How to fix]
2. **[Issue 2]** - [How to fix]

---

## Next Step
[What the Copywriter should do now]
```

---
## Step 5: Gatekeeper Reviews

### What the Gatekeeper Does

1. **Gut Check** - Initial reaction to the hook and flow.
    
2. **Standard Check** - Verifies against Voice DNA, ICP alignment, and platform fit.
    
3. **Brief Check** - Ensures the draft delivers on the Strategist's specific "Angle."
    
4. **Decision** - [APPROVED / REVISIONS NEEDED].
    

### File Format: `gatekeeper-review.md`

Markdown

```
# Gatekeeper Review: [Topic Name]

**Status:** [APPROVED / REVISIONS NEEDED]

---

## What Works Well
- [Strengths]

## What Needs Work
1. **[Issue]** - [Actionable fix for the Copywriter]

---

## Next Step
[Approved for final-post.md / Back to Copywriter for v2]
```

---
## Step 5: Final Version & Publishing

When the Gatekeeper approves:

1. Copywriter or Gatekeeper saves the clean text to `final-post.md`.
    
2. **You copy-paste and publish to Metricool.**

---
## Step 6: Performance Analysis (48h Later)

### What the Analyst Does

1. **Gathers Data** - Pulls the stats (Impressions, Engagement, Saves) from Metricool.
    
2. **Tells the Story** - Explains _why_ the post performed the way it did based on the content.
    
3. **Actionable Insight** - Provides one specific lesson to improve the next post.
    

### File Format: `analyst-report.md`

Markdown

```
# Analyst Report: [Topic Name]

**Impressions:** [Total]
**Top Metric:** [e.g., Highest Shares in 30 days]

---

## Performance Story
[Explain the success or failure. Did the hook work? Was the timing right?]

## "The Loop" Updates
- **Keep:** [Pattern to repeat]
- **Adjust:** [What to change in the next brief]
```

---

## Step 7: Update Memory

The Analyst updates `M-memory/learning-log.md` to ensure the system gets smarter over time.

---

## Quick Checklist


### Before Starting

- [ ] New folder created in `O-output/`.
    
- [ ] Strategist provided the angle in `strategist-brief.md`.
    

### Execution

- [ ] Copywriter used the correct platform skill file.
    
- [ ] Gatekeeper checked for "Eye-Level" tone.
    
- [ ] Published to Metricool.
    

### Wrap-Up

- [ ] Analyst report completed.
    
- [ ] Learning log updated.

---

## Tips for Success

1. **Be specific** - Vague feedback doesn't help
2. **Document everything** - What worked, not just problems
3. **Learn from every round** - Update the learning log
4. **Adapt per platform** - What works on LinkedIn may not work on Twitter

---
