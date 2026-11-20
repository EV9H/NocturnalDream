---
name: nocturnal-dream-image-sets
description: Make Nocturnal Dream image sets (图文 posts for Douyin and 小红书) - an ordered run of photographic AI stills with a liminal, haunted-memory mood. Use for pitching set ideas, writing still prompts, generating test images on Jimeng, reviewing results, building and logging a set. For video work use the nocturnal-dream skill.
---

# Nocturnal Dream: Image Sets

An image set is 6–9 stills posted as one 图文, swiped in order, with music. It succeeds when the first image stops the scroll and the rest make the viewer feel something they can't quite name.

These rules come from the owner's reactions to test images. They are still proposals until released sets have audience data. Change them when the owner's feedback or the data says so, and note what changed and why in the scene's REVIEW.md.

## 1. Taste

**Mood: liminal and haunted memory.** The reference feeling is The Caretaker's music: a familiar place, slightly wrong, as if remembered rather than seen. Empty or nearly empty spaces, time that has slipped, warmth that is a little too still. Quiet, tender and uncanny, never horror.

**Look: a real photograph someone took.** Every image should read as a found or candid photo with a specific camera, film and era. No polished render, no HDR, no even, perfect sharpness.

**Subject: something striking.** Either the image itself is unusual (an impossible thing inside an ordinary space) or the photography is strong enough to carry an ordinary scene. Bland, correct pictures fail.

**Oddity: zero or one per image, never more.**
- An image may have one impossible or slipped detail, or none at all. Then the feeling comes from light, time and emptiness alone.
- Each set needs at least one clear oddity, usually in the cover or the last image, so the post passes the one-second test.
- Play the oddity completely straight: the same light, grain and framing as the rest of the frame, no emphasis, as if the camera didn't notice it. Two or more oddities, or a staged, emphasised one, turn the image into fantasy illustration.

**Reference artists.** Name one in the prompt or the brief to steer the look.
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

## 3. The prompt: a photographer's spec sheet

Write every prompt as these blocks, in this order. Fill each one. Leaving one out lets the model fall back to its generic look.

1. **Format.** Vertical 3:4 photograph.
2. **Look and era.** Camera body, lens and aperture, film stock or sensor, the year or decade, and how the film or file has aged (colour shift, fading, dust, scratches, noise, halation, grain).
3. **Camera position.** Who is holding it and where: height (sitting, standing, waist, tripod), distance, direction, tilt, what is in focus and what is blurred, and any foreground element between camera and subject (doorframe, glass, reflection).
4. **Scene.** The place, the time of day, the specific objects at near, middle and far, the oddity if this image has one (at most one), and any person (small, from behind or blurred, faces not the point).
5. **Light.** Each source, its direction and colour, and what stays dark.
6. **Mood.** One or two sentences of the feeling, written plainly.
7. **Avoid.** Only the things the model keeps adding: readable text, logos, faces, horror cues, modern clean interiors, cinematic grading.

Craft notes:
- Name a real camera, lens and film every time. It is the strongest lever on the look.
- Plant flaws: wear, dust, uneven light, slightly crooked framing, imperfect focus.
- One light logic per image. If something impossible is in the frame, it must light the scene, reflect, or cast shadows the way it would if real.
- No text in the image. Captions go in the post.
- Keep the main subject out of the bottom fifth, where the caption and buttons sit.

## 4. Generating on Jimeng

- **Model: Seedream 5.5 only.** Other models tested so far looked like AI slop or cost far more. Try another only if the owner asks.
- **One image per run** (count 1) while exploring. Use batches only after a direction is approved.
- **Free first.** Free Seedream images are started in the Jimeng web canvas with the **0积分畅用** switch on (the CLI has no free option). Before clicking generate, check the switch is on, the price reads 0/张, and the panel shows the right prompt, 3:4 and 1张.
- **Paid only when the free queue is stuck**, and only within the month's approved cap (see [Subscriptions](../../Subscriptions.md)). Save the node, run `node quote`, confirm with `--credit-ceiling` set to the quote, then run. Never run a model you have not quoted. Log every charge.
- When editing a saved node, pass `--prompt` again, or the edit fails and the quote stays stale.
- Download results with `dreamina-canvas resource download` into the scene's `Renders/`, keeping every take, including rejects.

## 5. Reviewing a result

For each image, write two separate things:
- **Observations:** what is actually in the frame, including what differs from the prompt.
- **Judgement:** whether it works, marked as yours until the owner confirms.

Check:
- Does it look like a real photo from the named camera and era, or like a render?
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
- The last image pays off or leaves a question that people will answer in the comments.
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
  - End the caption with a question the viewer can answer from their own life.
  - Use 3–5 hashtags.
- After release, log views, saves, comments and swipe-through per 1,000 views. Note which image the comments mention.
