# QA fixes: build.liorpozin.com, 2026-11-16

Source: Reut's voice QA, New Recording 28, transcribed and organized.
Site: https://build.liorpozin.com, one link that routes to 3 products:

- Store card → buildyourstore.ai landing page
- Business card → `/business` quiz → Lior AI
- AI Influencer card → `/ai-influencer` quiz → Avatar Factory, $2 trial

## Global principle, applies to every fix below

**Keep the user in the question flow.** Every interstitial screen that needs an extra click breaks momentum. Default rule: question → answer → next question. Feedback for an answer shows inline on the same screen or as an auto-advancing overlay, never as a separate screen with a "Next" or "I'm in" button.

Items marked ⚠️ were unclear in the recording. Confirm them with Reut before you implement.

---

## A. Home page, `/`

1. **Make the chooser feel like one sentence.** The headline reads "I want to build …". The 3 options then open from it, like a sentence completing, so the user goes straight from "I want to build" to the 3 choices with nothing in between.
2. **Replace the 3 card images.** The current images don't relate to the options. Use images that explain each option: a store, a business, an AI influencer. Use less Lior on this screen.
3. **Fix the stats counters.** The count-up animation is uneven: "$92M" races up much faster than the others, and the rest barely move. Sync the animation timing. Also reconsider whether the strip belongs here at all, because it doesn't strengthen the urge to pick an option. If it stays, frame it as "who Lior is" credibility, not as a decoration.

## B. Store path, Build Your Store landing page

4. **No copy changes requested.** Planned: a landing-page video, filmed at the villa on Thursday. Leave a video slot in the hero. No code change until the video exists.

## C. Business path, `/business` → Lior AI

### Welcome screen

5. **Reposition Lior in the intro.** Lead with Lior as an **investor and startup advisor** who helped many founders at the start of their journey build, scale and exit. "Helped people generate $1B on my platforms" moves down to supporting proof.
6. **Fix the example dashboard graph.** It shows a "2023" label and "Last 10 years", which look stale and unclear. Make the dates current or remove them, and make it clear what the graph shows.
7. **Rewrite the 2 testimonials.**
   - Both cards share the same structure and headline pattern, including "former …", so they look templated. Vary them.
   - Mark H.'s quote "I did not invent anything" reads as "I did nothing and got rich" and isn't believable.
   - New angle: "I couldn't get my business off the ground for a long time. Advisors were too expensive. I talked to Lior, and my business grew X times in Y months."
   - Keep the numbers. Reut says the revenue and days figures work well.
   - ⚠️ Compliance: these are illustrative members. Keep the existing "results came from their own work" disclaimer.

### Quiz questions

8. **Remove Lior's photos from the quiz screens.**
9. **Remove the helper line under each question**, for example "Pick the closest one, you can change it later". It breaks read-question → pick-answer. If it must exist, move it below the answers in small text.
10. **Remove the square brackets `[ ]` from every question.** Example: "Why do you want to start a [ business ]?" The brackets are part of the brand language, but they don't belong in the questions.
11. **Remove the screen that appears after one answer.** After choosing the agency option, a "Start with one client" screen appears with no further questions, and it's confusing. Go straight to the next question.
12. **Make the time-commitment feedback inline.** After "how much time can you give this", the separate screen "Your plan will fit under 5 hours a week. You don't have to quit. You said you want more time with your family" becomes inline feedback on the same screen, shown right when the answer is clicked. No new screen.
13. **Bug: a random idea card pops up after the Q5 "fear" answer.** "Startup 005, Product …, Home upgrades for rentals, no drill needed" appears out of context, with no way to close it. It looks like a mistake, so remove it.
14. **Rewrite or remove the "someone who said the same thing" quote** after the fear answer. "Failing once made me stop, having a plan to follow made me start again" isn't empathetic enough for a fear answer. If a quote stays, it has to hit the heart. Better still, fold it inline per item 12, with no separate screen.
15. **Remove the repeated testimonial screen after "build alone".** It repeats Mark's review and the same graph already shown. If it stays, show it as a popup in the same window, with no extra click.
16. **Change the 1-5 scale questions to binary.** Use "That's me" / "Not me" instead of "Do you relate to this?" on 1-5. A 1-5 scale is harder to answer.
    - Reference: https://nickjayala.com/assessment, Nick Ayala's "The Come Up" bottleneck quiz. Copy the *mechanics*, not the content:
      - One statement per screen, two buttons only: **That's me** / **Not me**, plus a small Back link.
      - A progress counter, for example "01 / 24", so a long list still feels fast.
      - A tap auto-advances to the next statement. No Next button, no helper text.
      - It closes with one "Which one hits hardest?" pick, then a short result: your one thing, what it costs you, your next step.
      - Results screen: one named result, then one primary offer, plus a cheaper "start smaller" option. This also supports item 18, cutting the answer recap.

