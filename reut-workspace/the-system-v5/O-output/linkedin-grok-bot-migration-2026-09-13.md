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


## v33 FINAL, 2026-09-14. REUT'S TEXT. Punctuation only: period after "on one screen", comma removed in "a name and a job". Step-2 parentheses are her choice.

--- POST STARTS ---

Grok Bot broke my sleep.

(If your day ends and your task list doesn't, this one is for you.)

Imagine your agents doing the work while you sleep.
Now open the laptop and make it real.

Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or Codex (wherever you manage your agents) and ask: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask: "Read the guide and generate every bot automatically." Each one writes its own instructions, takes a name and a job.

That's it.

Now the insane part starts:
All your agents are talking to each other on one screen.

Each agent has a real Chrome browser and a computer of its own, and a memory that holds.

You can talk to them from your phone, put them in groups, watch them hand work to each other at 1 am, and you?

Can go to bed.

The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v32 FINAL, 2026-09-14. Lior's 3 recording points folded briefly into the insane part (UX / own computer / memory).

## v31 (superseded) Reut: three subjects is too many (migration / why Grok Bot / what it gives). Cut Lior's "why Grok Bot" block; his own-computer fact folded into the insane-part line. His 3 reasons -> next post, "Why I moved to Grok Bot" (comparison).

--- POST STARTS ---

Grok Bot broke my sleep.

(If your day ends and your task list doesn't, this one is for you.)

Imagine your agents doing the work while you sleep.
Now open the laptop and make it real.

Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or Codex, wherever you manage your agents, and ask: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask it: "Read the guide and generate every bot automatically."
Each one writes its own instructions, takes a name and a job.

That's it.
Your Grok Bot is ready to go.

Then the insane part starts:
Now, all your agents are talking to each other, and you see every conversation on one screen.
Each one has a real Chrome browser and a computer of its own, and the memory holds from one day to the next.
You can talk to them from your phone, put them in groups, watch them hand work to each other at 1 am, and you can go to bed.

The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v31 FINAL, 2026-09-14. Reut: three subjects is too many (migration / why Grok Bot / what it gives). Cut Lior's "why Grok Bot" block; his own-computer fact folded into the insane-part line. His 3 reasons -> next post, "Why I moved to Grok Bot" (comparison).

--- POST STARTS ---

Grok Bot broke my sleep.

(If your day ends and your task list doesn't, this one is for you.)

Imagine your agents doing the work while you sleep.
Now open the laptop and make it real.

Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or Codex, wherever you manage your agents, and ask: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask it: "Read the guide and generate every bot automatically."
Each one writes its own instructions, takes a name and a job.

That's it.
Your Grok Bot is ready to go.

Then the insane part starts:
Now, all your agents are talking to each other, each on a real computer of its own.
You can talk to them from your phone, put them in groups, watch them hand work to each other at 1 am, and you can go to bed.

The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v30 FINAL, 2026-09-14. Lior's voice note (37s, Hebrew, Whisper large-v3) added as a "Why Grok Bot, 3 reasons" block before the close. Step 2: "Claude or Codex" (Reut asked about ChatGPT; Codex is where OpenAI-side agent systems live).

Lior's note, transcript: "הייתי מוסיף אולי למה גרוק בוט. הסיבה מבחינתי זה שאפשר בצורה... ה-UX מדהים, אפשר בצורה מאוד נוחה לראות את כל ההתכתבות של כל האג'נטים ביניהם, זה אחד. שתיים, הממורי והקונטקסט עובדים ממש טוב. שלוש, זה מבחינתי הכי [לא ברור], יש להם גישה, לאג'נטים, למחשבים משלהם, לכל אחד מהם, שהוא לא סטייטלס בראוזר אלא ממש כרום בראוזר ומחשב משלהם. הם יכולים לעשות הרבה פעולות ככה בצורה מאוד יציבה ונוחה."

--- POST STARTS ---

Grok Bot broke my sleep.

(If your day ends and your task list doesn't, this one is for you.)

Imagine your agents doing the work while you sleep.
Now open the laptop and make it real.

Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or Codex, wherever you manage your agents, and ask: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask it: "Read the guide and generate every bot automatically."
Each one writes its own instructions, takes a name and a job.

That's it.
Your Grok Bot is ready to go.

Then the insane part starts:
Now, all your agents are talking to each other.
You can talk to them from your phone, put them in groups, watch them hand work to each other at 1 am, and you can go to bed.

Why Grok Bot, 3 reasons:
The UX. Every conversation your agents have with each other, on one screen.
The memory. Context carries over between sessions, and it works.
The computers. Each agent gets a real Chrome browser and a machine of its own that keeps state, so it runs long jobs without falling over.

The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v29 FINAL, 2026-09-14. REUT'S TEXT. She resolved the sleep tension herself ("and you can go to bed"), cut the "people think it is complicated" block and "living in the cloud". Fixes: comma in "a name and a job"; "on the phone" -> "from your phone"; step-2 parentheses -> commas (flagged once, her call). Gate clean.

--- POST STARTS ---

Grok Bot broke my sleep.

(If your day ends and your task list doesn't, this one is for you.)

Imagine your agents doing the work while you sleep.
Now open the laptop and make it real.

Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask it: "Read the guide and generate every bot automatically."
Each one writes its own instructions, takes a name and a job.

That's it.
Your Grok Bot is ready to go.

Then the insane part starts:
Now, all your agents are talking to each other.
You can talk to them from your phone, put them in groups, watch them hand work to each other at 1 am, and you can go to bed.

The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v28 FINAL, 2026-09-14. REUT'S TEXT. Line 2 became her parenthetical; she added an "imagine / now make it real" line, rephrased. Alternatives: "Imagine a world where your agents do the work. Now open the laptop, it takes 2 prompts to build it." / "Picture your agents finishing the list while you sleep. Now open the laptop and make it real."

--- POST STARTS ---

Grok Bot broke my sleep.
(If your day ends at 5 and your task list doesn't, this one is for you.)

Imagine your agents doing the work while you sleep. Now open the laptop and make it real.
Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask:

"Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask it: "Read the guide and generate every bot automatically." Each one writes its own instructions, takes a name and a job.

That's it. Your Grok Bot is ready to go. People think it is complicated. Another tool, another switch. If your Claude or OpenAI system is built right, files and structure, it is easy. Then the insane part starts:
All the agents are talking to each other, doing whatever they need, living completely in the cloud. You can talk to them from the phone or the desktop. You put them in groups. Watch them hand work to each other at 1am, and you do not go to bed.
The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v27 FINAL, 2026-09-14. Reut: line 2 = the reader's pain + "this one is for you" (9-to-5, tasks unfinished), the sleep broke because the results are crazy. Options: "If you work 9 to 5 and never finish the list, this is for you." / "Working 9 to 5 and still behind? This one is for you." / "If your to-do list survives every workday, read this." / "If 9 to 5 is not enough for what is on your plate, this is for you."

## v26 (superseded) Reut: line 1 = "Grok Bot broke my sleep." fixed; line 2 options offered: "If your day ends at 5 and your task list doesn't, this one is for you." (pick) / "It won't break yours. The move is 2 prompts." / "Your agents can have the night shift by tonight." / "Yours will do the work while you sleep." / "Trust me, yours is worth the 2 prompts." Body = REUT'S TEXT. Her rewrite is the base; she cut the WHOOP line, "Mine do. Now I need to.", "Yours is next", "sign in, create nothing yet", hashtags. Those stay cut. Mechanical fixes only: 1/2/3 numbering, step-3 quote placement, asterisks removed, parenthetical caps/apostrophe.

--- POST STARTS ---

Grok Bot broke my sleep.
If your day ends at 5 and your task list doesn't, this one is for you.
Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask:

"Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask it: "Read the guide and generate every bot automatically." Each one writes its own instructions, takes a name and a job.

That's it. Your Grok Bot is ready to go.
People think it is complicated.
Another tool, another switch.
If your Claude or OpenAI system is built right, files and structure, it is easy.
Then the insane part starts:

All the agents are talking to each other, doing whatever they need, living completely in the cloud.
You can talk to them from the phone or the desktop.
You put them in groups. Watch them hand work to each other at 1am, and you do not go to bed.

The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v26 FINAL, 2026-09-14. Reut: line 1 = "Grok Bot broke my sleep." fixed; line 2 options offered: "Yours can start working while you sleep tonight." (pick) / "It won't break yours. The move is 2 prompts." / "Your agents can have the night shift by tonight." / "Yours will do the work while you sleep." / "Trust me, yours is worth the 2 prompts." Body = REUT'S TEXT. Her rewrite is the base; she cut the WHOOP line, "Mine do. Now I need to.", "Yours is next", "sign in, create nothing yet", hashtags. Those stay cut. Mechanical fixes only: 1/2/3 numbering, step-3 quote placement, asterisks removed, parenthetical caps/apostrophe.

--- POST STARTS ---

Grok Bot broke my sleep.
Yours can start working while you sleep tonight.
Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask:

"Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask it: "Read the guide and generate every bot automatically." Each one writes its own instructions, takes a name and a job.

That's it. Your Grok Bot is ready to go.
People think it is complicated.
Another tool, another switch.
If your Claude or OpenAI system is built right, files and structure, it is easy.
Then the insane part starts:

All the agents are talking to each other, doing whatever they need, living completely in the cloud.
You can talk to them from the phone or the desktop.
You put them in groups. Watch them hand work to each other at 1am, and you do not go to bed.

The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v25 FINAL, 2026-09-14. REUT'S TEXT. Her rewrite is the base; she cut the WHOOP line, "Mine do. Now I need to.", "Yours is next", "sign in, create nothing yet", hashtags. Those stay cut. Mechanical fixes only: 1/2/3 numbering, step-3 quote placement, asterisks removed, parenthetical caps/apostrophe.

--- POST STARTS ---

One of the best AI hacks right now is Grok Bot working while you sleep.
(But I don't sleep anymore.)
Migration took 2 prompts:

1. Open Grok Bot.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask:

"Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Back in Grok Bot, ask it: "Read the guide and generate every bot automatically." Each one writes its own instructions, takes a name and a job.

That's it. Your Grok Bot is ready to go.
People think it is complicated.
Another tool, another switch.
If your Claude or OpenAI system is built right, files and structure, it is easy.
Then the insane part starts:

All the agents are talking to each other, doing whatever they need, living completely in the cloud.
You can talk to them from the phone or the desktop.
You put them in groups. Watch them hand work to each other at 1am, and you do not go to bed.

The only edge left is agents that work while you sleep.

--- POST ENDS ---

## v24 FINAL, 2026-09-14. Reut's own rewrite, cleaned. Gate 🟢, score 8.5. Changes vs her text: Grok Bot once per line; "It won't break yours" removed (contradicted "you do not go to bed"), replaced by "Yours is next"; "That's it" moved after step 3 completes; WHOOP line restored (the image needs it); "Mine do. Now I need to." restored as the resolver; hashtags added. Open: Lior confirms "1am"; "AI hacks" vs "business hacks" is her call.

--- POST STARTS ---

One of the best AI hacks right now is Grok Bot working while you sleep.
(Trust me, it broke mine.)
Yours is next. Migration took 2 prompts:

1. Open Grok Bot. Sign in, create nothing yet.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job.

That's it. Your Grok Bot is ready to go.

People think it is complicated.
Another tool, another switch.
If your Claude or OpenAI system is built right, files and structure, it is easy.

Then the insane part starts:
All the agents talking to each other, doing whatever they need, living completely in the cloud.
You talk to them from the phone or the desktop.
You put them in groups.
You watch them hand work to each other at 1am, and you do not go to bed.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen.

The only edge left is agents that work while you sleep.
Mine do. Now I need to.

#aiagents #aiautomation

--- POST ENDS ---

## v23 FINAL, 2026-09-14. Reut: the sleep must be in the hook because the visual is the WHOOP screenshot. Confession moved into the "trust me" line. Alt line 2: "Trust me, it broke my sleep. Consistently." / "Trust me, Grok Bot cost me a week of bedtimes."

--- POST STARTS ---

One of the best business hacks right now is agents that work while you sleep.
Trust me, Grok Bot broke mine. Consistently.
Migration took 2 prompts:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

I still don't understand why everyone isn't doing this yet. People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

Then the insane part starts:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. You watch them hand work to each other at 1am, and you do not go to bed.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

The only edge left is agents that work while you sleep. Together, talking to each other, in parallel.
Mine do. Now I need to.

#aiagents #aiautomation

--- POST ENDS ---

## v22 FINAL, 2026-09-14. Hook on the donor "One of the best business hacks is being your own biggest cheerleader. / Trust me, you're going to need it." (Reut). Universal claim as a hack + second-person "trust me" promise. Grok Bot required in the hook. No parenthetical; "Consistently." pun moved to sit before the WHOOP line. Other options: "The best business hack of 2026 is moving your agents into Grok Bot. / Trust me, it takes 2 prompts." / "One of the best business hacks right now is Grok Bot. / Trust me, you are going to want your agents in it."

--- POST STARTS ---

One of the best business hacks right now is agents that work while you sleep.
Trust me, Grok Bot makes it 2 prompts.

The whole move, in order:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

I still don't understand why everyone isn't doing this yet. People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

Then the insane part starts:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. You watch them hand work to each other at 1am, and you do not go to bed.

It broke my sleep. Consistently.
WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

The only edge left is agents that work while you sleep. Together, talking to each other, in parallel.
Mine do. Now I need to.

#aiagents #aiautomation

--- POST ENDS ---

## v21 FINAL, 2026-09-14. Reut rejected "Don't open Grok Bot before bed". Hook = "You sleep. Your agents don't." Alternatives: "Your agents should work while you sleep." / "Grok Bot broke my sleep. Consistently. (And it may break yours.)" / "The only edge left works while you sleep. (Grok Bot broke mine. Consistently.)". Reut's thesis as the close: "the only way to build a competitive advantage today is agents that work while you sleep, together, in good communication, in parallel." Replaces the punchline close.

--- POST STARTS ---

You sleep. Your agents don't.
(Mine broke my sleep. Consistently.)
Migration took 2 prompts:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

I still don't understand why everyone isn't doing this yet. People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

Then the insane part starts:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. You watch them hand work to each other at 1am, and you do not go to bed.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

The only edge left is agents that work while you sleep. Together, talking to each other, in parallel.
Mine do. Now I need to.

#aiagents #aiautomation

--- POST ENDS ---

## v20 FINAL, 2026-09-14. Reut's thesis as the close: "the only way to build a competitive advantage today is agents that work while you sleep, together, in good communication, in parallel." Replaces the punchline close.

--- POST STARTS ---

Don't open Grok Bot before bed.
(It broke my sleep. Consistently.)
Migration took 2 prompts:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

I still don't understand why everyone isn't doing this yet. People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

Then the insane part starts:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. You watch them hand work to each other at 1am, and you do not go to bed.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

The only edge left is agents that work while you sleep. Together, talking to each other, in parallel.
Mine do. Now I need to.

#aiagents #aiautomation

--- POST ENDS ---

## v19 FINAL, 2026-09-14. Reut: the sleep is EXCITEMENT, not efficiency. Lior meant the thing is so insane, and the migration so easy, he could not sleep. Night-shift / efficiency lines removed. Pun: his word "consistently" vs WHOOP "sleep consistency 66%". Alt hook: "Grok Bot broke my sleep. Consistently. (And it may break yours.)". "1am" is a placeholder, ask Lior.

--- POST STARTS ---

Don't open Grok Bot before bed.
(It broke my sleep. Consistently.)
Migration took 2 prompts:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

I still don't understand why everyone isn't doing this yet. People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

Then the insane part starts:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. You watch them hand work to each other at 1am, and you do not go to bed.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

The move everyone avoids is 2 prompts and one bad night of sleep.

#aiagents #aiautomation

--- POST ENDS ---

## v18 FINAL, 2026-09-14. Reut: hook must say sharply that your agents keep working while you sleep, else you fall behind; line 2 = they broke his sleep. Alternative line 1 (her wording): "You close the laptop. Your agents keep working."

--- POST STARTS ---

You sleep. Your agents don't.
(Mine broke my sleep.)
If yours stop when you do, you are already behind. The fix is 2 prompts:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

I still don't understand why everyone isn't doing this yet. People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

What you get on the other side is the insane part:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. Approvals reach the phone. Nothing waits for morning.
Agents on a laptop work your hours. Agents in the cloud work theirs.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted. The bots slept fine.

The move everyone avoids is 2 prompts and one bad night of sleep.

#aiagents #aiautomation

--- POST ENDS ---

## v17, 2026-09-14. Hook shape from "If you hate your job, tonight, instead of ... go on LinkedIn and email 100 people" (Reut). Condition + tonight + swap + action. Line 1 = 18 words, over the under-10 rule, shape needs it. Profanity out.

--- POST STARTS ---

If your agents stop when your laptop closes, tonight, instead of watching another Grok Bot demo, move them.
(Mine broke my sleep.)
It takes 2 prompts:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

I still don't understand why everyone isn't doing this yet. People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

What you get on the other side is the insane part:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. Approvals reach the phone. Nothing waits for morning.
Agents on a laptop work your hours. Agents in the cloud work theirs.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted. The bots slept fine.

The move everyone avoids is 2 prompts and one bad night of sleep.

#aiagents #aiautomation

--- POST ENDS ---

## v16 (alternative, short hook), 2026-09-14. Shape from Reut's example "5 money rules that changed my life (And may change yours)". Other options: "Don't open Grok Bot until you read this. (Migration is 2 prompts.)" / "Move your agents into Grok Bot in 2 prompts. (Mine broke my sleep.)".

--- POST STARTS ---

Grok Bot broke my sleep.
(And it may break yours.)
Migration took 2 prompts:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude or OpenAI, wherever you manage your agents, and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." It does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

I still don't understand why everyone isn't doing this yet. People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

What you get on the other side is the insane part:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. Approvals reach the phone. Nothing waits for morning.
Agents on a laptop work your hours. Agents in the cloud work theirs.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted. The bots slept fine.

The move everyone avoids is 2 prompts and one bad night of sleep.

#aiagents #aiautomation

--- POST ENDS ---


I/me/my 3. "night shift" once (WIIFM line changed to "work theirs").

## v11 (superseded), 2026-09-14. Lior's voice-note words placed into the v10 structure, checked against Tom Orbach's hook formula (small effort + big real result + colon, deadpan).

--- POST STARTS ---

I still don't understand why everyone isn't doing this yet.

(Grok Bot broke my sleep.)

Migration took 2 prompts:

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Go to Claude and ask it to write a guide for Grok Bot about your agents and how to migrate everything: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." Claude does the whole thing.

3. Back in Grok Bot, ask it to read the guide and generate every bot automatically. Each one writes its own instructions, takes a name and a job, and your Grok Bot is ready to go.

People think it is complicated. Another tool, another switch, another week of wondering how. If your Claude or OpenAI system is built right, files and structure, it is easy.

What you get on the other side is the insane part:
All the agents talking to each other, doing whatever they need, living completely in the cloud. You talk to them from the phone or the desktop. You put them in groups. Approvals reach the phone. Nothing waits for morning.
Agents on a laptop work your hours. Agents in the cloud take the night shift.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted. The bots slept fine.

The move everyone avoids is 2 prompts and one bad night of sleep.

#aiagents #aiautomation

--- POST ENDS ---

~1,300 chars. I/me/my 2. "just" 0. "insane" once (Lior's word, same as Reut's Astra parenthetical). Tom check: effort = 2 prompts / ask / paste; result = agents in the cloud + sleep broken; self-deprecation = the parenthetical; colon after "2 prompts"; deadpan, no emoji; humor beat = "The bots slept fine".

## v10 (superseded), 2026-09-14. Reut: open with disbelief / (sleep) / 2 prompts, go straight into HOW to migrate Claude -> Grok Bot, then what it gives. Structure beat dropped.

--- POST STARTS ---

I still don't understand why everyone isn't doing this yet.

(Grok Bot broke my sleep.)

Migration took 2 prompts.

1. Open Grok Bot. Download it on the desktop and on the phone, sign in, create nothing yet. It needs a paid SuperGrok or Cursor plan.

2. Open Claude and paste this: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines." Claude reads your setup and writes the guide.

3. Back to Grok Bot. Paste the guide with: "Read this guide and create every bot in it." Each one writes its own instructions, takes a name and a job, and is live.

That is the whole move.

What you get on the other side:
Every bot runs on its own cloud computer, signed into your tools. They message each other and hand off work in a group chat that looks like Slack with an agent in every seat. Approvals reach the phone. Nothing waits for morning.
Agents on a laptop work your hours. Agents in the cloud take the night shift.

WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted. The bots slept fine.

The move everyone avoids is 2 prompts and one bad night of sleep.

#aiagents #aiautomation

--- POST ENDS ---

~1,150 chars. I/me/my 2. Steps in execution order: setup / prompt to Claude / prompt to Grok Bot. Paid plan fact: included in SuperGrok Heavy, Cursor Ultra, Cursor Teams Premium (layer3labs, composio). Visual: WHOOP screenshot uncropped, ALT text above.

## Version C (superseded), 2026-09-14. Hook shape from the Clay/SpaceXAI post Reut sent (access given, then "I closed my laptop"), posture only. Body = v9. Recommended over the locked sleep opening.

--- POST STARTS ---

5 Grok bots got my inbox, calendar and meeting notes.
Then I closed the laptop.
(I still don't understand why everyone isn't doing this yet.)

Your agents already work. So did these.
For a month I scrolled past every Grok Bot demo. Rebuilding a system that already runs sounded like a lost week.
Then those 5 landed in one group chat. Slack, with an agent in every seat.
Each one runs on its own cloud computer, already signed into the tools. They message each other, hand off work, and keep going with the lid down. Approvals reach the phone. Nothing waits for morning.
WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted. The bots slept fine.

What this buys you:
Agents on a laptop work your hours. Agents in the cloud take the night shift. Every task that waited for you to open the lid gets done before you wake up.
The move is the part everyone overestimates. 2 prompts, and Claude writes the guide.

The whole move, in order:

1. Keep every agent in files. A rules file, skills as markdown, one folder per agent, git.

2. Ask Claude for the guide. One prompt: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Open Grok Bot and paste it. "Read this guide and create every bot in it." Each one writes its own instructions, takes a name and a job, and is live.

Own the files. Every new tool is a 2-prompt job.

#aiagents #aiautomation

--- POST ENDS ---

Line 1 tools are PLACEHOLDERS: replace with the 3 real tools his bots are signed into. I/me/my = 4. "The bots slept fine" = humor beat, his own data.
Not used: "hottest new AI product in the world" (unverifiable superlative). "Hooked" optional at the end of the trigger line.

## v9, 2026-09-14. Three edits from the "Grok Bot better than 99% of people" YouTube course transcript (creator Brock): Slack line, step-2 prompt in Grok Bot's own primitives, step 3 says the bot writes its own instructions.

--- POST STARTS ---

Grok Bot broke my sleep.
Migration took 2 prompts.
(I still don't understand why everyone isn't doing this yet.)

Your agents already work. Mine did too.
For a month I scrolled past every Grok Bot demo. Rebuilding a system that already runs sounded like a lost week.
Then 5 of them landed in one group chat. Slack, with an agent in every seat.
Each one runs on its own cloud computer. They message each other, hand off work, and keep going with the laptop shut. Approvals reach the phone. Nothing waits for morning.
WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

What this buys you:
Agents on a laptop work your hours. Agents in the cloud take the night shift. Every task that waited for you to open the lid gets done before you wake up.
The move is the part everyone overestimates. Claude does it.

The whole move, in order:

1. Keep every agent in files. A rules file, skills as markdown, one folder per agent, git.

2. Ask Claude for the guide. One prompt: "Write a guide for Grok Bot to recreate every agent in this system. Instructions, skills, plugins, memory, routines."

3. Open Grok Bot and paste it. "Read this guide and create every bot in it." Each one writes its own instructions, takes a name and a job, and is live.

Own the files. Every new tool is a 2-prompt job.

#aiagents #aiautomation

--- POST ENDS ---

Verified from the course transcript (2026-09-14): bot creation = "+" > create new bot > plain-English brain dump, the bot writes its own instructions; skills are markdown files "just like Claude"; primitives = instructions / skills / plugins / memory / routines; each bot has its own virtual computer + browser; group chats; bots negotiate handoffs; phone app; paid SuperGrok or Cursor plan required; templates (share a bot) added early Sept 2026.
Option NOT taken: naming Hermes as the previous stack in the confession. True, but the 09-07 post said his systems lived in Claude. Reut decides.
Title idea parked: "Grok Bot: the full setup" as a LinkedIn ARTICLE (7 levels from his seat) anchoring 3-5 posts, per the AI-search-cites-articles memory.

## v8 (superseded) Reut: "take the 25K structure, add the what's-in-it-for-me". Beat order restored: trigger -> reason to move -> cost of staying -> enabler -> steps.

--- POST STARTS ---

Grok Bot broke my sleep.
Migration took 2 prompts.
(I still don't understand why everyone isn't doing this yet.)

Your agents already work. Mine did too.
For a month I scrolled past every Grok Bot demo. Rebuilding a system that already runs sounded like a lost week.
Then 5 of them landed in one group chat.
Each one runs on its own cloud computer. They message each other, hand off work, and keep going with the laptop shut. Approvals reach the phone. Nothing waits for morning.
WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

What this buys you:
Agents on a laptop work your hours. Agents in the cloud take the night shift. Every task that waited for you to open the lid gets done before you wake up.
The move is the part everyone overestimates. Claude does it.

The whole move, in order:

1. Keep every agent in files. A rules file, one folder per agent, git.

2. Ask Claude for the guide. One prompt: "Write a guide for Grok Bot to recreate every agent in this system. Role, files, tools, rules, schedule."

3. Open Grok Bot and paste it. "Read this guide and create every bot in it." Each one gets a name and a job, and they are live.

Own the files. Every new tool is a 2-prompt job.

#aiagents #aiautomation

--- POST ENDS ---

~1,250 chars. I/me/my 4. WIIFM block = laptop hours vs cloud night shift. Files/chat-history pair dropped, one contrast per post.

## v7 (superseded)

--- POST STARTS ---

Grok Bot broke my sleep.
Migration took 2 prompts.
(I still don't understand why everyone isn't doing this yet.)

Because it is one more platform. Agreed.

For a month I scrolled past every Grok Bot demo. The agents already ran, and rebuilding them somewhere new sounded like a lost week.
Then 5 of them landed in one group chat.
They message each other, hand off work, and run on their own cloud computers while the laptop is closed. Approvals reach the phone. Nothing waits for morning.
WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

Agents in files move anywhere.
Agents in chat history die with the tool.

The whole move, in order:

1. Keep every agent in files. A rules file, one folder per agent, git.

2. Ask Claude for the guide. One prompt: "Write a guide for Grok Bot to recreate every agent in this system. Role, files, tools, rules, schedule."

3. Open Grok Bot and paste it. "Read this guide and create every bot in it." Each one gets a name and a job, and they are live.

Own the files. Every new tool is a 2-prompt job.

#aiagents #aiautomation

--- POST ENDS ---

Parenthetical is 10 words, over the 6-word counter-hook cap. Reut's call, locked. "(Claude did the moving.)" dropped, one parenthetical per post.

## v6 (superseded)

Hook: I still don't understand why everyone isn't doing this yet.
Line 2: (Grok Bot. 2 prompts.)
Permission: Because it is one more platform. Agreed.
Body: identical to Version A below. Note: hook opens with "I", anchor lands in line 2 (two-beat exception). Reut's call.

## v5 candidates (superseded), 2026-09-13. Hook shape from ridark_eth (disbelief that others are not doing it), posture only, wording new. Reut picks.

### Version A (recommended)

--- POST STARTS ---

Why is nobody moving their agents into Grok Bot?

(Took me 2 prompts.)

Because it is one more platform. Agreed.

For a month I scrolled past every Grok Bot demo. The agents already ran, and rebuilding them somewhere new sounded like a lost week.
Then 5 of them landed in one group chat.
They message each other, hand off work, and run on their own cloud computers while the laptop is closed. Approvals reach the phone. Nothing waits for morning.
WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

Agents in files move anywhere.
Agents in chat history die with the tool.

The whole move, in order:

1. Keep every agent in files. A rules file, one folder per agent, git.

2. Ask Claude for the guide. One prompt: "Write a guide for Grok Bot to recreate every agent in this system. Role, files, tools, rules, schedule."

3. Open Grok Bot and paste it. "Read this guide and create every bot in it." Each one gets a name and a job, and they are live.

Own the files. Every new tool is a 2-prompt job.

#aiagents #aiautomation

--- POST ENDS ---

### Version B

--- POST STARTS ---

Grok Bot in 2 prompts. Almost nobody does it.

(Claude did the moving.)

One more platform is the last thing you need. Agreed.

For a month I scrolled past every Grok Bot demo. The agents already ran, and rebuilding them somewhere new sounded like a lost week.
Then 5 of them landed in one group chat.
They message each other, hand off work, and run on their own cloud computers while the laptop is closed. Approvals reach the phone. Nothing waits for morning.
WHOOP sent the bill. Sleep consistency 66%, the only orange number on the screen. The hours were fine. The bedtimes drifted.

Agents in files move anywhere.
Agents in chat history die with the tool.

The whole move, in order:

1. Keep every agent in files. A rules file, one folder per agent, git.

2. Ask Claude for the guide. One prompt: "Write a guide for Grok Bot to recreate every agent in this system. Role, files, tools, rules, schedule."

3. Open Grok Bot and paste it. "Read this guide and create every bot in it." Each one gets a name and a job, and they are live.

Own the files. Every new tool is a 2-prompt job.

#aiagents #aiautomation

--- POST ENDS ---

Body change vs v4: "WHOOP caught it" -> "WHOOP sent the bill", because the sleep claim left the hook.
v4 hook "Grok Bot broke my sleep. Migration took 2 prompts." kept above as the fallback.
Still open: Lior confirms "for a month" and "5 of them". Visual: WHOOP screenshot, uncropped, ALT text above.
