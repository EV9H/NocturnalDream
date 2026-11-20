# The Beacon Engines — reviews

Observations, unverified settings and creative judgment are kept separate.

## Pre-generation review of prompts v01 (2026-11-19)

Checked against chapters 01, 04, 05, 06 (F11–F15), 09 and 11, and Shanghai takes 08–09.

### Checked and passing
- **Ban list (ch. 01):** no banned words or feelings written as instructions in either prompt.
- **One-second test:** frame 1 contains the Wall (steps, crenellated parapet, watchtower) and the engine together. To be confirmed on the stills.
- **Scale cues (ch. 04, 11):** the watchtower and the porter sit in front of the engine, and there are guards on its galleries. Known-size objects in the same view.
- **System, not decoration (ch. 11):** every machine part has a job: flume → wheel → shaft → gears → ring. Soot, spill, stumps and firewood show the cost. No neon, no glowing circuits, Ming only.
- **F14:** no feet, legs or boots in the video prompt. Walking is shown by bob, sway, the parapet passing and footstep sound.
- **F15:** no gust and no fog over the Wall. Mist is kept low in the valleys and cloud only at the crown.
- **F11:** lanterns unequal; far engines fire after uneven pauses.
- **F12:** the near engine, ring and flame are named as persistent objects in fixed places.
- **Change only (ch. 06):** the video prompt describes motion and new light. Only the composition anchors are restated.
- **Audio:** separate paragraph, "No music, no speech", mid-frequency hero sounds (bell, gong, fire) for phone speakers.

### Fixed during review
- Jinshanling is **northeast** of Beijing (Luanping, Hebei), not north. Corrected in both still prompts and in the saved canvas nodes.
- Handoff beat 3 ("arrival at its foot") replaced with a stop and a ten-degree gaze lift. A 14 s climb covers about 15–20 m, not a kilometre, and a steep tilt invites drift (reasoning in PRODUCTION.md).

### Open risks (judgment)
- **Video prompt length:** about 470 words, above the 150–350 aim in ch. 06 but inside the 1,000-word limit. Kept because 30 s carries five beats. If the take ignores beats (F10), cut the fixed list first.
- **Two camera moves** (the climb, then the gaze lift and return). This breaks "one move per shot". The lift is small. If it drifts, the fallback is to remove 13–18 s and keep the gaze level.
- **Image model may produce a pagoda, not a machine.** Look for: a visible wheel, gears and ring; storey count; Ming brick on the base, not Qing glazed tile.
- **Ming detail check still to do on the stills:** step width and wear, square loopholes in the outer parapet, the arched windows of the watchtower. To verify against real Jinshanling photos.
- **30 s drift:** far-engine order and the porter's identity are the most likely to change. Review at 0.5 s intervals.
- **History claims unverified** against primary texts (成化二年 code). Keep them out of the post until checked.

### Unverified
- Whether Seedance 2.5 obeys 30 s timestamp beats (only 8 s takes tested so far, Shanghai 09).
- Whether Seedream 5.5 is free on this plan. The live quote on 2026-11-19 was **6 credits per image** at 2K, against the handoff's note that it is unlimited.

## Keyframe A1 — Seedream 5.5, prompt v01 (2026-11-19)

- **Submitted (verified from the CLI).** Canvas `3048a899-cd42-490d-94b8-73f6e33fff8d`, node `node_vb9hnx2ce5`, submit `cd4c3f8b-45b7-465b-8edc-ed9ed68a575f`. Model `seedream_5.5`, t2i, 16:9, 2K, one output. Quote 6 credits. The owner said up to three images were free and said to try. **Charged 6 credits**: the balance went from 12,420 to 12,414, taken from the batch expiring 2026-11-19. So it was not free. The other five nodes were not run.
- **File.** [01 A1](Renders/01-Seedream-5.5-Keyframe-v01-A1.png), resource `06e1b802-eed2-4de3-977f-4364c30df1a7`, 2560 × 1440 PNG, SHA-256 `cec44ddc…0369028`.

### Observed
- Left half: worn grey brick steps climbing the ridge, crenellated parapet on the left, low parapet on the right, the porter with two firewood bundles on a shoulder pole, back to camera, about a third of the way up. A watchtower on the crest with arched windows. The Wall continues along the crest beyond it.
- Right half: the engine stands on the slope **beside** the Wall, close to camera, not on the summit ahead. Brick base with an arched gate and crenellations, a water wheel at the base fed by a trestle flume, a waterfall from the base, stumps and stacked logs, about seven timber pagoda storeys with galleries and guards, large wooden gears on the face, two warm lanterns.
- The top is a closed, riveted, rust-brown metal cylinder. It reads as an iron water tank, not a bronze ring around a fire bowl.
- Guards on the galleries are human-sized relative to the storeys. By that and by the watchtower, the engine reads as roughly 60–100 m, not 400 m.
- Two more engines on ridges to the right, smaller, in valley mist. Blue dawn, no direct sun, steady texture in the shadows. No text.

### Judgment
- **Anchor: strong.** The Wall, the porter and the watchtower pass the one-second test.
- **Alteration: fails the scale brief.** It is a big pagoda next to the Wall, not a mountain-sized engine on the summit. The tank top reads as 20th-century industry, breaking the Ming era anchor and the ring payoff.
- **Video fit: weak.** The walker climbs past the engine, not toward it, so the climb would not grow the engine in frame.
- Score (draft): one image 1, anchor 2, alteration 1, composition 1, light 2, materials 2 → not a hero frame.

### Repair → prompt v02
[v02](Prompts/Seedream-5.5-Keyframe-16x9-v02.txt) changes only the engine's placement, scale and crown:
- The Wall runs into the engine's foot on the far summit.
- The watchtower is smaller than one storey, and the engine's top stands well above the horizon.
- The guards are specks.
- The crown is described as separate upright bronze vanes with sky between them, instead of "a ring of shutter panels" (which gave a closed tank).

## Free stills route (2026-11-19)

- **Observed (owner screenshot).** The Jimeng web image input shows Seedream 5.5, 16:9, 2K, 3 images, with **0积分畅用** on and a price of 0/张 (9/张 struck through). The switch's tooltip says turning it off uses credits for faster generation.
- **Observed (CLI).** `dreamina-canvas` 1.4.0 has no matching flag. `node run` takes only node IDs, submit IDs and a credit token, so CLI runs are charged (A1: 6 credits).
- **Action.** Node `node_aep7dydyvy` now holds prompt v02 with count 3, titled "Keyframe v02 ×3 (run with 0积分畅用)", for the owner to run from the web canvas with the switch on.

