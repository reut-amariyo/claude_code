# Source — Charlie Hills, "Claude Code → Codex (and keep everything you already built)"
https://x.com/charliejhills/status/2096550164278485292
Posted 2026-09-06. 124.6K views, ~512 likes, ~1.4K bookmarks, 53 reposts, 28 replies.
Pulled 2026-09-07. Full text archived below the analysis.

## What this source actually gives us

Five usable pieces, ranked by how well they survive the CEO relevance filter.

**1. Two models arguing caught an invention. 🟢 strongest.**
Hills had Codex build a comparison graphic, told it he did not like it, and instead of guessing
Codex went and asked Claude what was wrong. Claude's diagnosis was right on the real fault. Claude
also handed over three differences between the tools that were not real. Codex pushed back on all
three and Claude withdrew them.
His line: "the argument caught an invention that either of them would have shipped alone."
This is a quality-control principle, not a workflow tip, which is why it clears the filter. It is
also the natural sequel to yesterday's draft, where the point was who answers when an agent is wrong.

**2. The division of labour they negotiated themselves. 🟢**
He made the two models go three rounds over his real files and agree who does what.
Claude sets structure, hierarchy, visual language. Codex refines spacing and diagrams.
His close: "Running one is a preference, running both is a division of labour."

**3. Setup debt. 🟡**
His name for why people stay locked in: months spent teaching a tool your rules, your instructions
file, the way you brief it. Moving means going back to generic output.
⚠️ It is a renamed phenomenon, which the anti-AI rules ban us from coining. Usable only if we
attribute it to him, or describe the thing without naming it.

**4. The migration is now a four-minute job. 🟡**
Codex scans the machine, finds the agents already there, copies rules/skills/last 30 days of chats,
renames CLAUDE.md to AGENTS.md. Nothing deleted, both tools keep running.
Real news, but the moment we write the steps it becomes the banned lane.

**5. ARC-AGI 3. 🟡 one line only.**
Not a coding test. Drops a model into an abstract puzzle world with no instructions and it has to
work out the rules by trying things. Astra cleared levels in fewer moves than a human on 96% of
them. Claude Opus 5 scores under half of Astra's.
⚠️ Unverified second-hand number. Fine as "the benchmark everyone is quoting", never as our own fact.
Also note his caveat: the headline yellow blob is Astra on a setup nobody else was given.

**Not usable:** the install commands, the /plugin lines, the migration prompt, the newsletter and
waitlist CTAs. All creator lane.

## How this changes the 2026-09-07 draft on file

The routing draft argued "own the context, rent the engine" off Lior's own June stack swap. Hills
gives it a second, sharper mechanism: you do not run two models for speed, you run two because one
of them will confidently invent three things and the other will catch them. That is a review
process, and review is Lior's actual job at 200 people.

Three candidate directions, all built on the same source:

- **A. The cross-check.** One model invents, the second catches it. The reason to run both is the
  same reason nothing ships here on one person's say-so. Strongest fit, and it extends yesterday's
  accountability post into a series.
- **B. Own the context.** The 2026-09-07 draft as written, with Hills' migration news as proof that
  the switching cost just collapsed for everyone, not only for people with a file-based setup.
- **C. Division of labour.** Stop asking which model wins, start assigning seats. Closest to the
  org-chart post already published, so it risks repeating ourselves.

## Full text, archived

Claude Code → Codex (and keep everything you already built)

For months people have been telling me Codex is better than Claude Code.

I ignored all of it. I have built my whole business inside Claude Code (every pipeline, every system) and I did not fancy starting again.

Then GPT-6 Astra launched and I (finally) designed to make the switch.

The one thing keeping most people where they are is setup debt.

You have spent months teaching a tool how you work. Your rules, your instructions file, the way you brief it.

Moving means starting again on all of it and going back to generic output. That sunk cost is real, and it is why people stay.

Good news: OpenAI just made it a four-minute job!

Codex finds the agents already on your machine and offers to bring them across. Your setup, your skills, your last 30 days of chats.

And if you have never used one of these at all, this is the easiest moment there has ever been to start. It's ChatGPT that can see your folders and vibe code stuff.

Instead of pasting a document into a chat window, you point it at the folder the document lives in. That's it.

Step 1. Import it in the app.

Download Codex and open it. There is nothing to install in a terminal and no command to type (which is why most people avoid Claude Code).

The route is Settings, then Import, then Claude Code. It scans your machine on the way in and shows you what it found. Mine offered all three.

