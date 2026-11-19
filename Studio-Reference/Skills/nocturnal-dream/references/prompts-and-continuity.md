# Prompt、连续性与资产命名

## 07｜模型无关的 Prompt 体系（核心资产）

### 7.1 分层 Prompt 结构

**A. Identity Lock（人物身份）**：当用户提供获授权角色照片时，描述持续不变的脸部特征、发型、年龄感、身体比例；优先使用模型支持的 reference image / character reference / first-frame 机制。不根据照片猜测敏感身份。

**B. World / Reality Anchor（世界锚点）**：地点、时间、天气、材质、可信物理。

**C. Scene / Discovery（观看什么）**：Scene 说明核心现象、观察路径、运动或环境变化；Sequence 说明场景衔接；只有 Narrative Film 必须写角色目标、动作、情绪转折。

**D. Art Direction（视觉预设）**：Style Preset + 配色关系 + 服装 + 环境细节。

**E. Lighting（光位）**：Motivated key + ambient fill + shadow readability + reflection logic。

**F. Camera（摄影）**：景别、视角、镜头运动、焦点主体。

**G. World / Surreal Rule（世界规则）**：声明尺度、功能、交通、机械或文化逻辑；若有超现实事件，再解释它如何作用于现有物理环境。

**H. Constraints（失效约束）**：连贯性和常见 AI 瑕疵预防，不依赖长串无关 negative keywords。

### 7.2 Master Prompt — Scene-first（当前默认）

```text
[PROJECT] NOCTURNAL DREAM / [WORLD_ID] / [SCENE_ID]
FORMAT: Independent Visual Scene (not a story trailer); [duration], [aspect ratio].

CONCEPT THESIS:
[One alteration to reality. Name a specific cultural anchor that resonates with the intended Douyin audience and the emotional shift the shot is designed to evoke.]

REALITY ANCHOR & SCALE:
[Location, recognizable everyday details, functional architecture, small human/vehicle references for scale, wear and maintenance traces.]

WORLD DESIGN:
[Materials and era, technologies and their function, topology, foreground/midground/background hierarchy. If impossible, define its physical boundary and environmental consequences.]

VISUAL DISCOVERY:
[Where camera begins; what becomes visible as time passes; what must remain stable. This may be pure observation with NO twist.]

ART DIRECTION & LIGHT:
[Dominant Nocturnal Dream style preset, restrained palette, motivated key light and shadow structure; material response.]

CAMERA & MOTION:
[Composition, perspective, one justified movement or locked-off shot, depth and physically plausible motion.]

SOUND / SCALE:
[Environmental sounds, distance, mechanical low end, reverb, temporal dynamics; no forced voiceover or moral line.]

CONTINUITY / AVOID:
[Architecture, proportions, scale, fixed landmarks, consistent mechanics, natural material response; avoid arbitrary morphing, fake HDR, CGI gloss, unmotivated neon.]
```

**Story / Film 才额外要求：** character objective / established world rules / causal chain / choice / consequence / ending. 不把这些栏目强制套用到单场景。

**特别注意：** 输入视频模型的最终 Prompt 应按模型特性简化。Scene 的概念和世界复杂度来自构思与参考图设计，而不是每次贴 800 字形容词。

### 7.3 三套风格预设英文片段

**MIDNIGHT WITNESS**

```text
Restrained urban noir, deep but readable charcoal shadows. A warm practical streetlight shapes one side of the subject; cool night ambience gently separates the silhouette. Wet stone and glass reflect light without neon overload. Deliberate negative space, quiet tension, tactile realism. Slow lateral tracking or a composed locked-off frame.
```

**VELVET AFTERIMAGE**

```text
Poetic dreamlike realism grounded in a believable interior or street. Soft window light, translucent curtain or rain-streaked glass, restrained highlight halation, subtle atmospheric haze. Natural skin tones, muted teal and warm amber relationship, intimate gestures, gentle breathing room. A single uncanny detail emerges as if recalled from memory.
```

**EDITORIAL RUPTURE**

```text
High-end surreal editorial filmmaking inside a credible minimalist architectural space. Graphically controlled framing, sculptural directional light, deep shadows with precise highlights, limited charcoal-silver-burgundy palette. The camera remains calm while exactly one impossible physical event transforms the scene. Elegant visual tension, convincing materials and contact shadows.
```

