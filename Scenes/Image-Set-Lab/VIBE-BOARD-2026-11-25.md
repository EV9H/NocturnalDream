# Vibe board: four looks the owner wants (2026-11-25)

The owner shared eight Douyin screenshots as the quality bar, in four groups: the 氛围柔光 filter look (A), shiny 国风 texture, light and colour (B), the mega core (C), and film texture (D). They span several styles and themes, so treat each group as its own lane, not one look.

- **Files:** `References/vibe-board-2026-11-25/`, with a labelled `contact-sheet-vibe-board.jpg`.
- **Measurements:**
  - Made with the image-set skill's `scripts/measure_look.py` on crops that cut out the phone UI. A first pass left UI icons in B1 and D3, and these numbers replace it.
  - The screenshots are phone-compressed (about 360 px wide), so the numbers are good for tone and colour but not for grain.
  - Everything is on a 0–255 scale, the same as the T198 notes.
  - Tints are red minus blue (R−B), or green over the red-blue average (G) where the shadows lean green.
- **Engagement** is as the screenshots showed it on 2026-11-25.

| Ref | Account · post | Likes | Saves | Shares | Sat | Lum | Dark <40 | Brightest (p99) | Shadow tint | Highlight tint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | @24ZR · 沙漠游泳池 (filter 氛围柔光, used by 181.6万) | 86.8万 | 4.3万 | 3.9万 | 120 | 106 | 3% | 221 | navy (R−B −65) | cream (R−B +24) |
| B1 | @MosaicEcho马赛回声 · 一叶扁舟 #国风古韵 #巨物美学 | 93 | 26 | 3 | 77 | 101 | 11% | 210 | neutral (+4) | warm gold (+46) |
| B2 | same post | | | | 110 | 89 | 1% | 190 | brown-red (+25) | peach (+74) |
| C1 | @MosaicEcho · 这，就是我想去的终点 #复古未来主义 (4 images) | 1.9万 | 5,246 | 1,451 | 29 | 72 | 24% | 216 | neutral grey (−5) | near neutral (+8) |
| C2 | same post | | | | 38 | 69 | 1% | 163 | cool slate (−8) | warm stone (+35) |
| D1 | @赵一帆_ · Whatever Happens (6 images) | 1.3万 | 3,923 | 1,352 | 81 | 94 | 8% | 196 | green-teal (G +9) | cool white (−17) |
| D2 | same post | | | | 92 | 67 | 17% | 158 | green-teal (G +6) | neutral (0) |
| D3 | same post | | | | 61 | 57 | 49% | 119 | green-teal (G +4) | dusk-sky blue (−24) |

**Engagement (observation):** C and D are saved at about 28–30% of their likes; A at about 5%. B looks the way the owner wants, but that post got 93 likes.

---

## A · 氛围柔光: a real liminal place under a soft-glow filter

**Observations (A1)**
- **Scene:** an empty outdoor pool in high desert, with a wind pole, scrub, mountains and big cumulus. It's a real photo, run through Douyin's 氛围柔光 filter. The caption says they dug through their album to use the filter.
- **Framing:** a low wide view from the pool corner. The pool edge makes a hard diagonal into the horizon at about 40% from the top, and the sky fills the top half.
- **Filter traits:**
  - Heavy vignette: the top corners go to deep navy.
  - Highlights bloom: the clouds glow softly at their edges.
  - The frame edges are smeared soft (bottom-left deck, sky corners) while the centre stays readable.
  - Blacks are lifted and milky: no true black (p1 = 34). No pure white either.
  - Split tone: the shadows go navy-blue, the sunlit concrete goes warm cream.
  - The pool and sky are pushed to saturated cobalt and ultramarine.

**Why it works (my reading):** an ordinary place everyone has stood in, made to look like a memory by the lens alone. There is no oddity, which matches our "no oddity, liminal through light" route. The 拍同款 · 氛围柔光 chip on the post also invites copies (181.6万 uses). Whether the chip helps distribution is unverified.

**Two ways to get it, untested:**
1. **In post:** generate a clean still, then apply 氛围柔光 in the Douyin editor at posting, or our own glow-vignette-edge-blur pass. This is free, repeatable, and keeps Seedream from adding fake "fantasy glow".
2. **In the prompt:** use the look block below.

**Look block (draft)**
> Vertical 3:4 photograph on a 35mm compact with a 28mm lens, Kodak Ektar 100, shot through a Black Pro-Mist 1/2 filter. Bright midday summer sun. Highlights bloom softly and clouds glow at their edges. Blacks are lifted and milky, with no pure black and no pure white. A heavy natural lens vignette darkens all four corners to deep blue. The frame edges are soft and smeared; only the centre is sharp. Saturated cobalt sky and water, warm cream sunlight on concrete.
> Avoid: HDR, crisp digital sharpness, fantasy sparkle, lens-flare streaks, people, text.