## Keyframes v02 ×3 and A2 — Seedream 5.5 (2026-11-19)

- **Run by the owner** from the web canvas with 0积分畅用 on. Node `node_aep7dydyvy`, submit `1b1987d1-1131-441a-98fd-65cc2a5bc77c`, three outputs, each `creditsAmount: 0`. Balance stayed at 12,414. A2 (`node_rnnkw5c9p6`, prompt v01) was also run, also at 0 credits.
- Files: [02 A2](Renders/02-Seedream-5.5-Keyframe-v01-A2.png), [03 v02-1](Renders/03-Seedream-5.5-Keyframe-v02-1.png), [04 v02-2](Renders/04-Seedream-5.5-Keyframe-v02-2.png), [05 v02-3](Renders/05-Seedream-5.5-Keyframe-v02-3.png). All 2560 × 1440.

### Owner verdict
"The lighting is kinda bad, not realistic." "Too perfect, no far–near lighting change."

### Observed
- **Crown:** v02-1 and v02-2 show open crowns of upright bronze vanes around a bowl. v02-3 and A2 show the closed riveted tank again. v02-3 has a small glow inside its tank.
- **Placement and scale (not fixed by v02):** in all four the engine stands on the slope to the right of the Wall, about as near as the watchtower, and reads as about 5–8 times the watchtower's height (roughly 60–100 m). The guards read as people, not specks.
- **Light:** the near bricks, the watchtower and the engine have about the same contrast, sharpness and saturation. The engine at its supposed distance has as much detail as the parapet. The sky is a flat, evenly bright pale blue, with no low warm band and no direction. Faces of objects towards the camera are as bright as faces towards the sky. Foreground shadows are open and clean, with no noise.
- Present and good in all: worn steps, parapet, porter with firewood, watchtower, flume and trestles, waterfall, stumps and logs, two lanterns, far engines on the right, valley mist.

### Judgment
- The owner is right. The frames look tone-mapped (HDR): every plane is equally lit and equally sharp. That removes aerial perspective, which is also the main cue for distance, and it is probably why the engine reads near and small. Lighting and scale are the same problem.
- Best of the four: **v02-2**, for its crown, the visible gears and its clean silhouette. Not a hero frame. Draft score: one image 1, anchor 2, alteration 1, composition 1, light 0, materials 1.

### Repair → prompt v03
[v03](Prompts/Seedream-5.5-Keyframe-16x9-v03-Light.txt) leads with light and distance before the subject:
- One natural exposure set for the sky, with the sun below the right-hand ridges as the only source.
- The foreground is dark with noisy shadows, and the step treads are lighter than the risers.
- Each plane is paler, bluer and lower in contrast than the one in front, so the engine becomes a blue-grey mass edged on its right.
- The engine is placed directly behind and above the watchtower at ten times its height, with veiling glare toward the horizon.

Saved to node `node_nttw13fnsy`, count 3, for a run with 0积分畅用.

## Keyframes v03 ×3 — Seedream 5.5, light-first prompt (2026-11-19)

- **Run by the owner** with 0积分畅用. Node `node_nttw13fnsy`, submit `21dc720f-4a5f-4396-8df4-06d1341865e1`, three outputs, each `creditsAmount: 0`. The balance stayed at 12,414.
- Files: [06 v03-1](Renders/06-Seedream-5.5-Keyframe-v03-1.png), [07 v03-2](Renders/07-Seedream-5.5-Keyframe-v03-2.png), [08 v03-3](Renders/08-Seedream-5.5-Keyframe-v03-3.png).

### Owner verdict
"Everything is too perfect, no cloud, no flaw, no variance, you should plant them."

### Observed
- **Light, improved.** The sky grades from deep blue at upper left to a pale warm band at lower right. The foreground parapet and steps are darker than the sky. The far engines and ridges are paler and bluer. v03-1 has the strongest horizon glow and the clearest depth.
- **Sky.** Smooth gradient with soft smears. No cloud structure, no lit cloud bases.
- **Surfaces.** The merlons are regular and complete. The bricks are one even tone. The steps are clean and of equal height. Nothing is broken, overgrown or repaired.
- **Scale and placement, still failing.** The engine stands directly beside the watchtower, at about the same distance. It is only about three to four times the watchtower's height, smaller than in v02. Its base is fully visible on the same crest. It is as dark as the watchtower.
- v03-3 moves the engine to the left of the Wall, and its crown vanes are spiky and irregular.

### Judgment
- The light gets about halfway: it has direction and depth, but the frames are still too clean. The owner's diagnosis holds: there is no variance in cloud, wear, or condition. Real places carry damage, overgrowth, repairs and an uneven sky.
- **Scale: text size words do not work with this model.** Three rounds of "400 m", "taller than the mountain" and "ten times the watchtower" each gave a building of about 60–100 m next to the watchtower. The next attempt changes the cue, not the number:
  - A misty valley sits between the watchtower and the engine, and the engine's base is hidden in the mist.
  - The engine is paler than the watchtower (aerial perspective).
  - Its crown pushes into the cloud base.

### Repair → prompt v04
[v04](Prompts/Seedream-5.5-Keyframe-16x9-v04-Planted.txt) keeps the v03 light and adds three blocks:
- **Sky.** Broken stratocumulus with a torn gap, cloud bases lit orange and rose on the right and blue-grey on the left, cirrus, and smoke shearing left.
- **Scale.** The misty valley between the watchtower and the engine, as above, with the engine's base hidden and the engine paler than the watchtower.
- **Planted flaws, each with a place in the frame:**
  - **Wall:** two broken merlons and their rubble, a jujube sapling in a parapet crack, grass in the step joints, uneven steps with one broken corner, bricks of mixed tone with spalling, a leaning and bulging inner wall, frost only on the shaded edges, dropped twigs and a rope.
  - **Porter:** a patched jacket, a bending pole, uneven bundles.
  - **Watchtower:** a crumbled corner and a bricked-up window.
  - **Engine:** a bent vane and a missing vane, a patched storey, a scaffold, and lanterns that are bright, dim and dark.
  - **Far engines:** one half in cloud shadow, one unfinished in scaffolding, uneven mist.
- The camera tilts one degree off level.

Saved to node `node_2w3fywf3xy`, count 3.

