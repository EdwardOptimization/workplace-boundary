# Contributing

Contributions should improve defensive usefulness without weakening safety constraints.

## Acceptable Changes

- Add behavior-only examples.
- Improve evidence discipline, owner clarity, audience parity, deadline handling, and source-of-truth correction.
- Add regression cases for defensive failures.
- Tighten identity-redaction and non-retaliation guardrails.
- Improve documentation, validation, or install instructions.

## Review Checklist

- No identity group is used as evidence or a causal explanation.
- No private research, raw identity-recall search terms, or internal-only components are added.
- No instructions help a user manipulate, isolate, blame, harass, or take credit from a coworker.
- Drafts do not overclaim approval, ownership, causality, evidence, audience reach, or receipt.
- Examples separate verified facts from inference and pending fields.
- `python3 scripts/validate_repo.py` passes.

## Public Scope

This public repository contains only defensive skills and public-safe research artifacts. Do not add internal evaluation components, private traces, or raw search corpora.
