# Handoff prompt: The Beacon Engines

Paste everything in the block below into a new session started in this repository.

```text
You are directing a new Nocturnal Dream film. Load the nocturnal-dream skill first and follow it. Read chapters 01, 02, 03 (the Megastructure Sublime look), 04, 05, 06 (including failure codes F11–F15), 09, 10 and 11 (ancient-China megastructure) before drafting anything. Also read Scenes/Shanghai-After-the-Snow/REVIEW.md, especially takes 08 and 09, for what worked and failed on Jimeng.

## The direction (chosen, but needs the owner's approval as a written treatment)

Working title: 《烽火机关》 / The Beacon Engines.

- Anchor (universal, every generation): the Ming Great Wall, snaking over mountain ridges.
- Real system to fork (chapter 11): 烽燧, the beacon towers that relayed smoke and fire signals along the Wall. Check the real history before the treatment, and label the invented part as alternate history.
- Fork: the beacon towers never stopped growing. Each one is now a mountain-sized engine of timber bracket sets (斗拱), grey brick, bronze gears and water wheels fed by mountain streams. When it fires, a great bronze ring turns at its top and a signal flame is lit, and the next engine on the next ridge answers.
- Rule and cost: the engines run on water and timber. Show the water channels, the soot, the repairs, and the tiny guards and porters who tend them.
- Era anchor: Ming. Keep the brickwork, crenellations, roof forms and clothing consistent with Ming.
- One-second test: frame 1 must read as "that's the Great Wall, and that tower can't be real". The Wall must be unmistakable, and the engine must be impossibly large but structurally believable.
- Feeling: awe at scale, then the quiet thrill of a signal travelling to the horizon.
- Likely comments (hypotheses): "原来烽火台是这样", "这是明长城吧", "古人要是真造出来了".
- Generation reach: all ages.

## Format (decided by the owner)

- One Seedance 2.5 generation on Jimeng: 16:9, 720p, 30 seconds. The owner saw it quoted free. Check the live quote first.
- POV, one continuous take if the model holds it, as a walker on the Wall at blue dawn. Suggested beats (refine in the treatment):
  1. Hook, 0–5 s: eye-height POV on the Wall's walkway. The Wall climbs a ridge ahead, and the beacon engine rises at the top of the ridge, its upper ring in thin cloud. Instantly legible.
  2. Approach, 5–14 s: the POV climbs the Wall's steps toward it. Camera bob, crenellations passing, worn bricks. Tiny figures on the engine's galleries show its scale.
  3. Base, 14–22 s: arrival at its foot. A slow tilt up the timber bracket sets and bronze gears, water pouring through a wheel, steam from a vent, a bronze bell swinging.
  4. Payoff, 22–30 s: the great ring turns, the signal flame lights at the top, and on the far ridges the next engines light one after another into the distance. Wide hold.
- Sound: mountain wind, footsteps on brick (heard, never seen), timber groan, water through the wheel, a bronze bell, a distant chain of answering gongs. No music, no speech.

## Rules that are not optional

- Approval gates: write the one-page treatment (chapter 02 format, plus the chapter 11 pitch check) and get the owner's approval before generating anything. Quote every generation and ask for spending approval with the exact amount, unless the quote is 0.
- Free runs: the owner has two free Seedance 2.5 runs on Jimeng (see Studio-Reference/Subscriptions.md). Run this one with `--credit-ceiling 0` so nothing can be charged. If the quote is not 0, stop and ask.
- Keyframe first ("the still is the film"): make the 16:9 first frame as a still before any video. Use a Jimeng image model (Seedream 5.5 is unlimited on the owner's plan; check the quote is 0). Generate 4–8 candidates, check the Wall's Ming details against real photos, pick the best with keyframe QC, and show the owner before the video run. Use it as the first frame (`first_last_frame` mode).
- Avoid the known failures:
  - F14: no feet or legs in a level POV. Show walking through camera bob and passing bricks, and sound.
  - F15: no weather that hides the anchor.
  - F11: uneven windows and lamps.
  - F12: name the engine, the ring and the flame as persistent objects.
  - Chapter 11 clichés: no neon, no decorative gears, no glowing circuits, no mixed dynasties.
  - No faces, no brands, no on-screen text.
- 30 s risk: one continuous 30 s take may drift. Write the beats with timestamps (Seedance 2.5 accepts them). Review the result with frames every 0.5 s across the whole clip, especially the approach and the tilt.
- Tools: use the dreamina-canvas CLI (installed and logged in) on a new canvas named "The Beacon Engines". Verify the charged credits after the run with `auth account`.
- Records: create PRODUCTION.md (brief, treatment, approvals, sources for the real 烽燧 history), Prompts/ (every prompt as submitted, versioned), Renders/ (every output) and REVIEW.md (timecoded observations, kept separate from judgment) in this folder.
- Delivery note: 16:9 shows letterboxed on Douyin unless viewed full-screen. It suits B站 and the 横屏 viewer. Record which platforms it goes to.
- Post with Douyin's AI declaration turned on, and credit the real 烽燧 history in the description.

Start by restating the direction in two lines, then write the treatment for approval.
```

## Why this direction (for the owner)

- **The Great Wall is the most universal anchor in China.** It passes the one-second test for every viewer, which the school scene did not.
- **It is a megastructure with a real root.** Beacon towers really relayed signals along the Wall. The fork turns that into the payoff: a chain of lights crossing the mountains. Viewers who know the history will comment.
- **POV and 16:9 suit it.** The Wall to the horizon is a wide subject, and climbing toward the engine gives the POV a reason to move.
- **It's a fresh theme** after Shanghai, and it could become its own series: other engines, other passes (山海关, 嘉峪关).
