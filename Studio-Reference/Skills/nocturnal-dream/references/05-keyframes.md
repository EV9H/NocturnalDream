# 05 · Keyframes

The first frame decides most of the video. Spend here.

## Workflow

0. **Decide before the first still.** Write these down in this order, because each one changes the next, and fixing them late costs a round of stills:
   1. **Function and logic.** How the real counterpart of the altered thing works or worked, and where the altered thing sits relative to the real place and why. An invented structure needs a believable reason to stand where it stands.
   2. **Story and reason for the shot.** Who or what the viewer follows, what changes, and the one feeling. One sentence.
   3. **Light and weather that serve that feeling.** The sky is part of the story, not a backdrop.
   4. **Planted flaws.** Models default to clean, perfect frames. Name the wear, damage, asymmetry and uneven load that a real place would show.
   5. **Lens and capture medium.** Only then the look wording (see [04](04-cinematography.md), Optical realism).
1. **Reference pack.** Collect, with a stated job for each:
   - **Place:** real photos for geography, architecture style, signage, railing, landmark spacing.
   - **Material:** texture and wear (snow crust, rust, tile glaze).
   - **Light:** a photo or still that shows the intended light behavior.
   - **Composition:** a sketch, blocking diagram or earlier frame.
   Rights: use only references you can legally use. No real-person faces without permission.
2. **Layout test.** A cheap image to check geometry: where the camera stands, where each landmark sits, whether scale cues read. Fix geometry before polish.
3. **Look frame.** Settle light, palette and material treatment on one frame.
4. **Hero candidates.** Generate a batch (4–8) of the keyframe in native 9:16. Change one variable per batch (angle, light direction, foreground cue), not everything.
5. **Select.** Score with [08](08-production-and-qc.md). Pick by the six tests, not by "looks nice".
6. **Repair.** Fix local faults in an editor or with inpainting: a warped railing, a stray bright spot, a wrong tower. A cleaned still is worth more than ten video rerolls.
7. **Lock.** Record the hero frame as the continuity anchor and its role (first frame, end frame or reference).

## Still prompt structure

Write a photographer's shot sheet, not a mood board. Order:

1. **Frame and viewpoint.** Format (vertical 9:16), height, direction, distance to subject, lens feel, focus.
2. **Subject and place.** What and where, with the anchor made concrete.
3. **Evidence of the alteration.** The rule's visible proof and one consequence.
4. **Foreground, midground, background.** Name objects at each depth.
5. **Light.** Source, direction, quality, contrast, what is dark.
6. **Atmosphere.** What is in the air.
7. **Palette and accent.**
8. **Materials and wear.** Specific, with contact traces.
9. **Imperfections.** Grain, falloff, uneven light, one off-center flaw.

Say what is present. Avoid piling on negatives. If a fault keeps returning (gibberish text, extra tower), fix it with a reference, a crop or a retouch instead.

**Example (proposal, adapt).**
`Vertical 9:16 photograph from an adult's eye height on the west-bank Bund promenade, 28mm lens, facing across the Huangpu. A wind-packed snow drift rises to the second rail, so the lower bars of the wave-pattern railing are buried and a granite lamp plinth shows one bevel at left. Overlapping bootprints with compressed rims cross the foreground, older ones softened by powder. Beyond the rail, dark open water with broken reflections and a snow-capped low roofline on the far bank, the Oriental Pearl and two towers small and soft in the haze. One small tungsten lamp from behind camera-right grazes the drift crest and a few close flakes. Midnight-blue ambient fill, charcoal shadows with texture. Fine grain, soft highlight roll-off, slight vignette.`

## Real places

- Verify landmark order and relative size against a photo from the same vantage. Past tests drifted on tower spacing and rail design.
- Prefer a vantage where only a few landmarks appear and each one is large enough to be recognized.
- When using a reference image for geography, do not also copy its lighting unless wanted. State the roles: "geography only", "light only".
- If the model corrupts a landmark, composite the correct one in post.

## Models and settings

- Use the tool's current schema and quote cost before running. Record model, size, aspect ratio, quality, seed (if exposed), job id and the echoed prompt.
- Generate at the largest native size the tool offers. Crop-to-vertical from a different aspect is a fallback.
- For fidelity to references, use image-reference or edit modes with explicit role text.
- Different image models suit different jobs. Test two on the same shot sheet when a look is hard to get. Note results in the scene folder.

## Continuity bible

Write once, paste verbatim into every shot of a scene or sequence:

- **World block.** Place, hour, weather, rule, evidence.
- **Look block.** Light, palette, lens feel, texture.
- **Subject blocks.** Any recurring person or object, with fixed visible features (clothing, hair, scars, colors).
- **Fixed landmarks and their positions** relative to camera.
- **Screen direction.** Which way the camera and subjects travel.

People: use authorized reference photos or generated characters. Do not use real faces without rights. Keep a neutral headshot and a full-body reference per character, and reuse them in every shot.

## Motion-ready first frame

A first frame for video is judged by what it lets the take do, not only as a still. A strong still that hides what the video must show forces the model to invent a long move, and it tends to cut instead. These checks rest on one reviewed take; treat them as proposals until another scene confirms them.

- **Reveal within reach.** Everything the take must show is either already visible in the first frame or one short, nameable camera move away (a step aside, a short pan, two seconds of walking). Do not hide the payoff behind an occluder that the camera must travel a long way to clear.
- **First and last frame reachable.** With a first-and-last-frame mode, the end frame must be reachable from the first by the move the prompt describes, in the time given: same height and side of any barrier, a small change in position, a modest turn. If not, drop the end frame and use first-frame only, or shoot the end frame from close to the first camera position.
- **Something that moves on its own.** Include at least one element that keeps moving whatever the subject does (water, smoke, cloud, cloth, traffic). It carries the holds when the subject stops.
- **Payoff large enough to move visibly.** Anything whose motion must read (a rotating part, a flame, a door) needs enough frame area to show it at the test resolution on a phone, roughly a quarter of the frame width or more.

## Keyframe QC (before any video spend)

- Does the thumbnail test pass?
- Are scale, depth and the alteration readable?
- Are the landmarks right?
- Are surfaces and contacts believable?
- Is there an off-center, imperfect, real feeling?
- Does the first frame leave room for the planned motion (what enters, what leaves)?
- Is the payoff visible or one short move away, and is the end frame (if any) reachable from it?
- Does something in the frame keep moving when the subject stops?

If any answer is no, repair the still. Do not generate video from a frame you do not like.
