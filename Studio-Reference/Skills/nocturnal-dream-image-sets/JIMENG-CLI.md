# Jimeng CLI Playbook (`dreamina-canvas`)

The CLI handles everything except the free **0积分畅用** switch.
- **Canvas:** always pass `--project-id` explicitly for the target canvas (Image-Set Lab: `93c6f2e6-545a-4d1f-a1b0-25c9cf1a224e`), because the CLI's "current" project may point elsewhere.
- **Checked** on 2026-11-25 against the official `dreamina-canvas-cli` skill (load it before generating). The installed binary's `schema` is the authority for every command, flag and field.

## Before a round

- **Once per session:**
  - `briefing` gives environment guidance and promotions. Mention a relevant promotion once; never invent one.
  - `auth status` shows the token's expiry.
  - `auth account` shows the balance and VIP level.
- **Send the owner the canvas link** as soon as the canvas is settled: <https://jimeng.jianying.com/ai-tool/ai-canvas/93c6f2e6-545a-4d1f-a1b0-25c9cf1a224e>.
- **Don't use `canvas use` to switch canvases.** The "current canvas" setting is shared by every session on this machine, so switching it would redirect a parallel session. Pass `--project-id` instead.
- **Read `schema '<command>'` before using a flag you haven't used.** Guessing caused the `unrecognized option` errors on 2026-11-25.

## Standard Paid Loop

1. **Write the prompt file first** in `Prompts/` (e.g., `LA12-…-v01.txt`). The file is the source of truth.
2. **Create nodes without running:**
   ```bash
   dreamina-canvas node create image \
     --project-id 93c6f2e6-545a-4d1f-a1b0-25c9cf1a224e \
     --title "LA12-…" --mode t2i --model seedream_5.5 \
     --ratio 9:16 --resolution 2K --count 1 \
     --prompt "$(cat Prompts/LA12-…-v01.txt)"
   ```
3. **Check balance before:** `dreamina-canvas auth account` (optional but helpful for `REVIEW.md`).
4. **Quote the batch:** `dreamina-canvas node quote --project-id <pid> --node-id A --node-id B …` → read `totalMaxCredits`.
5. **Confirm ceiling:** `dreamina-canvas node confirm --project-id <pid> --credit-ceiling <quote> --node-id A --node-id B …` → returns a short-lived `creditConfirmationToken` (~10 min).
6. **Run with explicit submit IDs:** pass `--submit-id <uuid>` per `--node-id` in matching order, plus `--credit-token <token>`. Keep the submit IDs so any retry reuses them idempotently.
7. **Wait:** `dreamina-canvas operation wait <submitId> --project-id <pid> --timeout 10m --interval 5s` (verified; the operation ref is the submit ID), or poll `node show` until `data.nodes[0].node.status` is `success` (~20–60 s).
8. **Download:** `dreamina-canvas resource download <resourceId> --project-id <pid> -o Renders/<name>-Seedream-paid-v01.png` (lowercase UUID).
9. **Verify charge & balance:** read `resources[0].creditsAmount` from `node show` and check `auth account` after; log both in `REVIEW.md`. Also keep each response's top-level `meta.requestId`, which is what Jimeng support needs if a charge looks wrong.
10. **Measure & review:** run `python3 scripts/measure_look.py <render> --lane <A-D>`, build a contact sheet next to the reference, and log observations, judgement, and IDs in `REVIEW.md`.

**Job state** belongs in the scene's `REVIEW.md`, not a scratch file: take, node ID, submit ID, resource ID and request ID. Never save the credit token.

## One-step single frame

For a single frame, `node create image` can save, quote, approve within a ceiling, run and wait in one call. Its flags are verified in `schema`, but this studio has not used it yet:

```bash
dreamina-canvas node create image --project-id <pid> --title "…" --mode t2i --model seedream_5.5 \
  --ratio 9:16 --resolution 2K --count 1 --prompt "$(cat Prompts/….txt)" \
  --run --credit-ceiling 6 --wait --timeout 10m
```

It stops before running if the quote exceeds `--credit-ceiling`. For batches, keep the quote-first loop above so the owner sees the total.

## Consistency across a set

