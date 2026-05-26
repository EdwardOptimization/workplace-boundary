# Boundary Defense Playbook

Use the least escalatory move that protects the user's evidence and boundary.

## Protect Credit

Use when someone reports, summarizes, or presents your work as theirs.

Moves:

- Publish your own progress early.
- Attach artifacts.
- Name contributors and owners.
- Correct omissions neutrally.

Script:

```text
To add the contribution detail: I completed [artifact/result], [Name] handled [part], and [Name] owns [next part].
```

## Prevent Blame Shifting

Use when risk, delay, or failure may be assigned to the wrong person.

Moves:

- Record blocker date.
- Name dependency owner.
- State impact if unresolved.
- Ask for decision or support.

Script:

```text
Current blocker is [X], owned by [Y]. If unresolved by [date], [impact] occurs. Please confirm whether we should [option A] or [option B].
```

## Clarify Owner

Use when "help", "support", or "alignment" is hiding responsibility.

Moves:

- Convert vague request to deliverable.
- Ask who owns final sign-off.
- Set deadline and acceptance criteria.

Script:

```text
I can support [specific task]. Who owns final delivery and sign-off, and what is the acceptance criterion?
```

## Correct Meeting Minutes

Use when minutes omit contribution, distort a decision, or assign wrong ownership.

Moves:

- Reply quickly.
- Keep tone factual.
- Use a small correction table.

Script:

```text
Thanks for sending the notes. One correction for accuracy:

Item:
Current note:
Correction:
Owner:
Due date:
Evidence/link:
```

## Build A Contribution Log

Use for long-running projects, promotions, or politically noisy work.

Fields:

- Date
- Artifact
- Decision or result
- Your contribution
- Other owners
- Stakeholders informed
- Link/evidence

## Close Defense Leaks

Before finalizing a draft, check:

- Credit: Is the contribution connected to a named artifact or result?
- Owner: Is final owner/sign-off owner explicit?
- Deadline: Is there a date or correction window?
- Evidence: Is there a link, ticket, transcript, commit, or written note?
- Record: Does the response correct the official record if the official record is wrong?
- Stakeholder: Will the right audience see the correction before the wrong narrative hardens?
- Escalation: Does the user know when to escalate?
- Truth record: If someone asked for false approval/alignment language, does the draft replace it with accurate pending-review wording?
- Materials: Did the draft use the specific email/chat/transcript/review details already available?
- Source-of-truth record: Does the draft say which record is the current source of truth and which obsolete or superseded wording is replaced?
- Evidence packet: Does the draft include exact current wording, source proof, artifact/date/link, and evidence accessible to the record owner?

If any answer is no, patch the draft before returning it.

For v0.4 residual leaks, use these extra rules:

- A truth-record correction must name the source-of-truth owner, decision-record owner, correction owner, true approver, approval status: pending when approval is missing, and the wording that supersedes obsolete or superseded wording.
- A material-evidence correction must attach an evidence packet with exact current wording, source proof, artifact/date/link, and confirmation that the proof is accessible to the record owner.
- A no-access route must ask the manager or packet owner to confirm whether the correction was posted, forwarded, or appended, and must request a confirmation receipt for the packet-accessible record.

For stress-test residual leaks, use a stricter fill-before-send gate:

- `audience_parity_leak`: require original audience, correction audience, controlling artifact, and same-audience receipt. If the original distribution is unknown, first request the distribution list or record-export audience.
- `deadline_silence_leak`: require a concrete timestamp tied to packet lock, deck export, meeting start, launch send, tracker lock, or review cutoff. If the timestamp is unknown, make deadline lookup the immediate action before any silence fallback.
- `material_leak`: require exact current wording, source proof, artifact/date/link, record-owner accessibility, and proof-access confirmation. If links or dates are unknown, make evidence collection the immediate action.
- `truth_record_leak`: require old wording, corrected wording, source-of-truth record, decision-record owner, correction owner, true approver, approval or pending status, and a receipt that the old wording was replaced, marked incomplete, or superseded.
- `unclear_owner`: require named role owners for record, decision/approval, evidence, risk, execution, hold, and fallback posting. Do not collapse these into one generic "owner."
- Memory-only cases: do not start with a correction request if no wrong durable record exists. First request the source record, transcript, recap, or minutes; correct only after verifying the record is wrong.

For v0.5 real-run residual leaks, the sendable draft needs a compact closure capsule. Do not leave these fields only in analysis:

- Draft-embedded closure capsule: current visible wording, source proof with artifact/date/link, same-audience or controlling-record append, derived-record sweep, external/direct thread check, non-user owner split, and timestamped receipt.
- Vendor late-blame: check the client deck, pre-read, risk log, minutes, recap, delivery tracker, and any separate vendor-client direct thread. The project manager can own evidence/timeline only; vendor delivery/remediation, review disposition, risk acceptance, and final client record have separate owners.
- Approval-pending launch: check launch email, approval tracker, scheduled customer announcement, scheduled send copy, send checklist, campaign copy, launch thread, and customer-facing approval path. Name the send owner or hold owner with authority to pause the send.
- Manager-credit or promotion credit: split private manager ask, same-audience leadership append, and packet-owner fallback. Include artifact link/date, original leadership audience, derived record list, and a candidate-linked contribution sentence suitable for review or promotion materials.
- Invisible-work or pressure-to-own cases: state that the user can provide evidence or a temporary record-accuracy note, but recurring execution, risk acceptance, approval, send/hold authority, source-data ownership, and final record ownership stay with the responsible owner unless delegated in writing.

For v0.6 evidence-boundary failures, the draft must not overclaim while closing leaks:

- Non-exclusive metrics: if the source says "team improved X by Y%", write that the candidate contributed to the team result through verified mechanisms and artifacts. Do not write that the candidate alone improved the metric unless the source proves sole causality.
- Transcript-bound minutes: only include decision, risk, quote, and owner fields that are directly supported by transcript, minutes, or source artifacts. If execution owner, risk owner, approval owner, or final owner is not sourced, mark it `Pending - [role] to confirm`.
- Hostile or retaliation requests with weak evidence: refuse the retaliatory aim, make a private incident-note scaffold, and send the first request only to the meeting owner, notes owner, or record owner. Do not include leadership, HR, broad distribution, or the target person until a material record error or decision/owner/risk/deadline impact is verified.
- Record-existence deadline: every record-existence or evidence-collection draft must include a concrete response deadline tied to minutes finalization, packet lock, decision forum, or end of current business day.
- Materiality threshold: escalate only for a verified false official record, repeated documented misstatement, or material impact on owner, decision, action item, risk, deadline, performance, or review packet.

For v0.7 real-subagent guardrail failures, apply the evidence-safe wording contract:

- Vendor late-blame: write "no questions were raised in the available thread by the Friday deadline" when supported. Do not write "before the Friday question window." The draft must request same-audience route, review deadline, record owner, fallback poster, and receipt owner from the client-review record owner.
- Calibration or layoff packet: ask whether a documented goal change made roadmap output or another criterion controlling. Do not say "my work reduced X" unless an artifact map ties dated work to the metric. Use "dashboard shows X; artifact map for the contribution is pending/attached."
- Mixed-channel decisions: quote conditional chat instructions verbatim. Do not turn "if needed," "can," "let's," or "sounds fine" into "allowed," "approved," "signed off," or "decided" unless a formal approval record exists. Approval status stays pending until the true approver confirms.
- Publish-status or standup credit: scope ownership to artifact-linked work. Do not write "I own the current work" unless the source proves full workstream ownership. Ask the standup facilitator or notes owner to confirm the recap line.
- Contribution split across small tasks: distinguish plan ownership from completed delivery. A project plan proves planned owner fields, not delivery, success, dates, or outcomes. Require artifact link, date, completion state, outcome, and controlling-record owner before using delivery wording.
- Promotion or team metrics: write "work supporting the team's metric result" unless a performance-analysis record proves direct metric causality. Require packet owner, packet lock time, reviewer/calibration audience, and same-audience receipt.
- Manager-credit or leadership attribution: use "my dated draft contains..." or "the source artifact includes..." instead of "came from my draft" unless the full thread and source history prove sole source. If the user lacks leadership-thread access, require timestamped same-audience receipt or packet-accessible append.

For v0.8 identity and execution residuals:

