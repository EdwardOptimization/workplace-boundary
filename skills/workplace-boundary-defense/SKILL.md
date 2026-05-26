---
name: workplace-boundary-defense
description: Use this skill whenever the user wants to defend against workplace PUA, pressure, blame shifting, credit stealing, vague ownership, meeting suppression, information isolation, resource conflict, unclear action items, unfair performance narratives, or needs a professional email, meeting script, status update, escalation note, contribution log, or owner/deadline confirmation. It helps protect contribution, boundaries, evidence, and accountability without manipulation or discrimination.
---

# Workplace Boundary Defense

Help users protect their work, contribution, responsibility boundaries, and professional reputation through neutral, evidence-based communication.

## Operating Rules

- Defend with facts, artifacts, owner clarity, and calm wording.
- Do not retaliate, harass, insult, discriminate, fabricate, or escalate without evidence.
- Avoid identity-based reasoning. Respond to behavior and responsibility chain only.
- Prefer short written artifacts that can be sent or adapted immediately.
- Make invisible work visible without bragging or attacking.

## Workflow

1. Determine the defensive objective.
   - Protect credit
   - Clarify owner
   - Confirm decision
   - Record blocker
   - Correct meeting minutes
   - Escalate risk
   - Set assistance boundary
   - Prepare upward update

2. Choose the least escalatory effective move.
   - Private clarification
   - Public neutral correction
   - Written recap
   - Status update
   - Decision-needed escalation
   - Manager one-on-one
   - Skip-level or HR only when necessary

3. Generate the artifact.
   - Email
   - Meeting script
   - Standup update
   - Meeting-minutes correction
   - Contribution map
   - Decision log
   - Risk/issue log
   - Executive update

4. Add evidence hooks.
   - Artifact links
   - Dates
   - Owners
   - Due dates
   - Prior decisions
   - Open risks
   - Requested confirmation deadline

5. Close pressure leaks.
   - Credit leak: add contribution map and artifact link.
   - Owner leak: add final owner, sign-off owner, due date, and acceptance criterion.
   - Evidence leak: add dated source, ticket, doc, transcript, commit, or meeting note.
   - Record leak: correct the official record directly and ask for confirmation.
   - Stakeholder leak: send a concise factual update to the appropriate audience.
   - Escalation leak: state the threshold for escalation.
   - Truth-record leak: replace false approval/alignment wording with accurate pending-review wording, name the true approver, and mark the source-of-truth record that supersedes obsolete or superseded wording.
   - Material leak: use concrete details already available in the user's email, chat, transcript, deck, or review excerpt; include an evidence packet with exact current wording, source proof, and artifact/date/link fields.

6. Map the stakeholder path.
   Do this as a concrete record route, not a generic sentence. If a name is unknown, name the role or artifact owner that must be filled in before sending.
   - Hardening forum: meeting, client review, calibration, launch thread, leadership follow-up, project recap, review packet, promotion packet, QBR, decision log, or ticket.
   - Record owner: the person or role that controls the deck, minutes, tracker, review packet, decision log, recap, or status thread.
   - Required audience: the people who will decide, remember, or repeat the narrative.
   - Deadline: the latest time the correction must land before the record hardens.
   - First channel: the least escalatory channel that reaches the record owner.
   - Fallback channel: the next channel if the correction is ignored or the wrong wording enters the record.

7. Use record-specific routing.
   - Credit/promotion: route to project recap, leadership follow-up, brag doc, review packet, or promotion packet owner.
   - Client/vendor blame: route to client-review deck owner, delivery owner, vendor lead, and meeting-minutes owner.
   - Performance/layoff: route to manager, calibration packet owner, review-system entry owner, and HRBP only if an inaccurate official record persists after the normal correction path.
   - Side-channel decisions: route to decision log, shared project doc, release tracker, API owner, architecture record owner, and the branch-hold or launch-hold owner when silence would otherwise allow action.
   - Meeting minutes/risk acceptance: route to minutes owner, decision owner, launch approver, and status thread.
   - False approval/alignment: route to the approver/sign-off owner and the official decision record.
   - Pre-read decisions: route both the pre-read correction and the meeting agenda or decision log, so the meeting cannot open from the old framing.

8. Put the route inside the ready-to-send draft.
   It is not enough to describe the stakeholder path in notes. If the risk is a wrong visible record, the `## Draft` must include:
   - Audience parity: the correction reaches the same audience or record that received the wrong framing.
   - Controlling artifact: name the final record that will govern the decision, such as the meeting agenda, decision log, promotion packet, calibration packet, review-system entry, release tracker, branch-blocking note, or client deck.
   - Record-owner choice: ask the record owner to update the record by a deadline or, for deadline-critical records, state the neutral fallback the user will place if the record is not corrected.
   - Source link request: include or request the dated artifact link in the first correction.
   - Fallback sentence: state where the user will place the neutral correction if the record is not updated.
   - Silence default: if branch close, packet lock, calibration, or a decision meeting is imminent, do not leave fallback dependent on permission. State the default neutral addendum/recap path under silence.
   - Source-of-truth record: state the current source of truth, the obsolete or superseded wording, the corrected wording that supersedes it, and the correction owner who must post it.
   - Material evidence packet: include exact current wording, source proof, artifact/date/link, and confirmation that the evidence is accessible to the record owner.

9. Split owner roles when a decision has multiple responsibilities.
   Do not collapse different responsibilities into one vague owner. For client, release, calibration, pre-read, side-channel, or invisible-work cases, name a responsibility matrix:
   - Record owner: updates deck, minutes, tracker, packet, recap, launch email, or goals record.
   - Decision or approval owner: approves transfer, launch, skipped check, risk acceptance, or final status.
   - Evidence owner: provides links, dates, transcript, criteria, status, approval, or dashboard proof.
   - Risk owner: accepts residual risk if the risky path proceeds.
   - Execution owner: owns implementation, remediation, weekly report, or next action.
   - Hold owner: pauses branch close, client review wording, packet submission, or launch if required fields remain open.
   - Fallback poster: sends the neutral recap if the record owner does not update the record.

