# LinkedIn — hot AI topics + save-first post line (2026-09-10)

Brief (Reut, Hebrew): hot AI topics, posts that lead to saves, big promise / small effort.
Continue the Claude→Codex migration line. That post did 25K impressions.

## Hot topics this week, verified 2026-09-10

| Topic | Fact | Source |
|---|---|---|
| GPT-6 Astra | Released 2026-09-03, GA next day. Headline feature: computer use. 1.05M context. $10/$50 per M tokens. | openai.com/index/gpt-6-astra, fortune.com 2026-09-03 |
| Claude Fable 5.1 | Released 2026-09-01. Same price as Astra, $10/$50. Leads AA Coding Agent Index 70 vs 67; Astra wins Terminal Bench 4.0 57.9 vs 55.8. | artificialanalysis.ai comparison |
| codex-plugin-cc | OpenAI-maintained plugin that runs Codex INSIDE Claude Code. Commands: /codex:review, /codex:adversarial-review, /codex:rescue, /codex:transfer. | github.com/openai/codex-plugin-cc README |
| Astra computer use | Enable: update ChatGPT desktop, open Work, enable Computer Use, start with @Computer. Plus users get Astra only via Work and Codex, not chat. Enterprise off by default. | theneurondaily, layer3labs guides |
| Codex plugins for non-coders | Zendesk + OneNote plugins added 2026-09-03; 6 role plugins, 62 apps, 110 skills since June. | openai.com release notes |

## The line: 5 posts, ranked

Every hook on Tom's shape: small almost-embarrassing action + large specific outcome.
Every body on the 8-beat migration template. Every post leaves one reusable artifact.

1. **The rival reviews it** (sequel, drafted below). codex-plugin-cc adversarial review.
2. **1 text file made the move take 4 minutes.** Portability principle. Artifact: the 3 files that make you vendor-proof (rules file, skills folder, git). Pure management idea, pillar focus.
3. **A rival model audited 9 months of my rules in 60 seconds.** The beat cut from the migration post. One prompt: hand CLAUDE.md to Codex, ask what is wrong with it. Needs Lior to actually run it once and keep 3 real findings.
4. **I let GPT-6 use my Mac for a week.** Experiment report, Exception 2. Only if he runs it. Enable path verified above.
5. **Same price. $10 in, $50 out. Both.** Decode: price left the decision, fit is the only variable. Lower save value, reach play.

## Post 1 — draft

Donor: our own 2026-09-07 post, beat for beat. Hook donor: Tom Orbach shape.

| Beat | Line |
|---|---|
| Two-number hook, 9 words | Claude writes it. Codex tries to break it. 3 steps. |
| Line-2 parenthetical, 4 words | (OpenAI built the plugin.) |
| Permission line | Neither. Not alone. |
| Operator confession | A model reviewing its own work has the blind spot it had when it wrote it |
| Trigger | OpenAI ships an official plugin running Codex inside Claude Code |
| Named cost | Self-review |
| 3 real steps | login / install / run |
| Close refusing the verdict | Nobody reviews their own work well. Models included. |

--- POST STARTS ---

Claude writes it. Codex tries to break it. 3 steps.

(OpenAI built the plugin.)

Last week I moved my systems into Codex and kept Claude. The comments turned into Claude vs Codex within an hour.

Which one do I trust?

Neither. Not alone.

A model reviewing its own work has the same blind spot it had when it wrote it. Same training, same habits, same excuses.

So the rival reviews it now.

OpenAI ships an official plugin that runs Codex inside Claude Code. One of its commands is called adversarial review. Its job, in OpenAI's own words, is to break confidence in the change.

Here's how to set it up:

1. Log Codex in from your terminal.
codex login

2. Install the plugin inside Claude Code.
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins

3. Run the setup once, then the review.
/codex:setup
/codex:adversarial-review

Claude ships the code. Codex has to find a reason it should not ship. When Codex comes back empty, I ship.

Nobody reviews their own work well. Models included.

#aiagents #claudecode

--- POST ENDS ---

~1,150 chars.

## Verified facts, and against what

- All 7 commands: openai/codex-plugin-cc README, fetched 2026-09-10. Prerequisites: Node 18.18+, ChatGPT subscription incl. Free, or API key. `/reload-plugins` is listed in the README after install, kept so step 2 is executable as written.
- "break confidence in the change": the adversarial-review prompt file in the same repo says the reviewer's job is "to break confidence in the change, not to validate it".
- NOT verified: "The comments turned into Claude vs Codex within an hour." Reut checks against the real thread; swap for what actually happened.

## Gate

| Check | Verdict |
|---|---|
| Hook under 10 words, concrete anchor | ✅ 9 words, two named models + number |
| Archetype | ✅ tutorial exception, same frame that worked 2026-09-07 |
| Contradicts its own last line? | ✅ no. Nothing above says one model is better |
| Parentheses | ✅ only the line-2 counter-hook |
| Em dashes / "not X, it's Y" | ✅ none. OpenAI's quote trimmed to drop the "not validate" half |
| I/me/my | ✅ 3 |
| "just" | ✅ 0 |
| Red list | ✅ clean |
| Odd numbers | ✅ 3 steps |
| CEO relevance | ✅ the post is about not letting anyone grade their own homework, a management rule |
| Why follow | ✅ a reusable supplier-check rule + 3 steps to run it Monday |
| Read as a user, in order | ✅ Codex login before plugin; plugin before setup; setup before review; "the plugin" introduced before step 2 |

Visual: same family as the migration post. Animated GIF in the image slot, two terminal panes, Codex's review verdict landing on Claude's diff. Or a real screenshot of an adversarial review output with the first finding circled in red.

Risk: "why not just use /codex:review" comments. One-line reply: "Review checks the code. Adversarial review checks the decision."
