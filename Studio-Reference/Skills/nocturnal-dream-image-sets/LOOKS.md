# Target looks

On 2026-11-25 the owner set the quality bar with eight Douyin stills in four groups. Each group is a **lane**: a finished look we work towards. Lane B is locked; lanes A, C and D are still being tuned.

- **Contact sheet:** [references/vibe-board-2026-11-25.jpg](references/vibe-board-2026-11-25.jpg).
- **Full screenshots and first analysis:** `Scenes/Image-Set-Lab/References/vibe-board-2026-11-25/` and `Scenes/Image-Set-Lab/VIBE-BOARD-2026-11-25.md`.

| Lane | Look | Reference | What it teaches |
| --- | --- | --- | --- |
| A | 氛围柔光 soft glow | an empty desert pool, @24ZR | A real liminal place made into a memory by the filter alone |
| B | 国风 shine (**locked on LB04**) | gold leaf-boat over a cloud sea, and a maple-leaf close-up; @MosaicEcho马赛回声 | Gold-leaf silk with a soft glow, strong light and shadow, a far distance with things in it |
| C | Mega core | a light-ringed shaft with a waterfall, and a rose-tree ring with a moon; @MosaicEcho | One colossal form, an opening to the sky, a tiny tree, a dark matte palette |
| D | Film texture (胶片) | rain-window face, blue-hour desert road, couple lit by a lighter; @赵一帆_ | 35mm grain and halation, one warm practical light at blue hour, wet surfaces |

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

## Lane A · 氛围柔光 soft glow

**Target feeling:** "I've been here," seen through a memory: sunny, empty, glowing at the edges.

**Suits:** liminal everyday places under big summer sky or bright sun. For example an outdoor pool, a court, a car park, a roadside motel, a bus stop or a school field. No oddity is needed.

**There when:**
- All four corners fall off to deep blue.
- Clouds and bright surfaces bloom softly at their edges.
- The frame edges are smeared soft while the centre stays readable.
- The blacks are milky; nothing is pure black or pure white.
- The shadows go navy and the sunlit surfaces warm cream.
- Sky and water are saturated cobalt.

**Numbers:** sat 100–135 · lum 90–120 · black 20–45 · white 195–235 · vig 0.45–0.85 · shR-B −80 to −15 · hiR-B 0–45.

**Look block**
```text
Vertical 9:16 photograph on a 35mm compact with a 28mm lens, Kodak Ektar 100, shot through a Black Pro-Mist 1/2 filter, bright midday summer sun. Highlights bloom softly and clouds glow at their edges. Blacks are lifted and milky; no pure black, no pure white. A heavy natural lens vignette darkens all four corners to deep blue. The frame edges are soft and smeared; only the centre is sharp. Saturated cobalt sky and water, navy shadows, warm cream sunlight on pale surfaces.
```
**Avoid:** HDR, crisp digital sharpness, fantasy sparkle, lens-flare streaks, text.

**Ladder** (change one per take, in this order):
1. **Route.** The real look is a phone filter, so first try generating a clean still and applying Douyin's 氛围柔光 in the editor when posting. One filter across every image also locks the set's style. Compare that with the prompt route.
2. **Filter strength:** Pro-Mist 1/4 → 1/2 → 1.
3. **Vignette and edge-blur wording.**
4. **Film:** Ektar 100 for cobalt; Portra 400 for softer, warmer skin and sand.

**Watch for:** Seedream's "fantasy glow" (light rays, sparkle) instead of a soft halo, and a glow so strong the place disappears.

**Best so far:** none yet.

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

## Lane C · Mega core

**Target feeling:** silent awe and longing, "the place I want to end up" (这，就是我想去的终点).

**There when:**
- **The giant:** one coherent colossal form fills 70–90% of the frame and runs off at least two edges.
- **The opening:** a hole, ring or shaft-mouth shows sky or a small moon.
- **Scale:** falling water and mist cross the structure.
- **The anchor:** one tiny scale mark (a single tree or a tree line) sits at the bottom centre.
- **The palette:** dark, matte and near-monochrome slate grey, with at most one muted accent such as dusty rose. No black and no white anywhere except the brightest mist.

**Numbers:** sat 20–55 · lum 55–85 · sd 20–50 · white 150–220 · dark% 0–35.

**Look block**
```text
Vertical 3:4 photograph, worm's-eye one-point view, centred and symmetric. Medium-format film printed flat and matte: low contrast, no true black, no pure white, slightly faded. Near-monochrome slate grey with one muted accent of dusty rose. Soft light falls only from the opening in the sky above, through thick mist. The structure fills most of the frame and runs off its top and sides; mist and long falls of water cross it. One small tree stands at the bottom centre for scale.
```
**Avoid:** saturated colour, sci-fi neon, spaceships, crowds, a blurred foreground layer, HDR, crisp digital detail, fantasy glow, text.

