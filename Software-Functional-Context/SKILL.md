---
name: "software-functional-context"
description: "Analyze a software repository and generate detailed and compact portable functional context for downstream ticket or product analysis without source access."
---

# Software Functional Context

## Goal

Transform repository evidence into reusable documentation of what the product currently does. Generate functional knowledge, not ticket analysis, implementation plans, architecture dumps, or future requirements.

Use source code, tests, configuration, database constraints, migrations, APIs, UI routes, and repository documentation as evidence.

## Evidence

Classify uncertain statements:
- **OBSERVED**: directly demonstrated by repository artifacts.
- **INFERRED**: strongly suggested, never a confirmed product requirement.
- **UNKNOWN**: not established by the repository.
- **INCONSISTENCY**: artifacts disagree; preserve both sides.

Never fill gaps from common sense, industry convention, or framework defaults.

## Procedure

1. Inspect repository instructions, existing functional context, root documentation, modules, entry points, UI routes, services, domain models, migrations, configuration, tests, and integrations. Use routes, callers, wiring, tests, flags, and configuration to distinguish active behavior. Complete when major product areas and boundaries are mapped.
2. Identify functional domains, actors, permissions, workflows, states, transitions, validations, side effects, integrations, configuration variants, and evidence-backed edge cases. Normalize technical names into product language. Complete when another agent can locate behavior relevant to a ticket.
3. Write or incrementally update the detailed package under `docs/software-functional-context/`. Preserve stable business-rule identifiers. Remove content only when evidence shows it is obsolete. Complete when high-value domains and cross-domain effects are covered.
4. Generate `docs/software-functional-context/software-functional-context.compact.md` in addition to the detailed package. Make it autonomous for an agent that may receive only this file plus a ticket-analysis skill. Complete when it supports product-level reasoning without another file.
5. Validate internal links, Markdown structure, evidence labels, encoding, sensitive-data absence, and repository diff. Report files, limitations, contradictions, and unknowns.

## Detailed package

Create only useful files, normally:

```text
docs/software-functional-context/
├── README.md
├── software-functional-context.compact.md
├── overview.md
├── glossary.md
├── actors-and-permissions.md
├── business-rules.md
├── integrations.md
├── domains/<domain>.md
└── workflows/<workflow>.md
```

The README is the navigation entry point. Include purpose, short product description, major domains, workflows, files, guidance, and generation date.

Domain files capture applicable concepts, actors, states, transitions, behavior, rules, validations, permissions, side effects, related domains, edge cases, unknowns, and evidence.

Workflow files capture applicable actors, preconditions, trigger, functional flow, state changes, rules, permissions, side effects, failures, edge cases, related workflows, unknowns, and evidence.

Use stable identifiers such as `BR-001` for transverse rules.

## Compact document

The compact document is product-wide context, not a summary of the latest feature.

- Prioritize balanced coverage of major domains.
- Keep details specific to one feature, ticket, or recent change in the detailed package unless they establish a transverse rule.
- Give comparable depth to domains of comparable importance.
- Describe functional behavior and consequences. Omit transaction ordering, rollback mechanics, call sequences, SQL, DTO dumps, and class hierarchies.
- Preserve technical constraints only when they materially affect visible behavior, such as idempotency, external limits, concurrency risks, or non-compensated side effects.
- Make the document fully autonomous. Never require the detailed package to understand a rule.
- If necessary information is absent, treat it as unknown and never invent it. If the detailed package is available, consult it only to deepen the relevant domain.
- Include purpose, evidence definitions, product overview, actors, lifecycle, domains, states, transverse rules, side effects, integrations, edge cases, contradictions, unknowns, and a minimal glossary.
- State near the beginning that functional behavior is **OBSERVED** unless another evidence level is shown.
- Phrase existing behavior descriptively, not normatively. Avoid “must” and “should” unless repository evidence explicitly establishes an intentional constraint; otherwise write “currently does”, “is applied”, or equivalent.
- Preserve stable business-rule identifiers from the detailed package. When compact selection creates numbering gaps, explain that omitted identifiers remain reserved for alignment rather than implying missing content.
- Keep it significantly smaller than the detailed package.

### How to use this context

Near the beginning, instruct the consumer to:
- treat **OBSERVED** as existing behavior;
- use **INFERRED** as an indication, never a product requirement;
- convert relevant **UNKNOWN** items into clarification questions;
- flag tickets that appear to change or contradict existing behavior;
- not require preservation when the ticket explicitly asks to change existing behavior;
- focus on sections relevant to the ticket;
- treat missing necessary information as unknown.

### Ticket routing index

Near the beginning, map ticket topics to actual compact sections:

| Ticket topic | Read primarily |
|---|---|
| Need / forecast | needs section |
| Consultation | consultation section |
| Candidacy / analysis / award / notification | procurement section |
| Supplier | supplier section |
| Contract / amendment / order | execution section |
| Documents / signature | document section |
| External interface | integration section |
| Permissions / configuration | principles, actors, and transverse rules |

## Writing rules

Write behavior first. Repository references support statements but must not be required for comprehension. Prefer file and behavior names over fragile line numbers.

Document configuration variants instead of assuming one deployment value. Mark uncertain legacy or dead code unless active routes, wiring, callers, tests, or configuration establish use.

Explain cross-domain effects such as validation creating contracts, updating tasks, generating documents, or enriching suppliers.

Never expose passwords, keys, tokens, credentials, certificates, sensitive connection strings, or personal data samples.

## Boundaries

Do not:
- modify application source code;
- implement features or create pull requests;
- score ticket readiness;
- invent rules or transitions;
- treat current code as future product intent;
- assume optional or legacy modules are active;
- make the compact document depend on the detailed package;
- overrepresent a recent feature at the expense of balanced coverage.

The deliverables answer: **What does the software currently do, and what behavior matters when reasoning about change?**
