# Folder Guide

What each folder does and how to use it.

---

## A-agents/

**Purpose:** Your AI team definitions

**What goes here:**
- Agent personality files (one per agent)
- Each file defines: who they are, what they read, how they work

**Current agents:**
- `copywriter-agent.md` - Writes all content
- `gatekeeper-agent.md` - Reviews quality
- `tom-agent.md` - Your guide to the system

**How to create a new agent:**
1. Create `[role]-agent.md` in this folder
2. Copy structure from existing agent
3. Define: identity, required reading, responsibilities
4. Use prompt: `T-tools/02-prompts/BONUS/05-create-new-agent.md`

**Tips:**
- One job per agent (don't make generalists)
- Be specific about what "good" means
- Always include Required Reading section

---

## B-brain/

**Purpose:** Knowledge your agents need. **Brain is what you bring.**

**What goes here:**
- `brand-discovery-worksheet.md` - Your brand info
- `content-samples/` - Your social media posts (content track)
- `communication-samples/` - Your professional emails (communication track)
- `research-samples/` - Your reports/briefings (research track)
- `INBOX/` - Quick capture point. Drop anything new here first, organize later.
- Research documents, reference materials, data

**How to use:**
1. Add your past content to the samples folder matching your track
2. Fill in `brand-discovery-worksheet.md` to get started
3. Add research/references as needed
4. Use `INBOX/` when you're not sure where something goes. Sort it later.

**Brain vs Memory:**
- Brain = What YOU bring to the system (your knowledge, research, examples)
- Memory = What you LEARN TOGETHER with the system (patterns, feedback, decisions)

**"Brain is what you bring. Memory is what you learn together."**

**Tips:**
- More knowledge = smarter agents
- Add real examples, not descriptions
- Keep it organized (subfolders help)
- When in doubt, drop it in INBOX

---

## C-core/

**Purpose:** Your brand's DNA

**The three files:**

### project-brief.md
What you do, who you serve, what makes you different.
- Your mission
- The problem you solve
- What makes you unique

### voice-dna.md
How your brand speaks.
- Tone and style
- Words you use / avoid
- Formatting preferences
- Example sentences

### icp-profile.md
Your ideal customer.
- Who they are
- What they want
- Their problems
- Where they hang out

**How to fill these:**
1. Answer questions in `B-brain/brand-discovery-worksheet.md`
2. Run prompt `T-tools/02-prompts/[your-track]/01-convert-brand-discovery.md`
3. Claude fills in C-core automatically

**Tips:**
- Be specific (not "professional" but "short sentences, no jargon")
- Include examples
- These start stable but evolve through The Loop (insights from Memory get promoted here)

---

## T-tools/

**Purpose:** Skills, workflows, and prompts

**Structure:**
```
T-tools/
├── 01-skills/                              → Expert playbooks
├── 02-prompts/                             → Copy-paste instructions
└── 03-workflows/                           → Multi-step processes
```

### 01-skills/
Specialized knowledge for specific tasks.
- `social-post-skill/` - Social media best practices
- `professional-email-skill/` - Email writing
- `research-briefing-skill/` - Research formatting
- `tom-guide/` - System guidance

### 02-prompts/
Numbered instructions for common actions.
```
content/
├── 01-convert-brand-discovery.md
├── 02-learn-my-writing-style.md
├── 03-sync-agents-with-context.md
└── 04-create-social-post.md
research/
└── ... (same structure)
communication/
└── ... (same structure)
BONUS/
├── 05-create-new-agent.md
├── 06-create-new-skill.md
└── ... (up to 14-close-the-loop.md)
```

### 03-workflows/
Multi-step processes that chain actions.
- `social-post-workflow.md` - Idea → draft → review → publish
- `professional-email-workflow.md` - Context → draft → review → send
- `research-briefing-workflow.md` - Topic → research → review → deliver

**How to create new tools:**
- New skill: `T-tools/02-prompts/BONUS/06-create-new-skill.md`
- Skills go in their own subfolder
- Prompts are numbered for order

---

## O-output/

**Purpose:** Everything your agents create

**Organization:**
```
O-output/
├── 01-project-name/
│   ├── draft-v1.md
│   ├── draft-v2.md
│   └── final.md
├── 02-another-project/
└── drafts/
```

**How to use:**
- Number folders for order
- One project per folder
- Keep drafts until you're done
- Archive old projects

**Tips:**
- Consistent naming helps you find things
- Don't delete drafts (you might need them)
- Let agents save here automatically

---

## M-memory/

**Purpose:** What you learn together with the system. **Memory is what you learn together.**

**The three files:**

### learning-log.md
Execution patterns. What worked, what didn't.
- "Short hooks perform better"
- "Avoid starting with questions"
- "The gatekeeper catches too much, lower threshold"

### feedback.md
Audience signals. What they say after you publish.
- Comments and reactions
- Questions people ask
- What resonates

### decisions.md
Strategic rationale. Why you chose what you chose.
- "We focus on LinkedIn because that's where ICP is"
- "We don't use emojis in headlines"
- "Bilingual content, Hebrew for local, English for newsletter"

**When to update:**
- `learning-log.md` → After each review cycle
- `feedback.md` → After publishing and seeing reactions
- `decisions.md` → When you make strategic choices

**Why this matters:**
Agents read memory before starting work. Every entry makes future output better. This is the compounding effect.

**The Loop:** The best insights from Memory don't just stay here. They get promoted back into Brain (as new knowledge) and Core (as updated rules). That's what closes The Loop and makes the system compound.

Use bonus prompt 14 (`close-the-loop.md`) to run The Loop explicitly.

---

## Quick Reference

| Folder | Contains | Changes How Often |
|--------|----------|-------------------|
| A-agents/ | Team definitions | Rarely |
| B-brain/ | Knowledge, examples (what you bring) | Often (as you learn) |
| C-core/ | Brand DNA | Rarely (but evolves through The Loop) |
| T-tools/ | Skills, prompts, workflows | Sometimes (as you need more) |
| O-output/ | Created content | Every project |
| M-memory/ | Learnings (what you learn together) | After every project |

---

## The Pattern: The ABC-TOM Loop

1. **ABC feeds the system** (who you are, what you know)
2. **TOM executes** (skills create output, memory captures learning)
3. **The Loop: Memory feeds back into Brain and Core** (best learnings become knowledge and rules)
4. **The system starts stronger next time** (and keeps compounding)

This is The Loop. It's what makes the difference between a static template and a living system that grows with you.

---

> **© Tom Even**
> Workshops: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
