# 散场以后 · After Everyone Left — image set

**Status (latest):** the final 4-image set was picked by the owner on 2026-11-20 (see "Final set" at the end). Not yet released.

**Original status:** set plan written 2026-11-20, waiting for the owner's approval before any generation. The cover already exists: it is Image-Set Lab T06, which the owner called "perfect" on 2026-11-20.

## Idea

**Pitch.** At 3 am in places built for being together, the thing is over, but one person or couple is still doing it. The long exposure turns them into a soft, translucent ghost.

- **Feeling:** tender, haunted memory. The party ended long ago and nobody told them.
- **Structure:** one condition, many places. The last image returns to the cover's place.
- **Oddity (one per image):** in images 1–5, the ghostly figures who are still there. It is played straight as a real long-exposure blur. Image 6 has no people; its one detail is the footprints left in the dust.
- **Swipe reason:** where else is someone still there?
- **Caption question (draft):** 你有没有一个散场了还不想走的地方？ ("Is there a place you didn't want to leave even after everyone had gone?")

## Shared look (copied into every prompt)

- **Camera and film:** Mamiya 7 with a 43mm lens, Portra 400 pushed one stop.
- **Exposure:** tripod, about 4 seconds, printed warm.
- **Finish:** heavy shadow grain and halation.
- **Framing:** level and centred, at waist or seated height.
- **Light:** one practical warm source per space, with the rest falling into darkness.
- **Reference:** Sugimoto and Crewdson.

## Order

| # | Place | Who is still there | Oddity | Prompt | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Hotel ballroom, 3 am (cover) | A couple slow-dancing | The ghost couple | `Prompts/01-Ballroom-v01.txt` | Done: `Renders/01-Ballroom-v01.png` (Lab T06, `node_rcfa2v7j6f`, 6 credits) |
| 2 | Single-screen cinema after the last show | A couple in the middle row; the screen burned white | The ghost couple | `Prompts/02-Cinema-v01.txt` | Not generated |
| 3 | KTV room, 4 am | One singer at the screen; mirror-ball streaks | The ghost singer | `Prompts/03-KTV-v01.txt` | Not generated |
| 4 | Roller rink at closing | One skater with a ghost arc around the oval | The ghost skater | `Prompts/04-Roller-Rink-v01.txt` | Not generated |
| 5 | All-night noodle shop after closing | Two people at the last table | The ghost pair | `Prompts/05-Noodle-Shop-v01.txt` | Not generated |
| 6 | The same ballroom at dawn | Nobody; two sets of footprints circling in the dust | The footprints | `Prompts/06-Ballroom-Dawn-v01.txt` | Not generated |

**Risks to watch:**
- The figures come out too sharp. In T06 the man was fairly sharp.
- The KTV screen or the noodle-shop menus grow readable text.
- The footprints in image 6 look painted on rather than pressed into the dust.

## Generation plan (once approved)

- Seedream 5.5, 3:4, 2K, one image per run, on the "Nocturnal Dream Image Sets" canvas in a new row.
- Free (0积分畅用) first. Paid only if the free queue stalls, at 6 credits each.
- All four remaining images, if paid: 24 credits more, which takes the month to 145 of 300.
- Credits are logged in the Image-Set Lab ledger: `../Image-Set-Lab/REVIEW.md`.

## Revision 1: "theme" means the visual style (2026-11-20)

The owner clarified that "the same theme" meant **the cover's visual style**, not a story. The approved story-led scenes are kept in `Prompts/superseded/`: cinema couple, KTV, roller rink, noodle shop, and the ballroom at dawn. They were replaced by old grand interiors that fit the look: picture palace, station waiting hall, 酒楼 banquet hall, hotel staircase, and the same ballroom empty.

