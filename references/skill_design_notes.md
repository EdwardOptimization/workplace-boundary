# Skill Design Notes

Created: 2026-05-25

## Proposed Skill Split

The research supports two related but separate skills.

### 1. strategic-narrative-reporting

Purpose:

- Help the user report work upward with credible narrative, explicit facts, and management-level framing.
- Best for weak KPIs, mixed progress, resource asks, board/QBR updates, weekly reports, and promotion packets.

Core sources:

- S001, S002, S012, S014, S015, S018, S046, S047, S066, S067, S068, S069, S070, S071, S072, S075, S076, S083, S084, S085, S086, S087

Core outputs:

- executive one-pager;
- weekly/monthly update;
- bad-KPI reframe;
- resource request;
- slide outline with takeaway titles;
- delayed-project update;
- board/QBR written pre-read;
- pre-wire stakeholder brief.

### 2. workplace-political-patterns

Purpose:

- Help the user identify and respond to workplace political behavior: credit capture, blame shifting, meeting control, resource grabs, ambiguous ownership, goal shifting, and matrix crossfire.
- It should analyze observable behavior only, not identity.

Core sources:

- S008, S009, S010, S011, S013, S016, S017, S020, S021, S022, S024, S027, S028, S029, S041, S042, S044, S045, S048, S049, S050, S052, S053, S054, S055, S057, S058, S059, S060, S061, S062, S063, S064, S065, S088, S089, S090, S092, S093, S096, S097, S098, S100, S101, S102, S103, S104, S105, S106, S107, S117, S125, S126, S127, S128, S130

Core outputs:

- behavior pattern diagnosis;
- evidence strength;
- likely organizational mechanism;
- risk to user;
- recommended countermeasure;
- concrete email or meeting script;
- decision log / issue log / risk log template;
- contribution map;
- meeting airtime and attribution correction script.

## Trigger Conditions

Use `workplace-political-patterns` when the user asks about:

- 被甩锅 / 背锅 / 防甩锅;
- 抢功 / credit stealing / credit capture;
- 开会被抢话 / meeting control / agenda control;
- 老板或同事只汇报不干活;
- 资源被抢 / stakeholder management / influence without authority;
- 责任不清 / owner 不清 / action item 不清;
- 跨部门或矩阵组织中被多个老板夹击;
- 会议纪要、邮件留痕、决策确认;
- 如何保护自己的贡献和边界;
- analyzing a specific meeting, email, chat, or incident.

Use `strategic-narrative-reporting` when the user asks about:

- 高管汇报、老板汇报、周报、月报、QBR、董事会汇报;
- 弱 KPI 怎么说;
- 项目延期怎么汇报;
- 如何争取资源;
- 如何把执行过程写成管理层能看懂的故事;
- PPT 大纲和汇报叙事.

## Input Contract

Ask for missing facts only when needed:

- audience;
- decision needed;
- current facts;
- artifacts available;
- owner/dependency map;
- what the user wants to protect or obtain.

If the user only gives a rant, first convert it into a neutral incident table:

```text
Event:
People/roles:
What was said:
What was decided:
Who owns what:
Evidence available:
Risk:
Desired outcome:
```

## Analysis Workflow

1. Strip identity labels from the reasoning path.
2. Extract observable behaviors.
3. Identify the mechanism:
   - narrative control;
   - owner ambiguity;
   - visibility capture;
   - dependency risk;
   - matrix authority conflict;
   - goal shifting;
   - indirect feedback;
   - resource tradeoff.
4. Assign evidence level:
   - direct artifact;
   - repeated pattern;
   - interpretation only;
   - identity stereotype only.
5. Recommend response:
   - do nothing yet;
   - ask clarifying question;
   - send written confirmation;
   - publish progress update;
   - correct credit gently;
   - escalate decision;
   - refuse boundary breach.
6. Draft artifact:
   - email;
   - meeting recap;
   - status update;
   - escalation note;
   - one-on-one script;
   - contribution log;
   - decision log;
   - issue/risk log;
   - slide title rewrite.

## Expanded Pattern Coverage

The expanded search supports these pattern families:

- proactive upward framing;
- direct-but-diplomatic outcome framing;
- diplomatic decoding of indirect feedback;
- written confirmation and meeting accountability;
- credit overclaiming and visibility capture;
- influence without authority;
- escalation as decision framing;
- impression management and ingratiation;
- rational persuasion vs pressure/coalition tactics;
- bad-news avoidance and upward distortion;
- pre-wire / pre-brief before formal meetings;
- meeting airtime and process control;
- action-title narrative control in PPT/decks;
- asymmetric credit/blame funnels;
- matrix crossfire and goal-shift risk;
- language-faultline and side-channel decision risk;
- record-resistance risk;
- assistance boundary drift;
- ill-defined-goal politics;
- single-source status defense;
- root-cause reframing.

The skill should first identify which family the incident belongs to, then generate a response artifact. Avoid producing only abstract advice.

## Output Template For Incident Analysis

```text
## Pattern Diagnosis

Observed behavior:
Evidence:
Likely mechanism:
Risk to you:
Evidence strength:

## What To Do

Immediate move:
Written artifact:
Meeting move:
Escalation threshold:

## Draft Text

[ready-to-send email or meeting script]
```

## Output Template For Defensive Email

```text
Subject: Confirming [decision/action] from [meeting/project]

Hi [Name],

To keep us aligned, I want to confirm the current decision and next steps:

Decision:
Owner:
Due date:
Dependencies:
Risks:
My current action:
Decision needed:

Please reply by [date/time] if I missed anything or if the owner/date should change.

Thanks,
[Name]
```

## Output Template For Credit Protection

```text
Thanks for summarizing this. To make the ownership clear:

- [Person A] led [part A].
- I handled [part B], including [artifact/result].
- [Person C] is owning [part C].

The next decision is [decision], and the open risk is [risk].
```

## Output Template For Escalation

```text
Subject: Project Escalation: [Project] - [Issue] - Decision Needed by [Date]

Current status:
Impact if unresolved:
What has already been tried:
Decision needed:
Options:
Recommended option:
Owner after decision:
```

## Refusal And Redirection Rules

Refuse or redirect when the user asks the agent to:

- target someone because of nationality, ethnicity, race, religion, caste, gender, accent, or visa status;
- fabricate evidence;
- hide known failures;
- frame a person as guilty based only on group identity;
- write harassment, slurs, or discriminatory messaging.

Redirect to:

- observable behavior;
- artifact evidence;
- role and responsibility;
- decision chain;
- delivery facts;
- neutral defensive language.

## Minimum V0 Skill Content

For `workplace-political-patterns`, V0 should include:

- `SKILL.md`;
- `references/behavior_taxonomy.md`;
- `references/email_templates.md`;
- `references/evidence_levels.md`;
- `references/source_notes.md`.

No scripts are needed for V0.
