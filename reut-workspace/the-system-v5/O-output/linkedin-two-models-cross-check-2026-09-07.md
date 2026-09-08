# LinkedIn — the invented bug (2026-09-07)

Direction A, converged from three sources: Charlie Hills' migration post, and the anonymous
Astra Part 1 + Part 2 reviews. All archived in source-charlie-hills-codex-astra-2026-09-06.md.

## Thesis

The hard part of review is not finding what is wrong. It is not inventing what is not.
No model catches its own inventions, which is the entire argument for running two.

**"vs." :** a reviewer who misses a bug vs. a reviewer who invents seven.

Why this clears the CEO relevance filter: it is a management principle about review processes,
which is Lior's job at 200 people. The models are the news peg. Strip the model names and the
post still stands, which is the litmus test in the no-tool-tips rule.

It also continues 2026-09-06 into a series. That post asked who answers when an agent is wrong.
This one answers how you find out that it is.

## Donor

Charlie Hills' own post is the donor this time, not a Donnelly.
124.6K views, 2026-09-06. Its strongest beat is "two labs arguing about my work, and the argument
caught an invention that either of them would have shipped alone."

| Beat | Donor | Lior |
|------|-------|------|
| Hook | Tool A to tool B, keep what you built | Two numbers, one invented |
| Line 2 | — | The flip, 6 words |
| Sourcing | His own week, stated as one data point | Same honesty, stated in line 4 |
| Body | Steps and screenshots | The management principle, no steps |
| Turn | Get them to argue with each other | Kept, it is the mechanism |
| Close | Running both is a division of labour | Rewritten in Lior's register, then a question |

## Visual

Family 3, third-party authority. Screenshot of the two review outputs side by side, the invented
items circled in red. If we cannot get a clean one, family 1: a photo of a real code review thread
on his screen with the disputed comment circled. Shot, not designed.
ALT text: "Two model code reviews side by side, the invented findings circled in red."

## Draft

--- POST STARTS ---

One model found 3 real bugs. The other found 15.

Seven of the 15 did not exist.

That is from a developer two days into GPT-6 Astra, not from our stack. Take the numbers loosely.

Take the shape of it seriously, because anyone who has run a review process already knows which of those two reviewers is the expensive one.

A reviewer who misses a bug costs you a bug.

A reviewer who invents seven costs you the team's attention, and once that is gone nobody reads the reviews at all.

We learned this with people long before anyone pointed it at a model.

Which is why the Astra versus Claude argument is the wrong argument.

The same week, someone had one model critique the other's work. The critique was right about the real fault. It also handed over three differences that were not real, the second model pushed back on all three, and all three came out.

Neither of them would have caught that alone. No reviewer catches their own inventions. Not people, not models.

So the setup worth building is not the model that wins this month. It is two of them, briefed to disagree, with a person reading the argument.

That is not a clever trick. That is how every team that ships anything already works.

What in your process currently has no second reader?

#aiagents #ecommerceautomation

--- POST ENDS ---

~1,290 characters.

## Pre-publish gate

| Check | Verdict |
|---|---|
| Hook under 10 words, concrete anchor | ✅ 8 words, two numbers |
| Line 2 lands under 6 words | ✅ 6 words |
| No parentheses | ✅ |
| No em dash / en dash / double dash | ✅ |
| No "it's not X, it's Y" | ✅ line by line. "That is not a clever trick. That is how every team works" is a repeated assertion, not a contrast template, but it is the closest line in the draft. Swap to "Every team that ships anything already works this way" if it reads wrong to you. |
| No "Honestly" / sincerity filler | ✅ |
| Red list | ✅ clear |
| "just" count | ✅ zero |
| First-person singular | ✅ zero. Whole post is "we" and "you" |
| Odd numbers | ✅ 3, 15, 7, 3 |
| One idea, one quotable | ✅ a reviewer who invents seven costs you the team's attention |
| "vs." articulated | ✅ missing a bug vs. inventing one |
| Archetype | ✅ Exception 1, strategic significance, zero how-to |
| Not a tutorial | ✅ no steps, no commands, no prompts, no tool recommended |
| Sourcing honesty | ✅ line 3 says outright it is not his measurement |
| Stack accuracy | ✅ no claim about what Lior runs today |
| Pillar hit | ✅ focus |
| Team size | ✅ not used, the post does not need it |
| 2 on-pillar hashtags | ✅ |
| Engagement gap open | ✅ question about the reader's own process |
| Why would a stranger press Follow? | ✅ he took the loudest argument of the week and returned a management principle they can use on people, not only on models |
| No comment gate, no repost CTA | ✅ |

**🟢 GO.** Nothing here needs Lior to confirm a claim about his own stack, which is what held up
the 2026-09-07 routing draft.

## The two lines someone will argue with, and the answers

1. "You are quoting an anonymous developer." Yes, and the post says so in line 3 before anyone else
   can. That is why it survives. The same reviewer contradicted himself on regressions between day
   one and day two, so anyone treating this week's Astra takes as measurement is on thin ice.
2. "Two models cost twice as much." True, and the answer is in the post's own frame: so does a
   second reviewer, and every company that ships pays for one anyway.