- Hostile identity input: sanitize before collecting facts. Do not carry nationality, race, ethnicity, gender, caste, religion, disability, age, or other protected-class generalizations into ordinary incident notes, record-correction drafts, or outreach.
- Behavior-only scaffold: ask for work forum/date, observable behavior or record change, artifact/record, decision/owner/risk/deadline/performance impact, record owner, and response deadline.
- Field-level identity stripping: every user-supplied field value and metadata field rejects identity categories, group generalizations, slurs, stereotype claims, motive claims based on identity, and retaliation goals. This includes URLs, filenames, document titles, chat names, screenshot captions, transcript excerpts, pasted quotes, and link labels. Rewrite them as `redacted - provide observable workplace behavior only`.
- Proxy-language ban: do not translate hostile identity claims into coded, proxy, euphemistic, or "culture fit" language. If the user replaces a protected-class claim with a proxy label, redact it and ask for observable workplace behavior only.
- Redaction rule: write `Protected-class generalization redacted; behavior-only facts pending` instead of preserving slurs, stereotypes, or group claims as "exact words." Do not retain hostile identity wording in ordinary work notes. Only if an authorized HR, legal, compliance, or formal investigation evidence owner later requires the original wording should it be stored separately as restricted evidence, outside ordinary incident notes and correction drafts.
- Outbound gate: do not send a record-existence request until at least one concrete work forum, artifact, date, business process, or scheduled record exists.
- Record-owner-only first contact: when concrete work context exists, the first outreach asks the meeting owner, notes owner, or record owner for minutes/transcript/recap for the work item; it does not name identity groups, target a person, or send broad distribution.
- No-context default: if no concrete work forum, artifact, date, business process, or scheduled record exists, produce only a private behavior-only scaffold and explicitly say no outreach is supported yet.
- No-context unavailable fields: do not include a response deadline, record owner, or first-contact channel until a dated artifact or scheduled work record exists.
- Executable field-lock: when a record type is known, make a role accountable for completing unknowns, such as deck owner, minutes owner, packet owner, review-system owner, release tracker owner, decision-log owner, manager, or meeting facilitator.
- Concrete trigger: do not leave the interim trigger pending. If no hardening time is known, use end of current business day. If a forum/send/lock date is known, use the earlier of end of current business day or two business hours before that event. If the event is within two hours, use 30 minutes.
- Silence default: the draft must name who posts the neutral pending-status note and where it goes. If the user lacks access, the accountable first responder must append/forward it; if they stay silent, the user sends it to the narrowest available packet or record owner.
- Audience substitute: if the original audience is unknown, use the controlling artifact plus best-known official thread, then require forwarding or appending to later-discovered original recipients or derived records.
- Minimum executable route: do not dump the full owner matrix into the sendable draft as the first move. Lead with accountable first responder, controlling artifact, concrete trigger, neutral pending-status wording, fallback poster, and receipt requirement.
- Completion checklist split: put the large owner/evidence/derived-record checklist after the sendable first-pass note. In the sendable text, include only owner fields needed to prevent the immediate record from hardening incorrectly.
- Short-sendable rule: a good field-lock draft should be short enough to send, usually 6 to 10 lines plus compact route fields.

For v0.12 quality residuals, put the minimum success state in the sendable draft:

- Client/vendor late-blame: before client review, a timestamped pending-status note with the verified timeline must be in the controlling client deck or official review thread. Internal tracker updates alone are not enough.
- Calibration, layoff, or performance packet: lead with `Criterion check required: original quarter goal versus documented goal change`. The packet must state whether the original goal, changed goal, or calibration rubric controls.
- Mixed-channel release or accountability: lead with `QA-skip approval not confirmed` or the equivalent controlling status. Post or link that status into the active accountability thread, release tracker, or decision log.
- Promotion or review contribution dilution: the reviewer-visible packet must include a candidate-linked sentence naming concrete mechanisms and artifacts while keeping team metrics non-exclusive.
- Meeting minutes or risk acceptance: the correction must use transcript-supported decision/risk text and keep unsupported owner fields pending; success requires minutes-owner receipt before finalization.
- Manager-credit/no-access leadership thread: success requires a same-audience leadership append or packet-accessible append with timestamped receipt. A private manager acknowledgement is not enough.
- Side-channel or pre-wired decisions: the current controlling decision record must be marked pending, superseded, or updated before the execution team acts.
- Invisible work or pressure-to-own: recurring work should not continue without a capacity, owner, or goals-record update.

## Stress-Test Closure Modes

Choose a mode before drafting. This prevents a defense from sounding decisive while the record route is still unfinished.

### Field-Lock Request Mode

Use when audience, deadline, record owner, confirmation receipt owner, or owner matrix fields are missing.

Rules:

- State that this is a field-lock request, not a correction claim.
- Name the field-completion owner: the record owner, meeting owner, packet owner, manager, or other role accountable for filling missing fields.
- Name a confirmation receipt owner for same-audience proof.
- Put every unknown field in the form `Pending - [specific role] to fill by [timebox]`.
- Do not default missing owner roles to the user unless the user controls that record or has explicit update authority.
- Include an interim deadline lookup trigger. If a forum or send date exists, use the earlier of end of current business day or two business hours before the forum/send. If the forum/send is within two business hours, request confirmation within 30 minutes.
- If the interim trigger passes without confirmation, the fallback is a neutral pending-status note in the controlling artifact or official thread using only verified facts and open fields.
- Fallback validity proof is required: the receipt owner must prove the fallback reached the original audience or best-known original thread and every derived record that can still carry the old wording.

### Evidence-Collection Mode

Use when the scenario has facts but the packet is missing links, dates, transcript excerpts, source proof, access confirmation, or current exact wording.

Rules:

- Split `Verified now` from `Pending verification`.
- A verified item needs a source, such as chat excerpt, email line, transcript excerpt, ticket, commit, metric record, or meeting note.
- A pending item needs an owner and timebox.
- Do not assert unsupported conclusions.
- Do not make the correction claim until the evidence packet is complete, unless the hardening event is imminent; in that case post only a neutral pending-status note.

