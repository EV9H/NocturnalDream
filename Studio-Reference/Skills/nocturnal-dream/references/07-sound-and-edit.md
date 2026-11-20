# 07 · Sound and edit

Sound and the cut turn a convincing take into a film.

## Sound design

Decide the **listener position** first: where in the space is the ear. Then build layers.

1. **Room tone / bed.** The place's constant (wind, city hum, fluorescent buzz, river wash). Never silent.
2. **Mid events.** Things in the space that happen (a distant ship horn, a train, a shutter).
3. **Close foley.** Contact sounds timed to picture (boot compress, glove brush, cup rattle). They sell weight.
4. **Hero sound.** The one sound the viewer will remember: it should come from the alteration or the memory trigger.
5. **Silence and drop.** Plan where sound falls away so the eye can take over.

**One arc for picture and sound.** Picture and sound must tell the same emotional story. On School That Never Lets Out draft v02, the sound decayed like a burning memory while the picture stayed a clean, triumphant light event. The owner liked the sound but felt the whole lacked depth. If the sound fades, the picture must also visibly wear away, and the reverse.

Perspective rule: near sounds dry and detailed, far sounds low and diffuse, with air in between. The alteration should be audible when it can.

**Music.** Use it only when it adds something the place cannot. Prefer the place's own music (a broadcast, a radio, a bell). Original score cues should be sparse and tied to a physical event. No sentimental swell to tell the viewer how to feel.

Chinese cultural sound anchors are strong: 课间操广播, 公交报站, 小区喇叭, 卖货录音, 戏曲, 铁轨节奏, 麻将声. Preserve each one's position, timbre and entry time.

Generated audio is a draft: the model's audio is often mono and can clip at the tail. Rebuild or layer important sound in an editor or DAW, then mix for phone speakers and earbuds.

## Edit

- **Open on the image.** The first second must be a strong, specific frame, not a title or fade. A viewer decides in about a second.
- **Order of understanding.** Anchor first (what place), alteration second (what is different), feeling last (what it means).
- **Trim dead start.** Cut empty lead-in. A step that reaches the rail sooner is better than a slow approach, but keep one visible contact so the viewer feels the weight.
- **Hold the end.** Leave two to three seconds after the final reveal for the feeling. Do not add a punchline or a caption.
- **Cut for a reason.** On motion, on sound, or on a changed idea. Do not cut for variety.
- **Rhythm.** Long shot, then shorter, then a pause, then the payoff. The pause before the payoff matters most.
- **Loopability.** On Douyin, a clean loop can lift replays: consider an ending that rhymes with the opening frame. Treat this as a test, not a rule.
- **Rescue an unwanted cut.** If a take cuts on its own, judge whether the cut can read as a deliberate reveal, then trim the dead time on both sides of it. Treat this as an edit option before rerolling.
- **Speed.** Real time by default. Ramp once, deliberately.
- **Captions.** None unless the idea needs a place or date, and then in a short, clean title.

## Grade and finish

- Make the look consistent across shots with a gentle, controlled grade: protect skin, hold the dominant color, and keep shadows textured.
- Add fine grain over the whole image to unify AI-generated and composited parts. Keep it subtle.
- Check for AI tells in the final: banding in gradients, shimmer in textures, edge swim. Fix or crop.
- Upscale only from a selected final take. Check faces and text after upscaling.

## Export

- Measure loudness and peaks per channel with a real meter (for example ffmpeg `astats` or `ebur128`), not a mono sum, before deciding a take clips.
- 1080×1920, 9:16, H.264, AAC audio, 24 or 30 fps matching source. Verify against the platform's current spec.
- Review on a phone with sound off, then on with sound. Record what was readable at each step and what was lost.
