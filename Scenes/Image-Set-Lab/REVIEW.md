# Image-Set Lab — style experiments

These are single-image tests to find the look for image sets before any set is planned. The canvas is [Nocturnal Dream Image Sets](https://jimeng.jianying.com/ai-tool/ai-canvas/93c6f2e6-545a-4d1f-a1b0-25c9cf1a224e) (project `93c6f2e6-545a-4d1f-a1b0-25c9cf1a224e`). Every run used Seedream 5.5 in the web canvas with **0积分畅用** on. The CLI quoted 18 credits for 3 images and has no free switch.

## Credit ledger

The cap is 300 credits for 2026-11, approved 2026-11-20. Free runs come first; credits are spent only when the free queue stalls, one image per run.

| Date | Test | Model | Credits | Running total |
| --- | --- | --- | --- | --- |
| 2026-11-20 | T03 panda cover, Image 2 (`node_pg69v02ddm`, submit `2b213160-b65f-468b-9d5f-eea8c6601e16`) | 图片模型 Image 2, 3:4, 2K, high | 77 (balance 12,420 → 12,343) | 77 |
| 2026-11-20 | T02 metro snow cover (`node_40r6sqf6jr`, submit `766aca08-eba9-4c56-b10d-a7b6c6a17b32`) | Image 2.5 Pro, 3:4, 2K | 4 | 81 |
| 2026-11-20 | T04 giant moon cover (`node_n4xcf90mct`, submit `434a166f-0c7a-48ea-9514-4604d550fc77`) | Image 2.5 Pro, 3:4, 2K | 4 (balance → 12,335) | 85 |
| 2026-11-20 | T03 panda cover, Seedream paid (`node_tr7tswh79q`, submit `158ce81a-2ab0-4e09-a5f0-c4bc36e1b93c`) | Seedream 5.5, 3:4, 2K | 6 (balance → 12,329) | 91 |
| 2026-11-20 | T05 The Same Afternoon cover (`node_3jf072z43j`, submit `68b1f92d-4f67-42b3-9e6d-21e072d10e60`) | Seedream 5.5, 3:4, 2K | 6 | 97 |
| 2026-11-20 | T06 The Ballroom cover (`node_rcfa2v7j6f`, submit `9d8b1f3b-79ed-475a-8f5d-d52ccfca74c3`) | Seedream 5.5, 3:4, 2K | 6 | 103 |
| 2026-11-20 | T07 The Pool at 4am cover (`node_nt2w8qtcww`, submit `f7b3e09f-8c29-4e0b-96f1-32ef675d45a1`) | Seedream 5.5, 3:4, 2K | 6 | 109 |
| 2026-11-20 | T08 The Last Bus cover (`node_793a7c7pdj`, submit `47d51eae-3686-4aed-9a30-c348b1a213a1`) | Seedream 5.5, 3:4, 2K | 6 | 115 |
| 2026-11-20 | T08 The Last Bus image 2 (`node_r3dn8022m8`, submit `e2f6abdb-044a-44b8-b797-76ce1a87b513`) | Seedream 5.5, 3:4, 2K | 6 (quoted 6, `creditsAmount` 6) | 121 |
| 2026-11-20 | 散场以后 02 Picture Palace v03 (`node_80k46kjqbt`, submit `84c30a82-c727-4e26-b2fb-2b12c97d54c7`) | Seedream 5.5, 3:4, 2K | 6 | 127 |
| 2026-11-20 | 散场以后 03–06 v03 (`node_8q13yw4epd`, `node_ta23ztck57`, `node_z94per6zem`, `node_nvrb4v53tn`; submits `93c62795…`, `cee9c49c…`, `65b36045…`, `cba91d52…`) | Seedream 5.5, 3:4, 2K, quoted 24, ceiling 24 | 24 | 151 |
| 2026-11-20 | 散场以后 02–06 v04 (`node_2xhedneqd4`, `node_d0qep080y0`, `node_9ck1r5mcqw`, `node_xmcqp2qy17`, `node_3ac7dhray8`; submits `ad9310cb…`, `4fe59a91…`, `44d1c9a0…`, `13ad9e7e…`, `e116acf6…`) | Seedream 5.5, 3:4, 2K, each quoted 6, ceiling 6 | 30 | 181 |
| 2026-11-20 | 散场以后 v05 fight, rain run, leaving (`node_vgmtn35ebq`, `node_xzcwnzxdmt`, `node_1w33gm2xsn`; submits `06627a2a…`, `e9de4b7f…`, `9036f1bf…`) | Seedream 5.5, 3:4, 2K, each quoted 6, ceiling 6 | 18 | 199 |
| 2026-11-20 | 散场以后 v06 rain + carried (`node_4kjjt7z11t`, `node_ceg6htz7ck`), v07 rain (`node_0c4md9zp6n`; submits `c43fbeec…`, `b450db07…`, `38018a88…`) | Seedream 5.5, 3:4, 2K, each quoted 6, ceiling 6 | 18 | 217 |

**Mistake: the T03 Image 2 run was too expensive.** Image 2 quoted 77 at high 2K. The "same at every setting" check I did then was wrong: those edits failed because no prompt was passed, so the quote never changed. The owner said "don't use expensive" just after the run was accepted, and neither the CLI nor the web task list offered a way to cancel it. I should have quoted the cheaper models first. Image 2.5 Pro quotes 3 credits at 1K, 4 at 2K and 5 at 4K. From now on, paid runs default to Image 2.5 Pro (or Seedream 5.5 at 6). Quote first, and skip anything above about 10. 图片美学模型 V8.2 always makes 4 outputs, so it is out under the one-image rule. Two Image 2 nodes (`node_40r6sqf6jr` T02, `node_n4xcf90mct` T04) were saved and quoted but never run.

## T01 — Hukou Falls, the Yellow River runs clear (concept 《黄河清了》)

| Take | Node | Settings | Cost | Renders |
| --- | --- | --- | --- | --- |
| v01 | `node_7f2jfvpx9y`, submit `d42bae67-79bf-482d-80f9-a6af43407f20` | t2i, 3:4, 2K (1728×2304), 3 outputs | 0 credits each (verified from `creditsAmount`; balance stayed at 12,420) | `Renders/T01-v01-1..3.png` |
| v02 pastel deadpan | `node_0rd5g0m9z3` | t2i, 3:4, 2K, 3 requested; the owner cancelled one because the queue was slow | 0 (balance stayed at 12,420) | `Renders/T01-v02-1..2.png` |

Prompts are in `Prompts/T01-*`.

**Observations**
- v01: the water turned clear green and the silt stains on the banks read correctly. The framing is centred at the tourist viewpoint, everything is equally sharp, and the overcast is flat. Image 2 shows the green as a strip of colour inside the falling water, which looks wrong.
- v02: a high, wide deadpan frame, pale overexposed pastels, a small man in a dark coat with a red bucket on a sandstone shelf, and a jade channel. The man and the green water are the only accents. The falls are small and do not read as Hukou in one second.

**Owner's judgement:** "too bland". No artistic filter and no photographer's framing. The owner also dislikes the 黄河清 concept. They sent two style references: a flash-lit bar cat shot low and tilted on Provia, and a Chinese metro platform with a central vanishing point and motion blur. These are written up as the Taste section in the [image-set skill](../../Studio-Reference/Skills/nocturnal-dream-image-sets/SKILL.md).

**Repeat:** the free web route; downloading through `dreamina-canvas resource download`.
**Failed:** postcard framing, and no named photographic reference before prompting.
**Next test:** a new concept in the candid flash or street look, one image per generation.

**References researched (for v02)**
- Zhang Kechun, *The Yellow River*: 4×5 large format, overexposed on overcast days, pastel. [Huxley-Parlour](https://huxleyparlour.com/critical-texts/zhang-kechun-the-yellow-river/), [It's Nice That](https://itsnicethat.com/articles/zhang-kechun-photographer-241016)
- Nadav Kander, *Yangtze, The Long River*: small figures set against vast construction. [LensCulture](https://www.lensculture.com/articles/nadav-kander-yangtze-the-long-river)
- Edward Burtynsky, *Water*, Xiaolangdi Dam: aerial, painterly abstraction. [Hyperallergic](https://hyperallergic.com/flow-charts-edward-burtynskys-photos-of-the-worlds-watery-parts)
- Fan Ho: hard light and shadow geometry in Hong Kong streets. [M+](https://www.mplus.org.hk/en/magazine/10-facts-about-the-photographer-who-documented-1950s-and-60s-hong-kong/)

## T02–T04 — first covers in the candid look (2026-11-20)

All three had the same prompt for both routes (`Prompts/T02..T04-*`). The free Seedream 5.5 runs (`node_8nj7de4wze`, `node_fzvgqp984p`, `node_e2vcxnfys3`) were submitted 10:35–10:36 and were still queued at the time of writing. The paid runs are below.

| Test | Model | Render | Observations | Judgement (mine, unconfirmed) |
| --- | --- | --- | --- | --- |
| T02 metro snow | Image 2.5 Pro, 2K, 4 credits | `Renders/T02-Image2.5Pro-v01.png` | Central vanishing point down the platform, a woman standing still and looking up, commuters blurred by motion, umbrellas indoors, slush on the tiles, a red LED board with readable correct Chinese (本次列车 2分钟). Snow lies on the train roof, which reads as outdoors. It looks slightly digital/HDR, with little grain. | Strong and close to Ref B. It needs more grain and less sharpening, and no snow on the train. |
| T03 Chengdu panda | Image 2, 2K high, 77 credits | `Renders/T03-Image2-v01.png` | Flash-lit panda at a 串串 table holding a skewer and looking into the lens. An out-of-focus green bottle in the foreground, red and green stools, a scooter, diners behind. Provia-like colours. Very close to Ref A. | The most catchy. Test whether Image 2.5 Pro (4 credits) can reach the same level. |
| T04 giant moon | Image 2.5 Pro, 2K, 4 credits | `Renders/T04-Image2.5Pro-v01.png` | The 城中村 alley, laundry, cables, an auntie in pyjamas filming, neighbours at a barred window, a wet floor. The moon looks pasted on: no moonlight on the walls, and the image is HDR-flat. | The weakest. The light logic fails. |

**Owner's verdicts (2026-11-20).** Image 2.5 Pro is "really bad and AI slop", so use Seedream only. The owner doesn't like metro snow, so that concept is dropped.

**T03 panda on Seedream 5.5** (`Renders/T03-Seedream-v01.png`, 6 credits). A flash-lit panda sits upright on a red plastic stool at a 串串 table, paws on the table, looking into the lens. In the foreground is a green bottle that is sharp, not out of focus, and a cup of skewers. Diners and stools sit behind. It reads as natural, with no tilt and less flash falloff than asked. It is less stylised than the Image 2 version, but it doesn't look like a render.

## T05–T08 — liminal covers, Caretaker mood (2026-11-20)

The owner set the new direction: liminal, not limited to China, The Caretaker's mood. Each prompt names the camera, lens, film, era, angle and height. The free runs (`node_mr4yqfz135`, `node_zs53h61qrj`, `node_wgmbym7srh`, `node_eapb9vj74y`) were stuck in the queue, so at the owner's request the paid runs were made on Seedream 5.5 at 6 credits each (balance 12,329 → 12,305). Renders are `Renders/T05..T08-Seedream-v01.png`.

| Test | Observations | Judgement (mine, unconfirmed) |
| --- | --- | --- |
| T05 The Same Afternoon | A real-looking 1980s British-style living room. A sunbeam across a floral carpet, steam from a cup, dust in the beam, framed photos, a clock, an old TV, the doorframe blurred at left. The aged warm slide-film colour reads true. | The strongest of the four, with no AI sheen. It works as the stage-1 cover for a fading sequence. Next, test a middle stage (photos blank, furniture blurred). |
| T06 The Ballroom | A decayed ballroom with a peeling ceiling, mirrors, tables with cloths, streamers on parquet, one chandelier. The couple is only partly blurred: the man is fairly sharp, and the woman's dress is blurred. | Atmospheric but close to stock "romantic" imagery. It needs much more ghosting, and a harder flash or a longer exposure. |
| T07 The Pool at 4am | Very convincing early-2000s compact-camera look. An airport gate floor as a lane-marked pool, caustics on the ceiling tiles, seats standing in the water, one traveller with feet in the water, a parked plane outside. | Strong. It passes the one-second test and feels liminal and found. |
| T08 The Last Bus | Seen through a rain-specked window with the bus interior reflected (yellow rails, a fluorescent strip, red halation). A lit shelter in a dark grass field. The advertising panel glows red, not the white that was asked for. | Very strong mood, and the closest to the music. |

## T08 The Last Bus — image 2 (2026-11-20)

**Why T08.** The owner liked T05, T07 and T08. I picked T08 for three reasons. It is the closest to the Caretaker mood. Its structure (**one journey**: the same window seat while the world outside changes) gives a natural reason to swipe. And it lets the following images carry mood alone, with the oddity kept to the cover. These are my reasons; the owner has not confirmed them.

**Planned set (proposal, not approved):** 1 the shelter in the field (cover, oddity) → 2 a sleeping suburb, one lit window (no oddity) → later images go on through the night from the same seat. The last image should pay off the cover or leave a question.

**Image 2 brief:** the same look, camera position and interior reflection as the cover. Outside is an ordinary foggy suburban street at 3 am with one lit upstairs window and a sodium streetlight. Reference: Todd Hido, *House Hunting*. No oddity. Prompt: `Prompts/T08-Last-Bus-Image2-Seedream-5.5-3x4-v01.txt`.

**Route.** The free queue was still stuck. `node_mr4yqfz135` (T05 free) still showed `running`, and the T06–T08 free nodes were `empty`. I added a node in the web panel, but it did not keep the prompt, so I did not submit a free run. The run was paid through the CLI: quote 6, `--credit-ceiling 6`. Render: `Renders/T08-Image2-Seedream-v01.png` (1728×2304).

**Observations**
- Seen through the bus window: a two-storey suburban house with a porch, and one upstairs window lit warm yellow behind a curtain, with red halation around it. A sodium streetlight at the kerb, with strong red halation and raindrop bokeh around the lamp. A small hatchback parked to the left of the light. A wet road, motion-smeared in the lower third. Neighbouring houses fade into haze.
- The interior reflection is strong: two fluorescent strips, a yellow pole, a curved grab rail, and a row of empty seats laid over the right half of the house. The window frame and the rounded pane corner are visible at the right and bottom.
- Different from the prompt: the fog is a light haze rather than low fog between the houses. The frame is warmer and more orange than the cover's teal-green. Grain is lighter than asked. The streetlight is not smeared sideways; the motion shows only on the road. The bottom fifth is empty road, which is clear for the caption.
- No readable text, faces or obvious warped geometry. The reflected seats cross the house façade like a double exposure, which a real window reflection does.

**Judgement (mine, unconfirmed).** It matches the cover's look (CineStill halation, yellow rail, fluorescent reflection) and passes as a real photo, so it sits next to image 1 as the same ride. The lone lit window carries the feeling without an oddity. Weak points: it is cleaner and warmer than the cover, and the reflected seats take up a lot of the frame. Seen side by side, the shift from green to orange may jump.

**Repeat:** copying the Look, Camera and Light blocks between images. Naming the reference photographer.
**Failed:** adding a node in the web panel by clicking the toolbar. The empty node did not keep the typed prompt. Next time, create the node with the CLI and open it in the web panel to switch 0积分畅用 on.
**Next test (one change):** if the owner wants a closer match to the cover, rerun image 2 with only the colour changed: "cooler overall, teal-green like the frame before, sodium orange limited to the lamp's pool". Otherwise, go on to image 3.

## Canvas housekeeping (2026-11-20)

- **The free queue moved.** `node_mr4yqfz135` (the T05 free cover, started that morning) finished at 0 credits. It is saved as `Renders/T05-Seedream-free-v01.png`. The T06 free run (`node_zs53h61qrj`) was still running. The T07 and T08 free nodes are empty and have no resource.
- **The canvas is laid out in rows** using `node edit --x/--y`, and each row has a text label node. From the top: T08 (the set in progress), T07 and T05 (liked), then T06, T04, T03, T02 and T01, then one unused blank node (`node_faq35fr27z`, "图片 1"), which can be deleted. Each row reads: label, the free node, then paid takes from left to right. No node was deleted.

## Owner's verdict on T06 (2026-11-20)

The owner called T06 The Ballroom "perfect" and asked for a 4–6 image set built from it, with different scenes on the same theme. This overrides my earlier judgement that it was close to stock romantic imagery. The set lives in `Scenes/After-Everyone-Left/`, and T06 is its cover.

## Handoff for the next session (2026-11-20)

- **Done:** 散场以后 · After Everyone Left. The 4 final images were picked; see `../After-Everyone-Left/REVIEW.md`. Its rows are at the top of the canvas.
- **Credits:** 217 of the 300 cap are used for 2026-11, leaving 83.
- **Next:** find new set ideas on the same canvas. Start a new row above the 散场以后 header (y < −3600), or in a new block to the right.
- **What worked on 散场以后:**
  - One light with emphasis.
  - A different framing and action in each image.
  - A story arc across the set.
  - Propose ideas first, test one image, then batch.
- **How the owner picks:** by colour tags on the canvas.

## T09–T13 — light and colour covers (2026-11-20)

**Why.** The owner asked for new set ideas on the same canvas, with more play with light, colour and niche artists. Each idea got one cover test, with an artist reference and a colour recipe in the Look block. Prompts are `Prompts/T09..T13-*-v01.txt`.

**Route and credits.**
- The canvas row is at y = −4200 above the 散场以后 group, with the label node `node_5f55zhsc9p`.
- T10 ran free in the web canvas with 0积分畅用 on and the price showing 0/张. It finished within a few minutes.
- T09, T11, T12 and T13 ran paid on Seedream 5.5 at 3:4 and 2K. Each quoted 6 credits, and the four were confirmed under a ceiling of 24.
- Month total: 217 + 24 = **241 of 300**, leaving 59. The balance read 12,179 afterwards. I did not check the balance before the runs, so the 24-credit charge comes from the quotes and is not verified against the balance.

| Test | Node | Submit | Render |
| --- | --- | --- | --- |
| T09 停电那晚 · Power Cut | `node_defqwvpryz` | `78dca0a5-5efa-4375-8ec5-7be3183827bd` | `Renders/T09-Power-Cut-Seedream-v01.png` |
| T10 最后一场 · Last Reel (free) | `node_ppc916jcsm` | web panel | `Renders/T10-Last-Reel-Seedream-free-v01.png` |
| T11 洗衣房 · Laundromat | `node_mx6mtrf3q2` | `7671dbdc-26c6-464f-bd2c-6206aac03f8e` | `Renders/T11-Laundromat-Seedream-v01.png` |
| T12 等候 · Waiting Hall | `node_g7dtzr5e0a` | `a4913bbf-67f4-4c50-924f-4475c0dbd8f9` | `Renders/T12-Waiting-Hall-Seedream-v01.png` |
| T13 暑假最后一天 · Last Day of Summer | `node_33yrhxv2be` | `115fe805-ffbb-4be4-9ac5-3d7e4a8d101b` | `Renders/T13-Last-Day-Summer-Seedream-v01.png` |

**Observations**
- **T09:** three teenagers from behind on a rooftop ledge, the middle one pointing up, with a candle jar glowing amber beside her. Laundry, an antenna, a bamboo mat, potted plants and a rusted tank blurred in the foreground. A dense Milky Way fills the upper half. *Differs from the prompt:* many windows in the towers are still lit, so the blackout doesn't read. The starlight casts no visible shadows. The cross-process colour is weak, giving a clean, digital-looking night with only a faint red edge leak.
- **T10:** a man alone, seen from behind, in rows of red velvet seats. A beach home movie of a child running into the waves is on the screen. A teal-green beam with dust in it, and peeling columns. The look is close to Superia: green shadows and warm red seats. *Differs from the prompt:* the image on screen is sharp and bright, not a faded flickering home movie. The beam enters from the upper left, not from behind the camera. The foreground seat fills the lower third, which is fine for the caption.
- **T11:** seen through a steamed, rain-streaked window. A woman in a red scarf sits, a man in a grey coat stands by the dryers, and one dryer door shows a sunset sea, which throws an orange pool on the floor tiles. A green fluorescent tube, and a vending machine with blurred colour. The sunset is a perfectly centred sun on the horizon. No readable text.
- **T12:** a high mezzanine view of a bright mid-century terminal. About eighty travellers in mustard, teal, coral, cream and green coats stand in a pool of skylight with hard shadows, and the railing is soft in the foreground. *Differs from the prompt:* the crowd is not looking up at one spot. Most stand facing different ways, and no one clearly looks at the camera. The oddity is missing.
- **T13:** a chain-link fence sharp in the left foreground. A girl holding a basketball stands in a magenta pool from one streetlight, a boy sits by his fallen bike, and a third teenager stands at the far hoop. A deep cyan sky over low houses. The palette and the two light sources match the recipe. The finish is fairly clean and digital, with light grain.

**Judgement (mine, unconfirmed)**
- **T10 and T11 are the strongest.** Each one carries its colour idea, and in both the light belongs to the story. T11's oddity reads instantly as a thumbnail but is close to a postcard; next time, a lower, hazier sun.
- **T13 has the most original palette.** It needs grain and imperfection to stop looking like a render.
- **T09 fails its own premise because of the lit windows.** The next test should change one thing: "every window in every building is dark, no electric light anywhere".
- **T12 is a good Prager pastiche without the oddity.** It needs "every head tilted back looking up at the same point" in a stronger wording.

**Repeat:**
- Naming an artist plus a two-colour recipe in the Look block.
- One free run in the web panel while the others run paid.

**Failed:**
- Seedream ignores negative crowd and blackout directions ("no lit windows", "all looking up").
- Cross-processing as a term had little effect.

**Next:** the owner picks by colour tag on the canvas, then the chosen idea gets image 2.

**Owner's verdict (2026-11-20).** Ideas A (T09 停电那晚) and E (T13 暑假最后一天) are dropped. The owner said this kind of format and genre feels "much inferior". Both are teenage, nostalgic slice-of-life scenes with people as the subject. Still open: T10 Last Reel, T11 Laundromat and T12 Waiting Hall. The nodes stay on the canvas untouched.

## T14–T16 — a crowd plus one focal person (2026-11-20)

**Why.** The owner judged T10–T12 good artwork that doesn't invite a feeling the way the last dance did. What T12 did well: its colour palette, the way it redirects the viewer's eye, and its sense of mass. The new direction is a crowd in a controlled palette, one person breaking the pattern, and a Douyin emotion. The owner reminded me to specify the colour palette, the artist, photography or film reference, the lens, the filter and the camera angle, and to ban AI fake smiles. Every prompt now has a "Colour palette, strictly" line, a named filter (Tiffen Black Pro-Mist), and avoid lines for posed smiles, plastic skin and cloned people.

**Route.** All three ran **free** in the web canvas with 0积分畅用 on, one after another. Each finished in about 40 seconds. 0 credits; the month stays at 241 of 300. Row y = −4800, label `node_h0gr4n0g5k`.

| Test | Node | Render |
| --- | --- | --- |
| T14 婚礼上的那个人 · The One at the Wedding | `node_49jxtvzhpz` | `Renders/T14-Wedding-Seedream-free-v01.png` |
| T15 逆行 · Against the Flow | `node_9ypmgxr031` | `Renders/T15-Against-the-Flow-Seedream-free-v01.png` |
| T16 倒计时 · Countdown | `node_xmdcfhgc0w` | `Renders/T16-Countdown-Seedream-free-v01.png` |

**Observations**
- **T14:** a balcony view over about 30 red-clothed round tables in a 2000s-style Chinese banquet hall. Lazy Susans full of dishes, guests holding up phones, petals on the carpet, and the couple on a red stage at the upper left (bride in a red qipao). A blooming chandelier, a red railing soft in the foreground. It reads as a real event photo, with natural, unposed faces. *Differs from the prompt:* there is no single turned guest. Many guests across the hall face toward the camera, so the eye has no focal point. Jade barely appears. The stage spotlight is not the brightest point.
- **T15:** a high view down a crowded station waiting hall. The crowd smears in motion with red bags and red-and-white woven sacks. One woman in a celadon coat stands sharp and still in the centre, facing the camera, with a warm pool of light at her feet. Newspapers and an orange on the floor. Some blurred signage at the upper right, not readable. Natural faces, no fake smiles.
- **T16:** a riverside crowd from behind, magenta and green fireworks over a skyline, and phone screens in the foreground. In the middle, the couple face each other, very close. *Differs from the prompt:* it reads as a kiss, not as ambiguous. The fireworks look like stock and fairly digital, with little grain or flash character. The crowd is in muted dark coats, as asked.

**Judgement (mine, unconfirmed)**
- **T15 is the strongest.** It has the T12 qualities (palette, mass, a single focal point drawn by motion contrast) plus a strong Douyin emotion (过年不回家). Motion blur against one still figure is the device that worked.
- **T14** has the most cultural texture and is the most believable as a found photo, but it lacks the focal person. Next test, one change: make every guest's back face the camera (so the camera sits behind the crowd), and keep the one man turned toward us.
- **T16** works on its idea, but it looks the most like AI and the most like stock. It is the lowest priority.

**Repeat:**
- Motion blur against one sharp figure, to redirect the eye.
- An explicit colour-palette line.
- Free runs back to back (about 40 seconds each when the queue is clear).

**Failed:** asking for "everyone faces X except one" when the camera sits on the same side as X. The model then turns faces toward the lens.

**Owner's verdict (2026-11-20): T14–T16 all dropped, much worse than T10–T12.**
1. **The mass doesn't work.** The crowd takes up too much of the frame, is badly drawn, and makes the central character less obvious.
2. **The lighting looks like AI.** No texture, no real source or physically traced light, not realistic.
3. **T15:** the Hong Kong lens intent shows, but the angle and the story are not good enough.

**Lesson.** A crowd as the subject is the wrong reading of T12. What T12 had was a curated palette and a guided eye inside a designed space. Any light must come from a source you can see in the frame. Next, curated, art-photographer design with fewer clichés, back to the skill's liminal theme.

**Owner's verdict on the "Next Door" pitch (2026-11-20).** Rejected before any generation. The owner called "a man and a woman lean on the same shared wall, never knowing" dramatic, cliché and not realistic, and said liminal is not like this. People are optional: zero, one or many. I had kept pushing couple and near-romance plots since 散场以后. From now on the space comes first and there are no plot beats.

## T17–T18 — place first (2026-11-20)

Both ran free, 0 credits. Row y = −5400, label `node_cgdt00f9wy`.

| Test | Node | Render |
| --- | --- | --- |
| T17 样板间 · The Show Flat | `node_2x6kjz5y1f` | `Renders/T17-Show-Flat-Seedream-free-v01.png` |
| T18 凌晨三点的服务区 · The Service Area at 3am | `node_tqrkbrecej` | `Renders/T18-Service-Area-Seedream-free-v01.png` |

**Observations**
- **T17:** a living room seen frontally from the doorway. A printed sunny skyline backdrop behind sheers, its upper-right corner peeling to show plywood, with a track spot aimed at it. Plastic film on the sofa, plastic lemons, blank books, blue shoe covers, and construction-site blue at the right edge. *Differs from the prompt:* the downlights don't throw distinct pools. The room is evenly and softly lit, with a clean interior-render finish.
- **T18:** a fluorescent green canopy over pumps at the left, two sodium lamps glowing orange in fog, one coach lit inside, the service building with two vending machines and a mop bucket, cracked asphalt and dry grass in the foreground. *Differs from the prompt:* passengers are not readable through the windows. The grass is at the edge rather than growing through the cracks. The finish is clean, with little grain.

**Judgement (mine, unconfirmed).** T18 is the closer of the two to T05–T08: real sources, fog and quiet. T17 has the concept but looks like an architectural render.

## Prompt comparison: T05–T08 and T10 against T09–T18 (2026-11-20)

The owner asked why the later covers fall short of T05–T08 and T10, and whether the later work had polluted the skill. Both prompt sets were read side by side.

**What T05–T08 share.** They were written at 10:51, *before* the skill rewrite at 11:09.
- **About 230 words.** The later prompts run 255–414.
- **A found or amateur camera:** a Pentax K1000 family snapshot, a Canon PowerShot, a Leica with CineStill. The view is a person's own: a doorway, a gate seat, a bus seat. No large-format or tripod "authored" views, except the ballroom.
- **Colour comes from naming the film and how it has aged.** No "Colour palette, strictly" lists, and no diffusion filters.
- **No artist names in T05–T07,** and one in T08 image 2. The later prompts stack two or three.
- **Light is written into the scene as a physical event:** "low golden sun ... lays one long, sharp rectangle of light across a patterned carpet". There is no separate Light block with percentages.
- **Short avoid lines** of 4–6 items. The later ones list 10–15, including "HDR, CGI, teal-orange".
- **One plain idea and zero or one figure,** with no plot.

**Where the drift came from.**
1. **Memory, not the skill.** The 散场以后 lessons ("one emphasised light, about 70% dark", "figures with actions and tension", "a story arc") were saved as general rules. I then carried them into every new prompt. That caused the couples and plots and the "70 percent darkness" lines. The memory is now scoped to that set.
2. **The skill template was written after T05–T08 and asks for more than they had.** It requires a separate Light block, says to name a reference artist, and asks for every block to be filled. Read literally, that pushed the prompts towards long, over-specified "spec sheets" and authored views.
3. **My additions on top:** palette lists, Pro-Mist filters, large-format cameras, and long avoid lists. None of these came from evidence that they work.

**The skill file has not changed since commit `aa6d2d2`.** It contains nothing from T09–T18.

**Skill change (2026-11-20).** The owner approved the shape: keep the skill short and put the examples in their own file.
- §3 is rewritten as "a snapshot, not a spec sheet":
  - 200–250 words in five parts.
  - The light goes inside the scene.
  - No palette lists or filters.
  - A person's own viewpoint.
  - People only as they would really be there.
  - A short avoid list.
- §1 now says at most one reference artist per prompt.
- New file: `Studio-Reference/Skills/nocturnal-dream-image-sets/EXAMPLES.md`, holding the T05, T06, T07, T08 and T10 cover prompts.
- Evidence: the comparison above, T05–T08 and T10 against T09–T18.

## Owner's vibe board: four target looks (2026-11-25)

The owner shared eight Douyin screenshots as the quality bar: 氛围柔光 (A), shiny 国风 texture, light and colour (B), mega core (C) and film texture (D). The analysis, measurements, a draft look block per lane and the open questions are in `VIBE-BOARD-2026-11-25.md`. The screenshots and a contact sheet are in `References/vibe-board-2026-11-25/`. No generation yet.

**Skill change (2026-11-25), from the vibe board.** The owner asked for these looks to become directions in the image-set skill.
- **New chapter:** `Studio-Reference/Skills/nocturnal-dream-image-sets/LOOKS.md` holds four lanes (A 氛围柔光, B 国风 shine, C mega core, D cinema film texture). Each lane has:
  - a paste-ready look block;
  - a "there when" checklist;
  - target numbers;
  - a ladder of one-lever fixes;
  - known failure modes;
  - a "best so far" slot.
- **New script:** `scripts/measure_look.py` measures a render against a lane's ranges. It was calibrated on the eight references, all of which read on target. Run on T150–T250 renders, about 10% clip their whites (99th percentile at 245 or more), against none of the references.
- **SKILL.md changes:**
  - New sets start from a lane, and a lane's look block overrides the default camera, film and filter rules.
  - Lanes B and D may test 2.39:1; 3:4 stays the default until the owner decides.
  - The review step now runs the measurement.
  - Sets cut between wide and close.
- **EXAMPLES.md** now has a slot for lane winners.
- **Supporting evidence:** the owner's eight references only. No take has hit a lane yet, so the ranges should be re-centred on our first confirmed hit.

## LA01–LD01: round 1 of the target-look lanes, one cover per lane (2026-11-25)

- **Brief (owner):** "lets try one for each, and whatever ratio that the popular douyin posts use." Each lane took the frame shape of its reference post: A 9:16 (full-screen), B 21:9, C 3:4 (图文), D 21:9.
- **Prompts:** each opens with its lane's look block from `LOOKS.md`, copied unchanged.
  - **LA01:** a concrete bus shelter on an empty coastal road, under a cumulus tower.
  - **LB01:** a woman in white silk asleep on a giant backlit lotus leaf on a misty pond. The curled leaf shades her face, as the resting rule requires.
  - **LC01:** looking up an impossibly tall 福建土楼, with a waterfall from the sky circle and one rose-blossom tree by the well.
  - **LD01:** a lone lit phone booth on a wet desert highway at blue hour, seen through a rain-beaded windshield, in the style of Robby Müller's *Paris, Texas*.
- **IDs:** these use their own range (LA01–LD01), because a parallel session started T251–T255 ("Slide" prompts) in this lab three minutes before this round.
- **Runs:**
  - Free first: the canvas sat on "Loading canvas" for more than 20 seconds in the pane, as in the last six rounds, so all four ran paid under the one-minute rule.
  - Seedream 5.5 (`seedream_5.5`), t2i, 2K, count 1. Quote 24; `node confirm --credit-ceiling 24`; one `node run` with four submit IDs. Each `creditsAmount` is 6.
  - **Spent 24 (balance 8,923 → 8,899).** By this log's running total the month is **1,595 of 3,000**, not counting the parallel T251–T255 round if it ran paid.
  - CLI note: in zsh a flag list held in one variable is passed as a single argument, which caused the first confirm to fail with "unrecognized option". `node run` takes `--credit-token` from `node confirm`, not `--credit-ceiling`.
- **Canvas:** smart layout put the column at x 4400, y −31117 to −29561.
- **Files:**
  - Prompts: `Prompts/LA01…LD01-*-v01.txt`.
  - Renders: `Renders/LA01…LD01-*-Seedream-paid-v01.png`.
  - Each take beside its reference: `Renders/contact-sheet-LA01-LD01-lanes-vs-refs.jpg`.

| Take | Node | Submit | Ratio | Size |
| --- | --- | --- | --- | --- |
| LA01 | `node_ntfkn8hnz0` | `42ea5386…` | 9:16 | 1440 × 2560 |
| LB01 | `node_w2pz6j7g5f` | `d75eabbe…` | 21:9 | 3024 × 1296 |
| LC01 | `node_khs6t2rg84` | `9d113900…` | 3:4 | 1728 × 2304 |
| LD01 | `node_sfrgr0zynr` | `40a68c33…` | 21:9 | 3024 × 1296 |

**Measurements** (`measure_look.py --lane`):

| Take | Sat | Lum | White | Dark% | Vig | Off target |
| --- | --- | --- | --- | --- | --- | --- |
| LA01 | 87 | 154 | 250 | 2 | 0.37 | sat low, far too bright, whites clip, corners darker than the reference |
| LB01 | 71 | 119 | 251 | 9 | 0.61 | sat low, slightly bright, the sun disc clips |
| LC01 | 29 | 62 | 219 | 40 | 0.48 | slightly too dark (40% against at most 35) |
| LD01 | 124 | 42 | 120 | 52 | 0.76 | too saturated and too dark; shadows blue, not green-teal (shG −1) |

**Observations**
- **LA01:**
  - The shelter is small at the centre on the horizon line. The road makes a diagonal from the bottom left, and a tall cumulus fills the upper half.
  - The top corners fall to navy and the blacks are lifted. The cloud is blown out rather than softly blooming, and only the bottom edge is smeared.
  - The lower half is pale asphalt and sand, so blue covers far less of the frame than the pool does in A1.
- **LB01:**
  - The lotus leaf glows translucent yellow-green with lit veins, and droplets shine on it. Crimson lotus flowers stand in the foreground and the mist.
  - Hands and feet are hidden. Her face is softly lit under the curled leaf.
  - The robe reads as matte cotton gauze, not glowing silk. The palette is green-gold rather than the reference's gold-cream.
- **LC01:**
  - Rings of timber galleries and tiled eaves narrow to a round sky opening. A thin waterfall falls the whole height into mist, and a rose-blossom tree stands beside a round well, with a few warm windows.
  - About 12–15 rings are visible, the top is clear (no cloud inside the shaft), and the sky circle is large.
  - Small red paper on the doors is unreadable.
- **LD01:**
  - The dashboard and wiper are silhouetted, and raindrops become amber bokeh discs. A lit phone booth stands by a curving wet two-lane road, its reflection on the asphalt, with poles to the horizon and a haloed moon.
  - The whole frame is deep saturated blue and darker than D2. Grain is faint at phone size.

**Judgement (mine, unconfirmed)**
- **LC01 is closest to its lane.** It has the C1 grammar (round opening, light column, tiny tree) and a Chinese anchor read in one second. Its weakness is scale: it reads as a very tall building, not an impossible one. **Next lever (scale):** a tiny sky dot, rings "beyond counting", and the upper half dissolving into cloud inside the shaft.
- **LD01 has the strongest mood and story** ("the call nobody made") and the best foreground element. It is too late and too blue. **Next lever:** move the time to early blue hour with a luminous sky and tan desert, keeping everything else.
- **LB01 has the right shine source** (the backlit leaf, the droplets), but it is greener and brighter than B, and the silk doesn't glow. **Next lever (material):** a sheer gold-cream silk robe that glows where the sun passes through it, with the sun disc hidden behind the leaf.
- **LA01 is a pleasant clean film snapshot but not 氛围柔光:** too bright, too little blue, no real bloom. **Next lever (ladder step 1, route):** apply Douyin's 氛围柔光 to LA01 in the editor (free) before another prompt take. If the prompt route continues, make blue fill the lower half (sea or pool in the foreground) and bring the exposure down.
- **Across all four,** our takes are cleaner and brighter than the references, with less air between the planes.

**Owner's verdict on LA01–LD01 (2026-11-25):** "theme wise, not catchy or interesting enough, keep going for each." On the sleeper: "not getting the hang of it — like 金箔般的丝绸 有种云雾梦幻的远方, color pallete carefully chosen." On D: "is it too high res or something, it is more on the cinematic side than on a 胶片 side." Both notes went into `LOOKS.md` (lanes B and D, and a "catchy theme" rule for every lane).

## LA02–LD02: round 2, catchier themes, plus the B and D notes (2026-11-25)

- **Brief:** "keep going for each", with the notes above. New themes, each aiming at "a place or motif everyone knows, in an impossible state":
  - **LA02:** an old public pool whose deck ends at a sea of clouds, with a lifeguard chair against the cumulus.
  - **LB02:** the sleeper on a floating length of gold-leaf silk above a sea of clouds, with misty jade-blue peaks and two cranes. The palette is a closed list: gold leaf, ivory, a touch of cinnabar, jade-blue mist.
  - **LC02:** the Mount Tai Eighteen Bends stair rising between sheer cliffs and waterfalls to the South Gate of Heaven above the clouds, with one pine.
  - **LD02:** a couple slow-dancing on an empty desert highway at blue hour, their car behind them with doors open and headlights on. The look block is rewritten for 胶片: Contax T2 on CineStill 800T, a scanned negative, clumpy grain, soft focus, "not a cinema camera, not a movie still". It ran at 1.5K instead of 2K.
- **Runs:**
  - Paid; the free canvas was still unusable in the pane.
  - Quote 22 (the 1.5K frame costs 4); `node confirm --credit-ceiling 22`; one `node run`.
  - **Spent 22 (8,899 → 8,877); the month is 1,617 of 3,000 by this log.**
- **Files:**
  - Prompts: `Prompts/LA02…LD02-*-v01.txt`.
  - Renders: `Renders/LA02…LD02-*-Seedream-paid-v01.png`.
  - Sheet: `Renders/contact-sheet-LA02-LD02-lanes-vs-refs.jpg`.

| Take | Node | Submit | Ratio · res | Credits |
| --- | --- | --- | --- | --- |
| LA02 | `node_mmvfbt69j8` | `5cf4b01e…` | 9:16 · 2K | 6 |
| LB02 | `node_yy5jypwtfd` | `8e98c666…` | 21:9 · 2K | 6 |
| LC02 | `node_cdfyz75w7a` | `281ff413…` | 3:4 · 2K | 6 |
| LD02 | `node_k0m8346dte` | `4dfafdbe…` | 21:9 · 1.5K (2268 × 972) | 4 |

**Measurements:**
- **LA02:** sat 110, lum 119, vig 0.41. On target except clouds at 245 and corners darker than the reference.
- **LB02:** lum 161, far too bright; warm everywhere (shadow R−B +71).
- **LC02:** sd 57 and sky at 245: more contrast than C.
- **LD02:** sat 115, a little high; shadows not green (shG −2). Lum 84, black 21 and white 219 are all in range.

**Observations**
- **LA02:**
  - Cobalt water with caustics fills the lower half. The cracked deck ends at a flat sea of cloud with towering cumulus, and a white lifeguard chair stands at the edge.
  - The heavy round vignette looks like a cheap compact. It is still sharp, with little bloom.
- **LB02:**
  - She sleeps in billowing crinkled gold fabric above a cloud sea, with misty blue peaks and two cranes. A red sash shows at the waist, and there is no green.
  - The fabric reads as shiny gold lamé, and the whole sky is washed-out cream-gold. A strand of hair hangs below the silk.
- **LC02:**
  - A long straight stair between wet granite cliffs, with waterfalls on both sides, bands of mist, the red-walled gate at the top and a pine at the foot.
  - The sky opening did not appear: the gate sits in the V of the cliffs.
- **LD02:**
  - The couple embrace in the middle of the road with her dress blown sideways. The car's light flares red-orange behind them, and the wet asphalt and a sunset band glow on the horizon.
  - At 100% the grain is visible, the focus soft and the blacks milky, with halation around the car light: clearly more 胶片 than LD01.
  - The pose reads close to a pre-wedding photoshoot.

**Judgement (mine, unconfirmed)**
- **LA02 passes the one-second test.** You know it's a pool and you know it can't be. It's the first lane-A frame with a hook; the finish is still crisper than 氛围柔光.
- **LC02 is a strong cultural anchor and destination** (十八盘 to 南天门). The risk is plausible-big: Mount Tai really looks a bit like this. The next lever is scale: the stair continuing above a cloud layer, with the gate tiny far above.
- **LD02 moved toward 胶片.** Next: a less posed moment (a candid step or a laugh away from camera, not a near-kiss), and lower saturation.
- **LB02 hit the gold silk and the cloud distance,** but the shine is metallic. The owner's follow-up is below.

**Owner, mid-round (2026-11-25), on the gold sleeper:** "still the gold sky is a bit off — the original might have a 胶片 柔光滤镜 cinematic lens. the shining is soft glow obviously."

## LB03: the sleeper retaken with film and a soft-glow filter (2026-11-25)

- **Change from LB02:** the finish only. The camera line became Kodak Portra 400 on a cine 50mm through a Black Pro-Mist 1/2: "the shine is a soft glow… nothing crisp, glittery or metallic".
  - The silk is sheer, with gold leaf beaten in, glowing amber where the sun passes through it.
  - The sky is "soft hazy blue-grey, warm only close to the sun".
  - The avoid line adds metallic lamé, foil glitter, hard specular highlights and an all-gold sky.
  - Scene, framing and palette list are unchanged.
- **Run:** quote 6, `node confirm --credit-ceiling 6`, `node run`. Node `node_pm3p62srfv`, submit `63a2bc17…`. 21:9 at 2K (3024 × 1296). **Spent 6 (8,877 → 8,871); the month is 1,623 of 3,000 by this log.**
- **Files:**
  - Prompt: `Prompts/LB03-Guofeng-Gold-Leaf-Silk-Sleeper-SoftGlow-v01.txt`.
  - Render: `Renders/LB03-…-Seedream-paid-v01.png`.
  - Progress sheet, from the reference through LB01 and LB02 to LB03: `Renders/contact-sheet-LB01-LB03-sleeper-progress.jpg`.
- **Measurements:** sat 69, lum 167, black 73, white 244. Against B1 (sat 77, lum 101, black 10): much paler and much milkier.
- **Observations:**
  - The sheer translucent silk carries scattered gold-leaf flakes, a few shaped like stars. No metallic sheen.
  - She sleeps in ivory with a red sash, above a cloud sea, with misty blue-grey peaks and one crane.
  - The sky is hazy blue-grey with warmth only near the sun. Every edge is soft; there are no deep shadows anywhere.
- **Judgement (mine, unconfirmed):**
  - The soft-glow finish fixed the two things the owner named: no lamé shine, and no all-gold sky.
  - It overshot into a washed-out, low-contrast frame, and the gold is now pale cream, weaker than B1's rich amber.
  - **Next lever (filter strength):** Pro-Mist 1/4 instead of 1/2. Drop "lifted milky blacks" and "highlights melt", and ask for "rich amber gold, deep warm shadows under the silk". Keep the rest.

**Owner on LB03 (2026-11-25):** "the gold original has more shadow and light contrast, and other elements afar, some more color."

## LB04: the sleeper with contrast, far elements and colour (2026-11-25)

- **Changes from LB03** (the owner's three notes, taken together):
  - **Lighter diffusion:** Pro-Mist 1/4 instead of 1/2, with no "lifted milky blacks" or "highlights melt".
  - **Contrast:** a late, low sun behind-right; deep warm brown and blue-grey shadow in the folds, the robe and the cloud undersides.
  - **The far distance:** crimson and rust-orange maple islands rise from the cloud sea at several distances, with one faint peak, drifting maple leaves, and an out-of-focus maple branch in the lower-left corner.
  - **Palette list:** amber gold, ivory, crimson and rust maple, cinnabar, blue-grey cloud shadow.
  - The cranes are gone. The avoid line adds washed-out haze and flat low contrast.
- **Run:** node `node_697mgbhkj4`, submit `f8ddda83…`, 21:9 at 2K (3024 × 1296).
  - `node quote` returned **0**. I confirmed with ceiling 6 and ran it.
  - The resource then reported `creditsAmount` 6, so I treat it as **6 spent**. The month is **1,629 of 3,000** by this log.
  - The balance went 8,871 → 8,835 (−36) over the same minutes. The other 30 is most likely the parallel T251–T255 round (5 × 6); that session should log it.
  - **Lesson:** a quote of 0 did not mean free here.
- **Files:**
  - Prompt: `Prompts/LB04-Guofeng-Gold-Leaf-Silk-Sleeper-Contrast-v01.txt`.
  - Render: `Renders/LB04-…-Seedream-paid-v01.png`.
  - Progress sheet: `Renders/contact-sheet-LB01-LB04-sleeper-progress.jpg`.

**Measurements**

| Frame | Sat | Lum | Sd | Black | White | Dark% |
| --- | --- | --- | --- | --- | --- | --- |
| B1 reference | 77 | 101 | 53 | 10 | 210 | 11 |
| LB03 | 69 | 167 | 47 | 73 | 244 | 0 |
| LB04 | 90 | 96 | 50 | 20 | 231 | 8 |

LB04 is on target for lane B except white (231, against at most 230).

**Observations**
- **Light:** she sleeps in the middle on sheer gold silk, under a low warm sun from the right with blue-grey cloud shadow. The silk glows softly, with no metallic sheen. Her face is in soft shade.
- **The silk's pattern:** the model drew "gold leaf beaten in" as a woven pattern of gold maple leaves.
- **The distance:** crimson and orange maple islands rise from the cloud sea at three or four distances, with a peak on the horizon and leaves drifting.
- **The foreground:** a red maple branch, out of focus, crosses the lower left.

**Judgement (mine, unconfirmed)**
- **The closest any lane has come to its reference.** Contrast, palette and the far elements match B1, and the shine is soft.
- **The risk is now the opposite one:** it sits very close to MosaicEcho's own frame (a woman asleep on gold fabric above a cloud sea with maple islands). For a set, keep this finish and palette, but find our own idea and our own wide–close pairs.
- **The maple-leaf pattern** is pretty, but may read as decorative fabric rather than gold leaf.

**Owner's verdict on LB04 (2026-11-25):** "yea thats much closer can lock, write skill."

**Skill change: lane B locked on LB04.**
- **`LOOKS.md`:**
  - Lane B is rewritten as locked: the owner's five keys, the v03 look block, the "there when" list, the re-centred numbers, and a table of how LB01–LB04 got there.
  - The lane table marks B as locked, and lane D is renamed "Film texture (胶片)".
  - A new "Format" section records the owner's ratio decision: A 9:16, B 21:9, C 3:4, D 21:9. Lane A's look block now says 9:16.
- **`EXAMPLES.md`:** the LB04 prompt, under "Lane B · LB04 gold-leaf silk sleeper".
- **`scripts/measure_look.py`:** the lane B ranges are re-centred on LB04 and B1. LB04, B1 and B2 read on target; LB01, LB02 and LB03 do not.
- **`SKILL.md`:**
  - §3 points the format line at each lane's ratio.
  - §4 says to log the resource's `creditsAmount` after every run, since LB04 quoted 0 but was charged 6.
- **Supporting evidence:** LB01–LB04 and the owner's notes on each.
