# LinkedIn — Grok Bot migration post (2026-09-13)

v4: WHOOP verdict line rewritten so it reads without the bottom of the screenshot (hours green, consistency orange = bedtimes drifted).
v3 2026-09-13: visual locked = Lior's WHOOP screenshot (81% sleep performance, consistency 66% orange/poor, coach line 'held back more by schedule than by architecture'). Body now points the eye at the 66%.
v2 after the gate: named-cost line replaced by an explicit vs. pair (files vs chat history). Score 7.5 → 8.

Brief: Lior's voice note (English transcript) about Grok Bot. Structure donor: our own 2026-09-07
Claude→Codex migration post, beats only, no wording reused (rule: reuse-structure-not-content).

--- POST STARTS ---

Grok Bot broke my sleep. Migration took 2 prompts.

(Claude did the moving.)

Nobody needs one more agent platform. Agreed.

For a month I scrolled past every Grok Bot demo. The agents already ran, and rebuilding them somewhere new sounded like a lost week.
Then 5 of them landed in one group chat.
They message each other, hand off work, and run on their own cloud computers while the laptop is closed. Approvals reach the phone. Nothing waits for morning.
WHOOP caught it. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

Agents in files move anywhere.
Agents in chat history die with the tool.

The whole move, in order:

1. Keep every agent in files. A rules file, one folder per agent, git.

2. Ask Claude for the guide. One prompt: "Write a guide for Grok Bot to recreate every agent in this system. Role, files, tools, rules, schedule."

3. Open Grok Bot and paste it. "Read this guide and create every bot in it." Each one gets a name and a job, and they are live.

Own the files. Every new tool is a 2-prompt job.

#aiagents #aiautomation

--- POST ENDS ---

~1,050 chars.

## Beat map (function copied, wording new)

| Beat | Codex post 09-07 | This post |
|---|---|---|
| Two-number hook | 9 months / 4 min | Grok Bot / 2 prompts, 8 words |
| Line-2 parenthetical | (GPT-6 Astra is insane.) | (Claude did the moving.) |
| Permission line | I know. You love Claude. So do I. | Nobody needs one more agent platform. Agreed. |
| Operator confession | ignored everyone saying Codex was better | scrolled past every demo, rebuild = lost week |
| Trigger | Then Astra launched. | 5 agents in one group chat, cloud, phone |
| Named cost + vs. | setup debt | files vs chat history, v2 2026-09-13 |
| 3 steps | backup / install / run | files / guide / paste |
| Close refusing the verdict | It has a colleague. | Own the files. Every new tool is a 2-prompt job. |

## Needs Lior's real numbers (2 lines)
- "For a month" - Grok Bot launched August 2026, so plausible. Confirm.
- "5 of them" - how many bots did he actually put in the group. Grok Bot allows 2 to 6 per group chat.

## Verified facts, and against what (2026-09-13)
- Grok Bot: xAI (SpaceXAI) product, launched August 2026. Persistent named agents, each on its own
  always-on cloud computer with browser, file access and logins. Works with the laptop off.
  Sources: layer3labs.io/guides/what-is-grok-bot, composio.dev/content/guide-to-frok-bot
- Group chats: "You can put two to six Bots into a group chat. They can message each other, pass
  ownership, and continue work without you manually moving information between chats." (Composio)
- Platforms: macOS, Windows, iPhone. Linux/Android/iPad not at launch. (Composio) -> "phone" is safe.
- Bot creation: "Give it a short name, one main job, and a clear description of how it should work."
  (Composio) -> step 3 "each one gets a name and a job" is accurate.
- Access: included in SuperGrok Heavy, Cursor Ultra, Cursor Teams Premium. No standalone price
  published. Not in the post on purpose.
- NOT verified externally: that Grok Bot reads a pasted guide and generates every bot in one go.
  This is Lior's own account of what happened. Fine as his experience, do not add a claim
  that xAI documents it.
- No commands in the post, so nothing to check against a repo. The two quoted prompts are ours.

## Gate

| Check | Verdict |
|---|---|
| Hook under 10 words, concrete anchor | ✅ 8 words, named product + number |
| Line-2 parenthetical, under 6 words, once | ✅ 4 words |
| Other parentheses | ✅ none |
| Em dash / en dash | ✅ none |
| "It's not X, it's Y" | ✅ none |
| "Honestly" openers, red list | ✅ clean |
| "just" | ✅ 0 |
| I/me/my | ✅ 2 |
| Odd numbers | ✅ 3 steps, 5 agents; "2 prompts" is real data |
| Numbering 1/2/3 | ✅ |
| Rhymes with the 09-07 post | ✅ no shared sentence, no callback |
| Read as a user, in order | ✅ files exist before the guide, guide exists before the paste, "the guide" introduced in step 2 |
| Contradicts its own last line | ✅ no. Claude does the work, nothing says he left it |
| Never says he left Claude / Codex | ✅ |
| CEO relevance | ✅ the idea is owning the files, a management rule, not a feature tour |
| No disbelief lines | ✅ "I can't believe" and "wow" from the voice note cut |
| Why would a stranger follow | ✅ portability principle + a procedure to run today |
| Engagement gap | ⚠️ closed ending, the quotable is the trade-off |

## Visual (LOCKED by Reut 2026-09-13)
Lior's own WHOOP screenshot, taken 11:26 with the in-bed icon. Personal-artifact family. The 66% row sits in the top half so it survives any feed crop; the coach line is at the bottom and may not, which is why the copy names the 66% first and the verdict second.
ALT text: WHOOP sleep screen. Sleep performance 81%. Sleep consistency 66%, marked orange as poor. WHOOP note: sleep was held back more by schedule than by architecture.

Earlier note: first-party artifact beats everything: a real screenshot from his phone of the Grok Bot group
chat, bots messaging each other, names visible, taken at night with the clock showing. Same
mechanism as the exit-deck post. Fallback: animated GIF in the image slot, Claude writing the
guide on the left, bots appearing one by one on the right.

## Voice note kept / cut
Kept: "broke my sleep", "living in the cloud", "from the phone", "people think it's complicated,
another tool", "if the files and structure are built right it's easy", the Claude-guide method.
Cut: "wow", "insane" x2, "I can't believe" (no-disbelief rule), "just go to Claude" (just rule).
