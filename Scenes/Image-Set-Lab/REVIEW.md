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

**Owner on LC and LD (2026-11-25):** "LD LC Still far from original. LC is about composition and element. LD is about the look, lens, filter. color." The note went into `LOOKS.md` (lanes C and D). The lane-test files to this point were committed as `9bc110e`, without the parallel session's T251–T260 work.

## LC03 and LD03: C's composition grammar, and D's look on the same scene (2026-11-25)

- **LC03:** a new subject in C1's grammar, built from the reference's elements:
  - a worm's-eye centred view up a colossal round 天坑 (tiankeng) to a round sky with a small moon;
  - inner walls lined ring above ring with cave dwellings and tiny warm lights;
  - one huge waterfall falling from the rim through the centre, dissolving into mist;
  - pine silhouettes in mist along the base.

  3:4, 2K.
- **LD03:** the same slow-dance scene as LD02. Only the look changed:
  - Portra 800 pushed, through a vintage anamorphic 50mm wide open, behind a Black Pro-Mist 1/2;
  - low contrast with dim creamy highlights;
  - muted colour: steel-blue dusk, green-teal shadows, dusty tan desert;
  - after sunset, the car lights dimmed. The avoid line adds sunset colours, orange or red glare and saturated colour.

  21:9, 1.5K.
- **Run:**
  - Quote 10; `node confirm --credit-ceiling 12`; one `node run`.
  - LC03 `node_6aw8dcvr0g` (submit `e50876fa…`) charged 6; LD03 `node_x7bt8gmmxc` (submit `15d585e6…`) charged 4.
  - **Spent 10 (8,835 → 8,825); the month is 1,639 of 3,000 by this log.**
- **Files:**
  - Prompts: `Prompts/LC03-Mega-Tiankeng-Ring-City-Waterfall-v01.txt`, `Prompts/LD03-Film-Highway-Slow-Dance-MutedLook-v01.txt`.
  - Renders: `Renders/LC03…`, `Renders/LD03…-Seedream-paid-v01.png`.
  - Sheets: `Renders/contact-sheet-LC01-LC03-vs-C1.jpg`, `Renders/contact-sheet-LD02-LD03-vs-D-refs.jpg`.

**Measurements:**
- **LC03:** sat 44, lum 78, sd 51, white 237, dark 22%, vig 0.23. On target except contrast (51, against at most 50) and the bright sky disc (237).
- **LD03:** sat 107, lum 56, sd 26, white 100, dark 39%, shG +1, hiR-B −36. Against LD02, contrast fell from 47 to 26, close to D2's 30. But the whole frame is blue: saturation is still high, highlights are dimmer than any reference (100, against 119–196), and the highlights read cool rather than warm.

**Observations**
- **LC03:**
  - The round sky opening with a moon sits high in the centre. A broad waterfall falls from the rim down the middle into mist, and pine silhouettes stand at the base.
  - The walls curve off every edge, lined with wooden cave dwellings and warm windows in rings.
  - The walls read as legible houses rather than C1's abstract rings of light. The fall is a clean waterfall rather than C1's billowing mist column. The frame is crisper than C1's murk.
- **LD03:**
  - The couple are small at the left of the frame, embracing, with the wind in her dress. The car is parked behind them with its doors open and its warm lights dimmed low; poles and turbines stand on the horizon under an even, dim steel-blue dusk.
  - It is soft and low in contrast. The couple get no warm light; the only warm points are the car lights, far off.

**Judgement (mine, unconfirmed)**
- **LC03 is the first lane-C frame that follows the reference's layout and elements:** opening, central fall, walls off every edge, tree base. It is the candidate for "best so far".
- **LC03's gap is the finish:**
  - thicker mist and a matte murk;
  - walls as countless tiny light points rather than readable houses;
  - the fall as a billowing column of mist.
- **LD03 moved the contrast and softness toward D.** Side by side with D2 and D3, two differences remain.
  - **The warm key:** in the references the warm practical lights the subjects up close (the lighter on her face in D3), or the land is warm tan (D2). LD03's warmth is far away and the frame is all blue.
  - **The lens distance:** D3 is a medium close-up on a longer lens with the background soft. LD03 is a wide.