**v02 takes (free).**
- **02 Picture Palace v02:** `node_1mgnfhmwdn`, submit `538089e5-b9e1-4780-9ef6-fe08eb23bc14`, 0 credits. Render: `Renders/02-Picture-Palace-v02.png`.
- **04 Banquet Hall v02:** `node_qth0vherbz`, submit `92479310-b068-4c2e-9660-2458538fc05b`, 0 credits. Still running at the time of writing.
- The web canvas allows only one free job at a time. While one is running, the 0积分畅用 switch disappears and the price shows 6/张.

**Owner's verdict on 02 v02.** Worse than image 1: the lighting and texture are inferior, and the pose is basically the same as the cover. The owner said to name an artist or a colour palette, and to use paid runs because free is too slow now.

- **Observations on 02 v02:**
  - The light is a bare glaring lamp over the stage, not a chandelier.
  - The prompt's "almost monochrome amber … crushed blacks" gave an orange cast and blotchy, posterised shadows.
  - The couple slow-dancing repeats the cover's pose.

## v03: Polidori style block, a different pose in every image (paid)

**One change in the style block:**
- **Look:** Robert Polidori's large-format decaying interiors crossed with Sugimoto.
- **Colour:** natural cream, ivory, faded gold, walnut and burgundy, with no orange cast.
- **Shadows:** mid-tone texture readable, shadows that hold detail.
- **Light:** a visible crystal chandelier with candle bulbs as the source, and no spotlights.
- **Poses:** usher sweeping, traveller walking away, waiter carrying plates, woman on the stairs, then nobody.

Credits: 5 × 6 = 30. The month total is now 151 of 300 (ledger in `../Image-Set-Lab/REVIEW.md`).

| # | Render | Observations | Judgement (mine, unconfirmed) |
| --- | --- | --- | --- |
| 2 | `Renders/02-Picture-Palace-v03.png` | A chandelier with candle bulbs hangs at top centre. The proscenium, curtain and boxes show peeling plaster in fine detail. Burgundy seats line the aisle. A young usher in a waistcoat sweeps, with the broom and head blurred and the body fairly sharp. Popcorn boxes lie in the aisle. Brighter than the cover. | Much closer to the cover. The best of v03. |
| 3 | `Renders/03-Waiting-Hall-v03.png` | Arched windows, wooden benches, a clock over the far door. The traveller with a case is blurred mid-stride. The terrazzo reflects. Lit fairly evenly, with little falloff into darkness. | The scene works, but it is too bright and flat next to the cover. |
| 4 | `Renders/04-Banquet-Hall-v03.png` | Many round tables with red chairs and lazy Susans, mirrors, a red stage backdrop. The waiter in a white jacket carries plates, blurred, left of centre. Busy and evenly lit. It reads more European than 酒楼, apart from the red. | The weakest: cluttered, and the figure is off-axis. |
| 5 | `Renders/05-Hotel-Stair-v03.png` | A symmetrical double staircase with a red runner and a chandelier. The woman in a pale dress is on the stairs, a translucent blur. It is unclear whether she is going up or coming down. Lit warmly at the landing. | Strong. Possibly the second-best image. |
| 6 | `Renders/06-Ballroom-Empty-v03.png` | A ballroom with bentwood chairs and a chandelier. Footprints form circles under the light and a trail toward the camera. **A camera tripod stands in the centre under the chandelier**, which was not asked for. It is a different room from the cover (other walls, other chairs). | The payoff reads, but the tripod and the different room break it. Needs a retake. |

**Set-level judgement (mine, unconfirmed).**
- The chandelier sits at top centre in every frame. That unifies the set but risks feeling formulaic.
- v03 images 2–6 are brighter and more evenly lit than the cover, which is darker with deeper falloff.

**Repeat:** naming Polidori, a visible chandelier as the source, natural colour words, a different pose for each image.
**Failed:**
- "Monochrome amber / crushed blacks" (v02).
- Asking for "the same ballroom" without a reference image (06).
- Evenly lit large rooms (03, 04).