**Fits:** poolcore and liminal spaces, `[[blue-hour-film-flash-recipe]]` (the same "lighting and texture carry it" lesson, in daylight).

---

## B · 国风 shine: gold silk, backlight and crimson maple

**Observations**
- **B1 · 一叶扁舟:**
  - A woman in a loose white robe lies asleep in a huge translucent gold "leaf" hammock with gold veins, floating above a sea of clouds. Islands of crimson-orange maple stand in the cloud, and leaves fall through the air.
  - The sun is low and behind, top-right. It rim-lights her hair and turns the silk into a glowing, specular gold.
  - Out-of-focus maple in the bottom-left foreground; aerial haze to the horizon.
- **B2:**
  - A macro close-up. Her face, eyes closed, sits behind a backlit red maple leaf, with one water droplet hanging from its tip and catching a point of light.
  - Very shallow depth of field. Warm peach skin and glossy lips against a cool blue-teal background.
- **Format:** both are 2.39:1 widescreen frames, letterboxed in the vertical post.

**What makes it "shiny" (my reading)**
- **Translucent materials lit from behind:** silk, leaf, droplets. The shine is backlight passing through or glinting off a surface, not an added glow.
- **One low golden sun with haze.**
- **Palette:** gold and cream highlights, crimson-orange maple as the accent, cool grey-blue shadows in the cloud. Warm against cool.
- **国风 comes from costume, the maple leaf, the cloud sea and the poem**, not from buildings. That's a new route next to our palace work (`[[chinese-architecture-awe-and-respect]]`).
- **Rhythm:** the set alternates a mega wide shot (a person tiny on a giant leaf) with a macro close-up (a leaf on a face).

**Look block (draft)**
> Cinematic film still, 2.39:1, 35mm Kodak Vision3 250D, anamorphic lens, low golden sun directly behind the subject in light haze. Translucent gold silk glows where the sun passes through it, with bright specular sheen along its folds. Rim light on hair and fabric; a water droplet catches one point of light. Warm gold and cream highlights, crimson-orange maple accents, cool grey-blue shadows. Shallow depth of field with out-of-focus leaves in the foreground. Fine film grain, real skin texture.
> Avoid: smooth plastic skin, glitter particles, fantasy sparkle, an over-graded orange-and-teal look, game-engine render, text.

**Risks:** B1 still reads somewhat as an AI render: smooth, with mushy hands and feet. Keep `[[no-smooth-ai-texture-no-fake-smiles]]` in force and plant grain and skin texture.

---

## C · Mega core: one colossal form, a hole to the sky, a tiny tree

**Observations**
- **C1:**
  - A worm's-eye view up an immense round shaft. Its walls are concentric rings of thousands of tiny lights, like stacked floors of a circular city.
  - A column of falling water and mist drops from the round opening of sky to a black tree line at the bottom.
  - Centred and symmetric. Nearly monochrome grey (sat 29). The mist is the brightest thing in the frame.
- **C2:**
  - A colossal ring of rock covered in dusty-rose trees, with long waterfalls pouring from its rim. A small moon hangs in the hole.
  - One small rose tree stands on dark rocks at the bottom centre. Fog fills the base.
  - Very low contrast (sd 25): no black, no white, a matte faded print.

**The recipe (my reading)**
- **Size:** one coherent structure fills 70–90% of the frame and runs off its edges.
- **Scale anchor:** a tiny one at the bottom, a single tree or a tree line, not a crowd.
- **Haze** between the planes does the scale work, together with a long fall of water.
- **An opening onto the sky or moon** in the structure gives it the "destination" feeling (这，就是我想去的终点).
- **Palette:** dark, desaturated and matte, slate grey plus at most one muted accent (dusty rose). This is the opposite of our bright two-colour worlds, and it still reads as "this can't exist".
- **Agrees with** `[[realistic-but-obviously-unreal]]` (absurd scale, devices instead of comparisons) and the megastructure note (one colossal coherent mass, not stacked buildings).

**Look block (draft)**
> Vertical 3:4 photograph, worm's-eye one-point view, centred and symmetric. Medium-format film printed flat and matte: low contrast, no true black, no pure white, slightly faded. Near-monochrome slate grey with one muted accent of dusty rose. Soft light falls only from the opening in the sky above, through thick mist. The structure fills most of the frame and runs off its top and sides; mist and falling water cross it. One small tree stands at the bottom centre for scale.
> Avoid: saturated colour, sci-fi neon, spaceships, crowds, HDR, crisp digital detail, fantasy glow, text.

