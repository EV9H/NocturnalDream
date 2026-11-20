# Handoff prompt: The Night the Huangpu Froze

**Status: on hold (2026-11-19).** The owner wants a break from the Shanghai theme. The next big run is [The Beacon Engines](../The-Beacon-Engines/HANDOFF-PROMPT.md).

Paste everything in the block below into a new session started in this repository.

```text
You are directing a new Nocturnal Dream film. Load the nocturnal-dream skill first and follow it. Read chapters 01, 02, 03, 04, 05, 06 (including failure codes F11–F15), 09 and 10 before drafting anything. Also read Scenes/Shanghai-After-the-Snow/REVIEW.md, especially takes 08 and 09, for what worked and what failed on Jimeng.

## The direction (chosen, but needs the owner's approval as a written treatment)

Working title: 《黄浦江冻住的那一夜》 / The Night the Huangpu Froze. Episode 2 of the "Shanghai, impossible weather" series, after Shanghai After the Snow.

- Anchor (universal, every generation): the Bund, the Huangpu River and the Lujiazui skyline.
- Impossible condition: after the great snow, the Huangpu has frozen solid from bank to bank. Ships and ferries are locked in thick ice, and for one night people walk across the river from the Bund to Pudong.
- One-second test: frame 1 must read as "that's the Huangpu, and it's frozen". The river surface must be clearly ice (white, ridged, with pressure cracks), not dark water, and the Oriental Pearl must be readable.
- Feeling: awe at the scale, then a shared, quiet wonder as tiny figures cross a river that should be impossible to walk on.
- Likely comments (hypotheses): "走路去陆家嘴上班", "轮渡失业了", "上海人这辈子没见过".
- Generation reach: all ages.

## Format

- One Seedance 2.5 generation on Jimeng, 9:16, 20–30 seconds, as a short cut sequence of 3–4 shots in a single generation. Seedance 2.5 on Jimeng accepts 4–30 s and supports timed shots. Check the live schema before writing.
- Suggested shot order (refine in the treatment):
  1. Hook, 0–5 s: from the Bund railing, the frozen river and Pudong, with a ferry locked in ice in the middle distance. Mostly still, with the light snow ending.
  2. Scale, 5–12 s: a wide, slightly high view of tiny dark figures walking across the ice toward Pudong in loose lines. No faces.
  3. Detail, 12–20 s: a close, low view of a ferry hull gripped by ice, frost on its rails and windows lit, and a long crack running across the ice.
  4. Payoff, 20–30 s: a long wide hold. First blue light behind Lujiazui, the crossing figures small against the towers, warm windows reflected on ice.
- Sound: deep ice groans and cracks, distant footsteps on ice, one muffled ship horn, a low city hum, and silence before the final hold. No music, no speech.

## Rules that are not optional

- Approval gates: write the one-page treatment (chapter 02 format) and get the owner's approval before generating anything. Then quote every video generation and ask for spending approval with the exact amount, unless the quote is 0.
- Free runs: the owner has two free Seedance 2.5 runs on Jimeng (see Studio-Reference/Subscriptions.md). Use one for this film at the highest resolution that still quotes 0 credits (try 1080p, then 720p). Run it with `--credit-ceiling 0` so nothing can be charged. If the quote is not 0, stop and ask.
- Keyframe first ("the still is the film"): make the shot 1 first frame as a still before any video. Use Jimeng's image models (Seedream 5.5 is unlimited on the owner's plan, but check the quote is 0). Generate 4–8 candidates, pick the best with keyframe QC, and show the owner before the video run. Use it as the first frame (`first_last_frame` mode).
- Geography: viewed from the central Bund, the left-to-right order is the Oriental Pearl, Jin Mao, the World Financial Center, then the Shanghai Tower. Keep the convention-centre globes beside the Pearl. Keep the Bund's wave-pattern railing correct.
- Avoid the known failures:
  - F14: no feet or boots in a level POV.
  - F15: no gusts or weather that hide the anchor.
  - F11: lit windows uneven, not a grid.
  - F12: name any object that must persist across shots.
  - No real people's faces, no brands or logos, no on-screen text.
- Tools: use the dreamina-canvas CLI (already installed and logged in), on the existing canvas "Shanghai After the Snow" or a new canvas for this film. Verify the charged credits after each run with `auth account`.
- Records: create Scenes/The-Night-the-Huangpu-Froze/ with PRODUCTION.md (brief, treatment, approvals), Prompts/ (every prompt as submitted, versioned), Renders/ (every output), and REVIEW.md (observations by timecode, kept separate from judgment). Review video with dense frame samples, at least every 0.5 s across every action beat, not just 8 frames.
- Post with Douyin's AI declaration turned on.

Start by restating the direction in two lines, then write the treatment for approval.
```

## Why this direction (for the owner)

- **It is the series.** Same city, same storm, one step more impossible. Viewers who liked the snow will recognise episode 2 at once.
- **The impossibility reads in one second.** A frozen Huangpu needs no explanation, and the crossing figures give it a human scale and a story ("people walked to Pudong").
- **It is epic without needing faces or dialogue,** which suits what the models do well and the studio's rules.
- **It uses 20–30 s,** so the free run buys far more film than the 8 s takes did.
