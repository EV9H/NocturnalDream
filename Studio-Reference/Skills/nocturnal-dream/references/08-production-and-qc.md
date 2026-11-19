# 08 · Production and QC

How a scene moves from approved idea to released film, and how to judge each step honestly.

## Stages and gates

| Stage | Product | Gate |
| --- | --- | --- |
| Concept | Pitch of three, then one-page treatment | User approves the written direction |
| References | Reference pack with roles, layout test | Geometry and landmarks verified |
| Keyframe | Batch of candidates, selected and repaired hero frame | Keyframe QC passes (see [05](05-keyframes.md)) |
| Motion test | Batch of 3–4 takes inside a cap | User approves spend (model, outputs, cost or cap) before submitting |
| Select | One take chosen, notes on repair | Score ≥ ship threshold or a defined repair test |
| Final | Final-resolution generation, edit, sound, grade | Another spend approval if it exceeds earlier scope |
| Release | Export, phone review, notes | Publication decision tracked separately |

Approval of a concept does not approve spend. A request to "try it" does not approve spend.

## Scene folder

```
Scenes/<Scene-Name>/
  PRODUCTION.md     brief, treatment, look, decisions, status
  References/       files with their roles in the filename or notes
  Prompts/          each prompt as submitted, versioned (v01, v02...)
  Renders/          every take, including failures, numbered
  REVIEW.md         dated reviews, scores, next test
```

Fill the project's production checklist and the Scene First Workbook when used. Keep failed takes.

## What to record per generation

- Model and the settings requested.
- Prompt as submitted, references and the job of each.
- Number of outputs, quoted cost, charged cost.
- Job ids, files, dates.
- What the tool echoed back, and any difference.
- Unverified items stated as unverified.

## Score card

Score each 0 (fail), 1 (partial), 2 (strong). A frame, a take and a film each use the same card.

1. **One image.** A memorable, describable single image.
2. **Anchor.** Recognizable within two seconds, tied to the audience.
3. **Alteration.** A system with visible evidence and consequence.
4. **Composition.** Focal point, depth in three planes, off-center control, readable at thumbnail.
5. **Light and color.** Motivated, textured shadow, controlled palette with an accent.
6. **Materials and contact.** Weight, wear, reflection, shadow agree. Small things keep identity.
7. **Motion physics.** Camera move motivated, layers differ in rate, no sliding, no warping.
8. **Prompt fidelity.** The take does what the shot brief says, with no extra cuts or zooms.
9. **Sound.** Position, layers, timing, one hero sound.
10. **Emotional landing.** The held moment delivers the intended feeling without text.

**Ship at 16 or more of 20, with no zero in 2, 3, 6 or 7.** Otherwise repair or reshoot. Scores 12–15: choose one repair test. Below 12: return to concept or keyframe.

## Review protocol

Review in this order, separately for picture and sound:

1. **Mute, phone size, whole take.** Does the idea read? What did the eye land on first?
2. **Sound on.** What did sound add?
3. **Frame samples.** First, middle, last, and every contact or reveal. Compare spacing of fixed landmarks.
4. **Frame by frame at the risk points.** Contacts, occlusions, edge warps, flicker.
5. **Verdict.** Score, then the single most valuable repair.

Write findings as **Observed** (seen in frames, with timecodes), **Unverified** (settings, hidden causes), and **Judgment** (creative opinion). Do not present an inference about the cause of a failure as fact.

## After each product: the learning log

- **Repeat.** What worked and should be kept.
- **Fix.** What failed and the likely cause, as a hypothesis.
- **Next test.** One controlled change.
- **Shared rule.** Only promote a rule into these chapters if take evidence supports it. Log the scene and version that supports it. Mark everything else a proposal.

## Audience and slate

- Plan a slate that rotates anchors, looks and alteration families. Avoid back-to-back scenes with the same look or mechanism.
- STEPPS claims are hypotheses. Test with a small panel before posting: ask what they recognized, what they discovered, where they felt something, and what they would tell a friend. Record verbatim answers and compare with intent.
- Early publishing metrics (completion, replays, shares, saves) are observations, not proof. Track per scene and per look before drawing conclusions.
- Scenes become a sequence only when they share world rules and motifs and add up to more than a pile. Narrative film needs its own treatment and script: character want, cause, choice, consequence.