### Results / plan screen

17. **Shorten the loading or "calculating" moment.** Make it a bit faster.
18. **Cut the answer summary.** The user doesn't need a recap of what they chose. Keep **"Your next steps"**, which Reut says is great, and remove the rest of the text.
19. **Label every milestone on the timeline graph.** It only shows "You start" and "Launch day", but the steps include test, build your first offer and others. Put every step on the graph as labeled points.
20. **Add a claim step to the promo code.** It appears immediately. Consider a "Claim your promo code" button that reveals it in a popup. ⚠️ Decision for Lior / Reut: claim click or shown directly.
21. **Fix the duplicate "Get my plan" button.** It appears twice. Keep one large primary button at the bottom. The bottom one is currently cut off, so fix that layout.

### Messaging across the whole Business path

22. **Weave Lior's origin story in at every stage.** This is the biggest missing piece. Lior started from zero: no entrepreneurial knowledge, no connections, no money, no one to help him, no advisor. He still built and exited, and now he teaches others from his mistakes and lessons so they can get where he is. Add one short line of this per stage, in the intro, between questions and on the results screen, not one long block.

## D. AI Influencer path, `/ai-influencer` → Avatar Factory

23. **Move or remove the helper text under the niche question.** "Every niche comes with trending reels and copy" sits between the question and the choices. Move it to the bottom so the question is followed immediately by the choices. Cut text overall.
24. **Restructure the niche cards and make every subline about money.** Layout per card: niche title on top, for example "Money & Wealth", then an image, then a monetization line under it.
    - The bottom line must say **how this niche earns**. "Money & Wealth: e-books and courses sell here" works.
    - "Wisdom & Spirituality: short lessons, loyal followers" doesn't say what the user gains. Rewrite it as a revenue line.
    - Apply the same check to every niche.
25. **Fix the Travel & Luxury card design.** Its image looks different from the others, and with 5 cards the grid looks off. Make the cards consistent and fix the 5-item layout.
26. **Rewrite the Travel confirmation line.** "Everyone wants the trip. You can film it." doesn't land, because anyone can film a trip. Say why this niche is valuable or how it earns.
27. **Remove the screen after the face answer.** After "I want to show my face", a separate screen says "Your face never has to be in it". It contradicts the answer and breaks the flow. Make it inline or remove it.
28. **Auto-advance the "Join … people who …" screen.** Show it for about 2-3 seconds, then continue automatically. Remove the "I'm in" button.
29. **Add the Shopify logo and the Avatar Factory logo** on the $2 screen, where the text already names Avatar Factory and Shopify. Show the logos next to those names. Confirmed by Reut.
30. **Strengthen the $2 paywall screen.** This is the most important screen, because users abandon here when asked for money. Add a visual of *their* generated character, or something equally visual, that drives the urge to continue and pay.
31. **Reorder: show the "Building your influencer" screen before the $2 request**, not after.
32. **Bug: the influencer video plays with audio only.** Pressing play gives the voice, but the talking video isn't visible.
33. **Bug: the price changes mid-flow.** The quiz asks for $2, then the Avatar Factory checkout charges $1. Reut confirmed this is a bug, not a pricing decision. Owner: Lior. Find where the quiz price and the checkout price disagree, and make one price show end to end.

---

## Open questions for Reut before implementing

- Item 20: promo code shown directly, or behind a claim click?
