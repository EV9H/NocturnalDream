---
name: nocturnal-dream-image-sets
description: Make Nocturnal Dream image-set posts (抖音图文 / 小红书图文) - a batch of 6-9 photoreal AI stills in a deliberate order, with a cover, caption and licensed music. Use for planning, prompting, selecting, sequencing and releasing an image set, or for comparing image-set results with video posts. For video work use the nocturnal-dream skill.
---

# Nocturnal Dream: Image Sets

An image set is a short, ordered set of photoreal stills posted as one 图文 on Douyin and 小红书, with background music. It is the studio's second product line, next to video. Its job is to get more posts out of the same quality bar for less money and time. It is not a cheaper version of video work.

**The studio's rules still apply.** Use the [nocturnal-dream skill](../nocturnal-dream/SKILL.md) for the idea, look and still craft:
- the formula and the one-second test: [02 Concept](../nocturnal-dream/references/02-concept.md)
- looks: [03 Worlds and looks](../nocturnal-dream/references/03-worlds-and-looks.md)
- camera and composition: [04 Cinematography](../nocturnal-dream/references/04-cinematography.md)
- still prompts, references and real-place checks: [05 Keyframes](../nocturnal-dream/references/05-keyframes.md)
- audience and STEPPS: [10 Audience and popularity](../nocturnal-dream/references/10-audience-and-popularity.md)

This skill adds only what is different for image sets.

Everything here is a proposal until released sets are measured. The format was adopted on 2026-11-19 with no audience data yet.

## What makes an image set different from a video

- **The cover does all the hooking.** The feed shows only the first image, so it must pass the one-second test alone: a place the viewer knows, in a condition it can never have.
- **Every image is judged at full resolution.** There is no motion or 480p softness to hide flaws. Each image must meet the keyframe standard in [05](../nocturnal-dream/references/05-keyframes.md), not just the cover.
- **The order is the film.** Swiping is the camera move. A set needs a reason to keep swiping and a last image that pays off.
- **Music carries the emotion.** There is no designed sound, so the track choice does the work of the sound design.

## Set structures

Pick one before generating. Name it in the brief.

| Structure | How it runs | Best for | Example (unproven) |
| --- | --- | --- | --- |
| **One condition, many places** | The same impossible condition across 6–9 recognisable places | Reach and comments, because each place's viewers answer "我们这儿呢" | The same metre-deep snowstorm on the Bund, Guangzhou Tower, Chongqing's monorail, West Lake, Xiamen's coast |
| **One place, many conditions** | One famous view under a different impossible condition per image | A series signature and saves | The Bund in snow, then flood, aurora, sandstorm, fog to the top floors |
| **The walk-in** | Wide, closer, a detail, then one surprising last image | Depth and the feeling of being there, close to a scene film | A snowbound Bund: skyline, buried railing, a footprint, a lit window across the river |
| **Before and after** | Real-looking normal view, then the same frame altered, in pairs | Instant legibility and "wait, what?" | A Shanghai street in summer, then the same frame under snow |

Rules for every structure:
- **Image 1 is the strongest image**, not the establishing one.
- **One world block, one look.** Paste the same continuity text (from [05](../nocturnal-dream/references/05-keyframes.md)) into every prompt in the set so light, palette, lens feel and weather match.
- **Vary only what the structure varies.** In "one condition, many places", only the place changes. In "one place, many conditions", only the condition changes.
- **The last image invites a reply.** It holds the question the caption asks, or the most surprising image.
- **6–9 images.** Fewer than 6 feels thin, more than 9 loses swipes. This is an untested guess. Douyin allows up to 30.

## Format