- **Reference the cover frame.** To keep a set's frames matching (same tiles, lane lines, light), reference the cover's node with image-to-image: `--mode i2i --ref node:<cover-node-id>`. Use `{{node:<id>}}` in the prompt to say where it applies. Prefer the node ID (it keeps the canvas link) over a resource ID.
- **Keep edit prompts short.** Per the owner's earlier lesson, a short "编辑…只改X" prompt holds identity better than re-describing the whole image.
- **Check the result.** A reference helps but does not guarantee consistency.

## Retries and stop points

- **Exit codes:**
  - `2`: invalid input; nothing ran. Fix the command and retry with the **same** submit IDs.
  - `1`: does **not** prove nothing ran. Check with `operation status <submitId>` before writing again.
  - `20`: does not prove it was accepted.
- **Never resolve uncertainty with new submit IDs.** Retries after a timeout or a lost response reuse the original IDs.
- **Stop and ask the owner** when:
  - a spend needs approval, or a new quote is above the approved ceiling;
  - finished options need a subjective pick;
  - a result is uncertain and retrying could charge twice.

## Post-editing

The CLI can upscale finished images (`node upscale`), cut them out and interpolate video frames. Read the official skill's post-edit guide first. Upscaling may beat regenerating when a post only needs more resolution.

## Seedream 5.5 Sizing & Flags

Never guess flags — verify with `dreamina-canvas model find seedream 5.5 --type image` (supports `1:1`, `3:4`, `4:3`, `9:16`, `16:9`, `2:3`, `3:2`, `21:9`; `1.5K` or `2K`; count `1–8`).

| Ratio | Resolution | Output size | Credits | Notes |
| --- | --- | --- | --- | --- |
| `3:4` | `2K` | 1728 × 2304 | 6 | Lane C / 小红书 |
| `9:16` | `2K` | 1440 × 2560 | 6 | Lane A / Douyin full-screen |
| `21:9` | `2K` | 3024 × 1296 | 6 | Lane B |
| `21:9` | `1.5K` | 2268 × 972 | 4 | Lane D (cheaper, softer 胶片 look) |

Always set the ratio **twice**: in `--ratio` and in the prompt's opening words (`Vertical 9:16 photograph…`, `Widescreen 21:9…`).

## Canvas Layout & Owner Picks

- **Smart layout (default):** omit `--x`/`--y` to let the CLI place nodes without overlap.
- **Manual rows:** pass `--x`/`--y` to keep a clean row. Node sizes on the canvas (verified):
  - a `3:4` node is `320 × 427`: space nodes about 360 apart;
  - a `9:16` node is `320 × 569`;
  - a `21:9` node is `747 × 320`: space them about 790 apart.

  Create and position nodes with the CLI, and use the browser only for clicking free generate.
- **Reading owner picks:** `node show` returns `tags`, which carry the owner's colour-tag picks from the canvas.

## Free Web-Canvas Route

- The CLI has no `0积分畅用` option. To run free: create the node via CLI, open the canvas in the browser pane, and verify three things before clicking generate: (1) `0积分畅用` is on, (2) price reads `0/张`, (3) prompt, ratio, and `1张` match.
- Only one free job runs at a time (the switch disappears while one is active).
- If the large canvas (~300 nodes) hangs on "Loading canvas" past 1 minute, switch to paid within the approved credit ceiling.

## Gotchas

- **zsh variable splitting:** zsh does not split unquoted variables into words, so putting multiple flags in one shell variable fails with `unrecognized option`. Write flags out directly.
- **Confirm vs. Run flags:** `--credit-ceiling` belongs on `node confirm`; `--credit-token` belongs on `node run`.
- **A quote of 0:** the official skill says a quote of 0 means *that* run is free (a promotion); it says nothing about later runs.
  - LB04 quoted 0, and its resource then showed `creditsAmount` 6. Whether 6 was actually deducted is **unverified**: `creditsAmount` may show the list price, the CLI has no credit ledger, and a parallel session was spending at the same time.
  - Log both the quote and `creditsAmount`. When it matters, check 积分明细 in the Jimeng app.
- **Parallel sessions:** canvas, balance, and ID namespaces are shared across parallel sessions. Check existing filenames/IDs first and use a distinct ID range or descriptive filename to avoid collisions, and note parallel spend when reconciling balance deltas.
- **Edit stale quote:** when using `node edit`, pass `--prompt` again or the edit fails and the quote stays stale.