10. Close truth-record and material-evidence residuals.
   Use this when a false approval, stale packet sentence, or unsupported summary can survive as the official record.
   - Source-of-truth owner: who owns the current source of truth.
   - Decision-record owner: who must update the tracker, packet, agenda, decision log, or approval tracker.
   - Correction owner: who posts the corrected wording and confirmation receipt.
   - Approval status: pending, approved, rejected, or unknown. Use `approval status: pending` when approval has not been given.
   - True approver: the person or team with decision rights. Do not imply approval unless that approver confirmed it in writing.
   - Supersession line: say the corrected record supersedes obsolete or superseded wording.
   - Required decision owners: list each owner whose confirmation is needed; the decision remains pending until they confirm.
   - Evidence packet: exact current wording, source proof, artifact/date/link, metric or transcript line, and record-owner accessibility.
   - No-access route: when the user cannot access the original thread, route through manager or packet owner and ask whether the correction was posted, forwarded, or appended.
   - Packet-accessible confirmation: ask for a confirmation receipt showing the correction reached the packet, tracker, or decision record.

11. Run the stress-test closure gate.
   Use this whenever the input includes stress-test traces, a wrong visible record, a packet/deck/minutes/tracker risk, or any of these leak labels: `audience_parity_leak`, `deadline_silence_leak`, `material_leak`, `truth_record_leak`, `unclear_owner`.
   - Do not leave bracketed placeholders in the ready-to-send action. If a value is unknown, the draft must first ask the user or record owner for that value before asking for correction.
   - Same-audience receipt: name the original audience or distribution list, the correction audience, and the confirmation receipt that proves the correction reached the same audience or controlling artifact.
   - Deadline silence trigger: name a concrete timestamp tied to meeting start, packet lock, deck export, tracker lock, launch send, or review cutoff. If unknown, require a "deadline lookup" step before fallback.
   - Material evidence packet: include exact current wording, source proof, artifact/date/link, and record-owner accessibility. If links or dates are missing, make evidence collection the immediate move.
   - Truth-record supersession: name the old wording, corrected wording, source-of-truth record, decision-record owner, correction owner, and receipt proving the old wording was replaced, marked incomplete, or superseded.
   - Owner matrix completion: do not accept generic "owner" fields. Name the role that must be filled before sending for record owner, decision/approval owner, evidence owner, risk owner, execution owner, hold owner, and fallback poster.
   - Existing-record gate: do not create a record dispute when no wrong durable record exists. For memory-only cases, first request the source record, transcript, minutes, or recap, then correct only if the source record is wrong.

12. Select the draft mode before writing.
   Red-team failures usually happen when a draft looks like a correction while the required audience, deadline, owner, or evidence fields are still unknown. Use exactly one mode and make it explicit in `## Recommended Action`.
   - Field-lock request mode: use this when audience, deadline, controlling artifact, receipt owner, or owner matrix fields are missing. The draft asks the record owner, meeting owner, packet owner, or manager to fill the missing fields first. It must not make a corrective claim beyond verified facts.
   - Evidence-collection mode: use this when material evidence is incomplete. The draft separates `Verified now` from `Pending verification`, asks for source proof with artifact/date/link, and does not assert unsupported conclusions.
   - Formal correction mode: use this only when the controlling artifact, required audience, hardening deadline, evidence packet, source-of-truth record, and accountable owner roles are complete; or when the hardening event is imminent and the draft states only verified facts plus open fields as a neutral pending-status addendum.
   - Do not use empty placeholders such as `[record owner]` in the sendable text. If a value is unknown, write `Pending - [specific role] to fill by [timebox]`.
   - Name a field-completion owner: the role accountable for filling missing audience, deadline, artifact, and owner fields. The user is not the default owner unless the user controls that record or has been explicitly delegated the record update.
   - Name a confirmation receipt owner: the role accountable for proving the correction or pending-status addendum reached the same audience or controlling artifact.

13. Close deadline and owner execution risk.
   When the exact hardening timestamp is unknown but the event is near, silence on the deadline lookup is itself a risk. The draft must include an interim lookup trigger:
   - If a known forum or send date exists, request deadline confirmation by the earlier of end of current business day or two business hours before the known forum/send.
   - If the forum/send is within two business hours, request confirmation within 30 minutes.
   - If no date is known, ask the record owner to confirm the earliest hardening event and deadline before any correction claim is sent.
   - If no one confirms the deadline by the interim lookup trigger, the fallback is a neutral pending-status note in the controlling artifact or official thread, using only verified facts and explicitly open owner/evidence fields.
   - The owner matrix must include an accountable first responder to complete the matrix, a hold owner with authority to pause or mark the record pending, and a fallback poster. Missing owner fields must be assigned to the field-completion owner to fill by the interim trigger.

14. Require fallback validity proof.
   A fallback does not close audience or truth-record risk merely because it is neutral. It only closes the risk when the draft requires proof that the fallback reached the places where the old framing can still harden.
   - Same-audience-or-derived-record proof: the fallback must reach the original audience and every controlling or derived record that can carry the old wording, such as agenda, minutes, recap, decision log, risk log, packet, review-system entry, launch tracker, status packet, recurring task, send template, leadership thread, promotion packet, or calibration note.
   - Timestamped receipt: name the receipt owner and require a timestamped receipt showing the correction or pending-status note was posted, forwarded, appended, or reflected before the hardening event.
   - Supersession marker: the old sentence or implication must be replaced, marked incomplete, marked pending, marked superseded, or marked not controlling in the source-of-truth record and derivative records.
   - No coexisting contradiction: do not allow an addendum to coexist with an unchanged decision label, approval line, owner field, contribution sentence, blame sentence, or launch-status sentence that still carries the old meaning.
   - If the original audience is unknown at the interim trigger, send the fallback to the controlling artifact plus the best-known original thread, then require the receipt owner to forward or append it to any later-discovered original recipients or derivative records.
   - In promotion or performance cases, pending-status wording must preserve the candidate-linked or person-linked contribution under review; do not reduce it to generic "details pending" wording.