Nothing is moved and nothing is deleted. You get a copy, and Claude Code carries on exactly as it was. Then it asks what to bring over. Tick everything.

Your rules file gets renamed on the way in, from CLAUDE.md to AGENTS.md, which is the thing Codex needs it to be called.

Step 2. Let the skill finish the job.

The import brings your files across. It does not convert everything, and the leftovers are the parts you built last: your shortcuts, subagents, hooks.

OpenAI published a skill for exactly that, and the funny part is where you install it. It goes inside Claude Code.

Save a copy of your Codex settings file before you run it. The skill rewrites that file from scratch, so anything you had set up in it goes.

Then run it and leave it alone. It converts what the import missed, checks its own work, and fixes what it got wrong. Ask it for a dual system and you keep both tools running side by side, which is what I did.

Step 3. Read your own rules back.

Neither of the first two steps does this for you. They move your rules. Neither tells you what they say.

Mine had been growing for nine months and I could not have recited half of it.

It does not answer in the chat. It writes you a report.

Read it once and look for three things. The rules it reworded, and whether you agree with the new wording. Anything it says only works in Claude Code. And the list at the bottom of what it left alone.

Then I gave both tools the same task. Same brief, brand rules on one graphic. Claude Code made the one on the left and I was ready to bin it. Codex finished the one on the right.

It took seven versions and a lot of my feedback, so this is not a one-prompt result (nothing good ever is). It found a cause I could measure and fixed it.

The thing I did not expect was how it talks. Claude Code, explaining a fault to me: correct, and it fixed it. Now read that as someone who has never opened a terminal. Here is Codex, reviewing a graphic it had just made. Same job. One is talking to an engineer. The other is talking to me.

And look at what it did first. It opened three of my past graphics and compared the new one against them, which took two minutes on a job I would have accepted at thirty seconds.

What everyone is (actually) arguing about

My own week is one data point, so I swept the last 30 days across Hacker News, Reddit, X, TikTok and Instagram. Every post about either tool, sorted by what it was actually about.

Almost every Claude Code thread is about the meter. Weekly caps, what people are spending, and not being able to see what it did with any of it.

Almost every Codex thread is somebody showing off what they built.

Get them to argue (with each other)

Claude Code can run as a command, not just a window you type into. Codex can run commands. So Codex can ask Claude a question and read the answer back, on its own, while it works.

I had Codex building a comparison graphic and I did not like it (I told it so, in those words). Instead of guessing, it went and asked Claude what was wrong with it.

Claude's diagnosis was right. The layout promised lots of differences, then filled itself with things both tools do. It also handed over three differences that were not real. Codex pushed back on all three, and Claude withdrew them.

Two labs arguing about my work, and the argument caught an invention that either of them would have shipped alone.

The thing I was (wrong) about

Letting an AI drive your screen has been the most disappointing thing in this whole category. Watching it hunt for a button you could have clicked in a second. I gave up on it a long time ago.

Then somebody uploaded a photo of himself, opened Canva, and gave both agents the same instruction: draw me.

So I pointed it at my own work. My infographic generator, the system behind every graphic you see on LinkedIn, and one line: "using only Computer Use, build a graphic from my recent newsletter."

It opened Figma and did it. Read the newsletter, checked my design system, and designed the entire graphic. That clip is sped up, but it honestly amazed me. It designed the whole thing from scratch and used Claude to self-critique the design until it hit 95 out of 100.

It did take a bit longer than I would have liked (a fair bit), so the Figma plugin is still what I run instead (not through the browser). But the accuracy is what's impressive here, not the speed.

There is one test (ARC-AGI 3) that measures this and it is not a coding test. It drops a model into a small abstract puzzle world it has never seen before, one turn at a time, with no instructions of any kind. It has to work out the rules by trying things, which is the same job as landing on a screen it has never met.

Astra got through levels using fewer moves than a human on 96% of them. On the same leaderboard, Claude Opus 5 sits at less than half its score.

Astra is the yellow line. Claude Opus 5 is the red dot below it. That lone yellow blob at the top is Astra again on a setup nobody else was given, which is the number you will see quoted everywhere.

The best setup is (both)

Do not pick one. The most effective way to use these is together, and OpenAI have made that the easy option. They built Codex into Claude Code as an add-on.

Now you can hand your work to Codex without leaving the tool you already know.

