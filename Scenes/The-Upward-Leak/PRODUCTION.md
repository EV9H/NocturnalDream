# The Upward Leak

**SC-007 · Rejected concept · Archived privately**

The user rejected the scene as outside the studio's creative direction. The render consumed 18 credits without explicit approval. Retained as a production record.

## 1. Scene brief

An abandoned-looking municipal pump room is still doing its job. In a shallow puddle beneath a rusted overhead pipe, a ripple tightens, a bead of water rises against gravity, and the pipe drinks it back through a pinhole.

- **Reality anchors.** Worn ivory tiles, a drain grate, a rust-stained pipe coupling and a single burgundy valve wheel establish the room's use and scale. The pipe and floor share the same frame so the viewer can see the air gap.
- **World rule.** Only the water directly below the pinhole rises. The bead picks up a silver highlight as it lifts, follows one vertical path and vanishes into the underside of the pipe. A wet mark stays at the opening and the puddle surface settles.
- **Discovery.** Read the pipe and puddle in the first second. See the puddle gather around one spot, follow the rising bead with the eye, then hold on the wet pipe and quiet floor.
- **STEPPS hypotheses.** Emotion comes from the small shock of watching a familiar leak run upward. Social Currency comes from a precise, easy-to-describe image of a pipe drinking from the floor. Audience response is unmeasured.
- **References and scope.** Original fictional room with no external assets. One 6-second vertical draft render. Spend capped at the single draft quote.

## 2. Art direction and shot plan

**Editorial Rupture.** Readable charcoal shadows frame a hard silver shaft from a high grated window at left. Faint haze makes the shaft visible, with crisp tile joints and cast iron in focus. A dull burgundy valve is the sole color accent and sets human scale. The water is the only surreal accent. Its surface tension, highlight and lasting wet mark give the effect physical weight.

**Camera.** One locked-off vertical shot at about 0.7 m with a moderate-wide field of view. See the pump-room floor in the lower third and the underside of the pipe across the upper third. Leave clear negative space along the bead's route. Keep both endpoints sharp. The viewer tracks the bead through the frame.

| Anchor | Fixed features | Allowed change | Check |
| --- | --- | --- | --- |
| Pipe and valve | Horizontal pipe, one coupling, valve on right, pinhole above puddle | Local wet mark | Before lift, at contact and final hold |
| Tile wall and drain | Straight grout grid, drain left of puddle | Light and reflection consistent | Entire shot |
| Puddle and bead | Puddle fixed to floor under pinhole | Local dimple, bead rises once, ripples settle | Takeoff, midair, arrival |

**First test.** Does one readable bead travel from the floor to the pipe while the room holds its geometry? Pass if both endpoints stay visible, the travel direction reads at phone size and the pipe, valve, grout and grate hold position. Check whether the wet mark and settling ripple register. Picture-only draft. A later sound pass could use room hum and a small wet tick at the pipe.

## 3. Generation

- [First-frame prompt](Prompts/Opening-Still-v01.txt) records the intended composition for a still-based follow-up if needed.
- [Motion prompt](Prompts/Motion-v01.txt). First test is text-only to see whether the simple locked composition and one action hold in a single low-resolution render.
- **Take 01 submitted.** Higgsfield job `a45d1bfb-cda0-43cd-bb0e-d1c635b43a69`. The tool echoed the submitted motion prompt and confirmed Seedance 2.5, text-to-video, 6 s, 9:16, 480p, audio off, no input media. One request with an 18-credit quote. Transaction history shows a matching 18-credit Seedance 2.5 charge at submission. Seed was unavailable.

## 4. Review and finish

**Take 01 · Rejected.** [Archived render](Renders/01-Upward-Leak.mp4), 480 × 854, 24 fps, 6.04 s. Publication status is private. Picture review sampled across the shot at 4 frames per second.

| Check | Result | Observed in take 01 |
| --- | --- | --- |
| Aesthetic and scale | Pass | The left window motivates the silver light through the air gap. The burgundy valve, worn tile and drain give the room scale. The rendered wall is largely plain and the window enters frame. |
| Camera and geometry | Pass | Pipe, coupling, valve, window, floor grout and grate hold their positions across the sampled frames. Both endpoints stay visible. |
| Object persistence | Pass | One dominant bead stays on a continuous upward path. A thin trailing thread breaks into small droplets near takeoff. The puddle stays anchored to the floor. |
| Material response and contact | Rework | Around 1–2 s the bead lifts and sends rings across the puddle. Around 3.5–4.5 s it reaches the pipe, holds an almost perfectly round shape as it overlaps the metal, then disappears. A wet glint remains and the ripples fade, but the bead's deformation as it joins the pipe is hard to see. |
| Audio | N/A | Audio was disabled for this picture test. |

## 5. Checklist feedback

The preproduction review overemphasized a single visual effect and technical test. The next scene brief should show what the viewer learns about the world through visible function, scale and use. Review the written direction and obtain explicit approval for generation spending before submitting a render.