15. Separate the minimum protective act from the full checklist.
   When time is tight or the record is not yet proven wrong, the first message should be short enough to execute. Put the full owner/evidence/derived-record matrix under a `Completion checklist` after the first-pass note.
   - First-pass note: 5 to 8 concise bullets or short paragraphs that state response mode, verified facts, requested field lock, interim trigger, temporary execution default, and neutral fallback.
   - Completion checklist: full owner matrix, evidence packet, derived records, fallback validity proof, supersession marker, and reconciliation checklist.
   - Memory-only or no-durable-record cases: the first-pass note is only a record-existence check to the least necessary owner. Do not send the full matrix until a wrong durable record, recap, transcript, packet, or meeting note exists or is about to be created.
   - Deadline-critical cases: if roles remain pending at the interim trigger, the temporary execution default activates. The draft must say which role posts the neutral pending-status note and which role reconciles records afterward.
   - Temporary fallback poster: choose the narrowest role with access to the official thread or controlling artifact. The user may be temporary fallback poster only for a neutral record-accuracy note, and the draft must state this does not create execution, approval, risk, source-data, recurring-work, or final-owner responsibility.
   - Temporary receipt owner: if no official receipt owner accepts before the interim trigger, the accountable first responder owns timestamp capture and follow-up until the permanent record owner is identified.
   - Owner acceptance line: ask the accountable first responder to accept ownership of field completion, fallback posting, or receipt within the interim trigger; if they decline or stay silent, the temporary execution default applies.
   - Reconciliation checklist: after the fallback or correction, require each derived record to be marked `updated`, `appended`, `pending`, `superseded`, `not controlling`, `inaccessible with reason`, or `not applicable`.

16. Put a conditional Draft-embedded closure capsule in the sendable text.
   Use this when the case involves a verified or imminent visible record, credit signal, approval wording, client/vendor blame, leadership thread, launch send, review packet, or promotion packet. The capsule must appear inside `## Draft`, not only in `## Recommended Action`.
   - Current visible wording: quote the exact wording that could harden, or ask the record owner to paste it before any correction claim.
   - Source proof: name the dated source facts and the artifact/date/link still needed.
   - Same-audience or controlling-record append: ask for the correction or pending-status note to reach the original audience and the controlling record they rely on.
   - Derived-record sweep: list the decks, minutes, agendas, trackers, packets, scheduled sends, customer announcements, campaign copy, leadership threads, review records, or recaps that must be updated, appended, marked pending, superseded, or marked not controlling.
   - External/direct thread check: for vendor, client, partner, regional, leadership, or side-channel cases, ask whether any direct external or separate stakeholder thread already carried the old framing. Do not broadcast to that thread unless a wrong durable record is verified or imminent.
   - Non-user owner split: the user may provide evidence, but execution, approval, risk acceptance, send/hold authority, remediation, and final record ownership stay with the responsible owner unless explicitly delegated in writing. If an owner is not proven by the artifact, write `Pending - [role] to confirm` instead of naming a person or team.
   - Receipt: require a timestamped receipt showing the correction was posted, forwarded, appended, reflected, or marked pending before the hardening event.

17. Use domain closure add-ons for common residuals.
   - Vendor late-blame: include a client-facing path check for client deck, pre-read, risk log, meeting minutes, recap, delivery tracker, and any vendor-client direct thread. Split project-manager evidence/timeline ownership from vendor delivery/remediation ownership and review-disposition/risk ownership.
   - Approval-pending launch: reconcile launch email, approval tracker, scheduled customer announcement, scheduled send copy, send checklist, campaign copy, launch thread, and customer-facing approval path. Name a send owner or hold owner with authority to pause the send; if unknown, make field-lock the immediate action.
   - Manager-credit or promotion credit: split the private manager ask, same-audience leadership append, and packet-owner fallback. The draft must include artifact link/date request, original leadership audience, derived record list, and a candidate-linked contribution sentence that can be appended to review or promotion materials. If the metric is team-level, use non-exclusive wording such as "contributed to the team result by..." rather than saying the candidate alone produced the metric.

18. Enforce evidence-boundary guardrails before sending.
   This is a guardrail, not just style. Do not create a new inaccurate record while correcting an old one.
   - Non-exclusive metrics: if the source says "team improved X by Y%", do not rewrite it as "[candidate] improved X by Y%" unless a source proves sole causality. Use "For the team result of X improved by Y%, [candidate] contributed [verified mechanism/artifacts]."
   - Transcript-bound minutes: only put facts directly supported by the transcript, minutes, or source artifact into the correction. Do not add execution owner, risk owner, approval owner, or final owner unless the source names that owner. Unknown owner fields stay `Pending - [role] to confirm`.
   - Inference labels: separate `Verified now`, `Inference`, and `Pending verification`. Corrected wording may include verified facts and pending status; inferences go in the ask, not in the asserted record.
   - Hostile or retaliation input with weak evidence: refuse the retaliatory ask, create a private incident-note scaffold, and send the first request only to the meeting owner, notes owner, or record owner. Do not include leadership, HR, broad distribution, or the target person until a material record error, repeated documented misstatement, or decision/owner/risk/deadline impact is verified.
   - Record-existence deadline: every record-existence or evidence-collection draft must include a response deadline, such as end of current business day, before minutes finalize, before packet lock, or before the next decision forum.
   - Materiality threshold: escalation requires a verified false official record, repeated documented misstatement, or material impact on owner, decision, action item, risk, deadline, performance, or review packet.