- **Next for D:** put a small warm practical between or beside them (a lighter, a phone, the car's headlights raking across them), and frame a medium shot on a longer lens. Pull the sky toward neutral grey-lavender and keep the ground warm tan.

## LC04 and LD04: C's finish, and D's warm key and lens (2026-11-25)

- **Brief (owner):** "Yes, run both", for the fixes proposed after LC03 and LD03.
- **LC04, changing the finish only:** the same tiankeng composition, with these changes:
  - "slightly underexposed… murky grey haze over everything";
  - walls "too tall and far away to see dwellings: countless tiny warm points of light in thousands of thin concentric rings, like streaks of stars";
  - the fall as "an enormous column of falling water and billowing white mist… swelling into cloud";
  - the avoid line adds readable houses or windows, and balconies.
- **LD04, the warm key and the lens:**
  - an 85mm anamorphic medium shot from the waist up;
  - the car's headlights, out of frame to the right, raking across the couple in warm amber;
  - a grey-lavender sky, warm tan desert and green-teal shadows;
  - the avoid line adds an all-blue frame. The scene action is unchanged.
- **Run:**
  - Quote 10; `node confirm --credit-ceiling 10`; one `node run`.
  - LC04 `node_yfc51gkcn7` (submit `2ed6b112…`) charged 6; LD04 `node_x8nr834x8b` (submit `65de9ae6…`) charged 4.
  - **Spent 10; the month is 1,649 of 3,000 by this log.** The balance went 8,825 → 8,785 (−40); the extra 30 is the parallel session again.
- **Files:**
  - Prompts: `Prompts/LC04-Mega-Tiankeng-Light-Rings-Mist-Column-v01.txt`, `Prompts/LD04-Film-Highway-Slow-Dance-WarmKey-v01.txt`.
  - Renders: `Renders/LC04…`, `Renders/LD04…-Seedream-paid-v01.png`.
  - Sheets: `Renders/contact-sheet-LC03-LC04-vs-C1.jpg`, `Renders/contact-sheet-LD03-LD04-vs-D-refs.jpg`.

**Measurements:**
- **LC04:** sat 45, lum 69, sd 50, white 221, dark 31%. On the edge of the C ranges.
- **LD04:** sat 52, lum 78, sd 45, white 189, shG +2, hiR-B +8. Inside every D range, against LD03's sat 107 and white 100.

**Observations**
- **LC04:**
  - The walls now read mostly as rings of tiny warm lights on dark ledges, with only faint structure.
  - The fall is still a clean, fairly narrow waterfall, not C1's billowing column with dark clumps. The sky opening shows a moon in cloud.
  - The pine silhouettes grew larger and closer, filling the bottom third.
- **LD04:**
  - A medium shot: the couple **kiss** (not the head-on-shoulder that was asked), his jacket over her bare shoulders, wind in her hair.
  - Warm amber light reaches their faces from the headlights at the lower right, and the headlight itself shows in the corner.
  - The sky is grey-lavender and the desert warm tan, with blurred poles, turbines and a far light. Soft and muted, with shallow depth of field.

**Judgement (mine, unconfirmed)**
- **LD04 is the closest lane-D take so far.** Its palette (lavender sky, tan land, warm skin against cool dusk), long-lens softness and muted colour all sit with D2 and D3.
- **LD04's remaining issues are not the look:** the model turned the embrace into a kiss, and the headlight glare intrudes in the corner. Both are scene fixes for a set. It is the candidate for lane D.
- **LC04's walls moved toward C1's rings of light. Its fall and haze did not,** and the bigger pines start to make a foreground layer.
- **Next for C:** the fall as "a vast churning column of mist and cloud, wider than a river, with darker clumps inside it", and the pines "a low black tree line, small at the very bottom". LC04 replaces LC03 as the C candidate, by a little.

**Owner on LD04 (2026-11-25):** "Not yet" to locking lane D, then "continue from where you left off".

## LC05 and LD05: C's mist column, and a softer D without the kiss (2026-11-25)

- **LC05, changes from LC04:**
  - the fall becomes "a vast churning column of falling water, mist and cloud, wider than a river… darker grey clumps tumbling inside it";
  - the haze becomes "a murky grey-green haze veiling everything";
  - the pines become "a low black line of small treetops";
  - the avoid line adds a thin clean waterfall and large trees in the foreground.
- **LD05, changes from LD04:**
  - a slow handheld shutter, "nothing tack-sharp… faint motion softness";
  - the scene asks for "not kissing", her cheek on his chest, him three-quarters from behind, and the headlights out of frame;
  - the avoid line adds kissing, faces turned to camera, and headlights or glare in the frame.
- **Run:**
  - Quote 10; `node confirm --credit-ceiling 10`; one `node run`.
  - LC05 `node_mxcqxap131` (submit `aed888b0…`) charged 6; LD05 `node_ra7kwa59v5` (submit `754fef38…`) charged 4.
  - **Spent 10 (8,755 → 8,745); the month is 1,659 of 3,000 by this log.**
- **Files:**
  - Prompts: `Prompts/LC05-Mega-Tiankeng-Billowing-Mist-Column-v01.txt`, `Prompts/LD05-Film-Highway-Slow-Dance-Soft-v01.txt`.
  - Renders: `Renders/LC05…`, `Renders/LD05…-Seedream-paid-v01.png`.
  - Sheets: `Renders/contact-sheet-LC04-LC05-vs-C1.jpg`, `Renders/contact-sheet-LD04-LD05-vs-D-refs.jpg`.

**Measurements:**
- **LC05:** sat 31, lum 83, sd 46, white 223, dark 11%. Inside every C range except the sky disc (223, against at most 220).
- **LD05:** sat 54, lum 73, sd 35, white 137, hiR-B −3. Contrast and highlights now sit inside D2 and D3's own values (sd 30–39, white 119–196). The highlights are no longer warm.

**Observations**
- **LC05:**
  - A broad billowing column of mist and cloud pours from the round sky opening (with the moon) down the centre, and is the brightest thing in the frame.
  - The walls are dark and covered in thin concentric rings of tiny warm light points, with no readable buildings. A grey-green haze sits over everything, and a low dark tree line runs along the bottom.
  - Nothing in the frame now says "Chinese tiankeng": it reads as an abstract shaft.
- **LD05:**
  - A medium-long shot of the couple embracing, not kissing. Her face rests on his shoulder and his face is hidden in her hair. His jacket hangs over her and he is in a white shirt.
  - A lavender dusk, tan desert, poles and turbines; soft overall, with no headlight in the frame.
  - The warm raking light barely reaches them: the faces are lit almost as evenly as the dusk.

**Judgement (mine, unconfirmed)**
- **LC05 is the closest lane-C take:** C1's composition and elements, finish included. It is the new C candidate.
- **The trade-off:** pushed this far toward C1, the cultural anchor disappeared. For a set, put the anchor back in a way the composition can carry, such as a recognisable tiankeng rim with trees, or a small temple roof on the rim, without going back to readable houses on the walls.
- **LD05 fixed the pose and softness but lost LD04's warm key.** D3's look depends on one small, strong warm light on her face against cool dusk.
- **Next for D:** LD05's softness and pose, plus a close practical (a lighter or match between them, or the headlights much brighter and closer, raking hard across her face). Keep it a medium shot.

**Owner on lane C (2026-11-25), mid-round:** "for C i dont like tiankeng, see original pic, it is using like even mythical, destiny-vibe, even some kind of majestical or something, to form its composition. why are we in a well."
- **My reading:** C1's concentric light streaks are the sky turning (star trails or a halo), and the column is pouring down from heaven. LC03–LC05 misread those streaks as the walls of a pit.
- **What changed:** recorded in `LOOKS.md` lane C, "Mythical and majestic, never a well".

## LC06 and LC07: lane C out of the well, into mythical open sky (2026-11-25)

- **Brief:** the owner's note above, which rules out wells and asks for a mythical, destiny, majestic subject that builds the composition. Two different myths, both 3:4 at 2K:
  - **LC06 · the Yellow River coming down from heaven** (黄河之水天上来), in C1's grammar: the night sky wheeling in concentric star trails around one opening of light overhead; a colossal ochre-tinted column of water, mist and cloud pouring straight down through the centre; a low forest line at the bottom.
  - **LC07 · the Gate of Heaven** (天门), in C2's grammar: an ancient stone moon gate as large as a mountain range, standing in a sea of clouds and framing the full moon, with waterfalls pouring from its arch and one small blossoming tree on dark rocks below.
- **Run:**
  - Quote 12; `node confirm --credit-ceiling 12`; one `node run`.
  - LC06 `node_wdz5ygvcc5` (submit `6b5c4744…`) and LC07 `node_k18vv5yqcv` (submit `1f2365cf…`) each charged 6.
  - **Spent 12 (8,745 → 8,733); the month is 1,671 of 3,000 by this log.**
- **Files:**
  - Prompts: `Prompts/LC06-Mega-Yellow-River-From-Heaven-v01.txt`, `Prompts/LC07-Mega-Moon-Gate-of-Heaven-v01.txt`.
  - Renders: `Renders/LC06…`, `Renders/LC07…-Seedream-paid-v01.png`.
  - Sheet with C1 and C2: `Renders/contact-sheet-LC06-LC07-vs-C1-C2.jpg`.

**Measurements:**
- **LC06:** sat 32, lum 90, sd 42, white 211.
- **LC07:** sat 24, lum 95, sd 48, white 198.
- Both are in range except brightness: they are a little lighter than C, which wants at most 85.

**Observations**
- **LC06:**
  - Star trails wheel around a glowing break in the clouds overhead. From it a huge churning column of grey-white water and cloud with ochre-gold streaks drops to a dark forest line, with mist spreading at its foot.
  - It is open sky, not an enclosed space. But the column has no visible falling edge or spray at the top, so it can read as a rising plume or eruption.
- **LC07:**
  - A pale stone ring frames the full moon in a misty sky, with waterfalls pouring from the inner arch and a small pink blossom tree on dark rocks at the bottom. Ridges stand in the mist.
  - The model drew two nested arches rather than one ring. The rose trees on the rim did not appear, and the carved ruin edges look a little like a game portal.

**Judgement (mine, unconfirmed)**
- **Both now have the mythical, majestic, open-sky feeling,** with a Chinese myth or line of poetry as the anchor.
- **LC06 is the more original idea and the stronger hook.** Next, the column must clearly fall: a lip of water spilling over the edge of the opening, sheets of falling water, and spray exploding at the bottom.
- **LC07 has the cleaner C2-style composition.** Next: one single ring, no inner arch, and blossom trees along the rim.
- **For both:** pull the exposure toward C's darker, murkier print.

**Owner's verdict on LC06 and LC07 (2026-11-25):** "alright finally a really good one LC07."

**Skill change: lane C confirmed on LC07.**
- **`LOOKS.md`:**
  - Lane C is rewritten around LC07: the owner's two rules (composition and elements; mythical and majestic, never a well) and the LC07 composition (one centred mythical form framing the moon, waterfalls into mist, a sea of clouds, one small tree on dark rocks).
  - Also new: the v02 look block from LC07, re-centred numbers, more myths for the same grammar, and a "how we got here" table for LC01–LC07.
- **`EXAMPLES.md`:** the LC07 prompt, under "Lane C · LC07 moon gate of heaven".
- **`scripts/measure_look.py`:** the lane C ranges are re-centred on LC07, C1 and C2 (sat 15–50, lum 60–100). All three read on target.
- **My earlier notes on LC07** (the two nested arches, no blossom on the rim) were my judgement. The owner liked the frame as it is, so the skill says not to "fix" the double arch unless asked.

**Owner (2026-11-25):** "D can lock for now stop chasing, it is the best when it is video. A can lock too. and can you use A's style to develop like 3 poolcore ideas, creative?"

**Skill change: lanes A and D locked.**
- **`LOOKS.md`:**
  - **Lane A** is rewritten as locked on LA02 (the pool above the clouds). The v02 look block is LA02's camera paragraph; it also has "there when" checks and re-centred numbers. The Douyin 氛围柔光 filter stays an optional finishing touch, so that open decision is closed.
  - **Lane D** is rewritten as locked for now on LD04: Portra 800 through an 85mm anamorphic with a Pro-Mist 1/2, a warm key raking across the subjects, a lavender sky and tan land. It also has a table of LD01–LD05, and the owner's note that D is best as video, so moving work goes through the nocturnal-dream video skill.
  - The lane table and intro say all four lanes are set.
- **`EXAMPLES.md`:** the LA02 and LD04 prompts.
- **`scripts/measure_look.py`:** the A ranges are re-centred on LA02 and A1, and the D ranges on LD04 and D1–D3.
  - On target: LA02, A1, LD04, D1, D2, D3.
  - Off target: LA01, LD03, LD05.

## Poolcore in lane A's look: three ideas, prompts written, not yet generated (2026-11-25)

Each idea opens with lane A's locked block (LA02's camera paragraph) and is 9:16. Each changes the space itself, not an added object, and leaves the viewer somewhere different:
- **LA03 · The sea is a pool** (大海是泳池). From a ladder on a seawall at noon, the whole open sea is a swimming pool: pale blue tiles to the horizon, black lane lines and rows of red-and-white lane floats running out until they vanish. The feeling is endlessness: every summer pool made infinite.
- **LA04 · The pool has no bottom** (泳池没有底). Looking straight down into an old public pool, there is no floor, only open sky and drifting cumulus far below. The ladder goes into the water and ends above the clouds. The feeling is a gentle vertigo.
- **LA05 · The street is a pool** (街道是泳道). An ordinary sunny residential street, seen in one-point perspective from the kerb, where the road between the kerbs is a long pool: a lane line down the middle, a ladder by a lamppost, a pedestrian crossing showing through the water. The feeling is the city on the hottest day of a summer that never ended.

