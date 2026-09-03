---
name: project-lior-agent-stack-hermes-codex
description: "Lior's personal AI agent stack switched from OpenClaw+Anthropic to Hermes+Codex (June 2026) due to Anthropic's June 15 billing split. Reference for any content about his AI setup."
metadata: 
  node_type: memory
  type: project
  originSessionId: 26ec4c48-392b-4c3e-a795-a842d3ec2d7c
---

# Lior's Agent Stack: Hermes + Codex (as of June 2026)

**The trigger:** Anthropic's June 15, 2026 billing split. Until then, third-party agents (OpenClaw etc.) could draw on the flat Claude subscription. From June 15, the subscription only covers Claude chat + Claude Code directly; any outside agent / API integration moves to a separate metered credit pool at API rates (also applies to headless Claude Code, Agent SDK, GitHub Actions).

**Lior's move (explained to Reut by voice note, 2026-06-10):**
- Replaced OpenClaw with **Hermes Agent** (Nous Research, open-source) + a **Codex subscription from OpenAI** as the engine. Hermes runs on the flat Codex subscription instead of per-credit API.
- He finds Hermes better than OpenClaw: faster, lighter, less buggy.
- The switch took minutes because his whole system is file-based and local (the ABC-TOM build): install Hermes, point it at CLAUDE.md, it learns the entire setup. Everything backed up on GitHub.
- His stance: PRO switching platforms when the money is significant (vs. Reut's initial "stop chasing the cheapest platform" framing). Owning the files is what makes each switch a ten-minute job.

**Why:** Any post/reply about Lior's AI workflow must reflect this stack, not Claude/OpenClaw.

**How to apply:** Content about his agent setup = Hermes + Codex/OpenAI models. Claude Code may still appear for direct terminal use. Related: [[feedback-claude-timeline-accuracy]], [[project-lior-tasks-q2]].
