# Workplace Boundary

职场压力模式识别与证据化边界防御的 agent skills。

一句话：反职场 PUA，不靠情绪对抗，靠证据、记录、边界和闭环。

## 这个项目是什么

`workplace-boundary` 是一组公开的防御性 agent skills，用来帮助人在复杂职场环境中识别压力模式，并生成专业、克制、可执行的防御动作。

它关注的不是“某类人怎么样”，而是：

- 谁在什么工作场景里说了什么、写了什么、改了什么记录；
- 哪个会议、邮件、文档、ticket、review packet 或决策记录会变成事实来源；
- 贡献、责任、风险、owner、deadline、approval 是否被模糊或转移；
- 如何用最小必要升级、准确证据和清晰边界保护自己。

## 公开包含的 skills

### `workplace-pressure-patterns`

识别可观察的职场压力模式和风险路径，例如：

- 抢功和可见度捕获；
- 甩锅和责任漂移；
- owner 不清、deadline 不清、decision 不清；
- 会议纪要、deck、status update 或 review packet 变成错误事实来源；
- side-channel 决策、预先定调、信息隔离；
- 让别人长期承担临时协助、救火或隐形工作的压力。

这个 skill 的输出重点是行为诊断、证据强度、风险路径和防御交接。

### `workplace-boundary-defense`

把诊断转成专业、可发送、可落地的防御文本，例如：

- 会后确认邮件；
- 会议纪要修正；
- contribution map；
- owner / deadline / approval 确认；
- status update；
- escalation note；
- review packet 或 promotion packet 的证据补充；
- source-of-truth record 修正。

它强调低冲突、高证据、清晰责任，不生成攻击、羞辱、操控或报复话术。

## 关于 agent 对抗模拟

这个项目在开发过程中使用了内部 agent 对抗模拟来构造真实职场压力场景：一边模拟更强的压力、甩锅、抢功、记录污染和责任转移路径，另一边不断强化识别与防御能力。

公开仓库只发布防御侧能力。

内部 Red Team 组件、提示词、脚本、运行轨迹、评分记录和任何可能被复用为攻击手册的材料，都没有上传到这个公开仓库。

## 为什么不公开 Red Team

因为这个项目的目标是帮助人保护自己，而不是教人压制同事。

公开材料只保留：

- 行为模式识别；
- 证据纪律；
- 边界防御；
- 责任和 owner 澄清；
- 记录修正；
- 最小必要升级；
- 身份去偏见和反歧视规则。

不公开：

- 如何诱导别人背锅；
- 如何抢功更隐蔽；
- 如何操控会议或记录；
- 如何绕开证据；
- 可直接复制发送的攻击话术。

## 安装

```bash
cp -R skills/workplace-pressure-patterns ~/.agents/skills/
cp -R skills/workplace-boundary-defense ~/.agents/skills/
```

建议两个 skill 一起安装：一个负责识别压力路径，一个负责生成证据化防御。

## 使用边界

可以用来：

- 分析具体会议、邮件、聊天记录、status update 或 review 文本；
- 把情绪化吐槽转成行为和证据问题；
- 生成克制、专业、可发送的澄清或修正文本；
- 保护贡献、owner、deadline、approval、风险和 source-of-truth record。

不可以用来：

- 歧视、骚扰、报复或身份攻击；
- 根据民族、国籍、种族、性别、宗教、口音、移民身份等推断行为；
- 编造证据、夸大贡献、伪造 approval；
- 生成操控、排挤、甩锅、抢功或压制他人的话术。

## 验证

```bash
python3 scripts/validate_repo.py
```

## 核心原则

分析行为，不分析身份。

职场边界不是情绪宣泄，而是一套可验证的记录系统：事实、证据、owner、deadline、decision、risk、audience、receipt、source of truth。