19. Apply the evidence-safe wording contract.
   Before returning the draft, scan every asserted sentence and downgrade any unsupported owner, causality, audience, completion state, or approval claim. Use this contract especially for guardrail failures:
   - Vendor late-blame: say "no questions were raised in the available thread by the Friday deadline" only when the thread proves the deadline passed without questions. Do not say "before the Friday question window." The draft must ask the client-review record owner to confirm the same-audience route, the review deadline, the record owner, the fallback poster, and the receipt owner.
   - Calibration or layoff packets: if the packet ignores the stated quarter goal, ask whether a documented goal change made another criterion controlling. Do not say the user caused a metric change unless an artifact map ties the user's dated work to that result. Use "the dashboard shows [metric]; my artifact map for [work] is pending/attached" rather than "my work reduced [metric]" when causality is not proven.
   - Mixed-channel decisions: quote conditional chat instructions verbatim. Do not convert "if needed," "can," "let's," or "sounds fine" into "allowed," "approved," "signed off," or "decided" unless a formal approval record exists. Use "approval status: pending" until the true approver confirms.
   - Publish-status or standup credit: scope ownership to artifact-linked work only. Write "I am posting the artifact links for the implementation/design work reflected in those artifacts" rather than "I own the current work" unless the record proves full workstream ownership. Ask the standup facilitator or notes owner to confirm the recap line.
   - Contribution split across small tasks: distinguish plan ownership from completed delivery. If the source is a project plan, say "the plan lists me as owner for..." and require artifact link, date, completion state, outcome, and controlling-record owner before saying "delivered," "completed," or "success included user-owned delivery."
   - Promotion or team metrics: keep team metrics non-exclusive. Use "work supporting the team's [metric] result" unless a performance analysis proves direct metric causality. Require packet owner, packet lock time, reviewer/calibration audience, and same-audience receipt.
   - Manager-credit or leadership attribution: say "my dated draft contains..." or "the source artifact includes..." Do not say an idea "came from my draft" unless the full leadership thread and source history prove sole source. If the user lacks access to the leadership thread, require a timestamped same-audience receipt or packet-accessible append.
   - If any of these fields are missing, choose field-lock or evidence-collection mode. Do not write a formal correction claim that sounds final.

20. Use behavior-only sanitization for hostile identity inputs.
   When the input contains nationality, race, ethnicity, gender, caste, religion, disability, age, or other protected-class generalizations, do not carry those generalizations into the working record.
   - Convert the user's description into observable behavior fields: who did what, in which work forum, what artifact or record changed, what decision/owner/risk/deadline was affected, and what evidence exists.
   - Field-level identity stripping is mandatory. Every user-supplied field value and metadata field must reject identity categories, group generalizations, slurs, stereotype claims, motive claims based on identity, and retaliation goals. This includes URLs, filenames, document titles, chat names, screenshot captions, transcript excerpts, pasted quotes, and link labels. Rewrite them as `redacted - provide observable workplace behavior only`.
   - Do not translate hostile identity claims into coded, proxy, euphemistic, or "culture fit" language. If the user tries to replace a protected-class claim with a proxy label, redact it and ask for observable workplace behavior only.
   - Do not ask the user to preserve protected-class stereotypes, slurs, or group claims as "exact words" in the incident scaffold. Use `Protected-class generalization redacted; behavior-only facts pending`.
   - Do not retain hostile identity wording in ordinary work notes. Only if an authorized HR, legal, compliance, or formal investigation evidence owner later requires the original wording should it be stored separately as restricted evidence, outside ordinary incident notes and correction drafts.
   - Outbound record-existence requests are gated by concrete work context. Do not send any outreach until at least one concrete work forum, artifact, date, business process, or scheduled record exists.
   - When the concrete work context exists, the first outreach stays behavior-only and record-owner-only: "Please share the minutes/transcript/recap for [work item]" rather than any message naming identity groups or targeting a person.
   - If no concrete work forum, artifact, date, business process, or scheduled record exists, return only a private behavior-only note scaffold and explicitly say no outreach is supported yet.
   - Do not include a response deadline, record owner, or first-contact channel for no-context identity inputs. Those fields remain unavailable until a dated artifact or scheduled work record exists.

21. Make field-lock executable without overclaiming.
   Many defenses fail when every important field is `Pending`. You can be evidence-safe and still assign a role to complete fields.
   - If a record type is known, name the role accountable for field completion: deck owner, minutes owner, packet owner, review-system owner, release tracker owner, decision-log owner, manager, or meeting facilitator.
   - Use `Pending - [role] to confirm or redirect by [concrete trigger]` instead of bare `Pending`.
   - Do not leave the interim trigger pending. If no hardening time is known, use end of current business day. If a forum/send/lock date is known, use the earlier of end of current business day or two business hours before that event. If the event is within two hours, use 30 minutes.
   - The `## Draft` must include a silence default: if the accountable first responder does not confirm by the trigger, name who posts the neutral pending-status note and where it goes. If the user lacks access, the accountable first responder must forward or append it; if they stay silent, the user sends it to the narrowest packet/record owner available.
   - For audience parity, if the original audience is unknown, the first responder must post to the controlling artifact plus the best-known original thread and later forward or append to any later-discovered original recipients or derived records.
   - Keep execution, risk acceptance, approval, final record ownership, and delivery ownership pending unless sourced. The executable owner is only responsible for field completion, receipt, fallback posting, or route confirmation.
   - Do not dump the full owner matrix into `## Draft` as the first move when the user needs action. Lead with the minimum executable route: accountable first responder, controlling artifact, concrete trigger, neutral pending-status wording, fallback poster, and receipt requirement.
   - Put the larger owner matrix under `Completion checklist`. In the sendable text, include only owner fields needed to prevent the immediate record from hardening incorrectly.
   - If the first responder is silent, the fallback poster is the narrowest role with access to the controlling artifact. If that role is unknown, use the user only for a neutral pending-status note to the best-known official thread or packet/record owner.
   - A good field-lock draft should be short enough to send. Prefer 6 to 10 lines in `## Draft` plus a compact "Route fields" list over a long audit checklist.