**Proposed shared lesson (one scene, needs more evidence):** Seedream ignores numeric scale. Scale has to come from occlusion (a hidden base), aerial perspective (lighter with distance) and a separating band of mist. Clean, uniform surfaces read as AI. Plant named flaws, each at a specific place in the frame.

## Keyframes v04 ×3 — Seedream 5.5, planted flaws (2026-11-19)

- **Run by the owner** with 0积分畅用. Node `node_2w3fywf3xy`, submit `6a9ef4a8-b378-43da-a2f7-1d131375c0f3`, three outputs at 0 credits. The balance stayed at 12,414.
- Files: [09 v04-1](Renders/09-Seedream-5.5-Keyframe-v04-1.png), [10 v04-2](Renders/10-Seedream-5.5-Keyframe-v04-2.png), [11 v04-3](Renders/11-Seedream-5.5-Keyframe-v04-3.png).

### Owner verdict
"Kinda better, but still no lens feeling. It should start from a human's eye. A human eye doesn't have HDR like this."

### Observed
- **Planted flaws arrived** in all three:
  - Rubble from broken merlons on the walkway (left).
  - Mixed and rust-red bricks, frost on the right parapet's top edge, dropped twigs and a rope on the steps.
  - A sapling against the parapet.
  - A patched jacket on the porter, with uneven bundles.
  - A crumbled corner and grass on the watchtower.
  - Pale new planks patching one engine storey, bamboo scaffold on its left side, and one of the far engines unfinished in scaffolding.
- **The sky is now a broken cloud field**, with an orange and rose band low on the right and smoke shearing from the crown.
- **Placement:** the engine has moved to the left of the Wall, on its own hill rising out of valley mist. In v04-2 and v04-3 its lower slope is in mist, which partly separates it from the watchtower. It is still about two to three times the watchtower's height in the frame and as dark as the watchtower, so it does not read as far or huge.
- **Tone:** strong local contrast everywhere:
  - Clouds have crisp, posterised edges, and the orange band is saturated.
  - The dark foreground bricks still show full texture.
  - There are bright halos where the watchtower edges meet the sky.
  - Every plane is sharp.

### Judgment
- Better world, wrong camera. The scene now has variance, but the image is still rendered like a tone-mapped HDR composite: the halos, the full shadow detail and the crisp clouds. That is not what one exposure, or a human eye at dawn, would record.
- Best of the three for content: **v04-2**. It has the clearest mist separation of the engine, the crumbled watchtower corner, and the most even spread of flaws.