My graphics had been coming out worse, so I had the two of them go three rounds over my actual files and work out who should do what. This is what they agreed on:

Claude sets the structure, the hierarchy and the visual language.

Codex refines that same artwork, the spacing and diagrams.

They are both exceptional coding agents. Running one is a preference, running both is a division of labour.

I am not moving off Claude Code. I am running both, and letting the work decide.

## Notable reply, worth knowing
Beard Operator @BeardOperator: "I actually use both. Claude is my hands on builder/tester/worker.
Dex is design/intel/strategy. They each have a unique perspective/strength which helps balance &
refine output."

---

# Added 2026-09-07 — second batch Reut sent

## 🔴 The "free Astra + Fable 5.1" link is a scam. Do not use it.

`platform.experientiallabs[.]ai/models` — "log in via Gmail or GitHub, get API key, free GPT-6
Astra and Claude Fable 5.1". Not opened, not visited, and it should not be.

Why it reads as credential harvesting:
- Nobody gives away frontier models from OpenAI and Anthropic on one unbranded domain. Those are
  the two most expensive inference products on the market and they are not resold at zero.
- The ask is a Google or GitHub OAuth login. That is the payload. A Google grant can reach mail
  and drive, a GitHub grant can reach private repos. The "API key" is the bait for the login.
- The model list mixes real names with plausible fakes to look complete.
- The post defangs its own URL with (.), which is what people do when they know a link gets flagged.
- "not many people" as a selling point is urgency-scarcity, the standard pattern.

**If anyone on the team already logged in:** revoke the app in Google account permissions and in
GitHub settings, then rotate anything that account could reach. Nothing to do beyond that.

Nothing from this item goes into a Lior post. A CEO recommending a sketchy API mirror is a
reputational hit with no upside.

## 🟢 The Astra "Part 2" review is the real material

Anonymous, two days of use, one person. Unverified and it cannot be quoted as Lior's own test.
But the shape of it is the sharpest version of the both-not-either argument we have seen.

**What it says Astra is best in the world at:** planning a complex technical task, auditing and
reviewing, finding bugs a QA team would miss, building hypothetical failure scenarios, UX, and
computer use.

**What it says Astra is bad at:** executing. Writes poor code, acts before it thinks, never clean
on the first try, introduces regressions into files it was only asked to add to, cannot finish a
task and verify it in one pass, and writes tests that fit its own bugs rather than the spec.

**The line that matters:** the model that is the best reviewer on the market is one of the worst
builders on the market. Same model, same week.

## This settles the direction

Direction A, the cross-check, now has a mechanism instead of an anecdote.

Hills gave us the event: two models argued and the argument caught an invention neither would have
caught alone. This review gives the reason it works. They are not two interchangeable engines you
run twice for safety. They are opposite skill shapes. One plans and audits and cannot build. One
builds and does not catch its own mistakes.

That is a sentence Lior can say from his own seat without borrowing anyone's benchmark, because it
is how he already staffs a company. The person who finds the flaw in the plan and the person who
ships fastest are rarely the same person, and no one running 200 people would ask one of them to
be both. The model argument is the same argument, and the answer is the same answer.

⚠️ Sourcing rule for the draft: none of the pros/cons above may appear as Lior's measurement. He
can say what he has actually seen in his own stack. Everything else is "what the people two days
into it are reporting", or it is cut.

## Third batch — the same reviewer's Part 1, and it contradicts his Part 2

Part 1, day one: "It stopped introducing regressions into the project's code."
Part 2, day two: "It introduces regressions into existing projects."

Same person, same model, opposite finding, one day apart. Also day one: "about twice as smart as
GPT-5.6 Sol". Day two: "isn't AGI at all, just Sol bloated with more parameters."

This is not a reason to throw the source out. It is the reason none of it can be stated as fact in
a Lior post, and it is a useful thing to know about every Astra take flying around this week.

**The one item that survives, and it is the best line in all three sources:**

Part 1, point 2: "the first model that doesn't invent problems when auditing code. GPT-5.6 Sol
would come back with 15 issues, half of which were pointless over-engineering and false claims.
Astra pinpointed exactly 3 critical issues and gave an honest assessment of what had been done right."

Put that next to Hills: his reviewer model found the real fault AND handed over three differences
that were not real, and the second model pushed back until they were withdrawn.

Two independent sources, same failure mode. The hard part of review is not finding what is wrong.
It is not inventing what is not. And no model catches its own inventions.

That is the post.