Prompts: `Prompts/LA03-Poolcore-The-Sea-Is-a-Pool-v01.txt`, `Prompts/LA04-Poolcore-The-Pool-Has-No-Bottom-v01.txt`, `Prompts/LA05-Poolcore-The-Street-Is-a-Pool-v01.txt`. Plan: Seedream 5.5, 9:16, 2K, one image each: 18 credits, awaiting the owner's go-ahead.

## LA03–LA05: three poolcore ideas in lane A's locked look (2026-11-25)

- **Approved:** "Yes, generate all three" (Seedream 5.5, 9:16, 2K, 18 credits).
- **Run:**
  - Quote 18; `node confirm --credit-ceiling 18`; one `node run`. Each `creditsAmount` is 6.
  - **Spent 18 (8,733 → 8,715); the month is 1,689 of 3,000 by this log.**

| Take | Node | Submit |
| --- | --- | --- |
| LA03 The sea is a pool | `node_wheg2bw3q1` | `0a373e45…` |
| LA04 The pool has no bottom | `node_0yx8xm27sm` | `1b4885ec…` |
| LA05 The street is a pool | `node_2w7eqt4n5s` | `ea5699bf…` |

- **Files:** `Renders/LA03…LA05-*-Seedream-paid-v01.png`; a sheet with A1 and LA02: `Renders/contact-sheet-LA03-LA05-poolcore.jpg`.

