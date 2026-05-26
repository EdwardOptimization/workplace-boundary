# Example: Meeting Minutes Correction

## User Input

The meeting recap says I own the blocker, but the dependency belongs to another team. I have the ticket showing the dependency owner and a Slack message confirming the handoff.

## Pressure Pattern Output

Pattern: Meeting-Minutes Control plus Blame Shifting.

Mechanism: the recap becomes the official memory. If the wrong owner remains in the notes, later delay can be attributed to the wrong person.

Defense handoff: correct the official record quickly, with evidence.

## Boundary Defense Output

```text
Subject: Correction to meeting notes for integration risk

Thanks for sending the notes. One correction for accuracy:

Item: Backend endpoint blocker
Current note: [user] owns the blocker
Correction: backend team owns endpoint contract; I own connector integration after the endpoint is available
Owner: [backend owner]
Due date: [date]
Evidence/link: [ticket] and [Slack handoff]
Impact if left unchanged: connector delivery may appear blocked by the wrong owner

Please reply by [date/time] if this correction does not match your understanding.
```

