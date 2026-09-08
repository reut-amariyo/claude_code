# Prompt receipt — V-twin engine visualization for the Claude→Codex post
Built 2026-09-07. For the post in linkedin-claude-to-codex-FINAL-2026-09-07.md

## Reference
Dilum Sanjaya, 2026-09-05: "Asked GPT-6 Astra to create a highly detailed, interactive
visualization of a V8 engine." 2.9M views, 12K likes, 5.1K bookmarks, 960 reposts, 234 replies.
52-second clip. https://x.com/DilumSanjaya/status/2096280244663775423

The format is not a video model. Astra writes an interactive web page and the creator screen-records
himself using it. The recording is the video.

## Why a motorcycle engine and not a V8
A bike is the one machine where everybody already knows you can change the engine and keep the bike.
That is the post's thesis in an object. The swap sequence is the part that ties the visual to the
text; without it this is a nice engine animation with no connection to anything.

## Caption to run with it
"The frame is yours. The engine is a supplier."

## The prompt, as sent to Reut 2026-09-07

Build a single self-contained HTML file. No external assets, no CDN links, everything inline
including the 3D library. It will be screen-recorded for a social video, so design it to look good
in a 4:5 vertical crop: keep the subject centred, leave headroom, dark background, no UI chrome
around the edges.

A highly detailed, interactive 3D visualization of a four-stroke V-twin motorcycle engine.

Geometry, modelled accurately and to scale relative to each other:
crankcase, crankshaft, two connecting rods, two pistons with rings and wrist pins, two cylinder
barrels with cooling fins, two cylinder heads, intake and exhaust valves with springs and rockers,
camshaft, timing chain and tensioner, spark plugs, throttle bodies, clutch basket, and a five-speed
gearbox with visible gear pairs.

Materials: brushed aluminium cases, dark anodised barrels, steel internals, copper wiring. Studio
three-point lighting, near-black background, soft contact shadow. Cinematic, not clinical.

Interaction:
- Orbit, pan and zoom with the mouse.
- An explode slider that pulls every component out along its assembly axis into a floating exploded
  view, and reassembles smoothly.
- Click any component to isolate it: everything else drops to 15 percent opacity and a small label
  appears with the part name and one sentence on what it does.
- A cutaway toggle that slices the near cylinder lengthways so the piston, valves and combustion
  chamber are visible.
- An RPM slider from idle to redline driving the animation speed. Pistons, crank, cam, valves and
  timing chain stay mechanically in sync at every speed.
- A four-stroke mode that slows to a single cycle and labels each phase as it happens: intake,
  compression, power, exhaust.

Then the engine swap.

Put the engine inside a minimal motorcycle frame drawn as thin tubes only, no bodywork. The frame,
the wiring loom and the gearbox linkage are clearly one system, visually separate from the engine.

Add a button labelled "swap engine". Pressing it unbolts the V-twin at its four mounting points,
lifts it out and sets it down to the left still running, then lowers an inline-four into the same
frame, bolts it to the same four points, and reconnects the same loom and the same linkage. Nothing
about the frame changes. Both engines end up running, one in the bike and one on the floor.

The mechanics must be correct, not decorative. Valve timing follows the piston. The V-twin fires at
the correct interval. Get the kinematics right before you make it pretty.

## Capture
Cmd+Shift+5, Record Selected Portion, box around the render area only, 40-50 seconds.
Beat order: orbit once, explode and reassemble, cutaway, RPM to redline, swap. End on both running.

## Export
ffmpeg -i engine.mov -vf "scale=1080:-2,crop=1080:1350" -c:v libx264 -crf 20 -pix_fmt yuv420p -an engine-linkedin.mp4

## The risk, from the reference post's own comments
Dilum's V8 won on mechanical correctness. His replies are engineers checking valve timing. If the
swap lands on an engine that runs wrong, that is the only thing the comments will discuss.
