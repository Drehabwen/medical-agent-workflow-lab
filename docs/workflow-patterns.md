# Workflow Patterns

## Evidence Packet First

Medical and rehabilitation agents should not jump directly from prompt to advice. They should first build an evidence packet:

```text
source
claim
confidence
review status
```

## Recommendation Gate

Recommendations should declare the evidence sources they require. Guardrails can then block unsupported output before it reaches the user.

## Patient-Facing Output

Patient-facing recommendations need stricter handling:

- Use reviewed evidence.
- Avoid diagnostic certainty.
- Include clinician escalation rules.
- Separate education from treatment decisions.

## Product Integration

This workflow layer can sit between:

- family follow-up apps
- research assistants
- clinical documentation tools
- screening report generators
