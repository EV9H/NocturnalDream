# Handoff prompt: fusion videos — internet café, supermarket, bathroom

Paste the block below into a new session started in this repository.

```text
You are directing three short videos for Nocturnal Dream (Douyin account RJK). They are built from three stills in the 异空间 fusion set: an ordinary room whose ceiling and walls stop at a clean edge, so the room runs straight into an everyday landscape.

Load the nocturnal-dream skill first. Read chapters 04 (cinematography), 05 (keyframes, especially "motion-ready first frame"), 06 (video prompting and failure codes F1–F17), 07 (sound and edit) and 09 (resolution tiers). Then read:
- Scenes/Fusion-Anthology/POST.md: the set and its sources.
- Scenes/Fusion-Anthology/Video/PRODUCTION.md: settings, quotes, the two test clips, and the owner's camera direction.
- Scenes/Fusion-Anthology/Video/Renders/01-Corridor-Field-v01.mp4 and 03-Night-Train-Sea-v01.mp4: what the first tests looked like.

## The three clips

| Clip | Still (first frame) | Video node already saved (v01 drift prompt, superseded) |
| --- | --- | --- |
| 02 Internet café → night grassland | Image-Set-Lab/Renders/T23-Internet-Cafe-Grassland-Seedream-free-v01.png, node node_y7ygqemr9b | node_m0bwckk1ea |
| 06 Supermarket → snow plain | Image-Set-Lab/Renders/T19-Supermarket-3am-Fusion-Seedream-free-v02.png, node node_nx94n598mj | node_d6zgdm4qmt |
| 07 Bathroom → tide | Image-Set-Lab/Renders/T28-Bathroom-Tide-Seedream-free-v01.png, node node_e80aat8yt0 | node_t6vk4gezsd |

Look at each still before planning. The look is an old phone camera with flash (2006–07): flash burning the nearest objects, fast falloff into noisy dark, JPEG blocking, a tilted handheld frame. Keep that look in the video.

## The owner's direction on camera (most important)

The slow forward "drift" of the v01 prompts is rejected; it reads like a camera rig. For each clip, decide the camera deliberately before writing:
- Fixed camera: often the right choice. The life comes from the frame: a screen glowing or flickering in an organic or strange way, something appearing or moving on a screen, grass moved by wind, an object or snow blown across the frame, lens defects, flare, bloom.
- Handheld: say where the shot starts, what it aims at (for example down at the legs or feet, then elsewhere), and when the aim changes.
- POV: decide whether hands appear; use head-like movement (a glance, a dip, a turn).
Starting proposals are in PRODUCTION.md ("Starting proposal per clip"): 02 fixed (CRT scan-roll and flicker, field monitors blinking unevenly, wind in the grass); 06 POV with hands pushing a shopping trolley along the freezer row toward the snow; 07 fixed from the doorway (curtain lifting in sea breeze, a wave around the tub's feet, a tap drip). Improve or replace them. Say why.

## Audio (design it, do not leave it to the model)

Seedance generates sound with the picture. For each clip write a separate sound paragraph:
- the listening point (where the ear is);
- the room tone of the inside space, close and specific (CRT whine and fan hum; freezer compressors, a trolley wheel clicking; a tap drip in a tiled room);
- the outside landscape as a separate layer (wind over grass and crickets; cold wind over snow; small waves on sand);
- how the sound crosses the seam: the inside sound thins and the outside grows, or one sound bridges both;
- one hero sound with timing, and where silence falls;
- "No music, no speech" (music is added in Douyin). Mid-frequency hero sounds, for phone speakers.
After each take, measure levels with ffmpeg (volumedetect or astats). Mark the sound as unverified until the owner has listened.

## Multi-reference stills for consistency (use where it helps)

If a clip needs a second angle, a second place in the same world, or a two-shot cut, first make extra reference stills so places and objects stay consistent:
- Make them with Seedream 5.5 image-to-image (i2i), using the original still as the reference, in the same phone-flash look. Examples:
  - a closer view of the trolley handle and the freezer row from the shopper's position;
  - the bathroom seen from the sand looking back into the room;
  - one monitor out in the grass, close.
- Then use them in Seedance 2.5 m2v mode (up to 30 image references, each with one stated job: "Image 1 sets the place, light and look; Image 2 is the view after the turn").
- Or use first_last_frame with an end frame. Keep the end frame close to the first camera position, or you get a hard cut (F16).
- Propose the reference plan in writing before generating.

## Settings, cost, approvals

- Video: Seedance 2.5 (seedance_2.5), 3:4, 720p, 4 s minimum. Live quote on 2026-11-23: 64 credits per 4 s clip at 720p; 1080p is 256. The two free 720p runs are used. 480p is for tests only (chapter 09). Quote again before any run; durations other than 4 s will cost differently.
- Stills: Seedream 5.5 only (other models were rejected as AI slop). Free in the Jimeng web canvas with 0积分畅用 on, via the in-app browser pane, which is signed in; otherwise 6 credits each through the CLI. The image cap is 1,000 credits for 2026-11; about 287 are used. Log every charge in Scenes/Image-Set-Lab/REVIEW.md.
- Credits: about 12,300 on the Jimeng account; the monthly credits do not roll over.
- Approvals (AGENTS.md):
  - Get the owner's approval of the written plan for each clip (camera, motion, sound, references) before generating anything.
  - Get separate spending approval with model, output count and quoted cost; ask again if a run would exceed the approved cap.
  - Test one clip before running the others.
- Canvas: the project is "Nocturnal Dream Image Sets" (93c6f2e6-545a-4d1f-a1b0-25c9cf1a224e). The owner organises it, with groups for some sets. Do not drag nodes in the web canvas; move nodes only with the CLI. The video row sits at y = −3300 under the fusion stills. Put new reference stills in a labelled row next to it.

## Records and review

- Version the prompts as Scenes/Fusion-Anthology/Video/Prompts/02-…-v02.txt and so on. Keep v01.
- Save renders in Video/Renders/ and keep every take.
- Log each take in Video/PRODUCTION.md: node, submit ID, settings, quote and charge, ffprobe facts, frames at 0.5 s intervals, observations, your judgement marked as yours, and the owner's verdict.
- At the end, record what to repeat, what failed and the next test. Propose any changes to chapter 06 with the supporting takes.

Done means: three clips the owner has approved (or clear reasons and a next test for any that failed), logged as above, ready to cut into the fusion video with clips 01 and 03.
```
