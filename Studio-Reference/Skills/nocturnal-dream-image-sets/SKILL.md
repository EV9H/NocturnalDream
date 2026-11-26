---
name: nocturnal-dream-image-sets
description: Make Nocturnal Dream image sets (图文 posts for Douyin and 小红书) - an ordered run of photographic AI stills with a liminal, haunted-memory mood, built in one of four target looks (氛围柔光 soft glow, 国风 shine, mega core, cinema film texture). Use for pitching set ideas, writing still prompts, generating test images on Jimeng, reviewing and measuring results, building and logging a set. For video work use the nocturnal-dream skill.
---

# Nocturnal Dream: Image Sets

An image set is 6–9 stills posted as one 图文, swiped in order, with music. It succeeds when the first image stops the scroll and the rest make the viewer feel something they can't quite name.

These rules come from the owner's reactions to test images. They are still proposals until released sets have audience data. Change them when the owner's feedback or the data says so, and note what changed and why in the scene's REVIEW.md.

**Read [Studio-Reference/OWNER-TASTE.md](../../OWNER-TASTE.md) first.** It holds the owner's later verdicts. Where it disagrees with this skill, it wins; it lists any known conflicts.

**Target looks.** The owner's quality bar (2026-11-25) is four looks, one per lane, in [LOOKS.md](LOOKS.md):
- **A:** 氛围柔光 soft glow.
- **B:** 国风 shine.
- **C:** mega core.
- **D:** cinema film texture.

Start every new set from one lane: its look block, its "there when" checks and its ladder of fixes. Where a lane's look block differs from the defaults in §3, the lane wins.

## 1. Taste

**Mood: liminal and haunted memory.** The reference feeling is The Caretaker's music: a familiar place, slightly wrong, as if remembered rather than seen. Empty or nearly empty spaces, time that has slipped, warmth that is a little too still. Quiet, tender and uncanny, never horror.

**Look: a real photograph someone took.** Every image should read as a found or candid photo with a specific camera, film and era. No polished render, no HDR, no even, perfect sharpness.

**Subject: something striking.** Either the image itself is unusual (an impossible thing inside an ordinary space) or the photography is strong enough to carry an ordinary scene. Bland, correct pictures fail.

**Oddity: zero or one per image, never more.**
- An image may have one impossible or slipped detail, or none at all. Then the feeling comes from light, time and emptiness alone.
- Each set needs at least one clear oddity, usually in the cover or the last image, so the post passes the one-second test.
- Play the oddity completely straight: the same light, grain and framing as the rest of the frame, no emphasis, as if the camera didn't notice it. Two or more oddities, or a staged, emphasised one, turn the image into fantasy illustration.

**Reference artists.** Use them as mood vocabulary in the brief, not as the look: the owner found these photographers' methods "kinda boring" as a route (T42–T47). The look comes from a capture device or a lane's look block. Put at most one artist in a prompt.
- *One oddity, played straight:*
  - René Magritte (*The Empire of Light*: a night street under a day sky)
  - Gregory Crewdson (*Twilight*, *Beneath the Roses*: staged suburban dusk with one strange event)
  - Jeff Wall (staged photographs that read as documents)
  - Kane Pixels (*The Backrooms*: found-footage realism in ordinary spaces)
- *No oddity, liminal through light and time:*
  - Todd Hido (*House Hunting*: houses at night through fog or a windshield)
  - Hiroshi Sugimoto (*Theaters*: a whole film in one exposure)
  - Edward Hopper (rooms where time has stopped)
  - Thomas Demand (rooms rebuilt in paper, almost right)

**Not by default:** national landmarks, traditional culture, older people as the subject, tourist viewpoints, scenic landscapes. Any of these can be one direction, but never the default. Places can be anywhere in the world.

## 2. The idea

Pitch an idea in one sentence: **a space everyone has stood in + the set's oddity + one feeling.** Say which images carry the oddity and which carry mood alone.

Test it before writing any prompt:
- **One-second test.** Does a thumbnail of the cover read as both "I know this kind of place" and "this is not right"?
- **Recognition.** Is the space universal: a room, corridor, vehicle, waiting area, public building, street at night? It should not need a caption to place it.
- **Feeling.** Can you name the one feeling (loneliness, nostalgia, calm unease, tenderness) and the detail that causes it?
- **Swipe reason.** Does the idea give a reason to see the next image (the change grows, the place repeats, the night goes on)?

Pitch at least three ideas that differ in what the viewer experiences, not only in props. Recommend one and say why.

## 3. The prompt: a snapshot, not a spec sheet

Write about 200–250 words in five short parts. See [EXAMPLES.md](EXAMPLES.md) for covers that worked.

1. **Format.** Vertical 3:4 photograph by default. A set in a lane uses that lane's ratio from [LOOKS.md](LOOKS.md#format-decided-by-the-owner-2026-11-25): A 9:16, B 21:9, C 3:4, D 21:9.
2. **Camera and film.** For a set in a lane, paste that lane's look block from [LOOKS.md](LOOKS.md) here; it names its own camera, film, filter and palette. Otherwise:
   - Name one real camera, lens and film or sensor, the year, and how the print or file has aged.
   - Prefer cameras an ordinary person owned: a 35mm SLR, a rangefinder, a compact, a disposable.
   - Let the film carry the colour, and don't add diffusion filters. When the set's oddity is a palette no real place has, name its two main colours in one line ("two main colours only: …"); don't list more.
