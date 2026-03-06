# The ABC-TOM System Guide

A complete reference for understanding and using the ABC-TOM framework.

---

## The Core Insight

**AI doesn't have memory. But your files do.**

Every conversation with AI starts from zero. It doesn't remember what you told it yesterday. That's why most people get inconsistent results.

The ABC-TOM system solves this by storing everything in files. Before any task, your agents read those files. Your preferences, your standards, your voice, your past learnings. All there. Always.

**Files = Long-term memory for AI.**

---

## The Framework

```
ABC-TOM
├── ABC = The Foundation (Set Up Once)
│   ├── A-agents/    → Your AI team definitions
│   ├── B-brain/     → Knowledge, research, references (what you bring)
│   └── C-core/      → Brand DNA, identity, ICP
│
└── TOM = The Execution (Run Daily)
    ├── T-tools/     → Skills, workflows, prompts
    ├── O-output/    → Everything they create
    └── M-memory/    → What the system learns together with you
```

**The Mantra:** "Set up ABC once. Run TOM daily."

**The Distinction:** "ABC is who you are. TOM is what you do."

---

## ABC: The Foundation

### A = Agents

Your AI team. Each agent has a specific role and knows how to do their job.

**What's in an agent file:**
- Core identity (who they are, what they do)
- Required reading (what they need to know before working)
- How they work (their process)
- Quality standards (what "good" means to them)

**Examples:**
- `copywriter-agent.md` - Writes all content
- `gatekeeper-agent.md` - Reviews quality before publishing
- You can create any agent you need

**Key principle:** One clear job per agent. Don't make jack-of-all-trades agents.

---

### B = Brain

The knowledge your agents need to do their job well. **Brain is what you bring.**

**What goes here:**
- `content-samples/`, `communication-samples/`, `research-samples/` - Examples of your past writing (one per track)
- `brand-discovery-worksheet.md` - Quick onboarding questionnaire
- `INBOX/` - A visible capture point for new stuff. Drop anything here first, organize later.
- Research documents
- Reference materials
- Data and analytics
- Competitor information

**Key principle:** The more you feed the brain, the smarter your agents get. Knowledge compounds.

**Brain vs Memory:**
- Brain = What YOU bring to the system (your knowledge, your research, your examples)
- Memory = What you LEARN TOGETHER with the system (patterns, feedback, decisions)

One-liner: **"Brain is what you bring. Memory is what you learn together."**

---

### C = Core

Your brand's DNA. The non-negotiables that define who you are.