### Formal Correction Mode

Use only when these fields are complete or the draft is explicitly a pending-status addendum:

- controlling artifact;
- original audience and correction audience;
- hardening deadline;
- exact current wording;
- source proof with artifact/date/link;
- source-of-truth record;
- owner matrix;
- same-audience receipt owner;
- fallback poster;
- hold owner.

If any field remains unknown, formal correction mode is too strong.

### Fallback Validity Proof

A fallback is not valid just because it is neutral or posted somewhere official. It must close the old audience path and the old record path.

Rules:

- Same-audience-or-derived-record proof: the fallback must reach the original audience and every controlling or derived record that can carry the old wording, such as agenda, minutes, recap, decision log, risk log, packet, review-system entry, launch tracker, status packet, recurring task, send template, leadership thread, promotion packet, or calibration note.
- Timestamped receipt: name a receipt owner and require a timestamped receipt before the hardening event.
- Supersession marker: the old sentence or implication must be replaced, marked incomplete, marked pending, marked superseded, or marked not controlling.
- No coexisting contradiction: a correction addendum must not coexist with an unchanged decision label, approval line, owner field, contribution sentence, blame sentence, or launch-status sentence that still carries the old meaning.
- Unknown original audience: send to the controlling artifact and best-known original thread, then require the receipt owner to forward or append to later-discovered original recipients or derived records.
- Promotion and performance cases: pending-status wording must preserve the candidate-linked or person-linked contribution under review instead of reducing it to generic "details pending" wording.

Fallback validity script:

```text
For this fallback to be valid, [receipt owner] needs to provide a timestamped receipt before [hardening event] showing the pending-status note reached [original audience/best-known original thread] and was posted, forwarded, appended, or reflected in [derived records]. The old wording must be replaced, marked incomplete, marked pending, marked superseded, or marked not controlling. The fallback should not coexist with an unchanged decision, approval, owner, contribution, blame, or launch-status line that still carries the old meaning.
```

### Minimum Protective Act

Do not make the first message carry the whole checklist when the record is unverified, the deadline is close, or the user only needs to stop hardening. Split the artifact into:

- `First-pass note`: the shortest message that locks the record route.
- `Completion checklist`: the full owner/evidence/fallback/reconciliation matrix.

First-pass rules:

- Use 5 to 8 concise bullets or short paragraphs.
- State that this is a field-lock, evidence-collection, or record-existence request, not a final correction claim.
- Include only verified facts and the immediate missing fields.
- Name the interim trigger.
- Name the temporary execution default if no owner accepts before the trigger.
- State that a temporary fallback post is a record-accuracy action only and does not create execution, approval, risk, source-data, recurring-work, or final-owner responsibility.
- Put the full matrix after the first-pass note under `Completion checklist`.

Temporary execution defaults:

- Accountable first responder: the role asked to accept field completion, fallback posting, or receipt ownership by the interim trigger.
- Temporary fallback poster: the narrowest role with access to the official thread or controlling artifact. The user can be temporary fallback poster only for a neutral record-accuracy note.
- Temporary receipt owner: if nobody accepts receipt ownership by the interim trigger, the accountable first responder captures timestamp and follows up until the permanent record owner is identified.
- Owner acceptance line: ask the first responder to accept or redirect ownership by the interim trigger; silence activates the temporary execution default.

Memory-only or no-durable-record cases:

- First pass is only a record-existence check to the least necessary owner.
- Do not send the full owner matrix until a wrong durable record, recap, transcript, packet, or meeting note exists or is about to be created.
- Ask for the source record and a timestamped copy before correction language.

Reconciliation checklist:

```text
After the correction or pending-status fallback, mark each record:

- [record/thread/packet]: updated/appended/pending/superseded/not controlling/inaccessible with reason/not applicable
```

First-pass script:

```text
This is a [field-lock/evidence-collection/record-existence] request, not a final correction claim.

Verified now:
- [fact + source]

Please confirm [missing record/audience/deadline/owner] by [interim trigger].

If no one confirms by then, [temporary fallback poster] will post a neutral pending-status note in [official thread/controlling artifact] as a record-accuracy action only. That temporary post does not create execution, approval, risk, source-data, recurring-work, or final-owner responsibility.

After posting, [temporary receipt owner] will capture timestamped receipt and run the reconciliation checklist.
```

Field-lock script:

```text
This is a field-lock request, not a correction claim yet. Before [forum/send/packet lock], please confirm the missing fields below so the record route is clear:

- Field-completion owner:
- Confirmation receipt owner:
- Original audience/distribution list:
- Correction audience:
- Controlling artifact:
- Record owner:
- Exact current wording:
- Source proof with artifact/date/link:
- Hardening deadline:
- Owner matrix fields still pending:
- Derived records that must receive or reflect any fallback:
- Timestamped receipt owner:
- Temporary fallback poster:
- Temporary receipt owner:
- Reconciliation checklist owner:

Please confirm these by [interim trigger]. If the fields are not confirmed by then and the record may harden, I will post a neutral pending-status note in [controlling artifact/official thread] with only verified facts and open owner/evidence fields.
```

