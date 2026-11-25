# Target looks

On 2026-11-25 the owner set the quality bar with eight Douyin stills in four groups. Each group is a **lane**: a finished look we work towards. All four lanes are now set: A locked on LA02, B locked on LB04, C confirmed on LC07, and D locked for now on LD04.

- **Contact sheet:** [references/vibe-board-2026-11-25.jpg](references/vibe-board-2026-11-25.jpg).
- **Full screenshots and first analysis:** `Scenes/Image-Set-Lab/References/vibe-board-2026-11-25/` and `Scenes/Image-Set-Lab/VIBE-BOARD-2026-11-25.md`.

| Lane | Look | Reference | What it teaches |
| --- | --- | --- | --- |
| A | 氛围柔光 soft glow (**locked on LA02**) | an empty desert pool, @24ZR | A real liminal place made into a memory by the filter alone |
| B | 国风 shine (**locked on LB04**) | gold leaf-boat over a cloud sea, and a maple-leaf close-up; @MosaicEcho马赛回声 | Gold-leaf silk with a soft glow, strong light and shadow, a far distance with things in it |
| C | Mega core (**confirmed on LC07**) | a light-ringed shaft with a waterfall, and a rose-tree ring with a moon; @MosaicEcho | One mythical, majestic form in open sky framing the moon, with waterfalls, a tiny tree and a matte palette |
| D | Film texture (胶片) (**locked for now on LD04**; best as video) | rain-window face, blue-hour desert road, couple lit by a lighter; @赵一帆_ | 35mm grain and halation, one warm practical light at blue hour, wet surfaces |

## Working a lane

1. **Pick one lane per set** in the pitch, and say which.
2. **Copy the lane's look block** (below) into every prompt unchanged. It replaces the default camera and film part of the prompt (SKILL.md §3). Write only the camera position, the scene and the avoid line fresh for each image.
3. **Check each take three ways:**
   - Measure it against the lane: `python3 scripts/measure_look.py <render> --lane A` (add `--crop x0,y0,x1,y1` to cut any phone UI). Put any off-target numbers in the observations.
   - Go through the lane's "There when" list.
   - Write observations and judgement as in SKILL.md §5.
4. **If a take misses, change one lever,** working down the lane's ladder in order. Log which lever changed in the scene's REVIEW.md.
5. **When the owner confirms a take has hit the lane:**
   - Add its prompt to [EXAMPLES.md](EXAMPLES.md) under the lane.
   - Name the take under the lane's "Best so far".
   - Re-centre the lane's ranges in `measure_look.py` on that take.

The numbers check exposure, palette and finish only. The owner's eye decides.

**The look alone doesn't carry a post (owner, 2026-11-25).** The first lane covers (LA01–LD01) were "theme wise, not catchy or interesting enough": a bus stop, a lotus pond, a tall 土楼, a phone booth. Every frame also needs an idea that stops the scroll. That means either a place or motif everyone knows in an impossible state, or a moment with feeling in it. Test the idea with the one-second test (SKILL.md §2) before writing the prompt.

## The finish every lane shares

1. **One light source you can see,** usually behind the subject or in the frame: low sun, an opening in the sky, a lighter, headlights. Never flat front light.
2. **Air between the planes:** haze, mist, a sea of clouds, rain or dusk air in every frame.
3. **Highlights roll off.** Nothing clips to pure white; in all eight references the 99th percentile is between 119 and 221.
4. **A narrow palette:** two hue families plus neutrals. Name both in the prompt.
5. **One central subject** with big empty areas around it.
6. **Real texture:** grain, halation, skin pores, wet surfaces. Never smooth AI skin.
7. **Sets cut between wide and close.** Follow a world-scale wide with a macro of skin, a leaf, a droplet, a hand or a material, and keep the light and palette the same across the cut.

---

## Lane A · 氛围柔光 soft glow: LOCKED on LA02 (owner, 2026-11-25)

**Status:** locked. The owner said "A can lock too". Use this block as written; change only the camera position, the scene and the avoid line. Applying Douyin's 氛围柔光 filter when posting stays available as a finishing touch on top of it.