**Measurements (lane A):**
- **LA03:** sat 120, lum 125. On target except shadows a hair bluer than the range (shR-B −81).
- **LA04:** sat 126, lum 120. Corners darker than the range (vig 0.32) and dark% 16.
- **LA05:** sat 98, lum 128, white 251. A little pale and bright, with the clouds clipping.

**Observations**
- **LA03:**
  - A chrome ladder on the seawall sits in the foreground. Tiled cobalt water with black lane lines runs out from the wall, and red-and-white lane floats cross it.
  - The tiles fade into darker open sea before a flat horizon under a tall cumulus tower. Heavy blue vignette.
- **LA04:**
  - Looking down past the pool coping and a chrome ladder into cobalt water, bright white clouds fill the water on the left.
  - The clouds read as a reflection of the sky on the surface, not as sky beneath a missing floor. The ladder goes into the water normally.
- **LA05:**
  - A whitewashed residential street with balconies and AC units, in one-point perspective. A long tiled lap lane fills the right half of the road, with a lane rope and a ladder by a lamppost.
  - The left half stays ordinary asphalt with a zebra crossing, and a cumulus tower stands at the end of the street.

**Judgement (mine, unconfirmed)**
- **LA03 is the strongest.** It passes the one-second test (you know it's a pool, and the sea can't be one) and is a clean, graphic cover in the locked look.
- **LA05 has the best liminal composition,** but with only half the road a pool it can read as a real street installation. A retake should make the whole road, kerb to kerb, the pool.
- **LA04's idea didn't land:** a pool showing sky reads as a reflection. To work it needs a view that proves there is no floor, such as looking down a pool wall that ends in open air, with the ladder hanging into nothing. It may suit video better than a still.