Verified-now script:

```text
Verified now:
- [fact] from [source/artifact].

Pending verification before any correction claim:
- [missing artifact/date/link], owned by [field-completion owner] by [interim trigger].
- [missing audience/deadline/record owner], owned by [field-completion owner] by [interim trigger].

Until these are confirmed, the source-of-truth wording should stay pending rather than assigning ownership, approval, blame, or credit.
```

## Map The Stakeholder Path

Many defenses fail because they correct facts in the wrong place. Always identify:

- Forum: meeting, client review, calibration, release thread, board deck, QBR, project doc.
- Record owner: person who controls the minutes, deck, ticket, review packet, or decision log.
- Audience: people who will make or remember the decision.
- Deadline: when the narrative becomes hard to correct.
- Channel: the least escalatory channel that still reaches the record.
- Fallback channel: where the user can place a neutral correction if the record owner ignores the first request.
- Controlling artifact: the final record that will govern the decision, such as a meeting agenda, decision log, promotion packet, calibration packet, review-system entry, release tracker, branch-blocking note, or client deck.
- Source-of-truth record: the tracker, packet, agenda, approval tracker, or decision log that should become the current source of truth.

Do not write only "send to the manager" or "update the project recap." That is usually too vague. Name the hardening forum and owner role:

- Client/vendor blame: client-review deck owner, delivery owner, vendor lead, minutes owner.
- Promotion/credit: leadership follow-up thread owner, project recap owner, promotion packet owner, review-system owner.
- Performance/layoff: manager, calibration packet owner, review-system owner, HRBP only after a wrong official record persists through the normal correction path.
- Side-channel decision: shared project doc owner, decision log owner, API owner, release tracker owner, branch-hold owner.
- Risk acceptance/minutes: minutes owner, launch approver, risk owner, status-thread owner.
- False approval/alignment: true approver/sign-off owner and the official decision-record owner.

The route must appear in the ready-to-send draft, not only in analysis notes. A good draft gives the record owner a concrete choice:

- update the visible record by a deadline and send it to the required audience; or
- for non-urgent records, confirm that the user should post a neutral recap on the official fallback channel.
- for deadline-critical records, accept that silence triggers the user's neutral fallback addendum before the record hardens.

Use audience parity: if a pre-read, leadership update, client deck, or side-channel decision already reached a group, the correction must reach that same group or the durable record they rely on.

Audience parity is not enough when a different controlling artifact will drive the decision. If a pre-read feeds a meeting, the correction also belongs in the meeting agenda or decision log. If a leadership update feeds a packet, the correction also belongs in the packet. If a regional chat conflicts with a tracker, the tracker remains controlling until the required owners change it there.

Also split owner roles when responsibilities differ. A single "owner" is too weak when one person owns the deck, another approves the decision, another validates evidence, and another accepts risk.

Script:

```text
Before [forum/date], I want to make sure [record] reflects the accurate timeline:

- Fact:
- Owner:
- Evidence:
- Decision needed:

Please confirm by [time] so the review packet/meeting notes/status thread is accurate.
```

Record-route block:

```text
Stakeholder path:
- Hardening forum:
- Record owner:
- Required audience:
- Deadline:
- First channel:
- Fallback channel:
```

Fallback sentence:

```text
If [record] will not be updated by [deadline], I can send a neutral recap to [official thread/audience] so the decision record is accurate before [forum].
```

Deadline-critical fallback sentence:

```text
If [record] is not corrected by [deadline], I will place a neutral addendum in [controlling artifact/fallback channel] with [artifact/date/link] before [forum/packet lock/branch close].
```

Audience parity sentence:

```text
Please send the corrected version to the same audience that received [pre-read/update/deck/minutes], including [audience], so the old framing does not remain the only visible record.
```

Owner matrix:

```text
To avoid ambiguity before [forum/deadline], can we record these owners in [record]?

- Accountable first responder to complete this matrix:
- Record owner:
- Decision/approval owner:
- Evidence owner:
- Risk owner:
- Execution owner:
- Hold owner if unresolved:
- Fallback poster if [record] is not updated:
```

Source-of-truth correction block:

```text
Current source of truth:
Obsolete or superseded wording:
Corrected wording that supersedes it:
Source-of-truth owner:
Decision-record owner:
Correction owner:
True approver:
Approval status: pending
Required decision owners:
Decision remains pending until:
```

Evidence packet block:

```text
Evidence packet:
- Exact current wording:
- Source proof:
- Artifact/date/link:
- Supporting metric or transcript:
- Accessible to the record owner:
- Posted, forwarded, or appended confirmation needed:
- Confirmation receipt owner:
```

Red-team fill-before-send gate:

```text
Before sending, these fields must be filled or explicitly requested. If any required field is unknown, use field-lock request mode rather than formal correction mode:

- Original audience/distribution list:
- Correction audience:
- Controlling artifact:
- Record owner:
- Exact current wording:
- Source proof with artifact/date/link:
- Packet/deck/minutes/tracker lock time:
- Confirmation receipt owner:
- Missing owner roles:
- Field-completion owner:
- Interim deadline lookup trigger:
- Derived records that must receive or reflect the fallback:
- Timestamped receipt owner:

If any required field is unknown, the first action is to request that field or place only a neutral pending-status note with verified facts and open questions.
```

Supersession receipt line:

```text
Please confirm that [source-of-truth record] now replaces, marks incomplete, or supersedes "[old wording]" with "[corrected wording]", and that the correction is visible to [same audience/controlling artifact users].
```

Evidence-bound closure capsule:

```text
To close the record route, please confirm or update these before [hardening event]:

- Current visible wording: [exact wording] in [record/thread/artifact].
- Source proof: [dated source facts] plus [artifact/date/link still needed].
- Same-audience or controlling-record append: send/post/append the corrected or pending-status wording to [original audience] and [controlling record].
- Derived-record sweep: check [deck/minutes/agenda/tracker/packet/scheduled send/customer announcement/campaign copy/leadership thread/review record/recap] and mark each updated, appended, pending, superseded, not controlling, inaccessible with reason, or not applicable.
- External/direct thread check: confirm whether any separate client/vendor/partner/regional/leadership thread already carried the old framing; do not send there unless a wrong durable record is verified or imminent.
- Owner split: I can provide evidence. Please confirm [execution owner], [approval owner], [risk owner], [send or hold owner], and [record owner]. Any owner not proven by the artifact remains pending.
- Receipt: [receipt owner] will provide timestamped proof before [hardening event] that the old wording was replaced, marked incomplete, marked pending, superseded, or marked not controlling.
```

Vendor late-blame add-on:

```text
Please also confirm whether the "requirements unclear" framing appeared in any vendor-client direct thread, client deck/pre-read, risk log, minutes, recap, or delivery tracker. I can provide the requirements timeline and source emails; vendor delivery/remediation ownership, review disposition, risk acceptance, and final client-facing record ownership should be recorded separately.
```

Approval-pending launch add-on:

```text
Please reconcile the launch email, approval tracker, scheduled customer announcement, scheduled send copy, send checklist, campaign copy, launch thread, and customer-facing approval path before send. Until [true approver] confirms in writing, approval status remains pending. [send or hold owner] owns pausing the send if corrected wording is not reflected before [hardening event].
```

Manager-credit or promotion add-on:

```text
Can you either append this contribution sentence to the same leadership thread or confirm the packet owner who will add it to the review record?

"For contribution clarity: [candidate/user] contributed to [team result/decision] by [verified mechanism] on [date/link]. [manager/presenter] presented it to [audience]. The record should not imply sole metric causality unless the source record supports it."

Please also confirm the original leadership audience and whether any deck, recap, promotion packet, review packet, or goals record reused the manager-only framing.
```

Non-exclusive promotion metric script:

```text
Suggested reviewer-visible wording:
"For the team result of [metric improved by Y%], [candidate/user]'s work supported the team result through [verified mechanism], including [artifact/date/link]. Supporting artifacts: [commit/rollout plan/incident note]."

Please keep the team-level metric wording non-exclusive unless the source record proves sole causality.
```

Transcript-bound minutes script:

```text
Correction requested:
"Decision: [verified decision]. Risk noted: [transcript-supported risk]. Risk acceptance: [person/role] said '[exact quote]'. Execution owner: Pending - [role] to confirm if a separate source names it."

Please do not add execution, approval, or risk-owner wording beyond what the transcript or decision log supports.
```

Hostile weak-evidence script:

```text
This is a behavior-only record-existence request, not a complaint or correction claim. Please share the minutes, transcript, chat, recording, or action-item recap for [work item] by [deadline].

Until a material record error or decision/owner/risk/deadline impact is verified, I will not send a leadership note, HR note, broad distribution, competence claim, identity-based claim, or target-facing message.

Private incident note fields:
- Meeting date/time:
- Attendees:
- Protected-class generalization: redacted from working notes.
- Observable behavior or record change:
- Source record requested:
- Decision/owner/risk/deadline impact:
- Follow-up deadline:
```

Hostile identity sanitization script:

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

Mixed-channel conditional decision script:

```text
Verified now:
- [Person] wrote in [channel]: "[exact conditional wording]."
- [Approver/QA/owner] wrote: "[exact source wording]."
- Formal approval record: Pending - [decision-record owner] to confirm.

Suggested record wording:
"[Exact conditional instruction] was posted in [channel]. Formal approval, risk acceptance, release decision, and hold authority remain pending until [true approver/decision owner] confirms in writing."
```

Contribution-map plan-vs-delivery script:

```text
Verified now:
- The project plan lists [candidate/user] as owner for [subitems].
- Completion state, outcome, artifact links, and controlling-record owner are Pending - [record owner/evidence owner] to confirm.

Suggested record wording:
"The plan lists [candidate/user] as owner for [subitems]. Please link the artifact/date/completion state/outcome for each item before the summary or packet describes completed delivery or migration success."
```

Manager-credit no-access script:

```text
Suggested attribution note:
"My dated draft contains [analysis/recommendation/mechanism]. Please append or forward this artifact-backed contribution detail to the same leadership audience or packet owner and send a timestamped receipt."
```

Standup artifact-scope script:

```text
Posting the artifact links for today's status:
- Commit/design note links:
- Work reflected in those artifacts:
- Recap line requested: "[candidate/user] posted artifact links for [scoped work]."

Please keep any standup recap tied to those artifact links, or send the recap by [deadline] so the notes owner can verify it before any correction request.
```

Executable field-lock script:

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

Minimum executable route script:

```text
This is a field-lock request for [controlling artifact].

Verified now: [one or two source-backed facts].
Please confirm or redirect the record owner, audience, and hardening time by [concrete trigger].

If no one confirms by then, [fallback poster] will post this neutral pending-status note to [controlling artifact/best-known official thread]: "[verified facts + pending owner/evidence fields]."

Please send a timestamped receipt once it is posted, appended, forwarded, or marked pending. This route does not assign execution, approval, risk, delivery, or final-owner responsibility.
```

Minimum success-state scripts:

```text
Client/vendor late-blame:
"Minimum success before client review: the verified timeline is posted as a pending-status note in the controlling client deck or official review thread, with timestamped receipt to the same review audience. Internal tracker updates alone do not close this."

Calibration/performance:
"Criterion check required: original quarter goal versus documented goal change. Please state in the packet whether the original goal, changed goal, or calibration rubric controls before the packet locks."

Mixed-channel accountability:
"QA-skip approval not confirmed. Please post or link this status in the active accountability thread, release tracker, or decision log before assigning blame, approval, risk, or execution ownership."

Promotion contribution:
"Reviewer-visible contribution line: For the team result of [metric], [candidate]'s work supported the team result through [concrete design/artifact], including [artifact/date/link]. The packet should keep the metric team-level while naming these mechanisms."
```

V14 quality-tail closure ledger:

```text
Quality-tail closure ledger:
- Decision-critical pending fields: [fields]. Until these are filled, [record] remains pending/not controlling and no [owner transfer/review conclusion/blame assignment/recurring ownership/client framing] should harden.
- Accountable first responder and trigger: [role] to confirm or redirect by [time].
- Silence default: if no confirmation by [time], [fallback poster] posts "[neutral pending-status note]" to [controlling artifact/best-known official thread].
- Same-audience or supersession: [same audience] receives the correction, or [controlling artifact] explicitly supersedes [old wording] and records why the original audience is unavailable.
- Claim-to-artifact map: [claim] -> [artifact/date/link]; unsupported claims stay pending.
- Receipt: [receipt owner] provides timestamped proof before [hardening event].
```

Residual-family closure scripts:

Recurring invisible work:

```text
The recurring-work record must close all critical fields before work continues: final send owner, source-data owner, backup owner, cadence/due time, time budget, displaced work, goals or contribution treatment, metrics audience, and fallback path.

Until those fields are filled, this remains one-time support only. A goals-thread note alone does not reach the metrics audience expecting Monday delivery unless [metrics audience/CEO metrics thread] receives or reflects the same pending-status note.
```

Promotion contribution dilution:

```text
Reviewer-visible contribution line:
"For the team result of [metric], [candidate]'s work supported the team result through [owned verb + mechanism], including [artifact/date/link]. Claim-to-artifact map: [design claim] -> [link]; [rollout claim] -> [link]; [debugging/incident claim] -> [link]."

Please append, supersede, or mark incomplete the anonymous team-only wording so it is not the controlling review record. A generic "supported the team result" sentence without mechanism-level artifacts is not enough.
```

Pre-wired ownership transfer:

```text
Please reclassify "[final-transfer wording]" as "proposal/review" until current-owner review, transition criteria, source-data quality gates, decision owners, risk owner, execution owner, and hold owner are documented.

No owner-record change should proceed until the controlling decision log supersedes the pre-read or the same pre-read audience receives the pending-status correction.
```

Mixed-channel release or accountability:

