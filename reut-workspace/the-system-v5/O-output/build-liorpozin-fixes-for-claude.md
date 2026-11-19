# build.liorpozin.com: QA fixes, 33 items

**Instructions for Claude:** implement these fixes on build.liorpozin.com. Work through them in order, one item at a time. After each one, report the item number and what changed. If an item can't be done as written, stop and explain why before moving on. Don't skip items silently.

**Site map:**
- `/` home: "I want to build" with 3 cards
- Store card → buildyourstore.ai landing page
- Business card → `/business` quiz → Lior AI
- AI Influencer card → `/ai-influencer` quiz → Avatar Factory trial

**Rule for every item:** keep the user in the question flow. Question → answer → next question. Feedback for an answer shows inline on the same screen, or as an overlay that advances by itself. Never add a separate screen that needs a "Next" or "I'm in" click.

---

## A. Home page `/`

1. Make the chooser read like one sentence. "I want to build …" opens straight into the 3 options, like a sentence completing, with nothing in between.
2. Replace the 3 card images with images that explain each option: a store, a business, an AI influencer. Use less of Lior on this screen.
3. Fix the stats counters. "$92M" counts up much faster than the others, and the rest barely move, so sync the timing. If the stats strip stays, frame it as credibility for who Lior is. Otherwise remove it.

## B. Store path, Build Your Store landing page

4. Leave a video slot in the hero. A landing-page video will be filmed this Thursday. No other changes.

## C. Business path `/business` → Lior AI

### Welcome screen

5. Reposition Lior in the intro. Lead with Lior as an investor and startup advisor who helped many founders at the start of their journey build, scale and exit. "Helped people generate $1B on my platforms" moves down to supporting proof.
6. Fix the example dashboard graph. It shows a "2023" label and "Last 10 years". Make the dates current or remove them, and make it clear what the graph shows.
7. Rewrite the 2 testimonials.
   - They share the same structure and headline pattern, including "former …", so they look templated. Make them different from each other.
   - "I did not invent anything" reads as "I did nothing and got rich", which isn't believable.
   - New angle: "I couldn't get my business off the ground for a long time. Advisors were too expensive. I talked to Lior, and my business grew X times in Y months."
   - Keep the revenue and days numbers.
   - Keep the disclaimer that results came from their own work.

### Quiz questions

8. Remove Lior's photos from the quiz screens.
9. Remove the helper line under each question, for example "Pick the closest one, you can change it later". If it has to exist, move it below the answers in small text.
10. Remove the square brackets `[ ]` from every question. Example: "Why do you want to start a [ business ]?"
11. Remove the "Start with one client" screen that appears after the agency answer. Go straight to the next question.
12. Show the time-commitment feedback inline. "Your plan will fit under 5 hours a week. You don't have to quit. You said you want more time with your family" appears on the same screen when the answer is clicked, not as a new screen.
13. **Bug:** after the Q5 "fear" answer, an unrelated idea card pops up with no way to close it: "Startup 005 … Home upgrades for rentals, no drill needed". Remove it.
14. The "someone who said the same thing" quote after the fear answer isn't empathetic enough. Rewrite it so it speaks to the fear, and show it inline, not as a separate screen. Otherwise remove it.
15. Remove the repeated testimonial screen after "build alone". It repeats Mark's review and the same graph. If it stays, show it as a popup in the same window, with no extra click.
16. Replace the 1-5 scale questions with two buttons, **That's me** and **Not me**.
    - Reference: https://nickjayala.com/assessment. Copy how it works, not its text.
    - One statement per screen, two buttons, and a small Back link.
    - A progress counter, for example "01 / 24".
    - Tapping an answer advances automatically. No Next button and no helper text.

### Results / plan screen

17. Make the loading or "calculating" moment a bit shorter.
18. Cut the summary of the user's answers. Keep only "Your next steps".
19. Label every milestone on the timeline graph. Today it shows only "You start" and "Launch day". Add every step as a labeled point, including test and build your first offer.
20. Promo code: replace the code that shows immediately with a "Claim your promo code" button that reveals it in a popup. *Lior's call: if you'd rather keep the code shown directly, skip this item.*
21. The "Get my plan" button appears twice. Keep one large primary button at the bottom, and fix the bottom one, which is cut off.

### Messaging across the whole Business path

22. Add Lior's origin story at every stage, one short line per stage: in the intro, between questions and on the results screen. He started from zero, with no entrepreneurial knowledge, no connections, no money and no one to advise him. He built and exited, and now he teaches others from his mistakes so they can get where he is.

## D. AI Influencer path `/ai-influencer` → Avatar Factory

23. Move the helper text "Every niche comes with trending reels and copy" below the choices, so the question is followed immediately by the choices. Cut text overall.
24. Restructure each niche card: niche title on top, then the image, then one line on how this niche makes money.
    - "Money & Wealth: e-books and courses sell here" is a good example.
    - "Wisdom & Spirituality: short lessons, loyal followers" doesn't say how it earns. Rewrite it.
    - Apply the same check to every niche.
25. The Travel & Luxury card image looks different from the others, and the 5-card grid looks off. Make all the cards consistent and fix the 5-card layout.
26. Rewrite the Travel confirmation line "Everyone wants the trip. You can film it." Anyone can film a trip. Say how this niche earns instead.
27. Remove the screen after the face answer. It says "Your face never has to be in it" right after the user chose to show their face. Make it inline or remove it.
28. The "Join … people who …" screen shows for 2-3 seconds, then continues by itself. Remove the "I'm in" button.
29. On the $2 screen, add the Shopify logo and the Avatar Factory logo next to where their names already appear.
30. Strengthen the $2 payment screen. It's the most important screen, because this is where people drop off. Add a visual of the user's own generated character, or something equally visual, that makes them want to continue and pay.
31. Move the "Building your influencer" screen to before the $2 request.
32. **Bug:** the influencer video plays the voice only. The talking video isn't visible.
33. **Bug:** the quiz asks for $2, then the checkout charges $1. Make one price show from start to finish.
