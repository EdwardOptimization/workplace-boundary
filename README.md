# Workplace Skills

Public agent skills for workplace pressure-pattern analysis and professional boundary defense.

This repository contains two public skills:

- `workplace-pressure-patterns`: identifies observable pressure patterns, narrative-control moves, credit-capture routes, blame-shifting paths, information isolation, meeting control, and responsibility traps.
- `workplace-boundary-defense`: helps diligent workers protect contribution, ownership, evidence, and professional boundaries through meeting scripts, written confirmations, status updates, escalation notes, contribution logs, and record-correction drafts.

The skills are designed for self-protection, fair communication, and evidence discipline. They must not be used for harassment, discrimination, identity-based targeting, fabrication, retaliation, or manipulation.

## Repository Layout

```text
workplace-skills-public/
├── README.md
├── SAFETY.md
├── DISCLAIMER.md
├── CONTRIBUTING.md
├── LICENSE
├── skills/
│   ├── workplace-pressure-patterns/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── pressure_taxonomy.md
│   └── workplace-boundary-defense/
│       ├── SKILL.md
│       └── references/
│           └── defense_playbook.md
├── evals/
│   ├── workplace-pressure-patterns.json
│   └── workplace-boundary-defense.json
├── examples/
│   ├── standup_status_capture.md
│   ├── meeting_minutes_correction.md
│   ├── identity_rant_redirect.md
│   ├── source_of_truth_correction.md
│   └── evidence_packet_addendum.md
├── references/
│   ├── behavior_taxonomy.md
│   └── skill_design_notes.md
├── research/
│   ├── evaluation_rubric.md
│   ├── artifact_templates.md
│   └── public_release_notes.md
└── scripts/
    └── validate_repo.py
```

## Installing The Skills

Copy the skill directories into your agent's skills directory:

```bash
cp -R skills/workplace-pressure-patterns ~/.agents/skills/
cp -R skills/workplace-boundary-defense ~/.agents/skills/
```

Install both skills together for best results: one skill diagnoses behavior and pressure routes, and the other turns that diagnosis into neutral, evidence-based defensive artifacts.

## Validation

Run the public repository checks:

```bash
python3 scripts/validate_repo.py
```

The validator checks that required public files exist, forbidden internal components are absent, skill frontmatter is present, examples remain behavior-only, and public terminology does not include known private research or identity-recall artifacts.

## Core Guardrail

The skills reason from observable behavior, role, incentive, decision rights, artifacts, responsibility chains, and evidence. They do not infer behavior from nationality, ethnicity, race, gender, caste, religion, accent, immigration status, or other protected traits.

See [SAFETY.md](SAFETY.md) for allowed and disallowed uses.

See [DISCLAIMER.md](DISCLAIMER.md) before using these skills in sensitive employment, legal, compliance, or HR contexts.
