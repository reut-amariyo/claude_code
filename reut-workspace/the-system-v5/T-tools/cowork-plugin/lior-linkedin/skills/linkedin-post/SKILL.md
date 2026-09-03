---
name: linkedin-post
description: >
  This skill should be used when the user asks to "write a LinkedIn post for Lior", "draft a
  post", "write a save-first post", "turn this into a post", or wants LinkedIn content for
  Lior Pozin. Produces a draft only, never publishes.
metadata:
  version: "0.1.0"
---

# Draft a LinkedIn post for Lior

Read first, in order:
1. `${CLAUDE_PLUGIN_ROOT}/references/brand-core.md`
2. `${CLAUDE_PLUGIN_ROOT}/references/voice-rules.md`
3. `${CLAUDE_PLUGIN_ROOT}/references/save-first-spec.md`

Then run `/linkedin-prepublish` on the finished draft before delivering it.

## The main axis is save-first

The monthly mix is **3 save-first : 1 personal**.

A save is a bet on **future utility**, never a reaction to enjoyment. Every save-first post
carries a concrete, enumerable, specific artifact the reader expects to need again. Vague
list items kill saves.

### The five save-first formats

- **Decision checklist** — "The 7 questions we ask before an AI agent touches a customer
  order." The question list is the object.
- **Thresholds** — the internal numbers he manages by. What he kills a test at, what margin
  makes him walk. People save numbers to benchmark themselves.
- **Teardown scorecard** — the event ages, the criteria he judged it by are the artifact.
- **Briefing with a "so what" list** — the saveable half is what to actually do.
- **Anti-checklist** — "5 things we stopped doing after the exit." Rarer, so saved more.

### The personal quarter

Real past failures, personal artifacts, operator confessions. Model the hook compression of
Sahil Bloom: four to six words, second person. Never his life-philosophy lane, and never his
X-not-Y constructions.

## Mechanics

- 750-1,200 characters, extended to **1,500 for save-first posts** because a manifest needs room.
- Hook under 10 words with a concrete anchor in line 1.
- Articulate the "vs." in one sentence before drafting. If you cannot, the post is not ready.
- One idea. One quotable principle.
- Visual from the four families only: third-party authority, personal artifact, cultural meme,
  signed illustration. **Never marketing-team graphics or Canva checklist cards.** For
  save-first posts the artifact must be the real thing photographed or screenshotted.
- Hand-drawn red circle when the post hinges on a small detail in the visual.
- Leave an engagement gap at the end. This is a note, never a blocker.

## Delivery format

Wrap the draft in these exact markers, as plain text, never a blockquote:

```
--- POST STARTS ---
<the post>
--- POST ENDS ---
```

Then give the visual recommendation and the archetype it maps to.

🛑 **Never publish.** Deliver the draft. Reut posts manually. "מאשר" or "approved" approves
the draft, it is not permission to post.
