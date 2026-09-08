# FINAL — moving Claude's brain into Codex (2026-09-07)

Reut's locked copy, 2026-09-07. Her text verbatim below.
Donor: Charlie Hills, 124.6K views, archived in source-charlie-hills-codex-astra-2026-09-06.md
Visual: claude-to-codex-visual/claude-vs-codex.mp4

--- POST STARTS ---

9 months with Claude. Moved to Codex in 4 min.

(GPT-6 Astra is insane.)

I know. You love Claude.
So do I.
Every system I run lives inside it, which is exactly why I ignored everyone telling me Codex was better.
Then Astra launched.
Don't stay behind because of setup debt.

OpenAI published a skill that does the whole move for you.
Here's how to move Claude's brain into Codex:

1. Back up your Codex settings first.

The skill writes to that file, so keep a copy before you start.

One line in your terminal: cp ~/.codex/config.toml ~/.codex/config.backup.toml

2. Install the skill inside Claude Code.

npx -y skills add openai/skills --skill migrate-to-codex --agent claude-code

3. Run it.

It scans, plans, migrates, checks its own work, and fixes what it got wrong.

Claude is not dead.
It has a colleague.

#aiagents #ecommerceautomation

--- POST ENDS ---

## Gate

| Check | Verdict |
|---|---|
| Hook under 10 words, concrete anchor | ✅ 9 words, two numbers |
| Line-2 parenthetical counter-hook | ✅ legal exception, 5 words, once |
| No other parentheses | ✅ |
| No em dash / en dash | ✅ |
| No "it's not X, it's Y" | ✅ |
| Red list | ✅ clear |
| "just" count | ✅ zero |
| First-person singular | ✅ 4, fine for a confession post |
| Odd list count | ✅ 3 |
| Numbering | ✅ 1/2/3 |
| Not a bare how-to | ✅ confession opener, insider framing, strategic close |
| Never says he left Claude | ✅ "brain into Codex" + "it has a colleague" |
| Stack accuracy | ✅ Codex is his engine of record since June |
| Every command verified | ✅ config path and install command checked against the skill's own SKILL.md |
| Squint rhythm | ✅ |
| Engagement gap | ⚠️ closed ending. The quotable is the trade-off, accepted |
| Hashtags | ✅ added |

## Final spacing, locked by Reut 2026-09-07

Her line grouping is deliberate: the middle block runs as five consecutive lines with no breaks,
which is what gives the squint test its long band in the centre. Do not re-space it.
Hashtags are the only thing added to her text. The hyphen-as-dash problem disappeared when she
dropped "The good news-".

## Optional, from earlier in the session
Tagging @OpenAI on the skill line and @Anthropic on a warm line buys reach, the same structure as
the 142K Google post. Not in this version. Reach lever, not a follower lever.

## Verified facts behind the post
- `~/.codex/config.toml` is the real path, named in the skill's own documentation.
- The install command is Hills'. The skill exists at openai/skills → skills/.curated/migrate-to-codex.
- ⚠️ The openai/skills repo carries a deprecation notice pointing to OpenAI Plugins. The skill file
  is still live there, but this could age within weeks.
- The skill runs autonomously through scan, plan, migrate, validate and fix without stopping to
  ask, which is what step 3 describes.
- 🛑 Hills says the skill "rewrites that file from scratch." The skill's own docs say it PRESERVES
  existing entries. Reut's line "writes to that file" is the safe wording and is what shipped.