**The three core files:**
- `project-brief.md` - What you do, who you serve, what makes you different
- `voice-dna.md` - How your brand speaks (tone, style, dos and don'ts)
- `icp-profile.md` - Your ideal customer profile (who they are, what they want)

**Key principle:** Be specific. "Professional but friendly" is useless. "Short sentences, no jargon, always include one number" is useful.

**Fill these first.** Everything else depends on knowing who you are.

---

## TOM: The Execution

### T = Tools

Reusable skills, prompts, and workflows that give your agents superpowers.

**Three types:**

| Type | What It Is | Example |
|------|------------|---------|
| **Skills** | Expert playbooks for tasks | `social-post-skill/` |
| **Prompts** | Copy-paste instructions | `01-convert-brand-discovery.md` |
| **Workflows** | Multi-step processes | `social-post-workflow.md` |

**The prompts folder structure:**
```
T-tools/02-prompts/
├── content/
│   ├── 01-convert-brand-discovery.md
│   ├── 02-learn-my-writing-style.md
│   ├── 03-sync-agents-with-context.md
│   └── 04-create-social-post.md
├── research/
│   └── ... (same 01-04 structure)
├── communication/
│   └── ... (same 01-04 structure)
└── BONUS/
    ├── 05-create-new-agent.md
    ├── 06-create-new-skill.md
    └── ... (more advanced prompts up to 14)
```

---

### O = Output

Everything your agents create lives here.

**Organization:**
```
O-output/
├── 01-first-project/
├── 02-second-project/
└── drafts/
```

**Key principles:**
- Number your folders for order
- Each project gets its own folder
- Keep drafts separate from finals

---

### M = Memory

What the system learns over time. This is what makes your AI team get smarter. **Memory is what you learn together.**

**The three memory files:**

| File | Purpose | When to Update |
|------|---------|----------------|
| `learning-log.md` | Execution patterns (what worked, what didn't) | After each review |
| `feedback.md` | Audience signals (comments, reactions) | After publishing |
| `decisions.md` | Strategic rationale (key choices and why) | When making decisions |

**Key principle:** Your agents read these before starting work. Every correction you log makes future output better.

**This is where The Loop starts.** The system improves itself.

---

## The Loop

The ABC-TOM Loop is what makes the system compound over time.

```
You use TOM to create output
        ↓
You review the output and log what worked in M-memory
        ↓
Best insights from Memory get promoted back into B-brain and C-core
        ↓
Next time agents run, they start from a stronger foundation
        ↓
Repeat
```

**Memory feeds back into Brain and Core.** That's The Loop.

A pattern you notice in `learning-log.md` ("short hooks always outperform long ones") becomes a rule in `voice-dna.md`. A strategic decision in `decisions.md` ("we focus on LinkedIn") becomes context in `project-brief.md`.

The Loop is what turns a static system into one that grows with you.

Use bonus prompt 14 (`close-the-loop.md`) to run The Loop explicitly.

---

## How It Works Together

### The Flow

```
You give direction → Agent reads ABC → Agent uses Tools → Output created → You review → Memory updated → The Loop feeds back to ABC
```

### Agents Check Agents

```
Agent A (creates) → Agent B (reviews) → Gatekeeper (approves) → You (publish)
```

Built-in quality control. Your standards, automated.

---

## The 4 Workshop Exercises

### Exercise 1: Feed Your Core
**Goal:** Teach agents who you are
**Edit:** `B-brain/brand-discovery-worksheet.md`
**Prompt:** `T-tools/02-prompts/[your-track]/01-convert-brand-discovery.md`
**Result:** Fills `C-core/` with your brand foundation

### Exercise 2: Set Your Style
**Goal:** Teach agents how you sound
**Edit:** Your track's samples folder in `B-brain/`
**Prompt:** `T-tools/02-prompts/[your-track]/02-learn-my-writing-style.md`
**Result:** Updates voice-dna and copywriter-agent with your patterns

### Exercise 3: Sync Your Team
**Goal:** Make sure all agents know your context
**Prompt:** `T-tools/02-prompts/[your-track]/03-sync-agents-with-context.md`
**Result:** All agents read and internalize core files

### Exercise 4: Create Your First Output
**Goal:** See the system in action
**Prompt:** `T-tools/02-prompts/[your-track]/04-create-....md`
**Result:** Your first AI-generated content, in your voice

---

## Key Concepts

### "You're the CEO"
The agents work for you. They execute. You decide. You stay in control.

### "Files = Memory"
The whole trick. AI can't remember, but files persist. Store everything in files.

### "Week 1 is rough. Week 10 is magic"
The system compounds. Every correction, every learning, makes future output better. Be patient.

### "One system, infinite projects"
Starting something new? Duplicate the ABC-TOM folder. Same structure, new context.

### "Agents check agents"
Built-in quality control. Copywriter writes, Gatekeeper reviews. You get better output.

### "The Loop closes the gap"
Memory feeds back into Brain and Core. The system doesn't just remember, it upgrades itself.

---

## Pro Tips

1. **Be specific in C-core.** Vague input = vague output.

2. **Feed the brain regularly.** Add new examples, research, references. The system gets smarter.

3. **Update memory after every project.** This is how compounding happens.

4. **Run The Loop periodically.** Promote your best insights from Memory back into Brain and Core.

5. **Use INBOX for quick capture.** Don't overthink where things go. Drop new stuff in `B-brain/INBOX/` and organize later.

6. **Start simple.** Don't build 10 agents on day one. Start with copywriter + gatekeeper.

7. **When stuck, check the basics.** Is C-core filled? Are agents pointing to right files? Is there something weird in memory?

---

## Getting Help

Type `/tom` or just ask any question about the system. Tom Agent is here to help.

---

> **© Tom Even**
> Workshops: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
