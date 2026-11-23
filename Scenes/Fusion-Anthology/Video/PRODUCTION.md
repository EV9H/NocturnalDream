# 异空间合集 · Fusion Anthology: video version

**Status (latest):** test clips 01 and 03 rendered free on 2026-11-23 and both pass. Clips 02 and 04–07 are quoted at 64 credits each and waiting for the go-ahead. Earlier status: seven nodes saved and quoted.

## Idea

- **Source:** the seven 图文 images from `../POST.md`, each turned into a short "living still".
- **The move:** in every clip, one slow handheld push forward toward the seam where the building stops and the landscape begins.
- **Motion:** small natural movement only (grass, waves, sand, a drip, a curtain). No people walking and no camera turns.
- **The cut:** each clip is trimmed to about 3 seconds, giving roughly 21 seconds with one music track across the cut.
- **Test:** post the video a few days after the 图文 of the same images. Compare swipe-away, completion, and likes and saves per 1,000 views.

## Settings

- **Model and mode:** Seedance 2.5 (`seedance_2.5`), `first_last_frame` with the first frame only. Image 1 is the first frame.
- **Format:** 3:4 to match the stills, 720p, 4 s (the model's minimum), 1 output per node.
- **Prompts:** `Prompts/01…07-*-v01.txt`, about 200 words each. They follow the skeleton in chapter 06: two beats, a fixed list and a separate sound paragraph.
- **Drip room source:** referenced by resource `e0886c86-91cf-4996-9bdf-275639532d45` (T25 take a, the one in the set). The node also holds take b.

## Nodes and quotes (2026-11-23)

| # | Clip | Video node | First frame |
| --- | --- | --- | --- |
| 01 | Corridor → field | `node_mhewtbn332` | `node_9gzpqq5yqp` |
| 02 | Internet café → grassland | `node_m0bwckk1ea` | `node_y7ygqemr9b` |
| 03 | Night train → sea | `node_e3esvm5rzq` | `node_y98sj1h3km` |
| 04 | Drip room → sea | `node_3fmjeyng72` | res `e0886c86…` |
| 05 | KTV → desert | `node_cbh87049dr` | `node_yndsr9405z` |
| 06 | Supermarket → snow | `node_d6zgdm4qmt` | `node_nx94n598mj` |
| 07 | Bathroom → tide | `node_t6vk4gezsd` | `node_e80aat8yt0` |

**Quotes:**
- **720p, 4 s:** 0 credits for each node, 0 in total (`node quote`, draft version 481).
- **1080p, 4 s:** 256 credits for one node (node 01 quoted at 1080p, then set back to 720p).

**More quotes (2026-11-23, node 01, 4 s, 3:4, one clip each):**
- Seedance 2.5 at 480p: 48.
- Seedance 2.5 Flash at 480p: 28.
- Seedance 2.5 Flash at 720p: 76.
- Seedance 2.5 draft (样片模式) at 480p: 36.

Node 01 was set back to Seedance 2.5 at 720p afterwards.

**The owner says only two free 720p runs remain.** The full price of Seedance 2.5 at 720p can't be quoted while the free runs show 0. My estimate is about 110 a clip, scaled by pixel count from the 1080p quote of 256. That figure is not verified.

**Caution.** A quote of 0 means each run is free on its own. It does not prove all seven stay free once submitted together. Run with `--credit-ceiling 0` so nothing is charged.

## Risks to watch

- The seam melts or drifts as the camera pushes in.
- The flash-lit foreground pulses, because the light source moves with the camera.
- Small text in 01 (door numbers) and 05 (the karaoke screen) may change into gibberish.
- Seedance may add music, despite "No music" in the prompts.

## Test clips 01 and 03 (2026-11-23)

**Approval.** The owner said to use the two free 720p runs on the corridor and the night train.

**Run.** Quoted 0, run under `node confirm --credit-ceiling 0`. Charged 0: the balance went 12,323 → 12,348; the rise is presumably a credit top-up, not a refund.

| # | Node | Submit | Resource | Render |
| --- | --- | --- | --- | --- |
| 01 | `node_mhewtbn332` | `84eaeb71-e894-4018-b5de-4a561d37f757` | `fae63b9a…` | `Renders/01-Corridor-Field-v01.mp4` |
| 03 | `node_e3esvm5rzq` | `2cc0e6d5-d08f-472e-a37c-f8176091a249` | `e4210b10…` | `Renders/03-Night-Train-Sea-v01.mp4` |

**Files (verified with ffprobe).**
- Both are 834×1112 (3:4), 60 fps, 4.06 s, with an audio track.
- Audio, by level only (not listened to):
  - 01: mean −40 dB, peak −24 dB.
  - 03: mean −35 dB, peak −17 dB.

  Both levels suggest quiet ambience rather than music. Not verified by ear.

**Observations (frames at 0.5 s intervals, plus first and last frames at full size)**
- **01 Corridor → field:**
  - One continuous forward move. It goes further than asked: it starts inside the corridor and ends just past the ceiling edge, with the field, the two lone doors and the apartment blocks filling the frame.
  - The seam stays a clean edge. The carpet stays continuous into the worn path, and the sunset sky and buildings hold their shape.
  - The room-service tray stays in place and gets closer.
  - *Drift:* the door number plates change as they pass (301 → a garbled "30…"); they are small and blurred.
- **03 Night train → sea:**
  - A slow push down the corridor. The opening frames the sea, the curtained berths standing in the water and the lamp-lit platform shelter. The water surface moves slightly.
  - The carriage geometry holds. The seam stays at the threshold line.
  - *Drift:* the lidded enamel mug at the far left leaves the frame early. The motion is small overall.

**Judgement (mine, unconfirmed)**
- Both pass. The seam holds under a push-in, and there is no melt, no cut and no pulsing light.
- 01 is the stronger clip, because the move carries you out of the building. It works as the opening shot.
- 03 is calmer and almost a still. It suits a middle slot.
- The lesson for the remaining five: the push can be bigger than "half a metre". 01's larger move is what made it.

**Quote for the remaining five (2026-11-23):** Seedance 2.5, 720p, 4 s, 3:4 is **64 credits each, 320 in total**, for clips 02, 04, 05, 06 and 07. My earlier estimate of about 110 was wrong.

## Owner's direction on camera (2026-11-23): replaces the "drift" idea

The owner said the slow forward drift in the v01 prompts is not what they want, because it reads like a camera rig. Clips 01 and 03 v01 are kept as tests, but the v01 approach is superseded. The owner will continue the video work in a separate session.

**Decide the camera for each shot before writing the prompt:**
- **Fixed camera.** Often the right choice. The life comes from objects and changes in the frame:
  - a screen glowing or flickering in an organic or strange way, or something appearing or moving on a screen;
  - grass moved by wind, or an object or snow blown across the frame;
  - lens defects, flare, halation, light blooming.
- **Handheld.** Say where the shot starts, what it aims at (for example down at the legs or feet, then somewhere else), and when the aim changes.
- **POV.** Decide whether hands appear. Use head-like movement: a glance, a dip, a turn.

### Starting proposal per clip (mine, for the owner and the video session to accept or change)

| # | Clip | Camera | What moves |
| --- | --- | --- | --- |
| 01 | Corridor → field | Handheld POV, no hands | Starts aimed down at the red carpet and the room-service tray beside the feet. Two slow steps, then the gaze lifts to the open end and the field, and stays there. Grass at the seam moves in the wind. |
| 02 | Internet café → grassland | Fixed | The near CRT rolls a scan bar and flickers. Out in the grass, the monitors blink on and off unevenly, one after another. The grass moves in the wind. Faint CRT glow and lens bloom. |
| 03 | Night train → sea | Fixed, at the berth | A breeze from the open end lifts the nearest blue curtain. The water rocks slightly around the berths. The platform lamp flickers once, with a small flare. |
| 04 | Drip room → sea | Fixed | A drop forms and falls in the drip chamber in the foreground. Waves wash around the chair legs. The ferry's light blinks on the horizon. |
| 05 | KTV → desert | Fixed | The karaoke screen pulses and a colour bar sweeps across it, with no readable text. Fine sand blows in across the table edge. Moon flare on the lens. |
| 06 | Supermarket → snow | Handheld POV with hands | Both hands on the handle of a shopping trolley, pushing it slowly along the freezer row toward the seam, the trolley's front wheel wobbling. Snow blows in across the floor. |
| 07 | Bathroom → tide | Fixed, from the doorway | The shower curtain lifts in a sea breeze. A wave runs up around the tub's feet and slides back. A drip falls from the tap. |

**Mix:** five fixed clips, one handheld POV without hands, one POV with hands. That gives the cut a rhythm instead of seven identical pushes.

## v02 round: clips 02 · 06 · 07 (plan in `PLAN-v02.md`)

**Approval (2026-11-23).** The owner approved the v02 plan and the spend: test 02 first (64), then 06 and 07 if 02 passes; cap 192 for three takes, rerolls ask again.

### Take 02 v02 · Internet café → grassland (fixed, degauss hook)

- **Prompt:** `Prompts/02-Internet-Cafe-Grassland-v02.txt` (372 words), saved into node `node_m0bwckk1ea` (retitled `…-v02`; v01 prompt kept in `Prompts/` and was never run).
- **Settings as saved:** Seedance 2.5, `first_last_frame`, first frame only (`node:node_y7ygqemr9b`), 3:4, 720p, 4 s, 1 output.
- **Quote:** 64 (draft version 526). **Confirmed** with ceiling 64. **Submit:** `b45367af-da5e-4aac-9a98-b9a4525a9762`. **Resource:** `c783d68b-333d-4091-856d-0670d5697839`. **Charged:** 64 (node reports `creditsAmount: 64`; balance 12,348 → 12,284).
- **File:** `Renders/02-Internet-Cafe-Grassland-v02.mp4`, sha256 `484a1b63…`. ffprobe: 834×1112, H.264, 60 fps container (node reports 24 fps effective), 4.06 s; AAC stereo 44.1 kHz.
- **Audio levels (astats / volumedetect, not listened to):** mean −28.2 dB, peak −5.5 dB. Short-window RMS: −42 dB at 0–0.2 s, a burst to −17 dB at about 0.2–0.4 s, then a steady decay to about −40 dB by 3 s, slight rise at the end. Fits a hit near the start then fading bed; whether it is a degauss thunk, and whether there is music, is **unverified until the owner listens**.
- **Review frames:** `Review/02-v02-frames-0.5s.png`, `Review/02-v02-first-second-8fps.png`, `Review/02-v02-field-strip.png`.

**Observations**
- Camera stays locked for the whole take; ceiling edge, fluorescent tube, horizon light and pylon hold position. No cut, no zoom.
- Degauss: a rainbow ripple crosses a monitor from about 0.375 s to 0.75 s, then the picture returns. It lands on the **monitor cut off at the left edge**, not the noodle-cup CRT named in the prompt. It covers roughly a tenth of the frame width.
- Field: the monitors in the grass do not flicker and recover; they **switch off in a chain**, the far-left group from about 1.0 s to 2.0 s, the nearer large one at about 2.5 s, and they stay off. Two or three stay lit at the end.
- Grass: a visible gust bends the lit grass at about 1.5–2.5 s.
- Look: phone-flash look, noise and tilt held; no pulsing of the flash-lit desks.

**Judgement (mine, unconfirmed)**
- The hook arrives in time (motion by 0.4 s) but is **small and on the edge** of the frame; on a phone it may read as a glitch rather than a degauss.
- The chain of monitors switching off was not asked for, but it is the stronger event: the field "going to sleep" gives the clip a beginning and an end, and it reads at phone size.
- Usable as a middle or closing clip as is. As the opener, the first second is weaker than planned.
- Repair, if wanted: name the degauss target by position *and* size ("the largest monitor, centre-left, with the noodle cup in front of it") and accept the chain-off as the field beat.

**Owner verdict (2026-11-23): fail.**
- The loud hit at the start (the degauss thunk) does not fit: the set needs a dreamcore sound world, not a jolt.
- The degauss looks wrong: the colour ripple spills off the screen onto the monitor's plastic casing.

**What to repeat:** the locked camera (held for 4 s, no drift, no pulsing); the field monitors going dark one after another (not asked for, not objected to).
**What failed:** a sharp transient sound as the hook (taste, not a technical fault); a screen effect described as a sweeping ripple, which the model painted over the casing as well as the glass.
**Next test:** 02 v03 with no hits and no screen distortion: soft breathing glow and a slow fade on the field monitors, wind already moving the grass at frame 1, a quiet, muffled bed. See `Prompts/02-Internet-Cafe-Grassland-v03.txt`.

### Take 02 v03 · Internet café → grassland (fixed, dreamcore: breathing glow and slow fade)

- **Prompt:** `Prompts/02-Internet-Cafe-Grassland-v03.txt`, in a **new node** `node_cwded4bfbf` at x 3256, y −3300 (end of the video row), so v02's take stays on `node_m0bwckk1ea`.
- **Settings:** Seedance 2.5, `first_last_frame`, first frame only (`node:node_y7ygqemr9b`), 3:4, 720p, 4 s, 1 output.
- **Quote:** 64 (draft version 528). **Approved by owner** ("Run v03"). Confirmed with ceiling 64. **Submit:** `e11d0953-690c-4525-a2be-d4a6ff6f9563`. **Resource:** `3dea0ce9-4a19-49d7-88a4-5ca939052071`. **Charged:** 64 (balance 12,284 → 12,220).
- **File:** `Renders/02-Internet-Cafe-Grassland-v03.mp4`, sha256 `a8d1b166…`. ffprobe: 834×1112, 60 fps container, 4.06 s, AAC stereo.
- **Audio levels (not listened to):** mean −44.4 dB, peak −28.8 dB. Peaks in 0.1 s windows stay between −33 and −39 dB with no burst (one window at −29 dB near 3.9 s); the last ~0.4 s is near-silent. About 16 dB quieter on average than v02, and even. Character unverified.
- **Review frames:** `Review/02-v03-frames-0.5s.png`, `Review/02-v03-field-strip.png`.

**Observations**
- Camera locked all through; the ceiling edge, the tube, the horizon and the pylon hold. No cut, no zoom.
- The field monitors fade one by one from the far left to the right, as prompted: first dark by 0.5 s, most dark by 2.5 s. At the end the nearest large field monitor and the ones at the right edge still glow.
- Screen changes stay inside the glass; the casings do not change. No ripple.
- The grass moves only slightly (small shifts of blades between 0.2 s and 2.6 s); the lit grass darkens as the screens near it fade.
- The monitors inside the room stay steady.

**Judgement (mine, unconfirmed)**
- It fixes both of v02's faults. It is calm and dreamlike, and the "field going to sleep" reads at phone size.
- The first second is gentle: the first fade lands by 0.5 s, but the grass motion is too small to count as a hook on its own. That suits the mood. It works better as a second or closing clip than as the opener.

**Owner verdict (2026-11-23): not yet — direction right, too timid.**
- The wind should move the grass much more, and the wind should be heard.
- Some PCs should *flash* (flicker), not just switch off one by one.
- The vibe: dreamcore — soothing, comforting, but an oddity happens.

**What to repeat:** locked camera; screen changes kept inside the glass; a quiet, even bed with no hits.
**What failed:** grass motion too small to read; a tidy, predictable fade with no oddity in it; wind not audible.
**Next test:** 02 v04 (`Prompts/02-Internet-Cafe-Grassland-v04.txt`, 437 words), saved in new node `node_zajtms6mpk` at x 3616, y −3300; quoted 64 (draft version 532); waiting for spend approval. Changes: strong wind with big travelling waves for the whole shot; three named monitors (two in the field, one in the room) flicker irregularly between blue and soft white, the room one sometimes in time with a field one; wind as the main, clearly heard sound with a soft buzz swelling with the flicker.


**Music previews (local only, not uploaded).** `Previews/cut-01-02v03-03-music1…4-*.mp4`: clips 01 v01, 02 v03 and 03 v01 cut together (4 s each, 12 s). Each preview uses one track from the owner's Downloads, starting 30 s in and loudness-normalised to −16 LUFS, over the generated beds. For judging fit only. The tracks are commercial releases, so for posting use Douyin's library.

### Take 02 v04 · Internet café → grassland (fixed, strong wind, flickering screens)

- **Prompt:** `Prompts/02-Internet-Cafe-Grassland-v04.txt`, node `node_zajtms6mpk` (x 3616, y −3300).
- **Settings:** Seedance 2.5, `first_last_frame`, first frame only (`node:node_y7ygqemr9b`), 3:4, 720p, 4 s, 1 output.
- **Quote:** 64 (draft version 532). **Approved by owner** ("Run v04"). Confirmed with ceiling 64. **Submit:** `a967fe70-8fbd-424e-ad71-9cb0cdd89d6d`. **Resource:** `1f9c444e-3bf9-4920-bb00-c11d5c7fd974`. **Charged:** 64 (balance 12,220 → 12,156).
- **File:** `Renders/02-Internet-Cafe-Grassland-v04.mp4`, sha256 `b1376452…`. ffprobe: 834×1112, 60 fps container, 4.06 s, AAC stereo.
- **Audio levels (not listened to):** mean −40.1 dB, peak −23.7 dB. Peaks in 0.1 s windows run −29 to −31 dB at first, rise to −24 to −27 dB at about 0.9–1.7 s (a swell, not a single hit), then −30 to −35 dB; the last ~0.4 s is near-silent. About 4 dB louder than v03 on average, with no burst. Whether that swell is wind is unverified.
- **Review images:** `Review/02-v04-frames-0.5s.png`, `Review/02-v04-grass-strip.png`, `Review/02-v04-flicker-frames.png`, `Review/02-v04-field-6fps.png`.

**Observations (brightness traced at 12 fps in boxes over each named screen)**
- Camera locked; ceiling edge, tube, horizon and pylon hold.
- **Grass:** visibly more movement than v03. The lit blades lean and shift between 0.3 s, 1.3 s, 2.3 s and 3.3 s. It is not the big travelling waves asked for.
- **Flicker:** two screens change **together**, the large field monitor on the right and the room monitor behind the tea bottle, at about 1.5–1.7 s and 3.3–3.6 s. Each event is a brightness dip and a swap of screen content (white window ↔ plain blue desktop), not a white flash. The third field monitor from the left does not change. Effects stay inside the glass.
- **Frame 0 to frame 1:** the two named screens brighten noticeably on the first frame change (box mean about 130–166 → 210); the whole frame changes by about 2 luma levels. A small pop that may show at the start of the clip.

**Judgement (mine, unconfirmed)**
- Closer to the brief: the grass now reads as wind, and the oddity of a room screen answering a field screen is there.
- Still under-powered: the flicker reads as two screens changing pictures rather than flashing, and the wind is a breeze, not big waves.
- If repeated: describe the flicker as brightness ("flashes bright white, then back to blue"), not as a signal or content; ask for waves "as tall as the monitors" with a named scale.

**Owner verdict (2026-11-23):** "kinda pass". The owner then asked whether the video is worth posting at all, compared with the 图文 post.

## Round learnings (2026-11-23, after 02 v02–v04)

**Spend:** 192 credits on clip 02 (three takes of 64). 06 and 07 not run; 128 of the approved cap left unspent.

**Decision:** post the 图文 first. Hold further video spend. For the planned comparison, cut 01 v01 + 02 v04 + 03 v01 (12 s, Douyin library music), post a few days after the 图文, and compare swipe-away, completion and saves per 1,000 views. No new credits.

**Repeat**
- Locked camera for screen and nature motion: it held for 4 s on all three takes, with no drift, cuts or pulsing flash.
- Keep screen effects inside the glass, and say so in the Fixed line (v03, v04).
- Make a new canvas node per prompt version, so every take stays on the canvas.
- Trace brightness in a box over each named object at 12 fps to see what actually flickered (v04).

**Failed**
- A sharp sound as the first-second hook (v02 degauss thunk). It breaks the dreamcore mood. Dreamcore here means **soothing, comforting, but an oddity happens**.
- Describing a screen effect as a "ripple sweeping across" (v02). The model painted it over the casing.
- Timid motion (v03). A slow, orderly fade with near-still grass is calm but has no life and no oddity.
- Describing a flicker as "a weak signal reaching them" (v04). The model swapped screen content instead of flashing light. Two of three named screens obeyed, together.
- **Format:** fixed "living stills" of a one-image idea add atmosphere but no information. They look like a photo in the first second, and each clip took about three takes to reach "kinda pass". For this set the 图文 does the job for free.

**Next test (only if the video beats the 图文)**
- Video must show what a photo can't. One continuous 8–15 s walk per world: start inside an ordinary room, the walls end, step out across the seam, and one dreamcore oddity happens (clip 01's move out of the corridor is the evidence).
- If a v05 of 02 is ever made, ask for light changes only ("flashes bright white, then back to blue"), and give the wind a scale ("waves as tall as the monitors").

**Proposed for chapter 06 (not adopted, needs a second scene)**
- Failure code proposal **F18 · Effect spills off its object.** A screen or surface effect described as a sweep or ripple spreads onto the surrounding casing or wall. First fix: describe it as a brightness change and add "only inside the glass; the casing stays unchanged" (02 v02 failed, v03–v04 held).
- Realism-phrasing proposal: for a flicker, name brightness, not cause. Cause words ("signal", "glitch") invite content changes (02 v04).
