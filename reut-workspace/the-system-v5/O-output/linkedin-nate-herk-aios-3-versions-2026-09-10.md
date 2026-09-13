# LinkedIn — 3 versions from Nate Herk's "GPT-6 Astra AI OS" video (2026-09-10)

Brief: same structure as the 25K Claude→Codex post. Find one SIMPLE idea inside the video, build a post. 3 versions.
Structure: the 8 beats from lior-post-claude-to-codex-migration. Hook donor: Tom's big promise / small effort.

The video has 3 ideas simple enough to fit "3 real steps". Everything else in it (4 Cs, 3D brain, audit
scores, dashboard) is a framework, and frameworks do not save. Each version takes one idea.

| | Idea in the video | Timestamp | Lior's real hook into it |
|---|---|---|---|
| A | CLAUDE.md and AGENTS.md are the same file. Copy, rename, done | 5:41-5:57 | He moved to Codex last week. This is the part the skill did not do |
| B | Get interviewed instead of writing context: grill-me | 14:13-15:24 | Records every meeting, still the priorities live in his head |
| C | Karpathy's LLM wiki: the agent files your sources into a linked wiki | 15:26-16:40 | Plaud transcripts piling up unopened |

## Verified before drafting, and against what

- AGENTS.md is Codex's CLAUDE.md: Karpathy's own gist says the schema file is "CLAUDE.md for Claude Code or AGENTS.md for Codex". Nate says the same at 5:45.
- grill-me: github.com/mattpocock/skills, path skills/productivity/grill-me/SKILL.md, description "A relentless interview to sharpen a plan or design." Install line from his README: `npx skills@latest add mattpocock/skills`. Works on Claude Code and Codex per README. NOTE: Matt's skill interviews you about a plan or decision. It does NOT save answers to a file by itself, Nate's kit adds that. Step 3 in version B therefore tells the agent to save, rather than claiming the skill does.
- LLM wiki: gist.github.com/karpathy/442a6bf555914893e9891c11519de94f, titled "llm-wiki", "designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code...)". Operations named in the gist: ingest, query, lint. The RAG line is his: "the LLM is rediscovering knowledge from scratch on every question. Nothing is built up."
- Lior records every meeting with Plaud: memory lior-content-capture-system-plaud.
- NOT verified: that Lior ran B or C. A is true already, his memory file says he pointed the new stack at CLAUDE.md. B and C need one real run each before publishing. B costs 20 minutes, C costs one paste.

---

# v2 — rewritten 2026-09-10 after Reut: "לשחזר את המבנה, לא להעתיק את התוכן"

v1 reused the 25K post's content (the 9-months number, the Claude-vs-Codex frame, "I know. You X. So did I.",
a "last week" callback). v2 keeps only the 8 beat FUNCTIONS. Side-by-side test: no sentence rhymes with the original.

| Beat | Function | A | B | C |
|---|---|---|---|---|
| 1 Hook | concrete anchor + small effort / big result | 1 filename solves lock-in | stopped writing, gets interviewed | 1-page gist runs a wiki |
| 2 Counter-hook | parenthetical flip, under 6 words | (Took 4 seconds.) | (One question at a time.) | (Nobody writes it.) |
| 3 Permission | let the reader keep their habit | build on one model, rules outside it | nobody briefs properly at 11pm | recording feels productive, that is normal |
| 4 Confession | a wrong assumption or a gap he owns | assumed the file belonged to the vendor | agents ran on a plan he had dropped | opened the archive only for disputes |
| 5 Trigger | one external thing changed | Nate Herk's side-by-side | Matt Pocock's skill | Karpathy's gist |
| 6 Named cost | borrowed vocabulary, credited | Karpathy's "schema" | Matt's "communication gap" | Karpathy's "nothing accumulates" |
| 7 Steps | 3, real, verified | cp / open / ask | install / run / save | copy / paste / ingest+lint |
| 8 Close | refuse the obvious verdict | "so switch anytime" → deed to the house | "the AI knows me" → unspoken priorities are moods | "record more" → filing is where memory starts |

## VERSION A — the rename

--- POST STARTS ---

AI vendor lock-in, solved with 1 filename.

(Took 4 seconds.)

Build everything on one model if you want. The only condition is that the rules live outside it.

For a long time I assumed the file where my agent's rules live belonged to the vendor. Like a CRM export you never fully get back.

Then a video by Nate Herk put two files side by side. Claude Code reads CLAUDE.md before your first message. Codex reads AGENTS.md. Inside, identical.

Karpathy calls that file the schema. It is the one part of your setup you own. The model is rented.

Ten seconds, no skill needed:

1. In your project folder, copy the file.
cp CLAUDE.md AGENTS.md

2. Open the same folder in the other tool. New project, local, pick the folder.

3. Ask it: "What are my rules?" Compare the answer to the file.

Keep both files in the folder. Whatever ships next quarter reads one of them.

Your setup is a text file. Treat it like the deed to the house.

#aiagents #codex

--- POST ENDS ---

~950 chars. I/me/my: 2. "just": 0.

## VERSION B — get interviewed

--- POST STARTS ---

Stopped writing context. My agent interviews me now.

(One question at a time.)

Nobody writes a full brief at 11pm. You type two lines and hope.

My priorities changed this year. The file my agents read did not. For weeks they were executing a plan I had already dropped, and the answers felt generic because they were.

Matt Pocock built a skill for exactly this. It is called grill-me. It asks, waits, asks again, and refuses to start working until it understands.

He names the problem the communication gap. The distance between what you meant and what you typed.

Three steps, twenty minutes:

1. Install his skills. One line, works in Claude Code and Codex.
npx skills@latest add mattpocock/skills

2. Run it on one topic.
/grill-me my priorities for Q4

3. Before the first answer, tell it: "Save every answer to a file in this project." Next week, new topic.

By the third session the file knew things my team had never heard me say.

Unspoken priorities are moods.

#aiagents #founders

--- POST ENDS ---

~950 chars. I/me/my: 3. "just": 0.
Flag: "By the third session" claims 3 runs. Either Lior does 3 sessions or the line becomes "By the end of the first session".

## VERSION C — the wiki that writes itself

--- POST STARTS ---

A 1-page gist from Karpathy runs my company wiki.

(Nobody writes it.)

Recording every meeting feels productive. Reopening one never happens. That is normal.

I record every meeting I take. The folder grew for months. I opened it when a dispute needed an exact quote, and for nothing else.

Then Andrej Karpathy posted a one-page pattern called an LLM wiki. The agent reads each transcript once, files it into pages that link to each other, and rewrites the old pages when a new one contradicts them.

His diagnosis of every notes tool so far: retrieval rediscovers your knowledge from scratch on each question. Nothing accumulates.

One paste, then a habit:

1. Copy his idea file. It is a single gist.
gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

2. Paste it into Codex or Claude Code with one line: "Build a wiki from my transcripts folder using this pattern."

3. Every new transcript goes in the raw folder, then say "ingest". Once a month say "lint". It flags stale numbers and pages that disagree.

Recording was the easy half. Filing is where memory starts.

#aiagents #knowledgemanagement

--- POST ENDS ---

~1,050 chars. I/me/my: 3. "just": 0.

## Verification unchanged from v1 (see top of file). Ship order unchanged: A, then C, then B.
Visuals unchanged. Gate re-run on v2: all rows pass; hooks 7 / 8 / 9 words.
