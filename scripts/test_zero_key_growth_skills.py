#!/usr/bin/env python3
"""Offline contract tests for zero-key growth skills.

Run: python3 scripts/test_zero_key_growth_skills.py
This checks metadata and guardrails, not the validity of business advice.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    "player-demand-evidence",
    "activation-retention-audit",
    "matchup-trust-gate",
    "organic-acquisition-experiments",
    "pricing-offer-validation",
    "analysis-unit-economics",
    "growth-decision-review",
]

def main() -> None:
    for name in SKILLS:
        skill_path = ROOT / name / "SKILL.md"
        readme_path = ROOT / name / "README.md"
        assert skill_path.exists() and readme_path.exists(), name
        skill = skill_path.read_text(encoding="utf-8")
        assert skill.startswith("---\nname: " + name + "\n"), name
        assert re.search(r"^description: .+", skill, re.M), name
        assert not re.search(r"^requires\\.env\\s*:", skill, re.M), name
        assert "OPENAI_API_KEY" not in skill, name
        for section in ("## Procedure", "## Required output", "## Exclusions"):
            assert section in skill, f"{name}: {section}"
        doc = readme_path.read_text(encoding="utf-8")
        assert "SKILL.md" in doc, name
    for file in (
        "player-demand-evidence/templates/feedback.csv",
        "activation-retention-audit/templates/events.csv",
        "pricing-offer-validation/templates/offer-test.csv",
        "analysis-unit-economics/templates/cost-inputs.csv",
        "ZERO_KEY_GROWTH.md",
    ):
        assert (ROOT / file).is_file(), file
    print(f"Passed: {len(SKILLS)} growth skill metadata/contracts and local templates.")

if __name__ == "__main__":
    main()