**Owner (2026-11-25):** "just do what you said before the 6 ideas. also can use some master-level, artist grade, color palette idea to create the visual impact and cleaniness." I read this as six poolcore frames: the three fixes I proposed (build on LA03, the whole street as a pool, a pool provably floating) plus three new ideas, each on lane A's locked finish with one named painter's palette as a closed list.

## LA06–LA11: six poolcore frames, lane A finish with artist palettes (2026-11-25)

- **Prompts:** each opens with lane A's locked camera paragraph (Ektar 100, Pro-Mist 1/2, heavy vignette, soft edges, milky blacks). The cobalt palette sentence is replaced by one painter's palette as a closed list, plus "Clean composition: very few objects and large flat planes of colour, like a painting". All 9:16, 2K.
- **Run:**
  - Quote 36; `node confirm --credit-ceiling 36`; one `node run` with six submit IDs. Each `creditsAmount` is 6.
  - **Spent 36; the month is 1,725 of 3,000 by this log.** The balance went 8,715 → 8,643 (−72); the other 36 was spent in parallel by another session.
- **Files:**
  - Prompts: `Prompts/LA06…LA11-Poolcore-*-v01.txt`.
  - Renders: `Renders/LA06…LA11-*-Seedream-paid-v01.png`.
  - Grid: `Renders/contact-sheet-LA06-LA11-poolcore-artist-palettes.jpg`.

