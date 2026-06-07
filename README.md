# Workplace Boundary

Agent skills for workplace pressure-pattern recognition and evidence-based boundary defense.

## Read This In Your Language

- [中文](README.zh-CN.md)
- [English](README.en.md)
- [日本語](README.ja.md)

## What This Repository Contains

This public repository contains two defensive agent skills:

- `workplace-pressure-patterns`: identifies observable workplace pressure patterns and risk routes.
- `workplace-boundary-defense`: drafts professional, evidence-based responses that protect credit, ownership, records, and boundaries.

During development, the skills were hardened with internal agent-based adversarial simulations of realistic workplace scenarios. The internal Red Team components, prompts, scripts, traces, and run artifacts are intentionally not included in this public repository.

The latest public version also includes a source-free distillation of private agent-reviewed workplace notes. Only abstract defensive boundary patterns are published; raw notes, titles, authors, quotes, paths, review data, and internal test materials are excluded.

## Install

```bash
cp -R skills/workplace-pressure-patterns ~/.agents/skills/
cp -R skills/workplace-boundary-defense ~/.agents/skills/
```

## Validate

```bash
python3 scripts/validate_repo.py
```

## Core Rule

Analyze behavior, not identity. These skills reason from observable actions, artifacts, decision rights, evidence, ownership, timing, and records. They must not infer behavior from nationality, ethnicity, race, gender, caste, religion, accent, immigration status, or other protected traits.