3. **Where the camera is.** A person's own viewpoint (a doorway, a seat, a window, standing height), with the tilt, what is sharp, and what is soft in front. Use a tripod or a high view only when the place calls for it.
4. **The scene, with its light inside it.**
   - The place, the hour, and specific everyday objects near, middle and far.
   - Write the light as a physical event from a source you can see.
   - Zero or one oddity, stated plainly as a fact.
   - People only as they would really be there: none, one or many. No plot.
5. **Mood and avoid.** The feeling in one or two plain sentences. Then four to six things to avoid, only what the model keeps adding.

Craft notes:
- Name a real camera, lens and film every time. It is the strongest lever on the look.
- Shorter beats longer. Long, over-specified prompts come out staged and rendered.
- Plant flaws: wear, dust, uneven light, slightly crooked framing, imperfect focus.
- One light logic per image. If something impossible is in the frame, it must light the scene, reflect, or cast shadows the way it would if real.
- No text in the image. Captions go in the post.
- Keep the main subject out of the bottom fifth, where the caption and buttons sit.

## 4. Generating on Jimeng

See [JIMENG-CLI.md](JIMENG-CLI.md) for the exact `dreamina-canvas` CLI loop, Seedream 5.5 sizing table, canvas layout, and gotchas.

- **Model: Seedream 5.5 only.** Other models tested so far looked like AI slop or cost far more. Try another only if the owner asks.
- **One image per run** (count 1) while exploring. Use batches only after a direction is approved.
- **Free first.** Free Seedream images are started in the Jimeng web canvas with the **0积分畅用** switch on (the CLI has no free option). Before clicking generate, check the switch is on, the price reads 0/张, and the panel shows the right prompt, 3:4 and 1张.
- **Paid only when the free queue is stuck**, and only within the month's approved cap (see [Subscriptions](../../Subscriptions.md)). Save the node, run `node quote`, confirm with `--credit-ceiling` set to the quote, then run. Never run a model you have not quoted. Log every charge.
- When editing a saved node, pass `--prompt` again, or the edit fails and the quote stays stale.
- Download results with `dreamina-canvas resource download` into the scene's `Renders/`, keeping every take, including rejects.
- After every run, log the quote, the resource's `creditsAmount` and the balance. A quote of 0 means that run is free, per the official skill. LB04's quote of 0 followed by a `creditsAmount` of 6 is unverified; see [JIMENG-CLI.md](JIMENG-CLI.md).
- Before generating, also load the official `dreamina-canvas-cli` skill. JIMENG-CLI.md covers how this studio applies it: the one-step single-frame run, referencing the cover for set consistency, retry rules and request IDs.

## 5. Reviewing a result

For each image, write two separate things:
- **Observations:** what is actually in the frame, including what differs from the prompt. For a set in a lane, also run `python3 scripts/measure_look.py <render> --lane <A-D>` and note any off-target numbers.
- **Judgement:** whether it works, marked as yours until the owner confirms.

Check:
- Does it look like a real photo from the named camera and era, or like a render? And does the place still read as impossible? A believable photo of a place that could exist fails (T155–T162).
- Does it pass the one-second test as a thumbnail?
- Is the impossible detail physically consistent with the light and space?
- Any AI faults: warped geometry, melted hands, gibberish text, repeated windows or tiles?

Change one thing at a time between takes, and say which.

## 6. Building the set

Choose the structure before generating the rest:
- **One place, changing:** the same frame and light, with one thing changing step by step.
- **One condition, many places:** the same impossible detail in different universal spaces.
- **A walk-in:** wide, closer, detail, then a surprising last image.
- **One journey:** the same viewpoint (a window, a seat) as the world outside changes.

Rules for every set:
- Image 1 is the strongest image, not the establishing one.
- Use one look across the set: copy the Look and era, Camera position and Light blocks into every prompt, and change only what the structure changes.
- Cut between wide and close. Follow a world-scale wide with a macro of skin, a leaf, a droplet, a hand or a material, in the same light and palette. All the owner's references do this; most of our sets have stayed at one distance.
- The last image pays off, or leaves something open that lingers.
- Lay the finished set side by side at phone size before posting. Check the light, colour and order.

## 7. Approval, records and release

- Get the owner's approval of the written idea before generating a set, and explicit approval for any spending above the approved cap.
- Each set or test series lives in `Scenes/<Name>/`:
  - `Prompts/`: every prompt, versioned.
  - `Renders/`: every take, numbered.
  - `REVIEW.md`: the credit ledger, node and submit IDs, model and settings, observations, judgements and the owner's verdicts.
- Release:
  - Turn the AI label on. It has been mandatory since 2025-09-01.
  - Pick the music from each platform's in-app library; never upload outside tracks.
  - Write the title and caption in Chinese.
  - Write the caption as short, open, plain lines that add what the photo can't (sound, heat, time, absent people). No question to the viewer and no self-posted first comment: the owner calls both engagement bait.
  - Use 3–5 hashtags.
- After release, log views, saves, comments and swipe-through per 1,000 views. Note which image the comments mention.