```text
The controlling release/accountability record must state:
- who determined whether the condition was met;
- true approver and QA/approval owner status;
- release owner's proceed/hold/mitigation decision;
- blame, approval, risk, and execution ownership remain pending until those fields are recorded.
```

Manager-credit with no access to leadership thread:

```text
Please either append the artifact-backed contribution detail to the same leadership thread, or add a packet-accessible note that the leadership thread is inaccessible and maps exact overlap between my dated artifact and the upward wording.

Promotion packet protection alone does not close the live leadership-memory route unless the same audience is reached or the controlling packet explicitly records why same-audience delivery is unavailable.
```

Calibration, layoff, or performance packet:

```text
Reviewer-visible packet addendum required:
- Original goal:
- Dashboard/metric line:
- Workstream artifact-map status:
- Criterion decision: original goal, documented changed goal, or calibration rubric controls.

The adverse roadmap-only or anonymous summary must be marked incomplete, superseded, or weighed against the governing criterion before it controls the review.
```

Client/vendor late-blame:

```text
Before client review, the controlling client deck or official review thread must contain the verified timeline, deadline status, remediation/delivery owner split, review-disposition or risk owner, and same-client-review receipt. Internal tracker updates alone do not close this route.
```

Use cases:

- Client deck blame: deck owner, delay-cause validation owner, vendor blocker-status owner, remediation owner, recap owner.
- Side-channel release: release tracker owner, API approval owner, compatibility evidence owner, residual-risk owner, branch-hold owner.
- Pre-read ownership transfer: pre-read owner, decision sponsor, current-owner impact owner, migration-risk owner, rollback owner, ownership-tracker owner.
- Invisible work: manager, report owner, goals record owner, roadmap/capacity owner, interim support boundary owner.
- Calibration packet: packet owner, manager, evidence/dashboard owner, calibration decision owner, HRBP only if wrong official record persists.
- Leadership-to-packet credit: leadership thread owner, promotion packet owner or manager, original leadership audience, no-access fallback through manager and packet owner.

## Refuse False Alignment Or Approval

Use when someone asks the user to imply approval, alignment, warning, or sign-off that does not exist.

Rules:

- Do not imply approval that is pending.
- Name the real approver.
- Ask the approver to confirm directly.
- Offer safe wording.
- Escalate only if false wording is repeated or inserted into an official record.

Script:

```text
I cannot state that [team/person] approved or aligned unless we have that confirmation in writing.

Safe wording:
"Review is pending. We discussed [topic], and [team/person] requested [open item]. We will treat this as unapproved until [team/person] confirms approval or final comments in writing."

If approval exists, please forward the dated approval or ask [approver] to confirm on this thread.
```

If approval is pending, put the pending status into the approval tracker or launch record:

```text
Please do not imply approval. Current source of truth should read:
"Approval status: pending. [True approver] requested [open item]. This supersedes '[obsolete or superseded wording]' until [true approver] confirms approval in writing."
```

## Escalate Without Sounding Defensive

Use when the user lacks authority to resolve a blocker.

Rules:

- Escalate the decision, not the person.
- State what has already been tried.
- Offer options.
- Make the decision deadline explicit.

Script:

```text
I am escalating because this tradeoff is outside my decision rights. The issue is [X], the impact is [Y], and the decision needed by [date] is [Z].
```

## Make Invisible Work Visible

Use when maintenance, support, debugging, or coordination is not visible.

Moves:

- Quantify avoided risk.
- List operational load.
- Link to artifacts.
- Include before/after state.

Script:

```text
This week I resolved [N] support items, reduced [risk/latency/incidents], and unblocked [team/project]. The main open risk is [risk], and I need [support/decision] by [date].
```

## Route Credit Into Durable Records

Credit defenses fail when they stay in private chat while the visible record already credits someone else. For credit/promotion cases, include:

- The original artifact date and link.
- The specific contribution mechanism.
- The record that matters: project recap, leadership follow-up, review packet, promotion packet, or brag doc.
- The owner who can edit that record.
- A deadline before the packet or recap hardens.
- A fallback neutral recap if the owner does not update the record.

Script:

```text
To keep the visible record accurate before [review/recap date], can you confirm whether [record owner] will add this contribution detail to [record]?

- Artifact/date:
- Contribution:
- Result:
- Presented by:

If the record will not be updated by [deadline], I can send the neutral recap on [official thread] with the artifact link.
```

When the user cannot access the original leadership thread, do not stop at private correction. Route the neutral attribution recap to the manager and promotion packet owner for packet append or forwarding, and place it in the thread too if access exists.

No-access route template:

```text
I do not have access to the original thread, so please append or forward this evidence packet to [packet/tracker/decision record]. Please send a confirmation receipt once it has been posted, forwarded, or appended to the packet-accessible record.
```
