# 06 · Video prompting (Seedance via Higgsfield)

Write complete, directed prompts. A complete prompt is not a long prompt: it is one where every element a camera would record has been decided, with nothing left to the model's average.

**Provenance.** Model rules below were gathered in November 2026 from third-party summaries of ByteDance's Seedance 2.0/2.5 guides, the Higgsfield blog, and other prompting guides. They have not been verified against the live tool. Before the first spend of a session, read the tool's current schema and the provider's guide, reconcile differences, and record them in the scene file.

## Core principles

1. **The start frame carries appearance. The prompt carries change.** With a first frame or image reference, do not re-describe what it shows. Describe what moves, in what order, how fast, and what stays fixed. Repeating the image invites conflict.
2. **One camera move per shot. Few beats.** Roughly three physical beats per five seconds, one hero action. Earlier tests failed when one eight-second turn tried to carry a snow touch, a crumble, a head lift, parallax and a frame match.
3. **Physical verbs, with contact.** Say what touches what, where weight lands, what deforms and what is left behind. Secondary motion (cuff swings, flakes skim, steam curls) makes realism.
4. **Name fixed references.** Tell the model what must not move or change: the railing, the tower spacing, the horizon, exposure.
5. **Layer the world's motion.** Foreground, midground and background move at different rates. Give each layer one clause.
6. **Sound is a separate paragraph** written as audio, not as picture.
7. **Positive wording.** Seedance has no negative prompt field. Say what you want. Negative phrases are only reliable for subtitles and audio (for example "No subtitles", "No BGM; only ambient and action sounds").
8. **Length.** Under about 1,000 English words (or 500 Chinese characters) per documented limits, but aim for 150–350 words. More words rarely add control.

## Skeleton

For one continuous shot:

```
[Format line] One continuous 9:16 shot, 6 seconds, no cuts, no zoom.
[Role of inputs] Image 1 is the first frame and sets place, light and palette. (Add Image 2 etc. with one job each.)
[Summary] One sentence: what the viewer sees happen.
[Beats]
0–2s: [camera, framing] [what moves in foreground] [one contact or action]
2–4s: [camera move: start→path→end] [what the camera reveals] [layer motion]
4–6s: [hold or end beat] [what stays fixed] [last change]
[Fixed] Things that do not change: ___.
[Light and texture continuity] Source stays fixed in the world, grain, exposure steady.
[Sound] Ambient bed; close sounds with timing; where silence falls. (Use the tool's audio syntax.)
```

Use second ranges only if the model accepts them (documented for Seedance 2.5 with integer seconds, continuous ranges, no gaps). On Seedance 2.0 use "Shot 1 / Shot 2" instead and avoid timestamps. Test both formats once and record which the tool obeys.

## Multi-shot

- Prefer a single continuous take for POV or witness scenes. Cuts break presence.
- For a cut sequence, write Shot 1, Shot 2, Shot 3. Each has one action and one camera instruction. State the transition (hard cut, match cut on motion). Keep total under 15 seconds at first.
- Reuse the same reference image and repeat key appearance descriptors in every shot for continuity.
- Escalation arcs such as calm → pressure → change → aftermath give shape. Use only what the idea needs.

## Referencing inputs

- Number references by type: Image 1, Video 1, Audio 1 (an `@` prefix is common). State one job for each: first frame, end frame, look reference, camera-move reference, sound reference.
- Bind a recurring subject once: "The person in Image 2 is Subject 1." Then refer to Subject 1.
- If a reference video demonstrates the motion, point to it and leave that motion out of the text.
- If the reference contains text or logos you do not want, remove them first.
- Real-person faces in references are restricted by the tool. Use generated or authorized characters.

## Realism phrasing

- Camera: `eye-height handheld with natural breathing`, `locked off on a tripod`, `slow lateral track at walking pace`. For POV: `head dips slightly at each footfall, gaze lags the body, one glove edge visible at lower right`.
- Motion speed: `real time`, `slowly`, `gust arrives from the left and fades in two seconds`. Avoid unspecific "smooth".
- Light: `fixed tungsten lamp behind camera-right, world-fixed, brightness steady`.
- Atmosphere layers: `close soft flakes out of focus, mid flakes sharp, low spindrift sliding across the promenade in uneven gusts`.
- Materials in motion: `snow crust cracks around the boot and a small ridge of powder spills over the track edge`.
- Protection against typical drift: `railing geometry and tower spacing remain stable`, `no change in exposure`, `no cuts`, `no on-screen text`.

## Examples (untested proposals)

