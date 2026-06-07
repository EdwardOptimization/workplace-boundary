---
name: workplace-pressure-patterns
description: Use this skill whenever the user asks about workplace pressure, workplace PUA, office politics, credit stealing, blame shifting, resource grabs, meeting control, narrative control, information isolation, vague ownership, responsibility traps, being suppressed at work, or wants to analyze a meeting/email/chat/status report for hidden pressure patterns. It identifies observable workplace pressure patterns and risk routes so the user can defend themselves professionally. Do not use identity labels as evidence.
---

# Workplace Pressure Patterns

Identify workplace pressure patterns from observable behavior, artifacts, incentives, and responsibility chains. The goal is to help users understand what is happening and what risk it creates, not to teach manipulation.

## Operating Rules

- Analyze behavior, not identity. Ignore nationality, ethnicity, race, gender, caste, religion, accent, and immigration status as causal explanations.
- Treat forum complaints and stereotypes as weak evidence. Ask what was said, decided, written, assigned, delivered, omitted, or escalated.
- Do not generate instructions for harming, manipulating, harassing, excluding, or discriminating against anyone.
- When the user uses identity-heavy or derogatory language, translate it into observable behavior and continue neutrally.
- Prefer evidence categories: direct artifact, written record, meeting behavior, repeated pattern, interpretation only.

## Workflow

1. Extract the neutral incident.
   - Who are the roles, not identities?
   - What was said or written?
   - What was decided?
   - Who owns the work?
   - What artifacts exist?
   - What outcome is at risk?

2. Identify pressure routes.
   - Narrative control
   - Credit capture
   - Blame shifting
   - Owner ambiguity
   - Record and audience control
   - Meeting airtime control
   - Meeting-minutes control
   - Information isolation
   - Resource or scope capture
   - Goal shifting
   - Bad-news avoidance
   - Deadline or expectation drift
   - Upward decision-cost transfer
   - Visibility and promotion-evidence drift
   - Assistance boundary drift
   - Language or side-channel faultline

3. Stress-test the likely route.
   - What is the cheapest ambiguity the pressure pattern exploits?
   - Which official record would make the pressure route durable?
   - Which missing artifact lets credit, owner, or blame drift?
   - Which stakeholder would believe the wrong narrative and why?
   - What would a stronger version of this pressure pattern try next?
   - Which channel or forum will harden the narrative first?
   - Which named record owner or owner role can edit that hardening artifact?
   - What first channel and fallback channel would get the correction into that record before it hardens?
   - Does the issue need an owner matrix because proposal, approval, execution, evidence, risk, and record ownership are split?
   - Is the user losing airtime, credit, or decision visibility because there is no concise memory hook or follow-up record?
   - Is a vague phrase hiding decision state, deadline, or escalation threshold?

4. Rate evidence strength.
   - Strong: direct email, document, ticket, commit, meeting minutes, transcript, manager decision.
   - Medium: repeated behavior with dated examples.
   - Weak: memory, interpretation, one-sided complaint.
   - Invalid: identity stereotype without behavior.

5. Explain the mechanism.
   - What incentive does the pattern exploit?
   - What ambiguity makes it possible?
   - Which artifact would prove or disprove it?

6. Hand off to defense.
   - Recommend what artifact or response `workplace-boundary-defense` should produce.
   - Name the minimum defense fields: owner, deadline, evidence, decision, risk, ask, correction window.
   - Name the hardening forum, record owner, required audience, first channel, and fallback channel.
   - Say whether the final draft needs audience parity: the correction must reach the same audience or durable record that received the wrong framing.
   - Name the controlling artifact that will govern the decision: agenda, decision log, packet, tracker, review-system entry, branch-blocking note, or client deck.
   - Ask for a record-owner choice clause: update the record by a deadline, or, when the deadline is imminent, state the neutral fallback the user will place under silence.
   - If responsibilities are split, require an owner matrix: record owner, decision/approval owner, evidence owner, risk owner, execution owner, hold owner, and fallback poster.
   - For truth-record risk, require the source-of-truth record, current source of truth, obsolete or superseded wording, corrected wording that supersedes it, true approver, approval status: pending when relevant, decision-record owner, correction owner, and required decision owners.
   - For material-evidence risk, require an evidence packet with exact current wording, source proof, artifact/date/link, and proof accessible to the record owner.
   - For no-access packet or leadership-thread risk, require a no-access route and confirmation receipt showing whether the correction was posted, forwarded, or appended to the packet-accessible record.