### Research (2026-11-19, third-party prompt guides, not verified on this model)
- Name the camera and film stock (for example Kodak Portra 400), and ask for a "raw, unedited" scan.
- Ask for natural dynamic range and authentic grain, plus a short list of things to avoid (HDR, over-sharpening, AI glow).
- High guidance causes the HDR look ([Seedream v3 guide](https://seedance.it.com/blog/seedream-v3-photorealistic-guide); guidance is not exposed on the Jimeng CLI).
- Sources:
  - [fluxnote Seedream 4 guide](https://fluxnote.io/guides/photorealistic-images-with-seedream-4)
  - [youmind "not HDR" templates](https://youmind.com/prompts/4998)
  - [hedra on imperfect photos](https://www.hedra.com/blog/make-ai-images-look-like-real-photos-prompting)
  - [aivideobootcamp 2026](https://aivideobootcamp.com/blog/photorealistic-ai-prompts-guide-2026/)
  - [atlascloud Seedream 5 Pro realism](https://www.atlascloud.ai/zh/blog/guides/seedream-5-pro-realistic-portraits)

### Next test: two prompts, each changing one thing
- **v05a, tone only** ([prompt](Prompts/Seedream-5.5-Keyframe-16x9-v05a-i2i-Film-Tone.txt)): image-to-image on v04-2, keeping its content.
  - A raw Portra 400 scan, 40mm lens, narrow dynamic range.
  - The horizon slightly blown and its glow spilling, the foreground near black, soft low-contrast clouds, muted peach.
  - Focus on the porter, soft corners, fringing, flare, grain.
  - An avoid line.
  - Node `node_km95cmyqtd`, count 3.
- **v05b, full re-generation** ([prompt](Prompts/Seedream-5.5-Keyframe-16x9-v05b-Film-Full.txt)): the v04 scene with the same film block, plus the engine "pale, almost the colour of the sky" through the haze. Node `node_7hx6h8nqd4`, count 3.
- **Reading the results:** if v05a fixes the look, the tone block works. v05b then shows whether it also works from scratch, and whether the 40mm lens and the paler engine help scale.

## Keyframes v05b ×3 — Seedream 5.5, film-look prompt (2026-11-19)

- **Run by the owner** with 0积分畅用. Node `node_7hx6h8nqd4`, submit `9555c7ad-74b5-4b05-8a0d-a5728e578f0a`, three outputs at 0 credits. The balance stayed at 12,414. The v05a image-to-image node (`node_km95cmyqtd`) was not on the canvas at review time (NOT_FOUND), so the tone-only test did not run.
- Files: [12 v05b-1](Renders/12-Seedream-5.5-Keyframe-v05b-1.png), [13 v05b-2](Renders/13-Seedream-5.5-Keyframe-v05b-2.png), [14 v05b-3](Renders/14-Seedream-5.5-Keyframe-v05b-3.png).

### Owner verdict
"The fog feels not so realistic, and the sky should serve a purpose for the mood you want to create. You can find any real photos."

### Observed
- **Tone:** somewhat softer than v04, and the horizon is brighter. The foreground bricks still show full texture, and the clouds are still crisp-edged with a saturated orange and rose band. Halos remain along the watchtower edges.
- **Fog:** separate smoky puffs and clumps wrapped around the engine's hill at different heights, with no common level, like smoke from a machine rather than weather.
- **Sky:** a busy, dramatic sunset across the whole frame.
- **Composition:** v05b-2 puts the engine on the right against the brightest part of the sky, with a softer silhouette and the waterfall into mist. It reads as the most distant engine so far. v05b-1 and v05b-3 have it on the left, still about 2–3 times the watchtower's height.

### Judgment
- **The fog is wrong physically.** Real dawn fog at Jinshanling is a 云海: after rain, cold damp air settles into the valleys under a temperature inversion. It forms one flat-topped layer at a single height, with ridges as islands and spills over saddles. Clumps at random heights read as fake.
- **The sky works against the film.** The mood is cold, quiet waiting, then the signal fire as the first warmth. An orange sunset spends the warm colour before the fire and fills the frame with competing drama. The sky's job is to be the stage for the payoff.
- **The fix, which also solves scale:** a low, still stratus deck.
  - The engine's crown disappears into the deck and its base into the cloud sea, so it spans between two cloud layers. Hiding both ends is a stronger scale cue than any number.
  - In the payoff the signal fires light the underside of the deck orange above each engine in turn, so the chain becomes visible across the sky.
  - Overcast light is soft and low in contrast by nature, which also removes the reason for the HDR look.

### Real conditions (searched 2026-11-19)
- Jinshanling's sea of clouds forms on early mornings after rain, when humidity is high, mostly from mid-July to mid-August and into early autumn, and is rare. It is photographed in the half hour around sunrise.
- Sources:
  - [China Daily, May 2025 cloud sea](https://www.chinadaily.com.cn/a/202505/14/WS68247052a310a04af22bf500.html)
  - [人民资讯网 summer cloud seas](https://www.rmzxw.com.cn/c/2021-08-24/2940277.shtml)
  - [weather.com.cn](https://www.weather.com.cn/hebei/gqtj/3213469.shtml)
  - [Top China Travel photo guide](https://topchinatravel.com/photography-tour-to-china/best-places-to-photograph-sunrise-and-sunset-at-jinshanling-great-wall.htm)
  - [Hasselblad: Yang Dong](https://master.hasselblad.com/inspiration/stories/yangdong-the-great-wall)
- I did not download or use any real photo as a reference. Rights to news and stock photos are not cleared. An owner-shot or licensed Jinshanling photo could serve as a geography and light reference.

### Repair → prompt v06
[v06](Prompts/Seedream-5.5-Keyframe-16x9-v06-After-Rain.txt) changes the weather and season to the real conditions:
- **Sky and cloud sea:** early autumn after rain. A still, low stratus deck with only a pale cold slit at the right horizon, no orange anywhere. A flat-topped sea of cloud at one level, with ridges as islands and a spill over a saddle.
- **The engine:** spans from the cloud sea to the deck.
- **The near Wall:** wet bricks with dry raised edges, puddles in the worn treads reflecting the slit, saturated wet moss, drips from the loopholes. Frost removed.
- **Kept from v04 and v05:** the planted flaws and the film and lens block.
- Node `node_7474kvh2tz`, count 3.

## Keyframes v06 ×3 — Seedream 5.5, after rain (2026-11-19)

- **Run by the owner** with 0积分畅用. Node `node_7474kvh2tz`, submit `1f72242d-91f8-487e-b530-34ac236843d8`, three outputs at 0 credits.
- Files: [15 v06-1](Renders/15-Seedream-5.5-Keyframe-v06-1.png), [16 v06-2](Renders/16-Seedream-5.5-Keyframe-v06-2.png), [17 v06-3](Renders/17-Seedream-5.5-Keyframe-v06-3.png).

### Owner verdict
"Kinda looks better now." But the engine and the Wall should have a logical relationship: think about how and whether it connects, which way it faces, and where it sits relative to the Wall.

### Observed
- **Looks like a real place for the first time:**
  - An even overcast deck, and a cloud sea at one level with ridges as islands.
  - Wet steps with puddles, moss, rubble, twigs, a sapling.
  - Soft, low-contrast light, with no HDR halos.
- **Siting:**
  - **v06-1:** the engine is on a separate hill to the right (the inner side), but it sits directly on the Wall's line, and nothing explains how anyone reaches it.
  - **v06-2:** the engine has shrunk to a small water mill built onto the Wall beside the watchtower, plus a tiny machine on a far peak.
  - **v06-3:** the engine is on the left (the outer, enemy side), rising straight out of the cloud sea.
- **The crown is gone in all three.** The engines have plain pagoda roofs, no bronze vanes, no fire bowls. My v06 prompt asked for the crown to disappear into the cloud deck, which conflicts with a payoff that needs the crown visible.
- **Waterfalls** fall from the engine itself (v06-1) or from the far ridges (v06-2, v06-3), with no clear source.

### Real siting (searched 2026-11-19)
- **Apart from the Wall.** Beacon towers mostly stand apart from the Wall body, on both its inner and outer sides ([北京日报 2026](https://news.bjd.com.cn/2026/08/07/11904411.shtml)).
- **No fire on watchtowers.** Hollow watchtowers housed soldiers, grain and gunpowder, so fires were not lit on them, because it was too dangerous. Fire structures were built beside them (same source).
- **Multiple fires as code.** A Tianjin University team found the smoke was usually lit not on the main tower but in several fire pits and smoke platforms beside it, so the number of smokes could carry the message (same source).
- **A system of points and lines.** Beacons are the "point" elements of a defence system, alongside forts and relay lines ([Li Yan 2018](https://pure.mpg.de/pubman/item/item_3212808_5/component/file_3212812/LI_YAN_2018.pdf)).
- **Wall orientation.** On the Wall itself, the outer side has the crenellated parapet with loopholes, and the inner side has a low plain parapet (宇墙). From general knowledge; to verify on Jinshanling photos.

### Siting rule for the engines (my design, alternate history, built on the facts above)
- **Apart:** each engine stands on its own summit, separate from the Wall, never built into it.
- **Inner side:** it sits on the inner side (the right-hand side of our frame), so raiders reach the Wall before the engine. Its water comes from springs further inland behind it.
- **Linked by a spur:** a spur wall with a walkway leaves the Wall at a right angle from a gate in a watchtower's inner side and runs to the engine's walled yard. The yard holds firewood stacks, a cistern and a guard hut. Porters carry fuel along the spur. That gives the porter in frame a destination.
- **Facing:** the engine's gate faces the spur and the Wall. The crown must be seen from the next engine along the line, so the engines sit on summits in sight of one another.
- **Nobody lives in the engine:** soldiers live in the watchtowers, as in the real system.
- **Five fire bowls:** the crown holds five separate bowls. The real Ming code cited in popular sources rose to five fires and five gun reports for the largest raids. The number lit carries the message. A proposal for the payoff, not yet decided.

### Repair → v07 (two routes)
- **[v07](Prompts/Seedream-5.5-Keyframe-16x9-v07-Siting.txt), text-to-image, layout first:**
  - The outer parapet with merlons on the left, the inner low parapet on the right.
  - A gate at the watchtower and the spur running right across the saddle to the engine's summit, about a kilometre inland.
  - The yard, the flume from inland, the crown just below the deck with five bowls.
  - Further engines each on their own inner-side summit with their own spur.
  - Node `node_dqf4pnh013`, count 3.
- **[v07b](Prompts/Seedream-5.5-Keyframe-16x9-v07b-i2i-Spur-Crown.txt), image-to-image edit of v06-1** (engine already on the inner side), keeping its weather and Wall. It adds the spur and yard, two more storeys, and the vane crown with five bowls. Node `node_d3qvw7wvt0`, count 3.

## Keyframes v07 ×3 (text-to-image) and v07b ×3 (edit of v06-1) — siting (2026-11-19)

- **Run by the owner** with 0积分畅用, all 0 credits.
  - v07: node `node_dqf4pnh013`, submit `7deb95a1-819d-490b-b6ab-a5c1d8213d68`.
  - v07b: node `node_d3qvw7wvt0`, submit `ce81d20e-cad1-4703-898f-1bd254f78d42`.
- Files: [18 v07-1](Renders/18-Seedream-5.5-Keyframe-v07-1.png), [19 v07-2](Renders/19-Seedream-5.5-Keyframe-v07-2.png), [20 v07-3](Renders/20-Seedream-5.5-Keyframe-v07-3.png), [21 v07b-1](Renders/21-Seedream-5.5-Keyframe-v07b-1.png), [22 v07b-2](Renders/22-Seedream-5.5-Keyframe-v07b-2.png), [23 v07b-3](Renders/23-Seedream-5.5-Keyframe-v07b-3.png).

### Observed
- **v07 (all three).**
  - The siting reads: the outer parapet with merlons on the left, the low inner parapet on the right.
  - A spur wall leaves the Wall to the right, crosses the saddle and climbs to a separate summit. Two porters with firewood walk on it.
  - The engine stands in a walled yard with firewood stacks, a stone cistern and a small guard hut.
  - The flume comes in from behind, feeding a wheel at the base, and there is a waterfall below the yard.
  - The crown is back: upright bronze vanes, some bent, around three to five bowls.
  - Further engines stand on summits to the right.
  - Weather and light match v06.
  - The engine is about twice the watchtower's height in the frame, at a similar distance, and reads as roughly 60–80 m.
  - v07-2 and v07-3 have a flat walkway rather than steps.
- **v07b (edits of v06-1).**
  - v07b-1 and v07b-3 add the vane crown with five bowls, more storeys, the spur and the yard.
  - v07b-3 has the tallest engine of any frame, about four times the watchtower's height, with eight storeys under the crown.
  - In v07b-3 the yard sits on a spur that meets the main Wall, porters walk on it, and the wheel and flume are at the engine's base.
  - v07b-3 shows no far engines, only a small watchtower on the far hill. There is still a waterfall with no source at the lower right, and smoke rises from the near watchtower.
  - v07b-2 turned the crown into ornamental leaf shapes and set the yard apart from the engine. It fails.

### Judgment
- **Siting now makes sense:** an engine apart from the Wall on the inner side, fed by the spur, porters with somewhere to go, a yard holding its fuel and water. The owner's logic note is met in v07-1, v07-2, v07-3 and v07b-3.
- **Best candidates:**
  - **v07b-3** for scale and crown. It is the only frame where the engine is clearly beyond any real tower. It lacks the far engines the payoff needs.
  - **v07-2** for the cleanest overall logic, with far engines present, but the engine is smaller.
- **Smoke on the watchtower** could be a kitchen fire, which is plausible, since soldiers lived there. But viewers might read it as a signal before the engine fires, so remove it.
- **Scale is still the open question.** The engine reads as a very large building, not as mountain-sized. Possibly a deliberate trade: v07b-3 is believable and still impossible for Ming. Owner's call.

### Next → v08, an edit of v07b-3
[v08](Prompts/Seedream-5.5-Keyframe-16x9-v08-i2i-Fix-Chain.txt) keeps everything else and makes three changes:
- Add two far engines on the right-hand hills, each smaller and paler, for the payoff chain.
- Remove the sourceless waterfall at the lower right.
- Remove the watchtower smoke.

Node `node_1xaxhdppvh`, count 3.

## Keyframes v09 (first frame) and v10 (last frame), prepared (2026-11-19)

- The owner approved director's statement v2 with the fact corrections (号炮, a garrison living in the engine's yard) and the clarification that the fire is kept inside the engine.
- Both frames are image-to-image from [v07b-3](Renders/23-Seedream-5.5-Keyframe-v07b-3.png), resource `1ec1b05a-…`, used as the design reference only. The camera position is new in both.
- **[v09 first frame](Prompts/Seedream-5.5-Keyframe-16x9-v09-First-Frame.txt)**, node `node_bbmd3j3qp4`, ×3:
  - The camera follows three to four metres behind the porter, 40mm. The porter and his load are in the lower left third.
  - The Wall rises on a diagonal to the watchtower, with the inner gate on its right.
  - The engine's upper storeys and unlit crown fill the upper right third, behind the watchtower and into the deck. Its lower body is hidden.
- **[v10 last frame](Prompts/Seedream-5.5-Keyframe-16x9-v10-Last-Frame.txt)**, node `node_2622hyxhm9`, ×3:
  - The camera is on the spur behind the porter as he lifts the pole again. The engine is across the saddle.
  - Two of the five bowls are burning, with an orange bloom on the deck above.
  - Far engines along the Wall to the right each burn two points under their own glow on the deck, fainter toward the horizon.
- **What to check:**
  - The porter's identity matches in both frames (jacket, wrap, pole, uneven bundles).
  - The engine's design matches v07b-3.
  - The fire is the only warm colour. Two bowls burn, not five.
  - The far chain reads as a line of glows under the deck.
  - The film tone holds.

## Keyframes v09 (first frame) and v10 (last frame) — results (2026-11-19)

- **Run by the owner** with 0积分畅用, 0 credits. The balance stayed at 12,414.
  - v09: node `node_bbmd3j3qp4`, submit `a5d0dacf-…`. The third output (`e24226e5-…`) was still running at review time.
  - v10: node `node_2622hyxhm9`, submit `4d441bcf-…`.
- Files: [24 v09-1](Renders/24-Seedream-5.5-Keyframe-v09-1.png), [25 v09-2](Renders/25-Seedream-5.5-Keyframe-v09-2.png), [26 v10-1](Renders/26-Seedream-5.5-Keyframe-v10-1.png), [27 v10-2](Renders/27-Seedream-5.5-Keyframe-v10-2.png), [28 v10-3](Renders/28-Seedream-5.5-Keyframe-v10-3.png).

### Observed
- **v09-1:**
  - The porter is large in the lower left, seen from behind: head wrap, patched dark jacket, a bending pole, two bundles of firewood, sharp focus.
  - The wet walkway rises to a watchtower with an arched gate in its right-hand (inner) face.
  - Behind the watchtower, the engine's upper storeys and its crown fill the upper right: tall flat bronze vanes around five unlit bowls, one faint window glow, the top in mist. Its lower body is hidden. A water wheel shows at its foot on the right.
  - Overcast grey-blue, a pale slit on the right horizon, the sea of cloud on the left.
- **v09-2:** the same design, slightly wider. The gate is in the watchtower's front face rather than its inner side.
- **v10-1:** three bowls are lit, not two. Far engines burn with glows. The porter has no head wrap.
- **v10-2:**
  - Two bowls lit and three dark, as asked.
  - Three far engines along the Wall to the right, each with two points and a glow above.
  - The porter walks the spur toward the yard.
  - The glow above the near engine is a smooth oval with concentric banding.
  - The whole scene is darker and duskier than v09.
  - The porter has no head wrap.
- **v10-3:** two bowls lit. Oval halos with visible banding. The ambient is duskier.

### Judgment
- **First frame: v09-1.** It passes the one-second read: the Great Wall and the porter, then a crown that cannot be real above the watchtower. It has the composition from the statement, the inner gate in the right place, and the fire held back.
- **Last frame: v10-2 after repair.**
  - **Oval halos.** The perfect ellipses with banding are an AI tell. Light on a cloud deck follows its folds.
  - **Ambient light too dark.** v10 reads as dusk, but in thirty seconds the morning should not get darker. Seedance would interpolate a darkening that is physically wrong.
  - **Missing head wrap.** The porter lost his head wrap, a continuity break.
- **Repair [v11](Prompts/Seedream-5.5-Keyframe-16x9-v11-i2i-Last-Frame-Repair.txt):** an edit of v10-2, with v09-1 as a second reference for the porter's clothing and for the ambient brightness. The glow is rewritten to follow the cloud. Node `node_vc9v29gqjv`, count 3.

## Keyframe v11 — last-frame repair of v10-2 (2026-11-19)

- **Cost:** the free run (submit `7e6388ce-…`) was cancelled after queueing. The node was re-run with credits: submit `5cb31ca8-c83a-4255-9a71-5abf7f83d955`, three outputs at **6 credits each, 18 total**. The balance went from 12,414 to 12,396. That run was started from the web canvas, not by me.
- Files: [29 v11-1](Renders/29-Seedream-5.5-Keyframe-v11-1.png), [30 v11-2](Renders/30-Seedream-5.5-Keyframe-v11-2.png), [31 v11-3](Renders/31-Seedream-5.5-Keyframe-v11-3.png).

### Observed
- Composition, the two lit bowls and the three dark ones, and the three far engines are all kept from v10-2.
- **Ambient:** brighter and bluer than v10-2, closer to v09-1, though the foreground is still somewhat darker than in v09-1.
- **Glow:** now an uneven orange in the cloud folds, not an oval. v11-2 is the most broken up and natural. v11-1 keeps a slightly oval patch above the far engines.
- **Porter:** now has a dark cap or wrap. In v09-1 it is a tied headband wrap, so the match is close but not exact.
- Some blotchy posterisation in the cloud at full size (2560 px). It is likely to be less visible at 720p.

### Judgment
- **Last frame: [v11-2](Renders/30-Seedream-5.5-Keyframe-v11-2.png)**, resource `6cccc4cb-86eb-4717-8b64-f4271346548e`.
- **First frame: [v09-1](Renders/24-Seedream-5.5-Keyframe-v09-1.png)**, resource `68a44d47-349b-4c4a-9aed-e6a8a52b391a`.

## Take 01 — prepared (2026-11-19)

- **[Video prompt v02](Prompts/Jimeng-Seedance-2.5-720p-30s-First-Last-Porter-v02.txt)**, 464 words, written to director's statement v2:
  - Six timed beats.
  - Gun reports instead of gongs.
  - Two bowls lit.
  - Far engines in order.
- **Node** `node_sqm3q0vpcw`: Seedance 2.5, `first_last_frame`, 16:9, 720p, 30 s, one output. First frame v09-1, last frame v11-2.
- **Live quote: 0 credits** (`totalMaxCredits: 0`), so this would use one of the free Seedance 2.5 runs.
- **Not submitted.** It waits for owner approval, and would run with a credit ceiling of 0.
- **Known risks:**
  - The two frames are from different camera positions: the walkway before the watchtower, then a farther position with the whole engine in view. The model has to invent the path between them, which may cause drift.
  - The prompt is longer than the 350-word aim.
  - The 30 s timing is untested.
- **Prompt v03** ([file](Prompts/Jimeng-Seedance-2.5-720p-30s-First-Last-Porter-v03.txt), 2026-11-19). Owner asked to revise before running. Changes from v02:
  - Cut from 464 to about 330 words.
  - Dropped re-description of what the two frames show.
  - Made the camera path explicit: the camera slows so the porter draws ahead, and the walkway bends right to clear the watchtower. This explains how frame 1 becomes frame 2.
  - Removed setting the load down and lifting it again, to avoid complex hand actions. He stops with the load on his shoulder.
  - Far engines light nearest first.
  - Saved to node `node_sqm3q0vpcw`. The quote was rechecked after the edit.

## Take 01 — submitted (2026-11-19)

- The owner approved the run ("继续 需要声音 不用音乐"). The prompt already asks for sound and says no music.
- **Submitted (verified from the CLI):** node `node_sqm3q0vpcw`, submit `8832f3d5-6f43-4e1a-bf18-a45fe57883bd`, resource `3ac8ed0e-0e50-4edc-82b8-ee05a74b6b22`.
  - Seedance 2.5, `first_last_frame`, 16:9, 720p, 30 s, one output.
  - First frame v09-1, last frame v11-2, prompt v03.
  - Credit ceiling 0. The resource shows `creditsAmount: 0`.
- **Balance before:** 12,396.

## Take 01 — review (2026-11-19)

- **Verified:** job succeeded. Balance 12,396 before and after, so 0 credits charged. This used one of the free Seedance 2.5 runs.
- **File:** [Take 01](Renders/32-Jimeng-Seedance-2.5-720p-30s-Take01.mp4), 1280 × 720, 24 fps, 30.02 s video, 30.05 s audio. 54.9 MB. SHA-256 `ac37b7d9…6da2c96`.
- **Contact sheets** at 0.5 s intervals: [Renders/Take01-Frames](Renders/Take01-Frames/). Extra frames at 4.583–4.917 s and at 20, 24 and 29.9 s.

### Observed: picture
- **0–4.83 s:**
  - Matches the first frame.
  - The porter walks toward the watchtower with the load swinging; the camera follows.
  - The crown is visible above the watchtower and unlit.
  - Light is steady.
- **4.83 → 4.92 s: a hard cut, in one frame (F2).**
  - The scene jumps to the last frame's geography: the porter on a different stretch of Wall, the whole engine in its yard beside a watchtower, the far Wall on the right.
  - A dark foreground wall edge on the left appears at 4.9 s and is gone by 6 s.
  - The ambient light also drops to a darker blue at the cut.
- **5–12 s:** the porter walks toward the engine. The camera follows slowly. The water wheel spills, and smoke drifts from a vent on the engine's left side. Nothing else changes.
- **12–17 s:** the porter stands still with the load on his shoulder. No hand problems. The image is quiet and static.
- **17.0 → 17.5 s:** fire appears in the crown within half a second, with an orange glow on the cloud above.
  - The vanes do not visibly turn in the samples.
  - Two main flames burn, with a possible small third at times (20 s, 24 s).
- **22–25.5 s:** far towers light in order, nearest first.
  - 22.0 s: the first.
  - 23.5 s: the second.
  - About 25 s: the third.
  - Each has a warm patch on the cloud above, at uneven intervals.
  - At this distance the far "engines" read more like watchtowers with fire on top.
- **26.5–30 s:** the porter walks on toward the yard, ending on the last frame.
- **Throughout:**
  - No text or watermark.
  - The engine's shape and the porter's clothing hold from 5 s to the end.

### Observed: sound (loudness timeline only, not listened to)
- **0–12 s:** a low bed around −30 to −38 dB.
- **13–16.5 s:** falls steadily to about −45 dB. The planned near silence is there.
- **17–18 s:** a loud event (−12 dB RMS). **The peak reaches 1.05, so it clips.**
- **21.5–22 s, 23 s, 24.5–25 s and 26.5 s:** further events, each fading (peaks 0.60, 0.27, 0.37, 0.29). They line up with the far fires at 22, 23.5 and 25 s.
- **Unverified:** whether these are gun reports, and whether any music or speech was added. The owner should listen.

### Judgment
- **The payoff works.** The fire lights the cloud, then the chain runs along the ridges with uneven timing and fading sound. The one-image test holds: "a line of fire under the clouds along the Great Wall".
- **The big failure is the cut at 4.9 s.** The two frames were too far apart in camera position for one continuous move. The model jumped instead of walking the turn. The earlier risk note predicted this.
- **Too long with nothing happening.** 5–17 s is about 12 s with little change. Douyin pacing wants something to change every 1.5–2.5 s.
- **The fire pops on rather than catching.** The crown turn is lost.
- **The audio clip at 17.5 s** needs a limiter in post.

**Score (draft):**

| Category | Score |
| --- | --- |
| One image | 2 |
| Anchor | 2 |
| Alteration | 2 |
| Composition | 2 |
| Light | 2 |
| Materials | 1 |
| Motion | 1 |
| Fidelity | 1 |
| Sound | 1 (unverified) |
| Emotional landing | 1 |
| **Total** | **15 / 20** |

That is one short of shipping, with no zero in the critical categories. The repair is in the edit.

### Edit options (no regeneration)
- **A. As is, 30 s.** Treat the 4.9 s cut as a match cut on the porter's back. It is honest about being a cut, but the jump in light is visible.
- **B. One continuous take, 4.92–30.0 s (about 25 s).** Start after the cut. The first frame still has the Wall, the porter, the whole engine and the far Wall, so the hook holds. This loses the crown-above-the-watchtower reveal.
- **C. Tight cut, about 20 s.** 0–4.8 s, then a deliberate cut to about 11.5–30 s. The cut becomes a chosen reveal, and the dead stretch goes.
- In all three: limit the 17.5 s clip, and post with the AI declaration.

## 2026-11-20 Edit C (from Take 01)

File: `Renders/33-Edit-C-Take01-Cut-23s.mp4` (1280×720, 24 fps, 23.38 s, H.264 CRF 16, AAC 192k, SHA-256 `a32262e1…4e71d55e97d`). Made locally with ffmpeg 8 (Homebrew), no credits.

Edit: Take 01 0–4.80 s, cut to 11.50–30.02 s. 80 ms audio fade out and in at the cut. Soft limiter at −1 dBFS.

**Observed**
- Scene-change detection finds one cut only, at 4.79 s (the planned one). The generated jump at 4.83→4.92 s is gone.
- The landing frame at 11.5 s shows the porter standing on the Wall with the whole engine, its yard and the far Wall. It matches 11.0 s, so this part of the take is static and the landing has no motion conflict.
- Fire lights at about 10.0 s in the edit (17.0 s in the source); the far chain runs at about 15–18.5 s.
- Correction to the Take 01 review: ffmpeg `astats` gives the source peak at −2.5 dBFS per channel. The 1.05 peak from my RMS script came from summing the channels into mono. The source does not clip, and the limiter changes nothing measurable (edit peak −2.5 dBFS).
- Length is 23.4 s, not the 20 s I estimated (4.8 + 18.5).

**Unverified**
- Not listened to: whether the audio contains music or speech, and whether the booms read as gun reports.

**Judgment**
- The cut now reads as a reveal: the crown above the watchtower, then the whole machine. The edit still holds about 5 s of standing before the fire (4.8–10 s). If that feels slow on a phone, start the second piece at 13.0 s instead of 11.5 s, which gives about 21.9 s.

## 2026-11-20 Edit C2 (owner chose about 22 s)

File: `Renders/34-Edit-C2-Take01-Cut-22s.mp4` (1280×720, 24 fps, 21.88 s, H.264 CRF 16, AAC 192k, SHA-256 `100c0d08…0450a08093`). Same recipe as Edit C (ffmpeg, 80 ms audio fades at the cut, limiter at −1 dBFS), but the second piece starts at 13.0 s instead of 11.5 s. Edit C is kept.

**Observed**
- Scene-change detection finds one cut only, at 4.79 s.
- Frames from 4.79 s to 5.1 s of the edit, and source frames from 12.0 s to 14.5 s, are the same framing: the porter stands with the whole engine in view. The landing is clean.
- Fire lights at about 4.0 s after the cut (8.8 s in the edit), and the far chain runs at about 13.5–17 s. Peak −2.5 dBFS.

**Unverified**
- Not listened to: music or speech, and whether the booms read as gun reports.

**Judgment**
- This is the release candidate. Its structure: reveal of the crown (0–4.8 s), the whole machine and a short held breath (4.8–8.8 s), the fire (about 9 s), the answer along the ridges, then the porter walks on.

## 2026-11-20 Learnings from The Beacon Engines (Take 01 → Edit C2)

Owner verdict: "not yet perfect but alright". Release candidate: `Renders/34-Edit-C2-Take01-Cut-22s.mp4`. Totals: 11 still-prompt versions, 31 stills, one free 30 s video take, two local edits.

### 1. The first frame (v09) — what it did and what it cost

**What worked (repeat)**
- It read in one second. A real place (the Jinshanling Wall, a hollow watchtower, wet bricks) plus one impossible thing (a bronze crown wider than the watchtower) passes the one-second test.
- A human point of view. Eye height, 40 mm, a companion three or four metres behind the porter, slightly tilted. The owner accepted it as "a human eye". The porter's back gives scale and a reason to walk without needing a face.
- Scale through hiding. The watchtower and the ridge hide the engine's body, and haze softens it. Written sizes in numbers failed (v01–v02); hiding the base worked.
- Light. An after-rain stratus deck with no sunrise colour, a raw Portra 400 scan, and fire as the only warm colour ended the HDR look that v01–v04 had.

**What it cost (failed)**
- The frame hid what the video then had to show. The engine's body was behind the watchtower, so the take had to walk about 40 m, turn and reveal it. The last frame (v11) stood on the spur, in a different place and at a different height. Seedance did not walk that distance; it cut at 4.9 s (F2) and then sat still from 5 to 17 s. The first and last frames were each good stills, but no continuous camera move could join them in the time given.
- Nothing in the first frame moves on its own except the porter. The cloud deck is still, the wheel is hidden, and the lantern is tiny. Once he stops, the frame is dead, which caused the static stretch from 5 to 17 s.
- The payoff object was small in the frame. The crown filled about a sixth of the frame width at 720p, so its turning vanes were not visible, and the fire just switched on.

**Rule I would now apply to any first frame meant for video**
- Shape the first frame around the move, not only around the still. Every element the take must reveal should be either already visible in it, or one short, nameable camera move away (one step aside, one pan, two seconds of walking).
- With first_last_frame, the last frame must be reachable from the first by the move the prompt describes. Use the same height and side of the Wall, a change in camera position of at most about 5–10 m, and no turn of more than about 30°. Otherwise drop the last frame and use first-frame-only.
- Put one thing in the first frame that keeps moving whatever the subject does: water, smoke, a flag, cloud crossing the ridge. That covers the holds.
- Make the payoff large enough to read at 720p on a phone: at least a quarter of the frame width for anything that has to visibly move.

### 2. Process — the order I should have decided things in

The owner had to push each of these in turn: lighting, then flaws, then the lens, then the fog and sky, then siting, then story, then history. Each push cost a round of stills (v03–v07). A better order, settled in writing before any still:

1. **Function and history.** How the real thing worked (beacon towers stood apart from the Wall, smoke by day and fire by night, 号炮 guns, the 墩军 garrison living in the yard), and where the invented machine sits and why (the spur wall, the 坞城 yard, the inner side of the Wall). Getting this wrong means redoing the siting later (v06 → v07).
2. **Story and the reason for this shot.** Who watches, what changes, what the viewer should feel. "火是机关自己点的，可烧的每一根柴，都是人挑上山的。"
3. **Light and weather that serve that feeling.** The sky is part of the story, not decoration: a low, oppressive cloud deck that the fire lights from below.
4. **Planted flaws.** By default the model makes everything clean. Write the flaws in: broken merlons, a missing vane, a patched storey, an uneven load, puddles, moss.
5. **Lens and film scan.** Only then the look wording.

### 3. The video take

**Repeat**
- The far chain of fires: sequential events, nearest first, with uneven pauses and a warm patch on the cloud above each. It came out readable and is the payoff of the film.
- A sound timeline written into the prompt (ambience, near silence from 13 s, the event at 17 s, fading answers) was followed almost to the second. No music appeared in the loudness data. This is still unverified by listening.
- The free queue (0 credits) gave a usable 30 s take at 720p.

**Failed**
- The distance between the first and last frames caused the cut (see 1).
- A 30 s clip with one event gave about 12 s of dead time.
- Ignition: "fire climbs into two bowls" produced a switch-on. Next time, name the stages: a spark in one bowl, a small flame, a lick of flame, a second bowl, full height over about 3 s.

### 4. The edit

- Treating the generated cut as a deliberate reveal turned a defect into structure: the crown alone, then the whole machine.
- Cut the dead time hard. Edit C2 is 21.9 s, with the fire at about 9 s.
- Tooling: measure the peak per channel with ffmpeg `astats`. My mono-sum RMS script overstated the peak (it reported 1.05, but the real value is −2.5 dBFS). ffmpeg is now installed, so do edits and checks with it.

### 5. Next test (not run)

Re-shape the first frame rather than the motion prompt:
- **Camera position.** Put the camera already on the spur wall, about 15 m behind the porter, with the engine's whole body, its yard and its water wheel in view. Keep the far ridges and the Wall on the right.
- **Size of the engine.** Make the crown about a quarter to a third of the frame width.
- **Something that moves on its own.** The water wheel, the spill and the cloud crossing the saddle.
- **Generation.** First frame only, 12–15 s. The porter walks toward the yard, and the fire builds in stages from about 4 s. The far chain follows from about 8 s.

**Compare with Edit C2 on:**
- whether the take has no cut;
- whether the fire builds rather than switching on;
- whether the vanes visibly move at 720p.

### 6. Proposed shared-checklist changes (not adopted yet; supporting scene: The Beacon Engines)

- **05 Keyframes, motion-ready first frame.** Add the reachability rule for first and last frames, plus the "something moves on its own" and "payoff at least a quarter of the frame width" checks.
- **05 or 02, decision order.** Settle function and history, then story, then light, then flaws, then lens, all before the first still.
- **06 Video prompting, staged ignition wording.** Add the wording for a fire that builds in stages, and the far-chain recipe as a candidate recipe (one take, unproven until repeated).
- **06 failure table, F2 cause.** Add "first and last frames too far apart" as a known cause of F2.
