from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class EvidenceItem:
    source: str
    claim: str
    confidence: float
    reviewed: bool = False


@dataclass(frozen=True)
class Recommendation:
    summary: str
    required_sources: tuple[str, ...]
    patient_facing: bool = False
    clinician_reviewed: bool = False


def validate_recommendation(
    recommendation: Recommendation,
    evidence: Iterable[EvidenceItem],
    min_confidence: float = 0.65,
) -> list[str]:
    """Return guardrail violations for one recommendation."""
    items = list(evidence)
    sources = {item.source for item in items}
    violations: list[str] = []

    for source in recommendation.required_sources:
        if source not in sources:
            violations.append(f"missing required evidence source: {source}")

    low_confidence = [
        item.source
        for item in items
        if item.source in recommendation.required_sources
        and item.confidence < min_confidence
    ]
    if low_confidence:
        violations.append(
            "low confidence evidence: " + ", ".join(sorted(low_confidence))
        )

    unreviewed = [
        item.source
        for item in items
        if item.source in recommendation.required_sources and not item.reviewed
    ]
    if recommendation.patient_facing and unreviewed:
        violations.append(
            "patient-facing recommendation uses unreviewed evidence: "
            + ", ".join(sorted(unreviewed))
        )

    if recommendation.patient_facing and not recommendation.clinician_reviewed:
        violations.append("patient-facing recommendation lacks clinician review")

    return violations