## Output Format

Use this structure:

```text
## Neutral Incident

Roles:
Observable facts:
Current ambiguity:
Artifact evidence:

## Pattern Diagnosis

Pattern:
Mechanism:
Risk to the user:
Evidence strength:
What would confirm it:
What would disconfirm it:

## Defense Handoff

Immediate defensive objective:
Needed artifact:
Suggested response type:
Minimum fields:
Escalation threshold:
Stakeholder route:
```

## Pressure Critic Mode

When asked to critique a defense, do not explain how to manipulate coworkers. Instead, identify remaining defensive leaks:

- `credit_leak`: contribution can still be omitted, renamed, or reported by someone else.
- `owner_leak`: final owner, sign-off, or due date is still ambiguous.
- `evidence_leak`: claim depends on memory instead of artifact, date, link, ticket, or transcript.
- `record_leak`: meeting minutes, deck, ticket, packet, tracker, or status report can still become the wrong official record.
- `stakeholder_leak`: the wrong audience may still receive the wrong narrative first, or the correction reaches an audience but not the controlling artifact they rely on.
- `escalation_leak`: the user lacks a clear threshold for moving from clarification to escalation.
- `truth_record_leak`: a false or overstated approval/alignment record is not explicitly corrected.
- `material_leak`: the response ignores concrete emails, chat lines, transcript lines, or review text already available.
- `truth_record_leak`: also applies when the draft does not name the source-of-truth record, true approver, approval tracker, decision-record owner, correction owner, or the corrected wording that supersedes obsolete or superseded wording.
- `material_leak`: also applies when the draft lacks an evidence packet with exact current wording, source proof, artifact/date/link, and proof accessible to the record owner.

For each leak, ask for a protective artifact or wording patch. Keep the analysis defensive and non-operational.

## Agent-Reviewed Pattern Add-Ons

Use `references/agent_reviewed_boundary_patterns.md` as public-safe qualitative background for these recurring artifact routes:

- Record and audience control: a CC list, recap, minutes, deck, tracker, review packet, or decision log can become the durable version of events.
- Owner and decision ambiguity: split who proposed, decided, approved, executed, blocked, accepted risk, and owns the record update.
- Meeting airtime and memory hooks: diagnose when the remembered sentence, not the underlying work, is controlling the narrative.
- Upward decision framing: identify when the user is sending an option menu instead of a recommendation with rationale, tradeoff, owner, and next step.
- Visibility, credit, and promotion evidence: ask which artifact maps contribution to business effect and which audience will remember it.
- Expectation and deadline anchoring: convert vague "later/review/revisit" language into decision state, date, owner, and threshold.
- Cross-functional stakeholder route: ask whether the dependency owner has authority and incentive, or whether the route needs a shared-goal stakeholder.
- Bad-news and risk packaging: convert status-only bad news into impact, options, recommendation, owner, and deadline.
- Language or pragmatic friction: treat it as a concrete artifact problem only when it affects action item, deadline, approval, relationship temperature, or clarification.
- Low-signal/noise handling: do not overfit slogans, sales copy, hashtags, or empty examples.

## Reference Map

Read `references/pressure_taxonomy.md` for pattern definitions. If available, use the repository-level `references/behavior_taxonomy.md`, `references/agent_reviewed_boundary_patterns.md`, and `references/source_notes.csv` as evidence background.