**A. Rework of the Bund walk, shorter and more physical.**
```
One continuous 9:16 shot, 6 seconds, handheld at eye height, no cuts, no zoom, no on-screen text.
Image 1 is the first frame and defines the place, storm and light.
A pedestrian walks the buried Bund promenade and lifts their gaze to the far bank.
0–2s: Boots break through the crust of an old track, the rim collapses inward and a small ridge of powder spills over. The camera dips slightly with each step. A charcoal glove edge swings at lower right.
2–4s: The head lifts and turns left in one motion while the body keeps walking. The post at left exits quickly while the wave-pattern rail stays continuous at the edge of the drift.
4–6s: The walker slows. The Oriental Pearl and towers settle at their original spacing across open water. Pale snow caps on far-bank roofs become readable. Hold.
Fixed: the rail pattern, tower spacing, dark horizon, steady exposure. One tungsten lamp behind camera-right, world-fixed.
Sound: close crunch with each step for the first two seconds, fabric brush, then wind over river wash and a low city bed as steps stop.
```

**B. Static witness with world motion.**
```
One locked-off 9:16 shot, 8 seconds, 28mm eye-height view, no cuts.
Image 1 is the first frame.
The camera does not move. In the foreground, snow lifts from the drift crest in a gust from the left and slides across the frame. In the midground, a lantern's amber halo flickers once and recovers. Far-bank roofs fade in and out behind veils of blowing snow, never changing shape.
Sound: wind builds over four seconds and falls to a distant river hush.
```

**C. Cut sequence, 3 shots (proposal template).**
```
Shot 1: Medium close-up, locked off. [action]. Transition: hard cut on the contact.
Shot 2: Wide, slow lateral track. [action]. Transition: match cut on the same motion direction.
Shot 3: Close detail, locked off. [last change]. Hold two seconds.
```

## Audio syntax

Tool-specific. Commonly documented patterns: music in parentheses, effects in angle brackets, dialogue in double quotes or braces, one language per line. Generated audio is likely mono. Plan to rebuild final sound in post if it matters. Verify the tool's syntax before relying on it.

## Settings policy

- **Two tiers.** Tests run at 480p to save credits. Finals run at 720p or 1080p once a direction is chosen and the test passes the promotion gate in [09](09-douyin-and-resolution-tiers.md). Judge motion, contact, geometry and hook from the 480p test. Judge texture, small landmarks and finish only on the still and the final. Reuse the same still, prompt and references for the final so only resolution changes.
- Check the first frame of every take against the prompt (named objects, colors, light) before judging anything else. Past takes lost the boot color, glove and lamp spec.
- Request 3–4 takes of a test inside one approved cap, vary only the variable under test, and review all.
- Record the requested settings and what the tool echoed back. If they differ, say so.
- Provider-managed seeds mean takes cannot be reproduced. Keep selected files.

## Failure codes and repair ladder

| Code | Symptom | First fix |
| --- | --- | --- |
| F1 | Subject drifts or morphs | Repair the still, shorten the shot, reduce motion, reference the same image again |
| F2 | Camera cuts or zooms against instruction | Add "one continuous shot, no cuts, no zoom"; state a single move; shorten |
| F3 | Scene settles into the reference like a dissolve | Use the image as a look or first-frame reference, not end frame; give the end an independent beat |
| F4 | Motion too small or too fast | State speed and distance; name the fixed reference that proves movement |
| F5 | Layers move as one | Give each layer a separate clause with a different rate |
| F6 | Contact has no weight | Specify deformation, spill and residual trace; test the contact alone |
| F7 | Lighting pulses or shifts | State world-fixed source and steady exposure; remove competing sources |
| F8 | Gibberish text or wrong landmark | Fix in the still or composite in post |
| F9 | Unwanted subtitles or music | Add the documented audio and text constraint |
| F10 | Ignores a beat | Reduce beat count; move that beat to a second test |
| F11 | Repeated elements form a regular grid (lit windows, lamps, flakes) | Ask for irregular brightness, colour temperature and spacing; light only some floors (School That Never Lets Out v01–v02) |
| F12 | A named object changes or moves between beats (the same lamp, a lantern) | Name it once with position and brightness, and state that it stays the same object in the same place throughout (School v03, Shanghai take 07) |
| F13 | A camera move reads as the wrong direction (a lateral track feels sideways, not forward) | Prefer a walking POV with a head turn that reveals the view; keep a near fixture passing to prove the move (Shanghai take 06 vs take 07) |

Ladder: fix the still, then simplify the motion, then strengthen references, then change the camera idea. After three failed rerolls of the same prompt, re-plan the shot. Do not keep rerolling.