**Target feeling:** "I've been here," seen through a memory: sunny, empty, glowing at the edges, with one impossible thing.

**Suits:** poolcore and liminal everyday places under big summer sky. Outdoor pools, piers, streets, courts and car parks, each with one impossible change to the space. LA01's ordinary bus stop with no oddity was "not catchy". LA02's pool whose deck ends at a sea of clouds is the locked frame.

**Look block (v02, locked from LA02)**
```text
Vertical 9:16 photograph on a 35mm compact with a 28mm lens, Kodak Ektar 100, shot through a Black Pro-Mist 1/2 filter, bright midday summer sun, exposed for the sky so nothing burns out. Highlights bloom softly and clouds glow at their edges. Blacks are lifted and milky; no pure black, no pure white. A heavy natural lens vignette darkens all four corners to deep blue. The frame edges are soft and smeared; only the centre is sharp. Saturated cobalt sky and water, navy shadows, warm cream sunlight on pale surfaces.
```
**Avoid:** people, readable text or signs, HDR, crisp digital sharpness, fantasy sparkle, lens-flare streaks.

**Format:** 9:16 at 2K (6 credits).

**Artist palettes on the locked finish (owner, 2026-11-25).** The owner asked for "master-level, artist grade, color palette idea to create the visual impact and cleaniness". Keep the camera, filter and finish of the block. Swap its last sentence (the cobalt palette) for one named painter's palette, written as a closed list. Then add: "Clean composition: very few objects and large flat planes of colour, like a painting."

Palettes on test in LA06–LA11:
- Hockney's pool paintings: turquoise, pale pink, cerulean.
- Barragán: magenta-pink, saffron, deep blue.
- Magritte's daylight: cerulean, soft white, pale stone.
- Van Gogh: chrome yellow and cobalt.
- Yves Klein: ultramarine and white.
- O'Keeffe: soft pink, peach and bone, with one turquoise.

**There when:**
- All four corners fall off to deep blue.
- Clouds and bright surfaces bloom softly at their edges.
- Blacks are milky; nothing is pure black, and the clouds don't burn out.
- Shadows go navy and the sunlit surfaces warm cream.
- Saturated cobalt water and sky fill most of the frame.
- One strong diagonal, such as a pool edge or a road edge, runs from a bottom corner toward the horizon.

**Numbers** (re-centred on LA02 and A1): sat 100–130 · lum 95–125 · black 15–45 · white 195–248 · vig 0.35–0.85 · shR-B −80 to −35 · hiR-B 0–40.

