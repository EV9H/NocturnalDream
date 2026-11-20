# Subscriptions and credits

Track paid plans for generation tools here. Record per-job costs in each scene's folder.

| Tool | Plan | Bought | Paid | Credits | Ends / renews | Auto-renew | Notes |
|---|---|---|---|---|---|---|---|
| 即梦 (Jimeng) | 高级会员 12.3K, 连续包季 (CLI reports `vipLevel: maestro`) | 2026-11-19 | ~¥1,227 (owner said ≈¥1,200; confirm the exact amount) | 12,320 a month. Each month's credits expire after about 30 days: the first batch expires 2026-12-19 | Membership ends 2027-02-19. List renewal price ¥2,798 per quarter | Owner to turn off; not yet confirmed | Calendar reminder on 2027-02-12. CLI `dreamina-canvas` 1.4.0 installed and logged in on 2026-11-19 |
| Higgsfield | Plus | before 2026-11-18 | not recorded | 186.96 left on 2026-11-19 | not recorded | not recorded | Live Seedance 2.5 quotes on 2026-11-19 (10 s, 9:16): 480p 30, 720p 70, 1080p 160 credits |

## Notes

- **Free Seedance 2.5 generations.** On 2026-11-19 Jimeng showed "free for four times" for Seedance 2.5. Takes 08 and 09 used two (each quoted 0 credits; the balance stayed at 12,420). Two should remain. Check the quote before each run, because a quote of 0 means only that one run is free, not that more remain.

- **Seedream 5.5 is not free (2026-11-19).** One 16:9 2K t2i image quoted 6 credits and was charged 6 (12,420 → 12,414), taken from the batch expiring that day. The owner had expected up to three free images. Treat a quote above 0 as a real charge. The web app has a **0积分畅用** switch on the image input (Seedream 5.5, 16:9, 2K, 3 images shown at 0/张 against 9/张; the switch's own tooltip says turning it off uses credits for faster generation). CLI 1.4.0 has no flag for it, so free stills must be started in the web canvas with the switch on.

- **Image-set canvas (2026-11-20).** A shared Jimeng canvas for image-set (图文) stills only: [Nocturnal Dream Image Sets](https://jimeng.jianying.com/ai-tool/ai-canvas/93c6f2e6-545a-4d1f-a1b0-25c9cf1a224e) (project `93c6f2e6-545a-4d1f-a1b0-25c9cf1a224e`). It was set as the CLI's current canvas. Film scenes keep their own canvases.

- **Image-test credit cap (approved 2026-11-20).** The owner approved up to **300 credits** this month for image-set style tests. The conditions:
  - Free (web canvas, 0积分畅用) comes first.
  - Spend credits only when the free queue is stalled.
  - One image per run, with no batches until a direction is found.
  - Use cheap models only, and quote before every run. Live quotes from 2026-11-20 at 3:4, one image:
    - 图片模型 Image 2.5 Pro (`jm_image_model_lib_s`): 3 credits at 1K, 4 at 2K, 5 at 4K. **The owner rejected it on 2026-11-20 as "AI slop". Use Seedream 5.5 only.**
    - Seedream 5.5: 6 at 2K.
    - 图片模型 Image 2 (`jm_image_model_oa_it`): 77 at high 2K. One run was made before the owner said "don't use expensive"; don't use it again.
    - 图片美学模型 V8.2: always makes 4 images.
  - Running total of spending: [Scenes/Image-Set-Lab/REVIEW.md](../Scenes/Image-Set-Lab/REVIEW.md).

- **Jimeng credits don't roll over.** Unused monthly credits are lost, so plan each month's work to use the 12,320.
- **Models available through the Jimeng CLI on 2026-11-19:**
  - Seedance 2.5, from 480p to 4K, 4–30 s
  - Seedance 2.5 draft (样片模式), 480p only
  - Seedance 2.5 Flash, 480p and 720p
  - Seedance 2.0 VIP and Fast VIP
  - Vidu, Wan, HappyHorse
  - Image models: Seedream 4.x–5.5, Image 2.5 Pro and Flash, N-Pro and others
