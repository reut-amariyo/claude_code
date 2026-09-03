# Lior LinkedIn

The LinkedIn operating system for Lior Pozin's personal brand, packaged so it runs anywhere.

**It never publishes anything.** Every skill produces a draft. Reut posts manually.

## What it gives you

| Skill | Use it when |
|---|---|
| **linkedin-daily** | Every morning. Scans the references, finds today's outliers, drafts ONE post |
| **linkedin-post** | Drafting a post. Save-first by default, 3 save-first to 1 personal |
| **linkedin-prepublish** | Before anything ships. Mandatory gate, outputs a ✅/❌ table and a verdict |
| **linkedin-comments** | Daily. Scans the target list, picks 5 fresh posts, drafts 3 comment options each |
| **linkedin-benchmark** | Before recommending anyone as a model. Measures the account instead of describing it |
| **linkedin-followers** | Monthly reporting against the follower KPI |

## The three decisions baked in

1. **The KPI is net new followers per month**, not impressions. Impressions moved 6x across
   four months while followers never left a 922-1,100 band.
2. **The main axis is save-first content**, 3 save-first to 1 personal. A save is a bet on
   future utility, so every save-first post carries a concrete enumerable artifact.
3. **Model accounts on engine efficiency, never follower count.** Scale inverted in our
   sample: the three biggest accounts ran the three weakest engines.

## What it needs

- **A logged-in LinkedIn session in a controllable browser** for `linkedin-comments` and
  `linkedin-benchmark`. Without it both degrade gracefully: paste the posts and they still work.
- **A writable workspace folder** for comment drafts and the dedup log.

## What did NOT come across

The daily 08:05 scheduled run is a Claude Code scheduled task and plugins have no scheduling
component. Re-create the schedules in the host app and point them at `linkedin-daily` and `linkedin-comments`.

## Reference material

Everything in `references/` travels with the plugin: voice and anti-AI rules, brand
non-negotiables, the KPI model, the save-first spec, the measured creator benchmark, and the
two target lists. Update `references/targets.md` to change who gets scanned.