**Best so far:** **LA02**, locked by the owner. Its prompt is in [EXAMPLES.md](EXAMPLES.md#lane-a--la02-pool-above-the-clouds).

**Watch for:**
- Seedream's "fantasy glow" (light rays, sparkle) instead of a soft halo.
- A glow so strong the place disappears.
- A pale ground (sand, asphalt) eating the frame: LA01 went too bright, with too little blue.

---

## Lane B · 国风 shine — LOCKED on LB04 (owner, 2026-11-25)

**Status:** locked. The owner confirmed LB04 ("much closer, can lock"). Use this block as written for every lane-B frame; change only the camera position, the scene and the avoid line.

**Target feeling:** poetic, weightless and precious: a classical line of poetry turned into light.

**Where the 国风 comes from:** materials, nature motifs and poems, not buildings. That means white or ivory silk robes, gold leaf in sheer silk, red maple (霜叶), lotus, jade, water droplets, seas of clouds, and a one-line poetic idea such as 一叶扁舟. If a building appears, keep the owner's architecture rules: faithful ornament, cinematic awe, and no gags on palace roofs.

**The owner's keys:**
1. **金箔般的丝绸:** silk that looks like gold leaf. Translucent amber where the sun passes through it, with a soft sheen.
2. **云雾梦幻的远方:** a dreamy far distance of cloud and mist, with things in it at several depths (maple islands, ridges, a peak), getting paler as they recede.
3. **A carefully chosen palette,** written as a closed list.
4. **The shine is a soft glow:** 胶片 plus a 柔光 (diffusion) filter on a cine lens. Edges bloom into halos; nothing glitters or looks metallic.
5. **Strong light and shadow:** deep warm shadow in folds and under the subject, against glowing rims. Soft glow does not mean soft everything.

**Look block (v03, locked)**
```text
Widescreen 21:9 photograph on 35mm colour negative film, Kodak Portra 400, a cinematic 50mm lens shot through a Black Pro-Mist 1/4 diffusion filter, late golden sun low behind the subject on the right. Strong light and shadow: the sun rims every edge with a soft glowing halo, while folds, fabric and the cloud undersides fall into deep warm brown and blue-grey shadow. The shine is a soft glow, never glittery or metallic. Fine film grain, rich colour, real skin texture. The palette, and nothing outside it: rich amber gold, warm ivory, crimson and rust-orange maple, a touch of cinnabar red, and blue-grey cloud shadow.
```
**In every scene, write:**
- a far distance with things in it at several depths;
- the gold material as sheer silk with gold leaf, glowing where the sun passes through it;
- for anyone resting, where the shade on their face comes from.

**Avoid:** washed-out pale haze, flat low contrast, metallic lamé, foil glitter, an all-gold sky, green tones, smooth plastic skin, ornate hairpins and heavy stage make-up, game-engine render, text.

**Format:** 21:9, as in the reference post, at 2K (6 credits).

**There when:**
- **Light:** a low sun sits behind the subject. Rims glow softly, and folds and cloud undersides hold deep warm or blue-grey shadow.
- **The gold:** it reads as gold leaf in sheer silk, never lamé.
- **The distance:** layered cloud with maple islands or ridges at several depths, and a peak on the horizon.
- **The colour:** amber gold, ivory and crimson-rust maple against blue-grey cloud shadow. No green, and no all-gold sky.
- **The foreground:** a soft out-of-focus element, such as a maple branch or leaves.
- **Skin:** real texture, with the face shaded when resting.

**Numbers** (re-centred on LB04 and B1): sat 75–120 · lum 85–110 · black 5–45 · white 185–235 · dark% 0–15 · shR-B −5 to 35 · hiR-B 35–80.

**Best so far:** **LB04**, confirmed by the owner (sat 90, lum 96, black 20). Its prompt is in [EXAMPLES.md](EXAMPLES.md#lane-b--lb04-gold-leaf-silk-sleeper).

**How we got here** (2026-11-25). Each take changed one thing the owner named:

| Take | Change | Result |
| --- | --- | --- |
| LB01 | A woman asleep on a backlit lotus leaf, in the v01 cinema block (Vision3 250D, anamorphic, "specular sheen") | Green, matte robe, a plain shore in the distance |
| LB02 | Gold-leaf silk, cloud-sea distance, closed palette list | Hard metallic lamé under an all-gold sky |
| LB03 | Portra 400 on a cine lens with Pro-Mist 1/2, "lifted milky blacks" | Soft shine, but washed out (lum 167, black 73) |
| LB04 | Pro-Mist 1/4, strong light and shadow, maple islands far off, fuller palette | Locked |

**Building a set from it:**
- Keep this finish, but find our own idea. LB04 sits very close to MosaicEcho's own frame, so take the finish, not the scene.
- Pair every wide with a macro in the same light: for example, a gold-silk wide, then a maple leaf with a droplet in front of closed eyes.

**Watch for:**
- Mushy hands and feet in wide shots. Keep them hidden, small or in shadow.
- So many falling leaves that it reads as fantasy illustration.
- A waxy AI face. The owner reads smooth skin with no grain as fake, and adding grain in post does not fix it.
- "Gold leaf" drawn as a printed pattern: LB04 wove in gold maple leaves. Fine once; say "beaten gold leaf, irregular flakes" if it starts to look like fabric print.

---

## Lane C · Mega core: confirmed on LC07 (owner, 2026-11-25)

**Status:** the owner confirmed LC07, the moon gate of heaven: "finally a really good one". Build lane-C frames from its look block and composition below, and change only the myth or subject.

**Target feeling:** silent awe and longing; mythical, majestic, a sense of destiny. "The place I want to end up" (这，就是我想去的终点).

**The owner's two rules:**
1. **Lane C is about composition and elements.** Keep the reference's grammar, and vary the subject, not the layout.
2. **Mythical and majestic, never a well.** "Why are we in a well." The subject that builds the composition is a mythical, majestic form standing in open sky. It is never a pit, shaft, well or any enclosed space. Chinese myth and poetry give the anchor.

**The composition (from LC07):**
- **The giant:** one colossal mythical form, centred, whose curve fills the frame and runs off the top and both sides. It frames a round opening.
- **The opening:** the full moon or a pale sky, in the centre of the frame and of the form.
- **The fall:** long waterfalls pour from the form and dissolve into mist long before they land.
- **The world below:** a sea of clouds, with ridges fading in the mist.
- **The anchor:** one small blossoming tree on dark rocks at the bottom centre, the only accent of colour.
- **The camera:** low, on a dark ridge far below, looking up with a wide lens.

**Look block (v02, from LC07)**
```text
Vertical 3:4 photograph, low-angle view, centred and symmetric. Medium-format film printed flat and matte: low contrast, no true black, no pure white, slightly faded, soft haze. Near-monochrome slate grey and pale stone, with one muted accent of dusty rose. Soft moonlight through mist.
```
**In every scene, write:**
- the mythical form and its size, with its curve running off the frame;
- what fills its opening (moon or sky);
- the waterfalls dissolving into mist;
- the sea of clouds below;
- the one small tree on dark rocks at the bottom centre.

**Avoid:** walls, wells, pits, tunnels, other buildings, people, saturated colour, sci-fi neon, spaceships, HDR, crisp digital detail, fantasy glow, text.

**Format:** 3:4 at 2K (6 credits).

**There when:**
- One centred mythical form frames the moon or the sky and runs off three edges.
- Waterfalls fall from it and vanish into mist; a sea of clouds and misty ridges lie below.
- One small tree sits at the bottom centre, the only colour.
- The finish is matte, hazy and near-monochrome, with no black and no white except the moon.

**Numbers** (re-centred on LC07, C1 and C2): sat 15–50 · lum 60–100 · sd 20–50 · white 150–220 · dark% 0–35.

**Best so far:** **LC07**, confirmed by the owner (sat 24, lum 95, sd 48). Its prompt is in [EXAMPLES.md](EXAMPLES.md#lane-c--lc07-moon-gate-of-heaven).

**More myths for the same grammar:**
- the Yellow River coming down from heaven (黄河之水天上来). LC06 needs the column to read clearly as falling water.
- the world tree (建木);
- the moon palace (广寒宫);
- 不周山, the pillar of heaven;
- 鹊桥, the magpie bridge across the Milky Way.

**How we got here** (2026-11-25):

| Take | What it was | Verdict |
| --- | --- | --- |
| LC01 | A tall 土楼 well looking up | "theme not catchy" |
| LC02 | The Mount Tai stair to the South Gate | "far from original": broke the composition |
| LC03–LC05 | A tiankeng ring city with a waterfall | Grammar matched, but "why are we in a well" |
| LC06 | The Yellow River coming down from heaven, star trails | Open sky; the column reads as a rising plume |
| LC07 | A mountain-sized moon gate framing the moon, waterfalls, one tree | "finally a really good one" |

**Watch for:**
- Wells, pits, shafts and canyons, which the owner rejected.
- Stacks of small buildings instead of one mass (T218, T220).
- A blurred foreground plus a middle layer plus a far giant (T151–T154). C has a single small anchor, not a foreground layer.
- Plausible-big, which reads as a real place.
- The model doubling the form: LC07 drew two nested arches. The owner liked it as it is, so don't "fix" it unless asked.

---

## Lane D · Film texture (胶片): LOCKED for now on LD04 (owner, 2026-11-25)

**Status:** locked for now. The owner: "D can lock for now, stop chasing; it is the best when it is video." Use this block for D stills, and don't spend more takes tuning it. The look is meant for video, so for moving D work use the nocturnal-dream (video) skill and carry this lens, filter and colour into the video prompt.

**Target feeling:** a real film photograph, or a film frame, from a night that mattered: lonely, tender, windy, night coming on.

**Lane D is about the look** (owner): lens, filter, colour. It is 胶片, not glossy cinema.

**Look block (v03, locked from LD04)**
```text
Wide 21:9 frame on 35mm colour negative film, Kodak Portra 800 pushed one stop, a vintage anamorphic 85mm lens shot wide open through a Black Pro-Mist 1/2 diffusion filter. Soft and low in contrast: every light blooms into a wide, gentle halo, and highlights stay creamy, never bright white. Muted colour: a soft grey-lavender dusk sky, dusty warm tan desert, green-teal shadows, and warm amber light on skin. Fine visible grain. Very shallow depth of field: the background is a soft blur with oval out-of-focus lights.
```
**In every scene, write:**
- a medium shot on the long lens;
- one warm practical light raking across the subjects up close (headlights, a lighter, a lamp), against cool dusk;
- a grey-lavender sky and warm tan ground.

**Avoid:** an all-blue frame, sunset colours, red glare, saturated colour, hard contrast, posed smiles, kissing unless asked, headlights or glare in the frame, smooth plastic skin, clean digital sharpness, HDR, glossy movie-poster look, text.

**Format:** 21:9 at 1.5K (4 credits).

**Numbers** (re-centred on LD04 and the D references): sat 45–100 · lum 50–100 · white 110–235 · dark% 5–55 · shG 0–25 · shR-B −25 to 15.

**Best so far:** **LD04**, locked for now. Its prompt is in [EXAMPLES.md](EXAMPLES.md#lane-d--ld04-highway-slow-dance-warm-key).

**How we got here** (2026-11-25):

| Take | Change | Result |
| --- | --- | --- |
| LD01 | Vision3 500T, anamorphic, "film still", phone booth | "More cinematic than 胶片" |
| LD02 | Contax T2 on CineStill 800T, scanned negative, 1.5K; a slow dance | More 胶片, but saturated, with a sunset band and red glare |
| LD03 | Anamorphic with Pro-Mist, muted colour, wide shot | Soft, but all blue, with the warm light far away |
| LD04 | 85mm medium shot, headlights raking warm across them, lavender sky, tan land | Locked for now. The model made them kiss, and the headlight shows in the corner |
| LD05 | Slow shutter, no kiss, no glare | Softer and better posed, but it lost the warm key |

**People:** couples belong only in the romantic lane the owner already likes, 散场以后. Empty places carry this texture well too.

**Watch for:**
- Muddy crushed blacks with an orange cast.
- Over-graded teal-and-orange.
- Scripted smiles or poses.

---

## Plan to reach the lanes

1. **Round 1, one cover per lane.** Four frames on the same day, each from its look block, compared side by side at phone size. The owner keeps or drops each lane.
2. **Round 2, tune.** For each lane the owner keeps, up to three takes, one ladder step per take, logged in REVIEW.md.
3. **Round 3, build.** A 6–9 image set in one lane, with the look block locked and the wide–close rhythm.
4. **A free check for lane A:** apply 氛围柔光 in the Douyin editor to an existing liked still before generating anything.

Spending follows SKILL.md §4 and §7: free canvas first, Seedream 5.5 at 6 credits a frame when paid, approval first.

## Format (decided by the owner, 2026-11-25)

Use the ratio the reference posts use ("whatever ratio that the popular douyin posts use"):
- **A:** 9:16, full-screen.
- **B:** 21:9.
- **C:** 3:4, 图文.
- **D:** 21:9. The 35mm still frame (3:2) is a possible lever if 21:9 keeps reading as cinema.

Seedream 5.5 on Jimeng offers all of these (`--ratio 9:16 | 21:9 | 3:4 | 3:2`).

## Open decisions (owner)

- **People in B and D:** how often a person is the subject.