| Take | Idea · palette | Node | Sat / lum |
| --- | --- | --- | --- |
| LA06 | The sea is a pool · Hockney | `node_9e81v4sgnm` | 84 / 157 |
| LA07 | The street is a pool, kerb to kerb · Barragán | `node_51t99bm52r` | 138 / 106 |
| LA08 | A pool floating in the sky · Magritte | `node_tnh1tb35r4` | 80 / 159 |
| LA09 | A pool in the wheat · Van Gogh | `node_k5z221yn7k` | 139 / 132 |
| LA10 | The pool stands up · Yves Klein | `node_0cf1w54h95` | 54 / 189 |
| LA11 | A pool in pink dunes · O'Keeffe | `node_2fnwhjxtf7` | 56 / 190 |

The artist palettes push several frames high-key (lum 157–190), past lane A's cobalt ranges. That is expected: the palette changes the numbers, while the finish (vignette, soft edges, milky blacks) holds.

**Observations**
- **LA06:** a flat pink seawall with a chrome ladder above turquoise tiled sea, with black lane lines, one lane rope, a straight horizon and one small cloud. Very few elements.
- **LA07:** magenta-pink and saffron walls line a long deep-blue pool that fills the street between narrow pavements, with one lane line, a ladder and a tree shadow on the pink wall.
- **LA08:**
  - A tiled rectangular pool with a ladder floats above a cloud bank over the sea, seen past a pale stone terrace.
  - The pool is small in the frame, and the terrace fills the lower 40%.
