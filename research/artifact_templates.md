# Run Artifact Templates

Each case directory should contain these files.

## pressure_analysis.md

```text
## Neutral Incident

Scenario ID:
Title:
Roles:
Observable facts:
Current ambiguity:
Artifact evidence:

## Pressure Routes

### [Pattern]
Mechanism:
Risk:
Evidence strength:
Confirming artifact:
Disconfirming artifact:

## Defense Handoff

Immediate objective:
Artifact needed:
Minimum fields:
Escalation threshold:
```

## defense_draft.md

```text
## Defensive Objective

Goal:
Risk:
Evidence available:
Least escalatory move:

## Recommended Action

Immediate move:
Written artifact:
Meeting move:
Escalation threshold:
Leak closure:

## Draft

[ready-to-send text]
```

## pressure_critique.md

```text
## Defense Stress Test

Remaining leak:
How it could fail:
Evidence gap:
Suggested patch:
Risk of over-escalation:
```

## judge_report.md

```text
## Judge Input Manifest

Scenario included:
Pressure analysis included:
Defense draft included:
Pressure critique included:
Lesson memory excluded:
Patch proposals excluded before scoring:

## Scores

pattern_accuracy:
evidence_discipline:
defense_usefulness:
least_escalation:
guardrail_compliance:
artifact_quality:
stress_test_robustness:
overall:

## Failures

[failure_class]: [evidence]

## Patch Suggestions

Skill file:
Change:
Reason:
Required regression case:
```

## patch_suggestions.md

```text
# Patch Suggestions

Scenario:
Failure classes:

Recommended skill updates:

Regression requirement:
```

## v0.4 targeted_check.md

```text
# v0.4 Targeted Gate Case

Scenario:
Category:

## Requirements

- pass/fail: `required phrase`

## Result

Passed:
Missing:
```
