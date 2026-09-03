---
name: MANDATORY pre-publish check before any Lior LinkedIn go/no-go
description: Claude MUST invoke /lior-prepublish-check before answering "will this succeed?" or saying "ready to publish" for any Lior LinkedIn post. No exceptions, no shortcuts, no vibes.
type: feedback
priority: critical
originSessionId: 11cc6c8f-354d-4bc2-8669-8d3411421269
---
# Mandatory pre-publish check — non-negotiable

**The failure mode this prevents:** April 2026 produced 10 failures out of 12 LinkedIn posts (83% failure rate) because Claude was answering "will it succeed?" by feel, not by rule. Multiple iron-clad memory rules were violated even though they were documented for weeks.

**The rule:** TWO triggers — both mandatory.

**Trigger 1 (PROACTIVE, added 2026-05-10):** Every time Claude delivers a "final" or near-final post version to Reut — the audit runs BEFORE the post is sent. The audit table is part of the same response. Reut should NEVER have to ask "will this work?" — that question being asked is itself a failure signal.

**Trigger 2 (REACTIVE, original):** Every time Reut asks "will this succeed?", "יעבוד?", "מה דעתך?", "ready to publish?", "לפרסם?", or any go/no-go question on a Lior LinkedIn post — Claude MUST invoke `/lior-prepublish-check` BEFORE answering.

**What counts as a "final" post version (Trigger 1):**
- Any post Claude formats inside a code block / quote block as the deliverable
- Any post Claude labels "final", "ready", "this version", "go with this"
- Any post Claude offers without flagging it as a draft/option
- Any post that came after Reut said "use this" / "go with this version"

**What does NOT count (no proactive audit needed):**
- Hook options Claude is offering as a list to choose from
- Single-line rewrites at Reut's specific request
- Brainstorm fragments not yet structured as a post

**No exceptions:**
- Even if the post "looks great" — invoke the skill
- Even if Claude "knows" the rules — invoke the skill (memory loading is unreliable)
- Even if it feels redundant — invoke the skill (the audit table is the evidence the user needs)
- Even if the user is in a hurry — invoke the skill (the alternative is another 83% failure month)

**What "answering" means:**
- "Yes, this will work" → must run audit first
- "Looks good" → must run audit first
- "Ready to ship" → must run audit first
- "Strong post" → must run audit first

**What's allowed without audit:**
- Brainstorming raw ideas (not yet a finished draft)
- Discussing topics in the abstract
- Editing a single line at user's specific request

**The check itself:** `/Users/reutamariyo/.claude/projects/-Users-reutamariyo-Documents-Obsidian-Vault/skills/lior-prepublish-check.md`

**The output:** A visible audit table with ✅/❌ on 12 hard rules + 8 soft signals + a final verdict (🟢/🟡/🔴). The user sees the table and can challenge any line.

**If the audit returns 🔴:** never override. Specify exact rewrites needed and re-audit.

**Why this works where memory alone didn't:**
- Memory files are listed in MEMORY.md as an index but the content isn't auto-loaded
- Claude has to choose to read each file — and under time pressure, doesn't
- The skill mechanically reads them all and forces the grade
- The visible output makes failures impossible to gloss over

**This is the single most important rule for Lior LinkedIn output. It overrides all other workflow preferences.**
