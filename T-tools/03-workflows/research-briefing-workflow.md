# Research Briefing Workflow

> A collaborative workflow between the Researcher and the Gatekeeper for creating a professional research briefing.

---

## Process Overview

```
[You] provide topic and question
          ↓
[Researcher] researches and compiles findings
          ↓
[Gatekeeper] reviews and approves / requests changes
          ↓
[Researcher] revises (if needed)
          ↓
[Gatekeeper] final approval
          ↓
[You] use the briefing for decision-making
```

---

## Step 1: Preparation

### Before Starting

Both agents must read:
- `C-core/project-brief.md` - Who you are and what you do
- `C-core/voice-dna.md` - How your brand sounds
- `C-core/icp-profile.md` - Who your target audience is
- `M-memory/learning-log.md` - What we learned from previous rounds

### Project Setup

Create a new folder in `O-output/` with a clear name:
```
O-output/
└── 01-research-[topic]/
    ├── researcher-briefing.md    ← Researcher's version
    ├── gatekeeper-review.md      ← Gatekeeper's review
    └── final-briefing.md         ← Final version
```

---

## Step 2: Researcher Compiles Findings

### What the Researcher Does

1. **Reads C-core documents** - Understands the business context
2. **Reads `T-tools/01-skills/research-briefing-skill/`** - Learns the correct format
3. **Researches the topic** - If web search is available, uses it. If not, works from existing knowledge
4. **Writes a structured briefing** - Following the format learned

### File Format: `researcher-briefing.md`

```markdown
# Research Briefing: [Topic Name]

**Date:** [Date]
**Version:** v1

---

## Executive Summary

[2-3 sentences. The main finding. What you need to know.]

---

## Key Findings

1. **[Finding]** - [Supporting detail + number]
2. **[Finding]** - [Supporting detail + number]
3. **[Finding]** - [Supporting detail + number]

---

## Analysis

[What this means for the business. Connections between findings.]

---

## Recommendations

1. [Specific action]
2. [Specific action]
3. [Specific action]

---

## Sources and Notes

- [Source 1]
- [Limitations or caveats]

---

## Researcher Notes

### Choices I Made
- [Why I focused on this angle]
- [What I excluded and why]

### Questions for the Gatekeeper
- [Is the analysis clear?]
- [Are the recommendations actionable?]
```

---

## Step 3: Gatekeeper Reviews

### What the Gatekeeper Does

1. **First read** - Does the executive summary stand on its own?
2. **Check against standards** - Numbers, sources, actionable recommendations
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
[What the Researcher should do now]
```

---

## Step 4: Revision (If Needed)

If the Gatekeeper requested revisions:

1. **Researcher reads the notes** - Understands what to fix
2. **Updates `researcher-briefing.md`** - Bumps version to `v2`
3. **Gatekeeper reviews again** - Updates `gatekeeper-review.md`

---

## Step 5: Final Version

When the Gatekeeper approves:

### File Format: `final-briefing.md`

```markdown
# Research Briefing: [Topic Name]

**Status:** Approved
**Approval date:** [Date]

---

## Executive Summary

[2-3 sentences]

---

## Key Findings

1. **[Finding]** - [Detail + number]
2. **[Finding]** - [Detail + number]
3. **[Finding]** - [Detail + number]

---

## Analysis

[One to two paragraphs]

---

## Recommendations

1. [Action]
2. [Action]
3. [Action]

---

## Sources

- [Sources]

---

*Created by: Researcher Agent*
*Reviewed by: Gatekeeper Agent*
```

---

## Step 6: Update Learning Log

After the process is complete, the Gatekeeper updates `M-memory/learning-log.md`:

```markdown
## [Date] - Research Briefing: [Topic]

### What Worked
- [Insight]

### What We Learned
- [Lesson for next time]
```

---

## Quick Checklist

### Before Starting
- [ ] New folder created in O-output
- [ ] Both agents read C-core documents
- [ ] Topic and question are clear

### Researcher
- [ ] Read project brief and ICP
- [ ] Read the Research Briefing skill
- [ ] Researched and compiled findings with numbers
- [ ] Saved to `researcher-briefing.md`

### Gatekeeper
- [ ] Executive summary stands on its own
- [ ] At least 3 specific numbers
- [ ] Actionable recommendations
- [ ] Saved to `gatekeeper-review.md`

### Wrap-Up
- [ ] Final version saved to `final-briefing.md`
- [ ] Learning log updated
- [ ] Ready to use

---

## Tips for Success

1. **Lead with the conclusion** - Don't build suspense, give the answer upfront
2. **Numbers > descriptions** - "Grew by 23%" beats "grew significantly"
3. **Label your certainty** - Fact, signal, or opinion
4. **End with action** - Research without "so what?" is just Wikipedia

---

*This workflow teaches the principles. Adapt it to your needs.*

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