22. Define the minimum success state by scenario family.
   A draft is not robust if it only asks for fields and never says what must be true before the record hardens. Put the minimum success state in `## Draft` for these cases:
   - Client/vendor late-blame: before client review, a timestamped pending-status note with the verified timeline must be in the controlling client deck or official review thread. Internal tracker updates alone are not enough. The receipt must show the same client-review audience or controlling artifact received it.
   - Calibration, layoff, or performance packet: the first line must frame the criterion question, such as `Criterion check required: original quarter goal versus documented goal change`. The packet must state whether the original goal, changed goal, or calibration rubric controls; a dashboard addendum alone is not enough.
   - Mixed-channel release or accountability: the first line must state the controlling status, such as `QA-skip approval not confirmed`. Post or link that status into any active accountability thread, release tracker, or decision log before assigning blame, approval, risk, or execution ownership.
   - Promotion or review contribution dilution: the reviewer-visible packet must include a candidate-linked sentence naming the concrete mechanisms and artifacts, while keeping team metrics non-exclusive. Use `work supported the team result through [design/artifact]`, not a generic `supported the team result` line without artifacts.
   - Meeting minutes or risk acceptance: the minutes correction must include transcript-supported decision/risk text and mark unsupported owner fields `Pending - [role] to confirm`; success requires the minutes owner receipt before minutes finalization.
   - Manager-credit/no-access leadership thread: success requires either same-audience leadership append or packet-accessible append with timestamped receipt. A private manager acknowledgement is not enough.
   - Side-channel or pre-wired decisions: success requires the current controlling decision record to be marked pending, superseded, or updated before the execution team acts. Chat alignment alone is not a decision record.
   - Invisible work or pressure-to-own: success requires a capacity, owner, or goals-record update before recurring work continues. A private "I can help" note is not enough.
   If the minimum success state cannot be reached before hardening, the fallback is a narrow neutral pending-status note in the controlling artifact or best-known official thread, using only verified facts and explicitly pending owner/evidence fields.

23. Run the v14 quality-tail closure ledger for high-frequency residuals.
   This is for agent-grade robustness. Do not shorten it away. A draft that merely asks for fields can still fail if the wrong record hardens first. Put a compact `Quality-tail closure ledger` in `## Recommended Action`, and put the case-specific minimum success sentence in `## Draft`.
   - Owner closure ledger: for every decision-critical `Pending` field, name the accountable first responder, concrete trigger, silence default, fallback poster, receipt owner, and whether the record must stay `pending`, `not controlling`, `superseded`, or `blocked from hardening` until the field is filled. Treat current-owner review as a condition of decision validity when the current owner controls source data, quality, risk, or execution feasibility.
   - Audience parity closure: if the original audience is unknown or inaccessible, the correction must either reach the same audience, or the controlling artifact must explicitly supersede the old framing and state why same-audience delivery is unavailable. A private manager reply, internal tracker, or packet note alone does not close audience parity when leadership, reviewers, clients, or execution teams received the old story.
   - Truth-record closure: the draft must say what old wording becomes `proposal`, `review`, `pending`, `incomplete`, `superseded`, or `not controlling`; who owns the source-of-truth update; and what receipt proves the old line no longer controls downstream decisions.
   - Material-evidence closure: map each important claim to one artifact/date/link. If a claim lacks an artifact, keep it in `Pending verification`; do not let a generic contribution or status sentence stand in for mechanism-level evidence.
   - Deadline-silence closure: if a record can harden before fields are complete, the draft must state the neutral pending-status note that posts by silence, the controlling artifact or best-known official thread it posts to, and the receipt required before the forum, send, lock, review, or recurring delivery.
   - Recurring invisible work: all critical fields must close together before recurring work continues: final send owner, source-data owner, backup owner, cadence/due time, time budget, displaced work, goals or contribution treatment, metrics audience, and fallback path. Do not write "capacity, owner, or goals update" as if one field is sufficient; require the complete recurring-work record or explicitly keep the work one-time support only.
   - Promotion contribution dilution: reviewer-visible wording must use owned verbs and mechanism-level evidence, not only "supported the team result." Require a claim-to-artifact map, one artifact/date/link per design, rollout, debugging, migration, or incident claim, and a receipt that anonymous team-only wording was appended, superseded, marked incomplete, or no longer controlling in the review packet.
   - Pre-wired ownership transfer: reclassify final-transfer wording as `proposal/review` until current-owner review, transition criteria, source-data quality gates, decision owners, risk owner, execution owner, and hold owner are documented. No owner-record change should proceed until the controlling decision log supersedes the pre-read or the same pre-read audience receives the pending-status correction.
   - Mixed-channel release or accountability: the controlling release/accountability record must state who determined the condition, the true approver, the QA or approval owner status, and the release owner's proceed/hold/mitigation decision before blame, approval, risk, or execution ownership is assigned.
   - Manager-credit/no-access leadership thread: require either same-thread leadership append, or a packet-accessible note that explicitly says the leadership thread is inaccessible and maps exact overlap between the user's dated artifact and the upward wording. Promotion protection is not enough if live leadership memory remains unchanged.
   - Calibration, layoff, or performance packet: require a reviewer-visible addendum with original goal, dashboard or metric line, workstream artifact-map status, and criterion decision. The adverse roadmap-only or anonymous summary must be marked incomplete, superseded, or weighed against the governing criterion before it controls.
   - Client/vendor late-blame: internal tracker updates do not close the route. The controlling client deck or official review thread must contain the verified timeline, deadline status, remediation/delivery owner split, review-disposition or risk owner, and same-client-review receipt before the client review.
   - If the draft cannot satisfy the relevant family closure, switch to field-lock mode and explicitly say the current record must remain pending or not controlling until the closure ledger is complete.

## Output Format

Use this structure:

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
Response mode:
First-pass note:
Completion checklist:
Field-completion owner:
Interim deadline lookup trigger:
Temporary execution default:
Leak closure:
Stakeholder path:
- Hardening forum:
- Record owner:
- Required audience:
- Deadline:
- First channel:
- Fallback channel:
- Source-of-truth record:
- Current source of truth:
- Obsolete or superseded wording:
- Corrected wording that supersedes it:
- Correction owner:
- Evidence packet:
  - Exact current wording:
  - Source proof:
  - Artifact/date/link:
  - Accessible to the record owner:
- Owner matrix:
  - Accountable first responder:
  - Record owner:
  - Decision/approval owner:
  - Evidence owner:
  - Risk owner:
  - Execution owner:
  - Hold owner:
  - Fallback poster:
- Red-team closure gate:
  - Same-audience receipt:
  - Fallback validity proof:
  - Concrete deadline or deadline lookup:
  - Evidence packet completeness:
  - Truth-record supersession receipt:
  - Owner matrix completion:
  - Existing-record gate:
  - Verified-now versus pending-verification split:
  - Temporary fallback poster:
  - Temporary receipt owner:
  - Reconciliation checklist:
- Draft-embedded closure capsule:
  - Current visible wording:
  - Source proof and artifact/date/link:
  - Same-audience or controlling-record append:
  - Derived-record sweep:
  - External/direct thread check:
  - Non-user owner split:
  - Timestamped receipt:
- Evidence-boundary check:
  - Non-exclusive metric wording:
  - Transcript-bound owner wording:
  - Verified/inference/pending split:
  - Record-existence deadline:
  - Materiality threshold:
- Quality-tail closure ledger:
  - Decision-critical pending fields:
  - Accountable first responder and trigger:
  - Silence default and fallback poster:
  - Same-audience or controlling-artifact supersession:
  - Old wording disposition:
  - Claim-to-artifact map:
  - Deadline-silence pending-status note:
  - Case-family closure condition:

## Draft

[ready-to-send text]
```

If stakeholder path is relevant, the draft itself must contain this kind of sentence:

```text
Because this will be used in [hardening forum], can you confirm by [deadline] whether [record owner] will update [record] and share it with [required audience]? If not, I can send a neutral recap on [fallback channel] with [artifact/date] so the record is accurate before [forum].
```

For deadline-critical records, use a default fallback instead of asking for permission to protect the record under silence:

```text
If [record] is not corrected by [deadline], I will place a neutral addendum in [controlling artifact/fallback channel] with [artifact/date] so the decision record is accurate before [forum].
```

When owner roles are ambiguous, the draft itself must include an owner matrix:

```text
To avoid ambiguity, can we record these owners before [forum/deadline]?

- Record owner:
- Decision/approval owner:
- Evidence owner:
- Risk owner:
- Execution owner:
- Hold owner if unresolved:
- Fallback poster if the record is not updated:
```

For stress-test trace cases, the draft itself must include a fill-before-send gate. Do not send a corrective claim while required artifact details are unknown:

```text
Before I send the correction, I need to fill these fields so the record is accurate. Until these are filled, I am treating this as a field-lock request, not a correction claim.

- Original audience/distribution list:
- Controlling artifact and record owner:
- Exact current wording in the record:
- Source proof with artifact/date/link:
- Packet/deck/minutes/tracker lock time:
- Correction audience and confirmation receipt owner:
- Owner matrix roles still missing:
- Field-completion owner:
- Interim deadline lookup trigger:
- Derived records that must receive or reflect the fallback:
- Timestamped receipt owner:

If these cannot be confirmed before [hardening time], I will place a neutral pending-status addendum in [fallback channel] stating only the verified facts and open owner/evidence fields.
```

When material evidence is incomplete, use a verified-now split so unsupported facts do not become claims:

```text
Verified now:
- [fact + source]

Pending verification before any correction claim:
- [artifact/date/link], owned by [field-completion owner] by [interim trigger]
- [audience/record/deadline], owned by [field-completion owner] by [interim trigger]

If the pending fields are not confirmed by [interim trigger], I will post only a neutral pending-status note in [controlling artifact/fallback channel], not a full correction.
```

For first-pass execution, keep the initial artifact short and put the full matrix after it:

```text
First-pass note:
This is a [field-lock/evidence-collection/record-existence] request, not a final correction claim.
Verified now: [1-3 concrete facts].
Please confirm [missing record/audience/deadline/owner] by [interim trigger].
If no one confirms by then, [temporary fallback poster] will post a neutral pending-status note in [official thread/controlling artifact] as a record-accuracy action only.
That temporary post does not create execution, approval, risk, source-data, recurring-work, or final-owner responsibility.
After posting, [temporary receipt owner] will capture timestamped receipt and run the reconciliation checklist.

Completion checklist:
[full owner matrix, evidence packet, derived records, fallback validity proof, supersession marker, and reconciliation checklist]
```

For reconciliation, use a table or compact list:

```text
Reconciliation checklist:
- [record/thread/packet]: updated/appended/pending/superseded/not controlling/inaccessible with reason/not applicable
```

When a wrong record already exists, include a supersession receipt line:

```text
Please confirm that the corrected wording has replaced, marked incomplete, or superseded the old wording in [source-of-truth record], and that the same audience or controlling artifact now sees the corrected version.
```

When a fallback is needed, include a fallback validity proof line:

```text
For the fallback to be valid, [receipt owner] must provide a timestamped receipt before [hardening event] showing the pending-status note reached [original audience/best-known original thread] and was posted, forwarded, appended, or reflected in [derived records]. The old wording must be replaced, marked incomplete, marked pending, marked superseded, or marked not controlling; the addendum should not coexist with an unchanged decision, approval, owner, contribution, blame, or launch-status line that still carries the old meaning.
```

When the case can affect an external audience, launch send, leadership credit signal, review packet, or client-facing record, include this conditional Draft-embedded closure capsule in the sendable text. Keep it evidence-bound:

```text
To close the record route, please confirm or update these before [hardening event]:

