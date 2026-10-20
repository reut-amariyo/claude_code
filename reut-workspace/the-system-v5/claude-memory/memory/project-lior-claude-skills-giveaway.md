---
name: project-lior-claude-skills-giveaway
description: "Oct 2026 Claude Skills giveaway post + page follow.liorpozin.com/skills (grill-me, handoff by Matt Pocock adapted, big-three by Lior); skillsclau.de is Ruben Hassid's, never link it"
metadata:
  node_type: memory
  type: project
  originSessionId: bf157686-78e6-44c8-bbd1-6c5240bba57a
  modified: 2026-10-12T14:24:32.601Z
---

Built 2026-10-12. Page live at https://follow.liorpozin.com/skills/ , source `~/Projects/lior-50/skills/`
(same repo as the 50-mentors page, which owns the follow.liorpozin.com CNAME, so no new repo needed).
Pushing is blocked for Claude by the auto-mode classifier ("Create Public Surface"): Claude commits,
Reut runs `cd ~/Projects/lior-50 && git push origin main`.

Skills: /grill-me and /handoff adapted from github.com/mattpocock/skills (MIT, license in each zip;
originals break in the Claude app: grill-me calls a second skill, handoff writes to /tmp).
/big-three is Lior's, built from the 2026-09-22 recording (morning 2-3 commitments, check-ins,
Friday + month-end committed vs done). One zip per skill; Claude app needs code execution ON
(Settings > Capabilities), upload under Customize > Skills > + > Upload a skill.

**Why:** Reut wanted known skills, not Lior's own library, and refused to ask Lior (abroad).
skillsclau.de (her donor post) is Ruben Hassid's: moratorium + someone else's gated library.
**How to apply:** don't call these skills "newest" (only the release is new); no "no email",
no date on page or post. Visual = carousel of real screenshots of the skills running, made-up
examples. You Should Know was cut: not a skill, and 10 days old by posting time.
Related: [[feedback-diversify-inspiration-creators]], [[lior-post-exit-deck-lead-magnet]],
[[reference-public-pages-github-pages]].

**Second page, 2026-10-19:** https://follow.liorpozin.com/html-plan/ (source `~/Projects/lior-50/html-plan/`):
Thariq Shihipar's html-plan skill (Anthropic claude-plugins-community, MIT) with his live example
(`example.html`, packed with the skill's pack.mjs) + one-line install
`npx -y skills add anthropics/claude-plugins-community --skill html-plan` (tested: works for Claude Code AND Codex).
Pairs with the LinkedIn post in O-output/linkedin-html-plan-thariq-2026-10-19.md (Codex-migration 8-beat structure).
Reut pushed herself; Claude commits only.
