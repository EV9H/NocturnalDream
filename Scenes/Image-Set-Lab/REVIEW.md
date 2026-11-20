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