- **LA09:** a rectangular cobalt pool sits alone in ripe golden wheat under a deep blue sky, with wheat ears soft in the foreground.
- **LA10:** a drained white-tiled pool ends in a deep blue upright surface with lane lines and sun glowing at its top edge. It reads as a painted blue wall, not standing water.
- **LA11:** a turquoise pool is set into smooth pink, peach and bone dunes, with sand drifting over one corner, a pale sky and one cloud.

**Judgement (mine, unconfirmed)**
- **Strongest:** LA11, LA06 and LA08.
  - **LA11** is the cleanest and most dreamlike, with the same salmon-pink and turquoise as the owner's favourite 永夏 palette.
  - **LA06** is the most graphic, and fixes LA03 by cutting it down to a few elements.
  - **LA08** proves the impossible: the pool clearly floats with nothing under it. A retake should make it larger in the frame.
- **Strong colour, weaker oddity:** LA07 and LA09.
  - **LA07** reads close to real Barragán architecture.
  - **LA09** could be a real farm pool.
- **LA10's oddity failed:** the water reads as a wall.
- **Possible set:** "six painters, one pool" (one condition, many palettes) could itself be a set idea. The skill's one-look rule holds through the shared finish and vignette.

**Owner (2026-11-25):** "Yes, build a set."

## Set built: 泳池在别处 · The Pool Is Elsewhere (2026-11-25)

- **Frames, in order** (no new generation):
  1. LA06, Hockney sea (cover)
  2. LA07, Barragán street
  3. LA09, Van Gogh wheat
  4. LA11, O'Keeffe dunes
  5. LA02, above the clouds
  6. LA08, Magritte floating pool (ending)
- **Structure:** one condition, many places. The pool travels further from the ground with each swipe.
- **Files:** `../The-Pool-Is-Elsewhere/POST.md` (copy, order logic and checklist) and `../The-Pool-Is-Elsewhere/Post/01–06.jpg`, with a phone-size strip.
- **Phone-size check (mine):** the shared finish (vignette, soft edges, milky blacks) holds the six palettes together as one look.
  - 05 is darker and crisper than the others.
  - 06's pool is small in the frame.
  - Every frame is a wide.