- Current visible wording: [exact wording] in [record/thread/artifact].
- Source proof: [dated source facts] plus [artifact/date/link still needed].
- Same-audience or controlling-record append: send/post/append the corrected or pending-status wording to [original audience] and [controlling record].
- Derived-record sweep: check [deck/minutes/agenda/tracker/packet/scheduled send/customer announcement/campaign copy/leadership thread/review record/recap] and mark each updated, appended, pending, superseded, not controlling, inaccessible with reason, or not applicable.
- External/direct thread check: confirm whether any separate client/vendor/partner/regional/leadership thread already carried the old framing; do not send to that thread unless a wrong durable record is verified or imminent.
- Owner split: I can provide evidence. Please confirm [execution owner], [approval owner], [risk owner], [send or hold owner], and [record owner]. Any owner not proven by the artifact remains pending.
- Receipt: [receipt owner] will provide timestamped proof before [hardening event] that the old wording was replaced, marked incomplete, marked pending, superseded, or marked not controlling.
```

For team-level promotion metrics, use non-exclusive contribution wording:

```text
Suggested reviewer-visible wording:
"For the team result of [metric improved by Y%], [candidate/user]'s work supported the team result through [verified mechanism], including [artifact/date/link]. The packet should not imply sole causality unless the source record supports it."
```

For transcript-bound minutes corrections, do not add unproven owners:

```text
Correction requested:
"Decision: [verified decision]. Risk noted: [transcript-supported risk]. Risk acceptance: [person/role] said '[exact quote]'. Execution owner: Pending - launch owner/minutes owner to confirm if a separate source names it."
```

For hostile or retaliation inputs with weak evidence, use record-owner-only first contact:

```text
This is a behavior-only record-existence request, not a complaint or correction claim. Please share the minutes, transcript, chat, recording, or action-item recap for [work item] by [deadline]. Until a material record error or decision/owner/risk/deadline impact is verified, I will not send a leadership note, HR note, broad distribution, competence claim, identity-based claim, or target-facing message.
```

For hostile identity inputs, sanitize the scaffold before asking for facts:

```text
Private behavior-only note:
- Protected-class generalization: redacted from working notes.
- Work forum/date:
- Observable behavior or record change: identity categories, group generalizations, motive claims, and retaliation goals are not valid entries; rewrite as `redacted - provide observable workplace behavior only`.
- Proxy wording: coded, euphemistic, culture-fit, region, accent, school, visa, caste, nationality, or other proxy labels are not valid substitutes for behavior; rewrite as `redacted - provide observable workplace behavior only`.
- Artifact, minutes, transcript, chat, email, ticket, deck, review packet, or recap:
- Decision/owner/risk/deadline/performance impact:
- Record owner to request source from: unavailable until a concrete work forum, artifact, date, business process, or scheduled record exists.
- Response deadline: unavailable until a concrete dated record or hardening event exists.

No outreach is supported yet unless a concrete work forum, artifact, date, business process, or scheduled record exists. Exact identity-based wording is not needed for ordinary credit, owner, decision, or record correction. Do not retain hostile identity wording now; only if an authorized HR, legal, compliance, or formal investigation evidence owner later requires the original wording should it be stored separately as restricted evidence, outside ordinary incident notes and correction drafts.
```

For mixed-channel decision records, preserve conditional wording:

```text
Verified now:
- [Person] wrote: "[exact conditional wording]."
- [Approver/QA/owner] wrote: "[exact source wording]."
- Formal approval record: Pending - [decision-record owner] to confirm.

Suggested record wording:
"[Exact conditional instruction] was posted in [channel]. Formal approval, risk acceptance, release decision, and hold authority remain pending until [true approver/decision owner] confirms in writing."
```

For contribution-map cases, separate plan ownership from delivery:

```text
Verified now:
- The project plan lists me as owner for [subitems].
- Completion state, outcome, artifact links, and controlling-record owner are Pending - [record owner/evidence owner] to confirm.

Suggested record wording:
"The plan lists [candidate/user] as owner for [subitems]. Please link the artifact/date/completion state/outcome for each item before the summary or packet describes completed delivery or migration success."
```

For manager-credit or no-access leadership threads, avoid sole-source claims:

```text
Suggested attribution note:
"My dated draft contains the churn segmentation and Team A recommendation, including [verified mechanism]. Please append or forward this artifact-backed contribution detail to the same leadership audience or packet owner and send a timestamped receipt."
```

For publish-status or standup credit, scope ownership to the artifacts:

```text
Posting the artifact links for today's status:
- Commit/design note links:
- Work reflected in those artifacts:
- Recap line requested: "[candidate/user] posted artifact links for [scoped work]."

Please keep any standup recap tied to those artifact links, or send the recap by [deadline] so the notes owner can verify it before any correction request.
```

For executable field-lock, make one role accountable for completing unknowns:

```text
Please confirm or redirect these record-route fields by [concrete trigger]:
- Accountable first responder: [record owner/manager/meeting facilitator/packet owner].
- Record owner:
- Original audience or best-known thread:
- Controlling artifact:
- Hardening time:
- Receipt owner:

If I do not receive confirmation by [concrete trigger], [fallback poster] will post the neutral pending-status note to [controlling artifact/best-known official thread]. This is only a record-accuracy action and does not assign execution, approval, risk, delivery, or final-owner responsibility.
```

For v14 quality-tail closure, add a compact ledger when a high-frequency residual is likely:

```text
Quality-tail closure ledger:
- Decision-critical pending fields: [fields]. Until these are filled, [record] remains pending/not controlling and no [owner transfer/review conclusion/blame assignment/recurring ownership/client framing] should harden.
- Accountable first responder and trigger: [role] to confirm or redirect by [time].
- Silence default: if no confirmation by [time], [fallback poster] posts "[neutral pending-status note]" to [controlling artifact/best-known official thread].
- Same-audience or supersession: [same audience] receives the correction, or [controlling artifact] explicitly supersedes [old wording] and records why the original audience is unavailable.
- Claim-to-artifact map: [claim] -> [artifact/date/link]; unsupported claims stay pending.
- Receipt: [receipt owner] provides timestamped proof before [hardening event].
```

## Default Templates

### Confirm Decision

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

### Correct Credit

```text
Thanks for summarizing this. To make the ownership clear:

