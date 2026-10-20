---
name: Lior Story - The $1 Bug That Almost Killed AutoDS
description: Foundational founder story. Early-days AutoDS production incident where Lior's code change repriced every product in every connected store to $1. Use for posts on production failures, founder accountability, transparency, customer trust, leadership under crisis.
type: project
originSessionId: 089726e4-d449-4241-96b0-412a0c43f612
modified: 2026-09-24T14:05:42.376Z
---
# The $1 Bug Story

## When
Very early days of AutoDS. Lior and co-founders were doing everything themselves - he describes it as: "As CEO I was doing customer service, coding, marketing, then talking to the accountant. Slowly we started closing gaps. When budget allowed we hired a developer, then a marketing manager."

## What happened
- Root cause, his own words (Hebrew podcast "99 Is Not 100", 2026-09): he was doing everything alone (code, accountant, legal, marketing) and ran a self-test that set ONE product to $1. The software repriced EVERY product in the system to $1: tens of thousands of items averaging $40-50.
- Hundreds of products sold within a few hours
- Around 3:00 AM ("a normal working hour for me") a customer messaged: she woke up to a flood of sale notifications. He replied "congratulations, what do you want from me?" She said the products sold for $1, 30-something sales. "Shit, I'm in trouble."
- Older telling said "dozens of orders in the past hour"; his 2026-09 numbers (hundreds of products system-wide, 30-something for her) win

## The eBay risk
On eBay, mass-cancelling orders gets the seller's account banned, which would have killed the customer's entire business. The stakes were existential for the customers, not just embarrassing for AutoDS.

## How Lior responded
1. Talked the panicked customer through it personally at 3 AM
2. Helped her craft honest messages to her buyers so eBay would not block her account
3. Admitted it was AutoDS's mistake; did not blame eBay ("I didn't say oh, it's not us, oh, it's eBay")
4. Offered her compensation coupons (older telling)
5. Next day: went live on Facebook to ALL AutoDS customers, apologized, explained exactly what happened and what would prevent it

## The outcome
- Nobody left. Those customers became the best ones; whoever still has a business is still with AutoDS
- A competitor then offered 20% to anyone who brought AutoDS customers over. Nobody moved
- The customer who caught the bug was an Israeli who had moved to Finland and could not find work there; he had "wrecked her business", so he hired her with no money: $200/month, then $400, rising with the company. Over time she became Head of Customer Support with ~100 people under her
- Guardrail: on tape he says "not options, not a percentage". The no-equity rule for drafts still applies: never write that line in Lior content

## Why this story matters for posts
- Real production incident the founder caused himself - rare vulnerability
- Specific time stamp (3 AM), specific number ($1), specific platform risk (eBay ban)
- Transparency-as-leadership response (live Facebook same day)
- The customer-to-employee arc is unusually strong
- Pairs naturally with any current AI-agent / production-failure / SaaS incident in the news (e.g., PocketOS April 30 2026 viral story)

## How to apply
- Lead with the 3 AM scene, not with the lesson
- Keep "$1" and "3 AM" verbatim - they are the specific anchors; the 3 AM "congratulations" misread is the freshest beat, lead with it
- Close on "nobody moved" (the 20% poach offer) rather than on the lesson
- 🔴 The 20% offer targeted CUSTOMERS, never employees. Never use it as a team-loyalty/culture proof (Reut corrected this 2026-09-24). For employee-growth proof use the $200/month hire → Head of Support arc
- Don't overclaim. Lior caused this. The post works because he owns it.
- Open ending should ask what the reader would do in the next 6 hours, not state the lesson