**Idea in this lane:** look straight up from the courtyard of an impossibly tall 福建土楼. Rings of lit windows climb into cloud, and a thin waterfall falls from the circle of sky into the courtyard well, beside one small tree.

**Ladder:**
1. **Scale devices:** cut off by the frame, mist crossing, a longer fall of water. Seedream ignores "as tall as X" comparisons, so show the size instead.
2. **Flat, matte print wording.**
3. **Viewpoint:** worm's-eye centred, or from far off with the horizon low.
4. **The opening:** sky, moon or light.

**Watch for:**
- Stacks of small buildings instead of one mass (T218, T220).
- A blurred foreground plus a middle layer plus a far giant (T151–T154). C has a single small anchor, not a foreground layer.
- Plausible-big, which reads as a real place.

**Best so far:** none yet.

---

## Lane D · Film texture (胶片)

**Target feeling:** a real film photograph someone took on a night that mattered: lonely, tender, windy, night coming on.

**胶片, not cinema (owner, 2026-11-25, after LD01).** LD01, a phone booth seen through a windshield, was "more on the cinematic side than on a 胶片 side". The owner asked whether it was too high-res. My reading of the causes:
- The block asked for a motion-picture stock, an anamorphic lens and a "film still".
- The render was clean 2K digital with no grain and deep, clean blacks.
- The 21:9 letterbox itself says cinema.

The block below now asks for a still-film camera, a scanned negative, clumpy grain and softness. LD02 tests it at 1.5K. If it still reads as cinema, the next lever is the 35mm still frame (3:2), instead of 21:9.

**There when:**
- **Grain** is visible at phone size, and every light (moon, headlights, lighter, bokeh) has a soft halo.
- **Highlights** fade gently: a lit face never goes shiny-white.
- **Colour:** shadows lean green-teal, while skin and the practical light stay warm. Saturation is modest.
- **Light:** late blue hour plus one warm practical light in the frame.
- **Wet surfaces** carry the sparkle: rain on glass, a wet road, wet skin. Wind moves hair or cloth.
- **Depth of field** is shallow, with an out-of-focus element in the foreground.

**Numbers:** sat 50–100 · lum 50–100 · white 110–235 · dark% 5–55 · shG 2–25 (green-teal shadows) · shR-B −25 to 15.

**Look block (v02, after the owner's 胶片 note)**
```text
Wide 21:9 frame cropped from a 35mm film photograph: a Contax T2 compact on CineStill 800T, pushed one stop, scanned from the negative. Heavy, clumpy film grain across the whole frame, slightly soft focus, red-orange halation glowing around every light, highlights that bloom and roll off, milky lifted blacks with a green-teal cast, warm skin, colours slightly shifted. Not a cinema camera and not a movie still: a real photograph a friend took, a little imperfect. Late blue hour, lit by one warm practical source in the frame.
```
**Avoid:** posed smiles, smooth plastic skin, clean digital sharpness, HDR, blockbuster orange-and-teal, glossy movie-poster look, text.

**Resolution:** 1.5K (4 credits) is on test against 2K for a softer, more 胶片 file.

The v01 block gave LD01's cinema look: "Cinematic film still on 35mm Kodak Vision3 500T with an anamorphic lens… In the style of [one master]". Keep it only for a deliberate film-still look.

**One master per prompt** (for the v01 film-still block). The reference creator says their style line names only one master. Test these one at a time (my guesses from the frames):
- Wong Kar-wai with Christopher Doyle, for rain, neon and close faces.
- Robby Müller's *Paris, Texas*, for empty roads and dusk.
- Bradford Young, for low-key, underexposed, soft light.

**People:**
- Empty places carry this texture well; the desert-road frame has no one in it.
- Couples belong only in the romantic lane the owner already likes, 散场以后. Elsewhere the space is the subject, with no romance beats.

**Ladder:**
1. **The still-film line:** CineStill 800T or Portra 800 pushed; Contax T2, Olympus mju-II or a 35mm SLR.
2. **Resolution:** 1.5K against 2K.
3. **Format:** 21:9 crop against the full 35mm still frame (3:2).
4. **The practical light:** what it is and where it sits.
5. **The wet surface.**

**Watch for:**
- Muddy crushed blacks with an orange cast (rejected in 散场以后).
- Over-graded teal-and-orange.
- Script-like smiles or poses.

**Best so far:** none yet.

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

- **Lane A route:** the Douyin filter when posting, or the prompt.
- **People in B and D:** how often a person is the subject.
