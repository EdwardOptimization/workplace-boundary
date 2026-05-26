# Pressure Pattern Taxonomy

Use these names when diagnosing workplace incidents.

## Narrative Control

Someone defines the problem, success criteria, root cause, or next step in a way that favors their position.

Signals:

- They summarize before others can state their part.
- They rewrite a miss as someone else's execution issue.
- They choose slide titles or status headlines that overclaim their role.

Advanced variants:

- Pre-wire: stakeholders are privately aligned before the formal decision forum.
- Title-layer capture: deck titles encode a conclusion stronger than the body evidence.
- Scope-transfer framing: a team's ownership is reframed as already aligned before the current owner is heard.

## Credit Capture

Someone turns team or peer work into their own visible contribution.

Signals:

- Reports another person's progress before they speak.
- Omits contributor names in upward updates.
- Presents draft, analysis, code, or design as their own.
- Controls the final meeting recap or deck.

Advanced variants:

- Manager bottleneck: the direct manager is the only upward channel and omits contributor names.
- Contribution fragmentation: a large contribution is split into many small tasks, then summarized as generic team progress.
- Mentoring-credit capture: time spent helping someone is reported as the other person's coordination or management work.

## Blame Shifting

Someone moves accountability for delay, defect, or risk to another person or dependency.

Signals:

- Mentions blockers only after failure.
- Uses vague "we were waiting on X" without dated evidence.
- Avoids naming who accepted risk or changed scope.

Advanced variants:

- Risk acceptance omission: minutes record a go decision but omit who accepted the risk.
- Late-green reversal: a party reports green until a review, then claims they were blocked.
- Verbal-order reversal: someone gives verbal direction, then later asks why the risky step happened.

## Owner Ambiguity

No one has explicit responsibility for a decision, deliverable, or dependency.

Signals:

- Action items lack owner or due date.
- Multiple managers assign conflicting priorities.
- "Support" or "help" becomes hidden ownership.

## Meeting Airtime Control

Someone controls speaking order, interrupts, closes topics, or owns final summaries.

Signals:

- They speak first and last on key topics.
- They repeat another person's point as their own.
- They redirect unresolved objections to offline follow-up.

## Meeting-Minutes Control

Someone writes the official memory of the meeting and controls who is named, omitted, or assigned.

Signals:

- Minutes omit contributors.
- Decisions appear stronger than what was agreed.
- Risks are softened or assigned to people who did not accept them.

High-risk signal:

- A risk acceptance statement is absent from minutes even though it was discussed.

## Information Isolation

Someone keeps a person out of the information path needed to execute or be credited.

Signals:

- Missing CCs.
- Side-channel decisions.
- Access denied using vague risk language.
- Private updates replace shared documentation.

Advanced variants:

- Vague risk access denial: "production risk" is used without written criteria or approval path.
- Regional side-channel: a local/private channel changes a shared project decision.
- Pre-read exclusion: key stakeholders receive a framing document before the affected owner sees it.

## Resource Or Scope Capture

Someone frames a request as strategic, urgent, or risk-reducing to win people, budget, project scope, or visibility.

Signals:

- High-visibility work is captured while maintenance stays invisible.
- Resource asks lack transparent tradeoff analysis.
- A sponsor relationship changes project ownership.

Advanced variants:

- Strategic-priority wrapper: a scope grab is framed as company priority without transparent tradeoff.
- Invisible-work dumping: low-visibility recurring work is framed as a small favor.
- Career-visibility arbitrage: visible projects are captured while operational work remains uncredited.

## Bad-News Avoidance

Someone delays, softens, or buries negative updates to avoid responsibility.

Signals:

- No early risk record.
- Optimistic status until deadline.
- Root cause appears only after failure.

## Assistance Boundary Drift

Advice or help becomes responsibility for someone else's deliverable.

Signals:

- A coworker asks for help, then says the output depended on you.
- Review comments become implied approval.
- Debug help becomes ownership of the bug.

## Goal Shifting

Targets or evaluation criteria change after work starts.

Signals:

- Original success criteria disappear.
- A new target is treated as if it was always agreed.
- Performance review ignores recorded scope changes.

## Defense Leak Taxonomy

Use this only to test whether a proposed defense is strong enough. Do not convert these leaks into manipulation instructions.

### Credit Leak

The defense does not attach contribution to an artifact, author, date, or visible status channel.

