---
name: project-lior-us-senior-connect-batch
description: "US senior connect list for Lior's LinkedIn - Reut added batch 1 on 2026-10-25, the rest wait for her next \"find US CEOs/investors\" request"
metadata:
  node_type: memory
  type: project
  originSessionId: e352c271-8cfe-49d9-aff4-a04f591c568b
  modified: 2026-11-07T14:27:13.273Z
---

On 2026-10-25 I found US 2nd-degree CEOs, founders, investors and C-suite with the most mutuals on Lior's account. List: `reut-workspace/the-system-v5/O-output/linkedin-networking/us-senior-connect-targets-2026-10-25.md`.

Reut added the first 16 from the chat table, Micha Breakstone through Itai Sadan, then hit LinkedIn's invite limit.

**Still to add**, in this order: Joseph Riviello, Brian V Anderson, Zvika Netter, Zane Lackey, John Frankel, then everything from Tier 2 on in the file except Zane Lackey and John Frankel, who are listed above. Joseph Riviello was in the file but not in the chat table, so he was skipped.

**Batch 2, 2026-10-30:** Reut asked for US CEOs only, 100+ mutuals, who posted in the last month. List: `reut-workspace/the-system-v5/O-output/linkedin-networking/us-ceo-connect-targets-2026-10-30.md`, 34 active CEOs, Ido Geffen 720 down to Dov Ben-Shimon 100. Searching for Israeli founders in the US gives by far the most mutuals. Next time, ask which of the 34 she added and skip them. Method that works: fetch() the search HTML and regex-parse it; the activity page HTML dates posts as "Oct 26" or "3d". Iframes froze the tab.

**Batch 3, 2026-11-05:** founders, CEOs and tech C-level, US, 100+ mutuals, batches 1 and 2 removed. 53 names, Amiram Shachar 878 down to Michael Diesu 100. File: `.../linkedin-networking/us-founder-ceo-connect-targets-2026-11-05.md`. Activity NOT verified because the Chrome extension dropped mid-check. Next time, verify activity first, then ask which ones she added. Learned: the search HTML is an RSC payload, so parse body.textContent by splitting on "• 2nd". JS output with "?" or "=" gets blocked, and long output gets truncated, so write results into a `<pre>` and read them with get_page_text. The /recent-activity/shares/ HTML has no timestamps; use /recent-activity/all/.

**Email-gated profiles:** some people only accept invites from someone who knows their email. Aviv Cohen (avivco) is one, removed 2026-11-07. Never put him in a future batch. Add any others Reut reports here.

**Why:** LinkedIn caps how many invites she can send each week, so the list is worked in batches.

**How to apply:** when Reut asks again for US senior connections for Lior, start by giving her the remaining names from the file. Then run a fresh search that skips anyone she already added, and update this memory with the new progress. Related: [[project-foundera-linkedin-agency]].