- **Aspect ratio: 3:4 vertical by default.** It fills the feed on both Douyin and 小红书. Use 9:16 only if the set is Douyin-only. This is an unverified platform assumption, so check how the cover crops in each app before posting.
- **Resolution:** the largest native size the model offers (2K on Jimeng's Seedream 5.5 for most plans). No upscaled 1K images.
- **No text inside generated images.** Models produce gibberish characters. Put words in the caption, or add clean text in post if it is essential.
- **Keep subjects away from the bottom fifth,** where the caption and buttons overlay the image.

## Workflow

1. **Brief, then approval.** Write a short brief: structure, the condition, the list of places or conditions in order, the look, the music mood, the likely first three comments and the generation reach (see [10](../nocturnal-dream/references/10-audience-and-popularity.md)). The user approves the written direction before generation, as for any new scene.
2. **Spending check.** Unlimited image generation in a paid plan (for example Jimeng's 30-day unlimited Seedream 5.5) needs no extra spending approval. Any credit-based image model still needs explicit approval with the model, count and cost, as [08](../nocturnal-dream/references/08-production-and-qc.md) requires.
3. **Real-place check.** For each place, collect one real photo from the intended vantage. Verify landmark order, spacing and architecture style, as in [05](../nocturnal-dream/references/05-keyframes.md).
4. **Shared blocks.** Write the world block and look block once.
5. **Generate per position.** For each image in the set, generate a batch of 4–8 candidates. Change one variable per batch.
6. **Select per position.** Score each candidate on the keyframe QC in [05](../nocturnal-dream/references/05-keyframes.md). Reject any image with a wrong landmark, warped geometry or visible AI artifacts (melted hands, gibberish signs, repeated windows).
7. **Repair.** Fix local faults by inpainting, cropping or retouching. Do not post a set with one weak image: replace it or cut the set shorter.
8. **Sequence check.** Lay all images side by side at phone size. Do they share light and palette? Is image 1 the strongest? Does the order have a reason?
9. **Cover check.** Shrink image 1 to feed-thumbnail size. Does it still pass the one-second test?
10. **Music, caption and release** (below).
11. **Log** in the scene folder (below).

## Music

- **Use a mood reference, not a source.** For example, Spotify's "liminal" playlist describes the mood. Never upload tracks from Spotify or other services: copyrighted audio uploaded from outside the platform risks muting or removal.
- **Pick from each platform's in-app music library.** Douyin and 小红书 each license their own libraries for use inside the app. Choose separately on each platform. Licensing terms were not verified for this skill. Check the current rules.
- **Original music is the long-term signature.** When the studio has its own tracks, reuse one motif across a series so a viewer recognises the account by ear.
- **Record the exact track title and artist** for every post.

## Caption and post copy

- **Title:** short, in Chinese. Lead with recognition or the question ("如果上海下了一场真正的大雪"), not with "AI".
- **Caption:** one or two lines. End with a question the viewer answers from their own life ("你的城市应该下多大的雪？").
- **Hashtags:** 3–5. Include the place names and the series name.
- **AI label:** always on. Mandatory since 2025-09-01.
- **No real trademarks, logos or people's faces.** See [10](../nocturnal-dream/references/10-audience-and-popularity.md).

## Release and cross-posting

- **Post the same set to Douyin and 小红书 on the same day.** Re-pick the music on 小红书. Adjust the caption to each platform's tone if needed.
- **Pair image sets with videos.** A working mix is 1 video and 2 image sets a week. An image set can also preview or extend a video scene (stills from its world).

## Records

Keep each set in its own folder under `Scenes/`, named for the set:

```
Scenes/<Set-Name>/
  PRODUCTION.md     brief, structure, order, approval, music, caption, status
  References/       real-place photos with their roles
  Prompts/          world block, look block, and each position's prompt, versioned
  Renders/          every candidate, including rejects, numbered by position
  REVIEW.md         selection notes, repairs, release data and learnings
```

Record the model, size, aspect ratio, job id and echoed prompt for every generation, and whether it used credits or an unlimited allowance.

## Measure and learn

Fill the learning log in [10](../nocturnal-dream/references/10-audience-and-popularity.md) for each set, and add three image-set fields:
- **Swipe-through.** The share of viewers who reached the last image, if the creator data shows it.
- **Saves per 1,000 views.** Image sets are expected to earn saves more than video. That is a hypothesis.
- **Which image the comments mention.** That tells you which place or condition to repeat.

Compare image sets with videos on saves, comments and follows per 1,000 views. Do not change these rules from one post. Wait until at least 4 sets have been released.