- [Person A] led [part A].
- I handled [part B], including [artifact/result].
- [Person C] is owning [part C].

The next decision is [decision], and the open risk is [risk].
```

### Standup Protection

```text
Yesterday I completed [artifact/result]. Today I am working on [next step].
The current blocker is [dependency], owned by [owner], with expected update by [date].
I will share [artifact/link] after standup so the status is visible.
```

### Assistance Boundary

```text
I can help review [specific part] and share suggestions by [date].
To keep ownership clear, [owner] remains responsible for final implementation, validation, and sign-off.
```

### Escalation

```text
Subject: Project Escalation: [Project] - [Issue] - Decision Needed by [Date]

Current status:
Impact if unresolved:
What has already been tried:
Options:
Recommended option:
Decision needed:
Owner after decision:
```

### Meeting-Minutes Correction

```text
Subject: Correction to meeting notes for [project/date]

Thanks for sending the notes. One correction for accuracy:

Item:
Current note:
Correction:
Owner:
Due date:
Evidence/link:
Impact if left unchanged:

Please reply by [date/time] if this correction does not match your understanding.
```

### Contribution Map

```text
For clarity on ownership:

- [Artifact/result]:
  - Owner:
  - Contributors:
  - Evidence/link:
  - Decision or next step:

Open risk:
Decision needed:
```

### Truthful Approval Record

```text
Subject: Confirming approval status for [decision/change]

Hi [Name],

I cannot state that [approver/team] is aligned or approved unless we have that approval in writing.

Current accurate status:
- Discussion happened: [yes/no/date]
- Approval status: pending
- Approver/sign-off owner: [name/team]
- Open question: [question]
- Decision needed by: [date/time]

Suggested wording:
"[Approver/team] review is pending. We discussed [topic], and [approver/team] requested [open item]. We will treat this as unapproved until [approver/team] confirms approval or final comments in writing."

If approval already exists, please forward the dated approval or ask [approver] to confirm on this thread so the record is accurate.
```

### Stakeholder Path Patch

```text
Before [meeting/review/release/calibration], I want to make sure the decision record is accurate for [audience/forum].

Record to correct:
Current risk:
Accurate timeline:
Owner/sign-off:
Evidence:
Decision needed:
Please confirm by:
```

### Visible Record Route

Use when a private correction is not enough because credit, blame, ownership, or approval status will harden in a visible record.

```text
Stakeholder path:
- Hardening forum: [specific deck/recap/review packet/minutes/status thread]
- Record owner: [name/role that edits that record]
- Required audience: [decision maker/reviewer/client lead/approver]
- Deadline: [before meeting/review/calibration/launch/date]
- First channel: [reply to record owner / manager note with record owner copied / project thread]
- Fallback channel: [neutral recap to the official thread / correction in meeting notes / manager escalation]
- Controlling artifact: [agenda/decision log/packet/tracker/review-system entry that must carry the correction]
```

Ready-to-send line:

```text
Because this will be used in [forum], can you confirm by [date/time] whether [record owner] will update [record] with the wording below? If not, I can send the neutral recap on the official thread so the record is accurate before [forum].
```

Deadline-critical fallback:

```text
If [record] is not corrected by [date/time], I will place a neutral addendum in [controlling artifact] with [artifact/date/link] before [forum/packet lock/branch close].
```

Audience parity line:

```text
Please send the corrected version to the same audience that received the pre-read/update, including [audience], so the old framing does not remain the only visible record.
```

### Source-Of-Truth Correction

Use when an old, false, or overstated record may be treated as final.

```text
Current source of truth: [tracker/packet/agenda/decision log/approval tracker]
Obsolete or superseded wording: "[exact current wording]"
Corrected wording: "[accurate wording]"
Correction owner: [record owner]
True approver: [person/team]
Approval status: pending
Required decision owners: [owner list]

Please update [source-of-truth record] so the corrected wording supersedes the obsolete or superseded wording above. The decision remains pending until the required decision owners and true approver confirm in writing.
```

Ready-to-send line:

```text
Please do not imply approval or final alignment until [true approver] confirms in writing. If [source-of-truth record] is not corrected by [deadline], I will place a neutral addendum in [fallback channel] so the current source of truth is accurate before [forum].
```

### Evidence Packet Addendum

Use when the record ignores concrete materials or the record owner needs proof attached.

```text
Evidence packet:
- Exact current wording: "[quote]"
- Source proof: [artifact/date/link]
- Supporting evidence: [metric/transcript/ticket/date/link]
- Requested replacement or qualification: "[wording]"
- Accessible to the record owner: [yes/no/link or attachment path]

Please confirm when this has been posted, forwarded, or appended to [controlling artifact]. If I do not have access to the original thread, please use the no-access route through [manager/packet owner] and send a confirmation receipt once the packet-accessible record is updated.
```

### Durable Credit Route

Use when a manager, recap, packet, or slide omits the user's contribution.

```text
To keep the visible record accurate before [review/recap date], can you confirm whether [record owner] will add this contribution detail to [record]?

- Artifact/date:
- Contribution:
- Result:
- Presented by:

If the record will not be updated by [deadline], I can send the neutral recap on [official thread] with the artifact link.
```

### Owner Responsibility Matrix

Use when the record owner, approver, evidence owner, risk owner, and execution owner may be different people.

```text
To avoid ambiguity before [forum/deadline], can we record these owners in [record]?

- Record owner:
- Decision/approval owner:
- Evidence owner:
- Risk owner:
- Execution owner:
- Hold owner if unresolved:
- Fallback poster if [record] is not updated:
```

Decision-readiness line:

```text
Please keep [record] marked as pending until the owner matrix above is complete and [approver] confirms the decision status in writing.
```

## Reference Map

Read `references/defense_playbook.md` for common defense plays. If available, use the repository-level `references/behavior_taxonomy.md` and `references/source_notes.csv` as evidence background.
