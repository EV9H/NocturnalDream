# Market analysis prompt (paste into a deep-research session)

Copy everything inside the code block. Works best in a research-capable model with web search. Ask it to search in Chinese as well as English.

```text
You are a senior short-video market analyst focused on Douyin (China's TikTok). Produce an evidence-based market analysis to decide the content strategy for a new solo-creator account. Search the web in both Chinese and English. Prefer primary data and dated sources. Today is late November 2026; treat anything older than 12 months as possibly stale and say so.

## 1. Context
- Account concept: "Nocturnal Dream". Cinematic, photoreal short films (9:16, 10-15 seconds) of "Altered Reality": a place or shared experience Chinese viewers know (old school corridors, humid-season walls, school broadcasts, neighbourhood compounds, ancient-Chinese machines scaled to city size), changed by one rule, designed to produce one feeling (nostalgia, awe, tenderness, quiet loss). Mostly no people, no dialogue, original sound design.
- Production today: AI image-to-video (Seedance 2.5 via Higgsfield or Jimeng, 480p tests, 720p-1080p finals), roughly US$8-20 per finished piece, 1-3 pieces per month at current budget.
- Alternatives under consideration:
  A. Cinematic AI-generated scenes (current path).
  B. Claude-coded HTML/CSS or Remotion animations (explainers, diagrams, kinetic type, "lore" animations for the fictional world).
  C. Hybrid 3D: Blender blockouts (geometry, camera, light timing) turned photoreal by AI video.
  D. A mixed slate of A + B (+ C later).
- Owner constraints: solo creator, based in Shanghai, limited generation credits and limited AI-assistant token budget, Chinese-language audience, no on-camera personality, wants an account that can grow a recognisable brand, not one-off virality.
- Prior (unverified) hypotheses to test, not to confirm: (1) the pure "dreamcore/liminal" aesthetic is niche, but shared-memory nostalgia (school, childhood, hometown) is mainstream; (2) the biggest Douyin AI hits are human-emotion, national-style (guofeng), sci-fi or story pieces; (3) a quiet, muted, no-people piece reaches a smaller audience than a colourful or story-driven one; (4) a first-second hook and a comment-provoking caption matter more than resolution.

## 2. Research questions
Answer each with data where it exists. If data does not exist, say "no reliable data found" and give your best-reasoned estimate labelled as an estimate.

1. Market size and demand
   - Which content categories on Douyin are growing in 2026 (AI-generated and not)? Give view/like/share ranges for typical, strong and viral posts in each category.
   - Size and engagement of these niches: dreamcore / 梦核 / 中式梦核 / liminal spaces (阈限空间), nostalgia and school-memory (怀旧, 校园, 童年), guofeng and ancient-China engineering (国风, 古代科技, 巨构, 蒸汽朋克), cinematic AI shorts, AI explainers / science animation (科普动画), code-made motion graphics.
2. Audience
   - Who watches each niche (age bands, gender split, city tier, interests)? Which audiences share and comment, and which only watch?
   - Which emotions and triggers drive shares and comments in these niches (cite examples)?
3. Platform mechanics (verify, do not assume)
   - Current Douyin rules for AI-generated content: mandatory labelling, restrictions, distribution treatment, music and sound licensing, likeness and copyright.
   - What signals the recommendation system appears to weight (early drop-off, completion, replays, comments, shares, follows). Separate official statements from creator folklore.
   - Best-supported guidance on length, hook timing, resolution (is 720p enough on phones?), caption style, posting cadence and time of day.
4. Competitors and comparables
   - 10-15 real accounts or series in the closest niches (cinematic AI shorts, dreamcore/nostalgia, guofeng AI, AI lore/explainer animation). For each: follower range, typical engagement, cadence, format, visible production method, how they grew, and what they monetise.
   - Which of them are the right benchmark for a solo creator with a small budget?
5. Production method comparison (A vs B vs C vs D)
   - Realistic cost per piece (credits, tokens, time), quality ceiling, repeatability, brand fit, and expected audience response.
   - Are code-made HTML animations crowded or still under-supplied on Douyin? What looks templated and what stands out?
6. Monetisation and growth
   - Realistic paths for a small AI-film account (巨量星图 / 商单, creator incentive programmes, 小店, courses, commissions, IP licensing). Give thresholds (followers, views) and typical earnings where available.
   - Typical timeline from zero to a first 10k / 100k followers for comparable accounts. Cross-posting value (小红书, B站, 视频号, TikTok international).
7. Risks
   - Platform, legal, reputational (AI fatigue, "AI slop" backlash), dependency on one model vendor, price changes, burnout/cadence.

## 3. Method requirements
- Use sources such as 新榜, 蝉妈妈, 飞瓜, 巨量算数, 抖音指数, 巨量星图, 抖音创作者中心, 36氪, 虎嗅, 数英, QuestMobile, plus direct inspection of public Douyin accounts and videos. Give each source's date and URL.
- Do not invent statistics. Distinguish: (a) measured data, (b) vendor or creator claims, (c) your inference. Mark each claim with one of these labels.
- Note sample sizes, survivorship bias and when a source is marketing.
- If sources conflict, show both and say which you trust more and why.

## 4. Output format
1. Executive summary (max 200 words) with a clear recommendation.
2. Market map: a table of niches with size, growth, competition, audience, and fit with this account (score 1-5 each, with one-line reasons).
3. Comparable accounts table (account, niche, followers range, cadence, format, production method, growth pattern, monetisation, link).
4. Decision matrix for options A, B, C, D scored on: reach potential, brand fit, cost per piece, repeatability, time to first traction, risk. Show the weighted total and the weights.
5. A recommended 90-day plan: how many posts, which formats, which lengths, which hooks, what to measure, and the kill/continue criteria for each experiment. Include the first 10 post ideas matching the account concept (school memory, humid-season wall, ancient-China machine, etc.) and the hypothesis each tests.
6. A list of the most important unknowns and the cheapest test for each.
7. Sources list with dates and a confidence rating (high / medium / low) for the main conclusions.

Be direct, quantitative where possible, and say plainly when the evidence is weak.
```