Patch:

- Add contribution map.
- Link artifact.
- Name owner/contributor roles.

### Owner Leak

The defense does not identify final owner, sign-off owner, due date, or acceptance criterion.

Patch:

- Add owner/date/criterion table.
- Ask for correction by a deadline.

### Evidence Leak

The defense relies on memory or tone instead of verifiable facts.

Patch:

- Add ticket, commit, doc, transcript, meeting note, or dated message.

### Record Leak

The wrong meeting note, deck, ticket, or status update could become the official record.

Patch:

- Correct the official record directly.
- Ask for written confirmation or correction.

### Stakeholder Leak

The wrong narrative can reach a decision maker before the user's factual correction.

Patch:

- Send a concise, non-accusatory status update to the appropriate audience.
- Keep normal reporting lines unless material risk justifies escalation.

Stakeholder path questions:

- Which forum will make the narrative durable?
- Who owns that forum or artifact?
- Who must see the correction before the meeting, review, release, or calibration?
- What is the least escalatory channel that still reaches the decision record?
- What fallback channel records the correction if the first owner does not update the artifact?
- What controlling artifact will decide the outcome if there is silence: agenda, decision log, packet, review-system entry, tracker, branch-blocking note, or client deck?

Defense handoff:

- name the hardening forum, record owner, required audience, deadline, first channel, and fallback channel.
- require audience parity when a pre-read, leadership update, client deck, or side-channel decision already reached a group.
- require the controlling artifact to be patched, not only the side thread or private chat.
- require a record-owner choice clause: update the visible record by a deadline, or, for deadline-critical records, state the neutral fallback the user will place under silence.
- require an owner matrix when different people own the record, approval, evidence, risk, execution, hold, or fallback recap.

Examples:

- Credit/promotion: leadership follow-up thread -> project recap owner -> promotion packet owner -> neutral recap with artifact link if omitted.
- Leadership update not accessible to user: manager + promotion packet owner become the fallback route into the packet; private correction is not terminal.
- Client/vendor blame: client-review deck -> delivery owner -> vendor lead and minutes owner -> correction in review recap if the deck is not updated.
- Performance/layoff: calibration packet -> manager/review-system owner -> calibration audience -> automatic review-system addendum if the packet is not corrected by lock -> HRBP only if a wrong official record persists.
- Side-channel decision: shared project doc or decision log -> API/release owner -> implementation stakeholders -> official tracker or branch-blocking note if side-channel decision remains undocumented.
- Risk/minutes: meeting minutes -> minutes owner and decision owner -> launch/review audience -> written correction before minutes are accepted.

### Escalation Leak

The user has no clear condition for escalating.

Patch:

- State time threshold, material-risk threshold, repeated-omission threshold, or wrong-official-record threshold.

### Truth-Record Leak

The defense refuses false wording but does not lock the accurate status into the record.

Patch:

- Replace false approval/alignment wording with pending-review wording.
- Name the approval owner.
- Ask that the approval owner confirm directly on the thread.
- Escalate if false status is inserted into an official record.
- Name the source-of-truth record, current source of truth, decision-record owner, correction owner, true approver, and required decision owners.
- State approval status: pending when approval has not been given.
- Say the corrected wording supersedes obsolete or superseded wording.
- Keep the decision remains pending until the required decision owners confirm.

Protective artifact:

```text
Source-of-truth record:
Current source of truth:
Obsolete or superseded wording:
Corrected wording that supersedes it:
Decision-record owner:
Correction owner:
True approver:
Approval status: pending
Required decision owners:
```

### Material Leak

The defense ignores concrete materials already available in the scenario.

Patch:

- Quote or cite the specific email/chat/transcript/review line.
- Use the exact date, owner, deadline, or phrase if present.
- Avoid generic placeholders when scenario materials provide concrete details.
- Build an evidence packet with exact current wording, source proof, artifact/date/link, and proof accessible to the record owner.
- If the user lacks access to the original thread, define the no-access route through manager, packet owner, or record owner.
- Ask for a confirmation receipt showing the correction was posted, forwarded, or appended to the packet-accessible record.

Protective artifact:

```text
Evidence packet:
- Exact current wording:
- Source proof:
- Artifact/date/link:
- Accessible to the record owner:
- No-access route:
- Posted, forwarded, or appended confirmation:
- Confirmation receipt:
```