### 7.4 人脸一致性：操作优先级

1. 使用得到肖像授权的清晰人像参考，确保是同一人、相近光照、尽量无强滤镜。
2. 尽量先制作 **hero reference frame**（稳定脸 + 发型 + 服装 + 环境），再做 image-to-video；多镜头复用该参考。
3. 全片保持一致的身份描述，减少每镜重新定义脸；优先中景、侧脸、背影与特写交替，避开连续大幅头部旋转。
4. 单次生成短镜头，控制动作复杂度；优先轻动作而非打斗、多次遮挡或极端镜头变形。
5. 对关键帧与关键脸进行人工对比；有 morph、眼距跳变或脸型漂移则重生该镜头。
6. 不在未获许可时模拟真实人物的误导性行为；必要时标明 AI 合成。

### 7.5 生成循环

**World Concept → Reference Research → World Sheet → Keyframe / Layout Test → Single Scene → Visual QC → Sound Design → Publish / Archive → Learn**。人物不是每条必选；**长时间镜头与多场景组合**按概念需要单独设计。先以低成本草稿筛创意，再用高规格生成关键镜头；具体 credits、模型和分辨率遵循实际套餐。

## 09｜Prompt / 镜头 / 选题的统一命名约定

```text
ND-[SERIES]-[EP##]-[SHOT##]-[VARIANT]-v##
例：ND-MW-01-S02-A-v03
```

**资产目录建议**：

```text
nocturnal-dream/
  00_Bible/Creative_Bible_v1.1.md
  01_References/reference-library.csv
  02_Ideas/idea-bank.csv
  03_Scenes/ND-SC-001/
    concept-world-sheet.md
    scene-plan.csv
    prompts/
    references/     # 仅保存有合法使用权的参考素材
    renders/raw/
    renders/selects/
    edit/
    publish/
  04_Sequences/ND-SQ-001/
    world-continuity.md
    scene-order.md
  05_Films/ND-FLM-001/
    treatment.md
    screenplay.md
    shotlist.csv
  06_Analytics/experiment-log.csv
  07_Templates/scene-master-prompt.txt
  CHANGELOG.md
```

**版本原则**：`v1.0` 确立不变量；`v1.1` 调整镜头标准或 Prompt；`v2.0` 改变账号定位才升级主版本。失败案例也保留，写清失败原因与改进动作。

### 7.6 从研究稿 Urban Nocturne 到可拍的两份指令

示范把「雨夜人物侧向跟拍」迁移至末班轮渡。当地锚点为上海轮渡的人车登船坡道与隔江可辨的岸线；设定为退潮翻出过去的等候线。先核对候船空间与所选码头参考是否一致。以下是待试文本，所选界面支持的参考图、首帧和音轨控制应在提交前确认。

**首帧指令（静态空间）。** Vertical frame from the Shanghai ferry landing, at the eye height of a waiting passenger. The hinged ramp cuts across the foreground. Behind it, a second, worn boarding line is just visible under a shallow sheet of river water. The opposite bank sits above the ramp rail. A single warm lamp grazes the chipped paint from the left. Wet patches catch narrow streaks of light, dry concrete stays matte.

**运动指令（从已选首帧出发）。** Hold the camera at the landing. Water drains down the slope in one continuous sheet, uncovering the faded line from left to right. Leave a dark wet edge behind it. The rail, ramp hinge, painted markings and opposite bank keep their positions. Hold long enough to distinguish both lines.

**若以人物为中心。** 保留同一坡道、光源和旧线，让等船人的鞋尖停在新线以内，焦点从鞋尖延伸到露出的旧线。若拍脸，用获准的角色参考并另查身份连续性。空景版让栏杆与坡道承担尺度。

**定位返修。** 首帧已经分不清两条线，先改俯视角或旧漆明度。首帧合格而中段线条游走，保留参考图，先缩减水流遮挡。若画面成立而退潮显得太快，先试延长露线后的停留。另给声音轨写近处水流沿斜坡退下、远处江面船机持续，不在画面生成指令中堆混音要求。