**Idea that fits this lane (untested):** look straight up from the courtyard of an impossibly tall 福建土楼. Its rings of lit windows climb thousands of storeys into cloud, and a thin waterfall falls from the circle of sky into the courtyard well, beside one small tree. It's C1's ring of lights, but with a Chinese anchor everyone recognises.

---

## D · Film texture: blue hour, one practical light, wet surfaces

The caption gives the creator's method: the style line names only one master ("风格只写「某位大师风格」"). Our skill already caps it at one reference artist per prompt.

**Observations**
- **D1:**
  - An extreme close-up through a rain-streaked car window at night.
  - Her eye is sharp. Her wet face and dripping hair glisten, and an out-of-focus white-and-red shape fills the left foreground.
  - City lights become big round white, pink and red bokeh behind rain trails. Green-teal shadows, warm skin.
- **D2:**
  - An empty two-lane desert highway in late blue hour, from road height, in one-point perspective. The wet asphalt mirrors one far pair of headlights and the moon.
  - The moon has a soft halo in a thin band of cloud. Telephone poles recede; faint stars.
  - The 99th-percentile brightness is only 158: the whole frame sits in a dim, even dusk, and nothing clips except the moon.
- **D3:**
  - A couple on the same road at blue hour. Wind lifts their hair, and their foreheads touch.
  - A small warm light held between them lights her face from below; the set's first thumbnail shows a lighter or candle.
  - He is a dark silhouette in a suit. Wind turbines and power poles stand on the horizon.
  - Low key: 49% of the frame is near-black.
- **Format:** all three are 2.39:1 frames.

**The texture, in parts (my reading)**
- **Grain and halation:** fine visible grain. Every light (moon, headlights, bokeh, lighter) has a soft glow and halo rather than a hard edge.
- **Highlight roll-off:** highlights fade gently; skin never goes shiny-white.
- **Colour split:** teal-green shadows against warm skin and warm practicals, held at modest saturation (61–92, against 120 for A).
- **Wet and moving surfaces** carry the specular detail: rain on glass, wet asphalt, wet skin, wind in hair.
- **Light:** blue-hour ambient plus one warm practical in frame. This is the same light recipe as our first liked round (`[[blue-hour-film-flash-recipe]]`), but with cinema film instead of a snapshot flash.
- **Depth of field:** shallow, with something out of focus in the foreground.

**Look block (draft)**
> Cinematic film still, 2.39:1, 35mm Kodak Vision3 500T, anamorphic lens, pushed one stop. Fine visible grain and soft halation around every light. Highlights roll off gently; deep shadows with a teal-green tint; warm skin. Late blue hour, lit by one warm practical source in the frame (a lighter, headlights, a streetlight, the moon). Wet surfaces carry specular reflections. Shallow depth of field with an out-of-focus element in the foreground. In the style of [one master only].
> Avoid: clean digital sharpness, smooth plastic skin, HDR, over-saturated teal-and-orange, fantasy glow, text.

**Master candidates (my guesses, to test one at a time):** Wong Kar-wai with Christopher Doyle (D1), Robby Müller's *Paris, Texas* (D2), Bradford Young (D3, low-key, underexposed and soft).

**People:** D2 shows the texture carries an empty place on its own. D3 belongs to the romantic lane the owner already likes (散场以后); `[[no-forced-couples-liminal-core]]` still holds for other sets.

---

## What all eight share (my reading)

1. **Light comes from one place you can see,** usually from behind or within the frame: the sun behind the subject, the sky opening, a lighter, headlights. Nothing is lit flat from the front.
2. **Air between the planes in every frame:** glow, cloud sea, mist, rain, dusk haze.
3. **No frame clips to pure white** (p99 119–221). The blacks are either lifted and milky (A, B, C2) or deep but soft (C1, D).
4. **A narrow palette:** two hue families plus neutrals.
5. **One central subject,** with big empty areas around it.
6. **Sets alternate wide and close.** B and D cut from a world-scale wide to a macro of skin, leaf or droplet. Our sets have mostly stayed at one distance.
7. **Five of the eight are 2.39:1 frames inside a vertical post.** The letterbox itself says "film still". Our skill currently fixes every still at 3:4.

## Open questions for the owner

- **Widescreen:** should cinematic lanes (B and D) use 2.39:1 frames, or stay 3:4? Widescreen reads as cinema but shows smaller on the phone. Seedream's 21:9 option on Jimeng is unverified.
- **氛围柔光:** apply it at posting (in-app or in our own post pass), or ask Seedream for it in the prompt?
- **Lanes:** which of A–D to test first.

## Next test (proposal, not approved)

- **One frame per lane, four in all,** each built from the look block above, on Seedream 5.5 at count 1.
- **Free canvas first;** paid only if the free queue hangs for more than a minute: 6 credits each, 24 at most.
- **A can also be tested free** by running a post-filter pass on an existing liked still before generating anything.
