# Medical Agent Workflow Lab

Technical experiments for medical and rehabilitation AI agent workflows.

This repository focuses on the layer between a language model and a clinical-facing product:

```text
task
-> evidence packet
-> tool-supported reasoning
-> guardrail checks
-> clinician-readable recommendation
```

It is not a diagnostic system. It is a workflow laboratory for making agent behavior more explicit, auditable, and safer.

## Scope

- Evidence packet schemas
- Guardrail checks for unsupported recommendations
- Minimal examples for tool-assisted medical workflow reasoning
- Separation between patient-facing text and clinician-reviewed output
- Reusable patterns for rehabilitation products and medical research tools

## Quick Start

```bash
python examples/review_packet.py
```

## Repository Layout

```text
src/medical_agent_workflow_lab/
  guardrails.py          # evidence and recommendation validation
docs/
  workflow-patterns.md   # agent workflow design notes
examples/
  review_packet.py       # minimal demo
```

## Related Products

- [RehabGPT-](https://github.com/Drehabwen/RehabGPT-)
- [Galen](https://github.com/Drehabwen/Galen)
- [ai-video-production-pipeline](https://github.com/Drehabwen/ai-video-production-pipeline)

## License

MIT
