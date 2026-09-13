---
name: feedback-read-drafts-as-a-user-follows-them
description: Reut reads instructional drafts in the order a reader would execute them; I was checking style and missing sequence faults. Read every how-to as a user, in order, before delivering.
metadata:
  type: feedback
---

2026-09-07, the Claude-to-Codex post. Across the session Reut caught four faults I had passed,
and not one of them was a style issue. All four were sequence or logic:

1. Step 1 referred to "the skill" before the skill had been introduced anywhere.
2. The backup was numbered step 2 when it has to happen before step 1.
3. "Install the skill inside Claude Code" appeared in two consecutive steps.
4. "Here's how to make the switch" contradicted the post's own ending.

She also asked the two questions a reader would ask and I had not answered: what are the two
models actually competing at, and where did that number come from.

**Why:** I was auditing drafts against the rule list, which catches em dashes and banned phrases
and catches none of the above. A checklist pass is not a comprehension pass.

**How to apply:**
- Before delivering any instructional draft, read it once as a person executing it, in order,
  with no prior knowledge. Every noun must be introduced before it is used, and every step must
  be executable at the moment it appears.
- Ask of every number in a draft: would a reader know what this means and where it came from.
- Check the whole draft against its own final line. That is where contradictions hide.
- Auto-numbering in her editor renumbers steps as 1/1/1. Always restore 1/2/3 without being asked.

Related: [[lior-post-claude-to-codex-migration]], [[feedback-never-revert-to-my-earlier-draft]].
