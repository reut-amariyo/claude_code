---
name: linkedin-prepublish
description: >
  This skill should be used when the user asks "will this post succeed?", "should we publish
  this?", "check this post", "audit this draft", "go or no go", or before any LinkedIn post
  for Lior ships. Runs the mandatory pre-publish gate and outputs a verdict table.
metadata:
  version: "0.1.0"
---

# Pre-publish gate

**Mandatory before any go/no-go answer.** Never answer by feel. April 2026 shipped 10 failures
out of 12 by skipping this.

Read `${CLAUDE_PLUGIN_ROOT}/references/brand-core.md`,
`${CLAUDE_PLUGIN_ROOT}/references/voice-rules.md` and
`${CLAUDE_PLUGIN_ROOT}/references/kpi.md`.

## Output a visible table

| Check | ✅ / ❌ | Note |
|---|---|---|

Then a 🟢 / 🟡 / 🔴 verdict. **Any hard-rule ❌ means do not publish. No overrides.**

## The checks

**Follower check, added 2026-08-23. This one comes first.**
> Why would a stranger who has never heard of Lior press Follow after reading this?

If the honest answer is "they would not, but it will travel", the post is a reach play and
only ships inside the 10% monthly reach budget. It does not publish by default.

**Save check.** Is there a concrete, enumerable artifact the reader expects to need again?
If the post is in the save-first three-quarters and the answer is no, it is not ready.

**Brand non-negotiables.** Archetype is Architect of Growth not Motivator · hits at least one
pillar · founder journey not product marketing · no "100 engineers" · no imposter syndrome or
fear confessions · no arrogance · no criticism of Shopify, Lovable or Wix · CEO relevance
filter · dyslexia rule.

**Anti-AI writing rules.** No parentheses · no em or double dashes · no "not X, it's Y" in any
wording including compressed forms · no "Honestly" openers · odd numbers · "I/me/my" under
about 3 · maximum one "just".

**Hook discipline.** Under 10 words, concrete anchor in line 1, not a banned opener.

**Archetype match.** Names one of the 10 confirmed archetypes. Under the follower KPI,
archetypes 8 and 9 are promoted and archetype 4 is a capped reach play, about one a month.

**The "vs." test.** State the foil in one sentence. If you cannot, the post is not ready.

**Visual family.** One of the four. Real artifact, never a designed card.

**Mechanics.** 750-1,200 chars, or up to 1,500 for save-first · no arrow lists · no "Read that
again" · no Unicode bold on the keyword line.

## Notes, not blockers

The engagement gap is a hypothesis, audited 2026-08-04: ending type has no proven effect on
impressions and is directional only on comments. Flag a closed ending as ⚠️, never as a ❌.