**Proposed additions, not run** (Seedream 5.5, 9:16, 2K, 6 credits each, 24 in all):
- **Close-ups in the same light**, for the wide–close rhythm:
  - a chrome ladder rung beaded with water against the pink wall (Hockney);
  - wheat ears dipping into cobalt water (Van Gogh);
  - pink sand sliding over white coping into turquoise water (O'Keeffe).
- **An LA08 retake** with the floating pool large in the frame, for a stronger ending.

**Owner (2026-11-25):** "i just deleted them. these are not what i want, keep going with the LA03 idea."
- **What was deleted:** the owner removed the LA07, LA08, LA09 and LA11 artist-palette nodes from the canvas. LA06 and LA10 nodes remain.
- **The set:** `../The-Pool-Is-Elsewhere/POST.md` is marked rejected, with files kept for the record.
- **The artist-palette direction is dropped:** go back to LA03 (the sea is a pool) in lane A's locked cobalt look.
- **ID clash:** a parallel session ran its own "poolcore + cloud" LA06–LA11 (Cloud-in-the-Pool … Cloud-Edge-Showers) at the same time, logged above. This session continues at LA12 to avoid clashes.

## LA12–LA15: growing the LA03 idea (the sea is a pool) in lane A's cobalt look (2026-11-25)

- **Prompts:** each opens with lane A's locked block unchanged (cobalt palette) and shares one sea-pool sentence. The scenes move through the place:
  - **LA12:** a lone diving tower far out at sea (wide).
  - **LA13:** a lane rope on the swell (close).
  - **LA14:** the beach ending at a straight line of pool coping, with a pair of flip-flops (the walk in).
  - **LA15:** the far wall of the pool at the horizon (the payoff).

  All 9:16, 2K.
- **Run:**
  - Quote 24; `node confirm --credit-ceiling 24`; one `node run` with four submit IDs. Each `creditsAmount` is 6.
  - **Spent 24 (8,643 → 8,619); the month is 1,749 of 3,000 by this log.**

| Take | Node | Submit |
| --- | --- | --- |
| LA12 diving tower at sea | `node_t1fcf972qj` | `254ff21e…` |
| LA13 lane rope, close | `node_fht19q7eb8` | `f937a5a0…` |
| LA14 the beach ends at the coping | `node_kykzzzq123` | `ca2dcd95…` |
| LA15 the far wall | `node_s32nnmbnjm` | `64ca3a06…` |

- **Files:**
  - Prompts: `Prompts/LA12…LA15-SeaPool-*-v01.txt`.
  - Renders: `Renders/LA12…LA15-*-Seedream-paid-v01.png`.
  - Sheet with LA03: `Renders/contact-sheet-LA03-LA12-LA15-sea-pool.jpg`.
- **Measurements:** all within or just at lane A's edges.
  - LA12 and LA14 are a touch bright (lum 128–129).
  - LA13 and LA15 have heavier corners (vig 0.22–0.24).
  - LA15's saturation is 135.

**Observations**
- **LA12:** the seawall makes a diagonal over tiled sea with lane lines. A three-platform concrete diving tower stands alone far out under a cumulus tower.
- **LA13:** red-and-white lane floats lie close across tiled water, with a chrome ladder on a concrete step at top left and a lane line beneath. The tiles run back to open sea and the horizon.
- **LA14:** the sand ends at white coping with a drain grate, and a pair of flip-flops lies on the sand. Beyond, tiled sea with lane lines and floats runs out to the real horizon.
- **LA15:** a white tiled wall with a ladder crosses the frame in mid-distance. But open sea continues beyond it to the horizon, so it reads as an ocean pool built at the shore, not as the sea ending at a wall.

**Judgement (mine, unconfirmed)**
- **One look:** all five frames (LA03 and LA12–LA15) read as the same place and finish.
- **Strongest:** LA03 (cover) and LA12. LA14 is a good walk-in, and LA13 gives the set its first close-up.
- **LA15's payoff failed** because there is sea beyond the wall. A retake should make the wall the horizon itself: "nothing beyond it but sky".
- **Possible order:** LA03 · LA14 · LA13 · LA12 · LA15 (retaken). One or two more frames would bring it to six or seven.

**Correction (2026-11-25): the LB04 "quote 0 but charged 6" lesson is unverified.**
- **What I logged:** the LB04 section above, and the lane-B skill change, said a quote of 0 "did not mean free".
- **Why that's not settled:** the official `dreamina-canvas-cli` skill says a quote of 0 means that run is free. The resource's `creditsAmount` of 6 may be the list price rather than the deduction. The CLI has no credit ledger (no transaction command; `resource get` and `node show` only show `creditsAmount`), and a parallel session was spending in the same minutes.
- **Status:** unverified, until the owner checks 积分明细 in the Jimeng app for the LB04 run (~14:10).

**Skill change (2026-11-25), official CLI skill checked.** Gemini wrote `JIMENG-CLI.md` and linked it from SKILL.md §4. It was kept and updated:
- **Before a round:** `briefing`, `auth status`, sharing the canvas link, why not to use `canvas use`, and `schema` before unfamiliar flags.
- **Verified additions:**
  - `operation wait <submitId>`;
  - canvas node sizes: 9:16 = 320 × 569, 21:9 = 747 × 320;
  - the one-step `node create … --run --credit-ceiling --wait`.
- **Also new:** keeping job state and `meta.requestId` in REVIEW; consistency across a set via `--mode i2i --ref node:<cover>`; exit-code retry rules; post-editing.
- **The quote-0 gotcha** is rewritten as unverified. SKILL.md §4 now points to the official skill and JIMENG-CLI.md.
