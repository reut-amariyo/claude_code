# Lior LinkedIn — Claude model map
Date: 2026-08-26
Reference: Ruben Hassid "How to pick the right Claude model"
Status: reviewer feedback applied, versions dropped, Anthropic named for tagging

---

## --- POST STARTS ---

There's a reason Claude keeps giving you mid output.

It's not (only) about your prompt.
It's the model you keep defaulting to.

Anthropic ships four models.
Most of us use only one.

I used to run Fable for everything.
Assumed the strongest wins.

But only ~10% of tasks actually need it.

So I built this map to sort out my everyday tasks.

Step 1: Does your task need a complex answer?

☑ No: use Haiku or Sonnet.
☑ Yes: use Opus or Fable.

Step 2: In a hurry?

☑ Yes: Haiku. Instant. Chat only, no heavy files.
☑ No: Sonnet. Runs 70% of my week. The default.

Step 3: Would you clear a weekend for this?

☑ No: Opus. Modeling, code review, deep analysis.
☑ Yes: Fable. Deep research. Analytical decisions.

[GRAPHIC: decision tree]

When Opus gets stuck, escalate to Fable.
Everything else, route down the tree.

The upgrade is learning when to step down.

## --- POST ENDS ---

---

## Routing check, pass 1: faithful to Ruben's post

| Branch | Ruben's post | Our post | Match |
|---|---|---|---|
| Step 1 No | Haiku 4.5 or Sonnet 5 | Haiku 4.5 or Sonnet 5 | ✅ |
| Step 1 Yes | Opus 5 or Fable 5 | Opus 5 or Fable 5 | ✅ |
| Step 2 Yes | Haiku 4.5 | Haiku 4.5 | ✅ |
| Step 2 No | Sonnet 5 | Sonnet 5 | ✅ |
| Step 3 No | Opus 5 | Opus 5 | ✅ |
| Step 3 Yes | Fable 5 | Fable 5 | ✅ |
| Escalation line | "When Opus gets stuck, escalate to Fable. Everything else, route down the tree." | verbatim | ✅ |

Question wording differs on purpose in two places, routing does not:
- Step 2. Ruben: "Need maximum speed & minimal tokens?" Ours: "In a hurry?" The token-saving half is dropped because Lior does not talk about token cost. Same branch, same models.
- Step 3. Ruben: "Is this your hardest, most ambitious work?" Ours: "Would you clear a weekend for this?" Same branch, same models.

## Routing check, pass 2: true about the actual models

Verified against the current model reference, not from memory.

| Claim in the post | Reality | Verdict |
|---|---|---|
| Fable 5 sits at the top of the tree | Fable 5 is Anthropic's most capable widely released model, for the most demanding reasoning and long-horizon work | ✅ |
| Fable 5 → "Complex decks" | ❌ **the one wrong line.** Building a deck is a production task, not what separates Fable from Opus. This phrase is ours, it was never in Ruben's post, and it came from the Michael board-deck story that got cut | ❌ **fixed above** to "Deep research. Analytical decisions.", which is Ruben's exact wording and is also what Fable is actually for |
| Opus 5 → modeling, code review, deep analysis | Opus 5 is the deep-work tier and the recommended default for coding and agentic work | ✅ |
| Sonnet 5 → the everyday default | Sonnet 5 is the fast everyday model, one tier under Opus | ✅ |
| Haiku 4.5 → instant, no overhead | Haiku 4.5 is the lightweight speed tier | ✅ |
| Escalation direction, Opus → Fable | Correct direction. Fable is above Opus, so escalating up is right | ✅ |
| "only ~10% of tasks actually need it" | Ruben's number, not a published Anthropic figure. Reads as Lior's opinion in this position, which is fine | 🟡 |

Ordering Haiku 4.5 < Sonnet 5 < Opus 5 < Fable 5 is correct. Neither branch crosses: Step 2 sits under the simple half and only offers the two small models, Step 3 sits under the complex half and only offers the two large ones.

## Two smaller things I fixed

1. **Haiku had no descriptor.** Every other model got a line, Haiku was bare "☑ Yes: Haiku 4.5." Put "Instant. No overhead." back so the four rows are symmetrical.
2. **Marked the graphic slot** in the blank gap.

## Haiku's limit, added on Reut's call

Haiku 4.5 is the only model in the tree capped at 200K context. The other three run at 1M. Ruben carried this as "Chat without files" under his Haiku box.

Our line: **"Instant. Chat only, no heavy files."**

No number, no jargon, and it tells the reader the one thing that will actually bite them. If they paste a long document into Haiku it will not fit, and that is the failure people hit first with the fast model. Same single line, no length cost.


---

## Reviewer feedback, applied 2026-08-26

**Note 1, missing context.** The reviewer read "tasks" as software tasks, where a four-box tree is too simplistic against real engineering methodology, and said it lands well for general work like checking, summarizing and research. Correct, and it was our gap: the post never said which kind of work it covers.

Fix, chosen by Reut, folded into the existing line rather than added as a new one:
"So I built this map to sort out my everyday tasks."

"everyday tasks" carries the scope in two words and keeps the framing that Lior built the map for himself. What it gives up versus the longer version is the explicit carve-out for engineers. The objection is no longer pre-empted in the post, so if it turns up in the comments the reply is: the map is for everyday work, engineering has its own methodology, and that is a different post.

**Note 2, drop the version numbers.** Applied everywhere. Haiku, Sonnet, Opus, Fable.

The reason I would give is longevity rather than reputation. Tier names stay true when the next version ships, so the post keeps working as a saved reference instead of expiring. It also keeps the post out of whatever argument is attached to any one release, which is what the reviewer was pointing at.

The tradeoff, so it is a decision and not a default: version numbers signal that a post is current, and freshness is part of why this one earns a save right now. Losing them costs a little urgency in exchange for a longer shelf life. My read is that a decision map is a save-and-return asset, so shelf life wins.

**Not changed:** "Instant. Chat only, no heavy files." stays under Haiku. The context limit that line describes is real for the current Haiku, and it is the failure people hit first.


## Anthropic mention, added 2026-08-26

"Anthropic ships four models. Most of us use only one." sits right after the hook so the tag lands high enough to carry reach.

"us" rather than "you" or "most people" puts Lior inside the group before he confesses, so the admission two lines later reads as continuation rather than reversal. No finger pointing, which is the eye-level register.

The line also earns its place independently: it states the premise the whole map resolves.

Tagging check: the post is neutral about Anthropic, and the ~10% line is a routing claim about where Fable fits, not a criticism. Safe to tag.
