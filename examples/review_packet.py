from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from medical_agent_workflow_lab import (  # noqa: E402
    EvidenceItem,
    Recommendation,
    validate_recommendation,
)


def main() -> None:
    evidence = [
        EvidenceItem(
            source="screening_report",
            claim="Trunk rotation was elevated during forward bend screening.",
            confidence=0.78,
            reviewed=True,
        ),
        EvidenceItem(
            source="home_checkin",
            claim="Family reported inconsistent home exercise adherence.",
            confidence=0.72,
            reviewed=False,
        ),
    ]

    recommendation = Recommendation(
        summary="Suggest clinician review before changing the home program.",
        required_sources=("screening_report", "home_checkin"),
        patient_facing=True,
        clinician_reviewed=False,
    )

    violations = validate_recommendation(recommendation, evidence)
    print("violations:")
    for item in violations:
        print(f"- {item}")


if __name__ == "__main__":
    main()
