# Workplace Boundary

Agent skills for workplace pressure-pattern recognition and evidence-based boundary defense.

Short version: defend against workplace pressure with evidence, records, ownership clarity, and professional boundaries.

## What This Is

`workplace-boundary` is a public defensive skill package for agents. It helps users analyze workplace pressure patterns and produce calm, professional, evidence-backed responses.

It does not ask "what kind of person is this?" It asks:

- What was said, written, assigned, changed, approved, omitted, or recorded?
- Which meeting, email, ticket, deck, review packet, or decision log may become the source of truth?
- Are contribution, ownership, deadline, risk, approval, or accountability being blurred?
- What is the least escalatory action that protects the record?

## Public Skills

### `workplace-pressure-patterns`

Identifies observable workplace pressure patterns and risk routes, including:

- credit capture and visibility capture;
- blame shifting and responsibility drift;
- unclear owners, deadlines, decisions, or approval status;
- meeting-minutes, deck, status-update, or review-packet distortion;
- side-channel decisions and pre-wired narratives;
- pressure to absorb recurring invisible work.

The output focuses on behavior diagnosis, evidence strength, risk path, and defense handoff.

### `workplace-boundary-defense`

Turns the diagnosis into professional defensive artifacts, including:

- meeting recaps;
- minutes corrections;
- contribution maps;
- owner, deadline, approval, and risk confirmations;
- status updates;
- escalation notes;
- review-packet or promotion-packet evidence addenda;
- source-of-truth record corrections.

It is designed for low-conflict, high-evidence boundary defense. It does not generate hostile, manipulative, discriminatory, or retaliatory messaging.

## Agent-Based Adversarial Simulation

During development, these skills were hardened with internal agent-based adversarial simulations of realistic workplace scenarios. The simulations tested whether defenses could survive stronger pressure patterns, record distortion, credit capture, blame shifting, and responsibility-transfer routes.

Only the defensive skills are public.

The internal Red Team components, prompts, scripts, traces, scoring records, and any material that could be reused as an attack manual are not included in this public repository.

## Why The Red Team Is Not Public

The goal is to help people protect themselves, not teach people how to suppress coworkers.

This public repository keeps:

- behavior-only pattern recognition;
- evidence discipline;
- boundary defense;
- ownership and accountability clarification;
- record correction;
- least-necessary escalation;
- identity-neutral and anti-discrimination guardrails.

It does not publish:

- steps for making coworkers take blame;
- stealthier credit-capture tactics;
- meeting or record manipulation tactics;
- ways to bypass evidence;
- copy-ready hostile workplace scripts.

## Install

```bash
cp -R skills/workplace-pressure-patterns ~/.agents/skills/
cp -R skills/workplace-boundary-defense ~/.agents/skills/
```

Install both skills together: one diagnoses pressure routes, and the other drafts evidence-based defenses.

## Appropriate Use

Use this project to:

- analyze a concrete meeting, email, chat, status update, or review artifact;
- turn emotional complaints into behavior and evidence questions;
- draft calm record-correction or clarification messages;
- protect contribution, ownership, deadlines, approval status, risks, and source-of-truth records.

Do not use this project to:

- harass, discriminate, retaliate, or target someone by identity;
- infer behavior from nationality, ethnicity, race, gender, caste, religion, accent, immigration status, or other protected traits;
- fabricate evidence, exaggerate contribution, or imply approval that does not exist;
- generate manipulation, exclusion, blame-shifting, credit-stealing, or suppression tactics.

## Validate

```bash
python3 scripts/validate_repo.py
```

## Core Rule

Analyze behavior, not identity.

Workplace boundary defense is a record system: facts, evidence, owners, deadlines, decisions, risks, audiences, receipts, and source of truth.