**Next tests (one change each):**
1. 06: i2i using the cover (`node_rcfa2v7j6f`) as the reference, to get the same room; add "no tripod, no equipment".
2. 03 and 04: darken toward the cover with "only the chandelier lit, the far half of the hall and the corners falling into near darkness".
3. 04: fewer tables, and put the waiter on the centre axis.

## Owner's verdict on v03, and a new direction (2026-11-20)

**Owner's verdict.**
- The light is too bright and has no emphasis, so it is still different from image 1.
- The same framing (构图) every time is unwanted: "we are not generating the image over and over".
- Take the idea of image 1 further. It holds strong tension: emptiness and sadness against a blurred couple dancing passionately and romantically. That contrast is the aesthetic, but not every image has to repeat it.
- Propose scene ideas first.

**What image 1 does (my reading).**
- **Light with emphasis:** one source, and about 70% of the frame falls into deep darkness with faint texture. The light lands on the subject.
- **Contrast:** the cold, empty, decaying room against warm, intimate motion.
- **The figures:** half there, like a memory.

**Proposal v04 (waiting for approval, nothing generated).** One place: the same old hotel on the night of the last dance. Each image uses a different framing, keeps one source of light, and frames the emptiness against intimacy in a different way.

| # | Idea | Framing | Light | Contrast | Reference |
| --- | --- | --- | --- | --- | --- |
| 1 | The ballroom (cover, done) | Wide, centred | Chandelier | The ghost couple in the empty hall | — |
| 2 | **From the gallery**: looking straight down on the dark parquet, the spinning couple smeared into a circle like a clock hand | Top-down, graphic | One pool from a chandelier below the camera | Motion against stillness | Sugimoto, Bill Brandt |
| 3 | **The mirror**: a tall spotted mirror in a dark side corridor; the room in front of it is empty, but in the mirror the couple is still dancing (the set's one impossible image) | Close, off-centre, the mirror filling the frame | One wall sconce | Presence only in the reflection | Wong Kar-wai and Christopher Doyle (*In the Mood for Love*) |
| 4 | **The table**: a crumpled tablecloth, two half-drunk wine glasses (one with lipstick), a pearl earring, a candle just blown out and still smoking | Close, 45°, very shallow focus | The last glow of the smoke and one distant light | Traces of passion, nobody there | Jeff Wall, still-life stillness |
| 5 | **The terrace**: from inside the dark ballroom, through a tall rain-streaked window, the couple dances in the rain on the terrace under one lamp | Window frame as a dark foreground, figures small on a third | The terrace lamp outside, the inside black | The empty inside against passion outside | Saul Leiter (through glass and rain) |
| 6 | **The doors (ending)**: from the dark foyer, through the narrow gap of the closing double doors, a slit of warm light with the couple still dancing inside | Tight vertical slit, mostly darkness | The light from the gap only | We leave; they stay | Wong Kar-wai |

**Alternatives:**
- **The ghost light:** the bandstand with a single theatre ghost-light bulb on a stand, a double bass on its side, an empty chair. From the wings.
- **The cloakroom:** rows of empty hangers and one coat never collected, under one lamp. A low counter-top view.

## v04 takes (paid, 2026-11-20)

The owner approved the v04 scenes. The prompts share the cover's look block and add a rule for light with emphasis: one source only, about 70% of the frame in darkness, a steep falloff. Each prompt has its own framing.

- **Credits:** 5 × 6 = 30. The month total is 181 of 300.
- **Canvas:** the row at y = −2080.
- **Contact sheet:** `Renders/contact-sheet-v04.jpg`.

| # | Render | Observations | Judgement (mine, unconfirmed) |
| --- | --- | --- | --- |
| 2 Gallery | `Renders/02-Gallery-Overhead-v04.png` | A high oblique view (not straight down). The dark balustrade runs across the bottom. One warm pool on the parquet from a pendant lamp. The couple is softly blurred, with the dress swinging. Tables are pushed to the edges. **A mirror at the back reflects the woman dancing alone. That was not asked for, and it adds a second strange detail.** | The light has emphasis now. Strong, and the closest in spirit to the cover. |
| 3 Mirror | `Renders/03-Mirror-v04.png` | A large gilt mirror off-centre, a fringed sconce at the right edge, the corridor empty. The reflection shows a brighter colonnaded room with the couple blurred mid-dance. | Works as the set's impossible image. The reflected room is brighter than the corridor, which suits the idea. |
| 4 Table | `Renders/04-Table-v04.png` | Two red wine glasses, one with a lipstick print, a wine stain, a pearl earring, a card with no readable text, a brass candlestick. **The candle is still lit, yet smoke rises as if it had been blown out.** A spotted mirror and a dark room behind. | Intimate and dark. The lit candle weakens "a minute ago". Retake with the flame out if the owner wants. |
| 5 Terrace | `Renders/05-Terrace-Rain-v04.png` | A dark interior with a curtain and an arched window in the foreground. Through the open bay, a couple dances in heavy rain under one lamp, with a wet stone reflection. The figures are fairly sharp, not translucent. | Possibly the strongest new image. |
| 6 Doors | `Renders/06-Doors-v04.png` | A dark foyer. One door leaf stands open (wider than a hand's width). Warm light spills across the floor. A small blurred couple dances inside a bright room. | A clear ending. The opening is wider, and the inside brighter, than asked. |

**Set-level judgement (mine).**
- The light now has emphasis and one warm palette across all six.
- Every frame differs: wide centred, high oblique, off-centre mirror, close still life, window frame, door slit.
- The couple appears in 1, 2, 3, 5 and 6, and is absent in 4.

**Possible retakes, one change each:** 04 with the candle flame out; 06 with the door gap narrower. The owner decides.

**Repeat:** the light-with-emphasis block; different framing for each image; naming the visual reference for each scene.

## Owner's verdict on v04, and v05 (2026-11-20)

**Owner's verdict.**
- The couple should not be dancing everywhere. The images need tension and actions that make sense: running, laughing, anger.
- The mirror (v04) is already good. The table shot is "kinda pointless" and is cut.

**v05 story, 5 images:**
1. They dance (cover).
2. The fight.
3. The mirror, which holds the memory of the dance (v04, kept).
4. Running and laughing in the rain.
5. Leaving together.

Each new prompt keeps the v04 look and framing and changes only the action. Credits: 3 × 6 = 18, so the month is at 199 of 300. Contact sheet: `Renders/contact-sheet-v05.jpg`.

| # | Render | Observations | Judgement (mine, unconfirmed) |
| --- | --- | --- | --- |
| 2 Fight | `Renders/02-Gallery-Fight-v05.png` | High oblique view over the balustrade. She walks away fast across the light pool holding a shoe. He follows from the shadow, his arm reaching out. Motion blur on both. Streamers on the floor. **The chandelier is unlit, yet a hard round pool of light falls on the floor, so the source is unexplained and the pool reads as a spotlight.** Her raised arm could also be read as a dance step. | The action reads, and the tension works. The light logic is the flaw. |
| 4 Rain | `Renders/05-Terrace-Run-v05.png` | Dark interior, curtain, arched door. On the terrace in heavy rain under one lamp, she runs barefoot with her shoes in hand and her dress blurred, and he runs with his jacket held over his head. Wet stone reflects the lamp. The faces are small. | Strong. The release after the fight is clear. |
| 5 Leaving | `Renders/06-Leaving-v05.png` | A dark foyer with a column, a bronze statue, a table with a cloth, a coat stand. Through the open glass front doors the couple walks out side by side toward a street lamp, small and slightly blurred, with long shadows falling back into the foyer. They walk; they are not clearly running or holding hands. | A quiet ending that works. Less action than asked. |

**Possible retakes, one change each:**
- **Fight:** make the chandelier lit and dim, as the source of the pool.
- **Leaving:** show them clearly hand in hand.

The owner decides.

## Owner's verdict on v05, then v06–v07 (2026-11-20)

**Owner's verdict.**
- The leaving image is weak.
- In the rain image, the woman runs in a different direction from the man. They should be sharing the jacket he holds, with him caring for her.

**Changes:**
- **Rain:** running together, his jacket over both heads.
- **Leaving:** replaced by "carried". He carries her down the hotel steps to a waiting taxi, seen from the dark doorway.

Credits: 3 × 6 = 18, so the month is at 217 of 300.

| Take | Render | Observations | Judgement (mine, unconfirmed) |
| --- | --- | --- | --- |
| Rain v06 | `Renders/05-Terrace-Run-v06.png` | They run together and laugh, but **he holds an umbrella**, mostly over himself. She wears a pale wrap. Faces are visible. | Fails the note. Rejected. |
| Carried v06 | `Renders/06-Carried-v06.png` | A dark doorway and glass door as foreground. He carries her, seen from behind, barefoot with her shoes dangling, across steps toward a black cab with its rear door open and its interior light on. Heavy rain, a street lamp. The steps seem to rise toward the street, which is ambiguous. | Strong ending. It continues the caring. |
| Rain v07 | `Renders/05-Terrace-Run-v07.png` | No umbrella. His jacket is held over both, tilted toward her. They run the same direction, and she laughs underneath, barefoot, holding her shoes. A big dark curtain in the foreground, an arched window, one lamp. **He is still wearing a suit jacket while holding another one.** | Meets the note. The doubled jacket is a logic flaw a viewer might spot. |

**Current set order:** 01 Ballroom → 02 Fight (v05) → 03 Mirror (v04) → 04 Rain (v07) → 05 Carried (v06). Contact sheet: `Renders/contact-sheet-v07.jpg`.

**Open faults:**
- 02: the chandelier is unlit, yet a pool of light falls on the floor.
- Rain v07: he wears one jacket and holds another.

## Final set (owner's picks, 2026-11-20)

The owner marked the picks blue on the canvas: the cover in indigo (`default-tag-2`), the other three in teal (`default-tag-1`). The owner said the v05 leaving image is better than the later carried and rain takes, so the rain image is out.

| # | Image | Render | Node |
| --- | --- | --- | --- |
| 1 | Dance (cover) | `Renders/01-Ballroom-v01.png` | `node_rcfa2v7j6f` |
| 2 | Fight | `Renders/02-Gallery-Fight-v05.png` | `node_vgmtn35ebq` |
| 3 | Mirror | `Renders/03-Mirror-v04.png` | `node_d0qep080y0` |
| 4 | Leaving | `Renders/06-Leaving-v05.png` | `node_1w33gm2xsn` |

- **Contact sheet:** `Renders/contact-sheet-FINAL.jpg`.
- **Story:** tender → anger → memory → leaving together.
- **Purple tags:** the owner also marked hotel stair v03 and empty ballroom v03 purple. The meaning is not confirmed; they could be alternates.
- **Owner's own work on the canvas:** the owner made a colour-grade node (`node_s680b64re1`, "图片调色") from picture palace v03. The owner also deleted the empty free v02 nodes and the blank node.
- **Canvas layout:**
  - Header at y = −3600.
  - Final row at −3240.
  - Takes not picked: v05–v07 at −2700, v04 at −2160, v02–v03 at −1620.
  - Image-Set Lab tests from −360 down.

**Total spent on this set:** 102 credits (one cover at 6, plus 96 across v03–v07). The month is at 217 of 300.

**What to repeat:**
- One source of light with about 70% darkness.
- A different framing for every image.
- A different action for each image, chosen so the images tell a story.
- Name a visual reference for each scene.

**What failed:**
- An "almost monochrome amber" palette.
- Evenly lit rooms.
- The same pose or framing repeated.
- A still life with no people (the table shot).
- Prompting "jacket over heads" without saying "no umbrella".

**Next:**
- Caption and title in Chinese, with the AI label on.
- Music from the in-app library.
- Lay the set out at phone size to check order and colour.
- Decide whether the fight image's sourceless light needs a fix.
