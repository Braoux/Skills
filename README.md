# OpenClaw Skills

Reusable, task-focused skills for AI coding agents. Originally designed for OpenClaw, they can also be consumed by other agents that support `SKILL.md` instructions.

**Current status:** five implemented skills. Their outputs are decision aids and must be checked against real evidence.

## Available skills

| Skill | Purpose | Documentation |
| --- | --- | --- |
| **Conceptual Analysis** | Clarify business rules, invariants and ambiguity before technical design. | [Instructions](Conceptual-Analysis/SKILL.md) · [Guide](Conceptual-Analysis/README.md) |
| **Ticket Readiness** | Assess whether a ticket is clear, actionable and testable, with a justified readiness score. | [Instructions](Ticket-Readyness/SKILL.md) · [Guide](Ticket-Readyness/README.md) |
| **Technical Design** | Turn an understood requirement into an implementable, proportional design. | [Instructions](Technical-Design/SKILL.md) · [Guide](Technical-Design/README.md) |
| **Architectural Audit** | Examine architectural cohesion, coupling and changeability at file or project level. | [Instructions](Architectural-Audit/SKILL.md) · [Guide (FR)](Architectural-Audit/README.md) |
| **Software Functional Context** | Create portable, evidence-based documentation of existing application behavior. | [Instructions](Software-Functional-Context/SKILL.md) · [Guide](Software-Functional-Context/README.md) |

> The mixed-case directories are historical names retained for compatibility. `Ticket-Readyness/` is a legacy path; the canonical skill identifier is `ticket-readiness`.

## Typical workflow

These skills are composable, not a mandatory waterfall:

1. **Ticket Readiness:** find missing information and blockers.
2. **Conceptual Analysis:** model non-trivial business behavior and invariants.
3. **Technical Design:** identify a safe, minimal implementation.
4. **Architectural Audit:** independently evaluate structural quality when useful.
5. **Software Functional Context:** generate a handoff when the recipient cannot inspect the source repository.

A trivial change may need none of them. Do not create documentation for its own sake.

## Getting started

1. Clone this repository:

   ~~~bash
   git clone https://github.com/Braoux/Skills.git
   ~~~

2. Select the desired skill directory. Copy or link the **whole directory** into the skills directory supported by your agent, or provide its `SKILL.md` directly. Installation paths vary by agent; this repository does not ship a universal installer.
3. Supply the ticket or code and the minimum necessary access. Review findings, unknowns and generated Markdown.

Example requests:

~~~text
Check whether issue ABC-123 is ready to implement and list blocking questions.
Analyze the domain invariants of a new primary-subscription requirement.
Design a safe solution based on the validated conceptual analysis.
Audit the architecture of src/modules/billing and explain the score.
~~~

## Design principles

- Separate **facts, deductions, assumptions and unknowns**.
- Never invent business rules to fill gaps.
- Read code and surrounding context before judging an implementation.
- Keep analysis **proportional** to actual complexity.
- Keep each skill's responsibility explicit: analysis is not implementation.
- Explain important findings and limitations using concrete evidence.

## Project-specific examples and confidentiality

This repository contains reusable skill instructions, not project-specific generated output. Keep functional context derived from private or employer repositories in authorized workspaces. Even without credentials, business rules, access roles and system structure may be sensitive.

## Contributing and quality checks

See [CONTRIBUTING.md](CONTRIBUTING.md). Validate skill metadata, Markdown fences and relative links with:

~~~bash
python3 scripts/validate_skills.py
~~~

The GitHub Actions workflow runs the same structural check on pull requests and pushes to `main`. It does **not** evaluate whether agents behave correctly; changes affecting behavior need representative manual or automated scenarios.

## Known maintenance work

- Several long skills need gradual progressive-disclosure refactoring backed by regression scenarios. This cleanup preserves their substantive instructions.
- Historical directory casing/spelling cannot be changed safely without migrating existing consumers.
- Keep any generated project-specific context in the appropriate private workspace; do not add it to the public skill catalogue.
