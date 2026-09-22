````markdown
---
name: ticket-readiness
description: Evaluate whether a development ticket is sufficiently clear, complete, and actionable before implementation. Identify missing requirements, ambiguities, dependencies, acceptance criteria, risks, and blocking questions, then produce a readiness score and Markdown report.
---

# Ticket Readiness

Evaluate whether a development ticket contains enough information to begin implementation safely and efficiently.

The purpose of this skill is to answer:

> Is this ticket actually ready to be developed?

The skill does not design the solution and does not implement the ticket.

It evaluates whether the requirement is sufficiently:

- understandable;
- complete;
- testable;
- scoped;
- unambiguous;
- actionable.

Every assessment must produce:

- a **Readiness Score from 0 to 10**;
- a readiness status;
- blocking questions when applicable;
- a persistent Markdown report when filesystem access is available.

---

# Language

Write the assessment in the same language as the ticket or user's request unless another language is explicitly requested.

Preserve existing:

- ticket identifiers;
- domain terminology;
- code symbols;
- project names;
- API names;
- external system names.

---

# When to use this skill

Use this skill before conceptual analysis, technical design, or implementation when a ticket needs to be evaluated.

Typical inputs include:

- Jira tickets;
- GitHub issues;
- GitLab issues;
- Azure DevOps work items;
- feature requests;
- bug tickets;
- product stories;
- maintenance tasks;
- technical tickets.

Examples:

```text
Is JIRA-142 ready to be developed?
````

```text
Review this ticket before I start coding.
```

```text
Check whether this user story is complete.
```

```text
Evaluate the readiness of this bug ticket.
```

---

# What this skill does NOT do

This skill does not:

* implement the ticket;
* produce source code;
* perform detailed technical design;
* choose architecture;
* redesign the feature;
* invent missing business rules;
* turn assumptions into requirements;
* rewrite the entire ticket unless explicitly requested;
* reject a ticket merely because it is short.

A short ticket may be perfectly ready.

A long ticket may still be unusable.

Readiness depends on information quality, not ticket size.

---

# Core principle

Do not ask:

> Is this ticket detailed?

Ask:

> Can a competent developer understand what must change, determine when the work is correct, and begin without inventing important product decisions?

That is the readiness standard.

---

# Evidence hierarchy

Evaluate information using this priority:

1. Explicit ticket content.
2. Linked specifications or documentation.
3. Existing acceptance criteria.
4. Attached screenshots or examples.
5. Existing project behavior when accessible.
6. User-provided clarification.
7. Reasonable technical inference.

Do not use reasonable inference to silently fill missing business requirements.

---

# Facts, assumptions, and unknowns

Always distinguish between:

## Confirmed

Explicitly stated information.

## Inferred

Information that follows reasonably from available evidence.

## Assumed

Information required to interpret the ticket but not explicitly established.

## Unknown

Information that cannot currently be determined.

An assumption may allow exploratory work.

It must not automatically make the ticket ready.

---

# Readiness dimensions

Score five dimensions from **0 to 2**.

Total:

```text
10 points
```

---

## R1 — Intent and expected outcome — /2

Evaluate whether the ticket clearly explains:

* the problem;
* the expected change;
* the desired outcome;
* who or what is affected.

### 2.0

The objective and expected behavior are clear.

### 1.5

The intent is clear but some secondary behavior remains uncertain.

### 1.0

The general objective is understandable but important interpretation is required.

### 0.5

The developer must guess significant parts of the expected behavior.

### 0.0

The ticket does not establish what should actually change.

---

## R2 — Business rules and behavior — /2

Evaluate whether the behavioral rules required by the ticket are sufficiently defined.

Look for:

* permissions;
* states;
* transitions;
* validation;
* limits;
* ownership;
* conditions;
* exceptions;
* lifecycle rules.

### 2.0

Important business behavior is sufficiently established.

### 1.5

Minor behavior remains implicit.

### 1.0

Several rules are missing but the core behavior remains identifiable.

### 0.5

Important product decisions would need to be invented during development.

### 0.0

The required business behavior is fundamentally unspecified.

Do not require business rules for purely technical tickets where none are relevant.

---

## R3 — Acceptance and verifiability — /2

Evaluate whether the developer and reviewer can determine when the ticket is complete.

Look for:

* explicit acceptance criteria;
* clear expected outcomes;
* examples;
* observable behavior;
* error cases;
* before/after behavior.

Acceptance criteria do not need to use formal Given/When/Then syntax.

### 2.0

Completion can be verified objectively.

### 1.5

Most expected behavior is testable with minor interpretation.

### 1.0

The main path is testable but important cases are unclear.

### 0.5

The developer would need to decide what "done" means.

### 0.0

There is no reliable way to determine whether the implementation satisfies the ticket.

---

## R4 — Scope and dependencies — /2

Evaluate whether the boundaries of the work are sufficiently understood.

Look for:

* systems involved;
* impacted areas;
* dependencies;
* external teams;
* prerequisite work;
* linked tickets;
* data requirements;
* rollout constraints;
* explicit exclusions.

### 2.0

Scope and relevant dependencies are clear.

### 1.5

Small uncertainties exist but should not significantly affect implementation.

### 1.0

Some important boundaries or dependencies remain unclear.

### 0.5

The developer may discover substantial hidden scope during implementation.

### 0.0

The ticket cannot reasonably be scoped.

---

## R5 — Edge cases and operational completeness — /2

Evaluate whether important non-happy-path behavior is defined enough for the feature.

Consider when relevant:

* missing data;
* invalid states;
* zero results;
* duplicate actions;
* retries;
* permissions;
* concurrent actions;
* cancellation;
* partial failure;
* existing data;
* compatibility.

Do not require exhaustive edge cases for simple tasks.

### 2.0

Relevant edge behavior is sufficiently defined.

### 1.5

Minor cases remain open.

### 1.0

Some meaningful cases require interpretation.

### 0.5

Important behavior outside the happy path is undefined.

### 0.0

The ticket ignores critical conditions necessary to implement safely.

---

# Score calculation

Add the five readiness dimensions.

Example:

```text
Intent and expected outcome        2.0 / 2
Business rules and behavior        1.0 / 2
Acceptance and verifiability       1.5 / 2
Scope and dependencies             2.0 / 2
Edge cases                         1.0 / 2

Ticket Readiness Score: 7.5 / 10
```

Use increments of:

```text
0.5
```

Do not use fake precision such as:

```text
7.83 / 10
```

---

# Readiness status

Assign one of three statuses.

## READY

The ticket can reasonably move into analysis/design/implementation without requiring important product decisions from the developer.

Typical score:

```text
8.0–10.0
```

A ticket may still contain minor non-blocking questions.

---

## NEEDS CLARIFICATION

The objective is understandable, but one or more significant uncertainties should be resolved before implementation.

Typical score:

```text
5.0–7.5
```

This is not automatically a bad ticket.

It means clarification is needed.

---

## NOT READY

Critical information is missing.

Implementation would require the developer to invent requirements, scope, or expected behavior.

Typical score:

```text
0.0–4.5
```

The numerical ranges are guidance, not a substitute for judgment.

A ticket with one severe blocking ambiguity may be `NEEDS CLARIFICATION` even with a relatively high score.

---

# Blocking vs non-blocking questions

Every unresolved question must be classified.

## Blocking

A question is blocking when its answer could materially change:

* expected behavior;
* data model;
* business rules;
* API contract;
* security;
* scope;
* implementation direction;
* acceptance criteria.

Example:

```text
Can a customer have multiple active primary addresses?
```

If different answers produce materially different behavior, this is blocking.

---

## Non-blocking

A question is non-blocking when implementation can proceed safely without resolving it immediately.

Examples:

* exact wording of a secondary log message;
* minor naming decision;
* optional documentation detail;
* non-critical UI copy when behavior is already defined.

---

# Ticket analysis process

Follow this order.

## 1. Identify the ticket type

Determine whether the ticket is primarily:

* feature;
* bug;
* technical task;
* refactoring;
* migration;
* integration;
* operational work.

Do not force feature-ticket criteria onto technical maintenance work.

---

## 2. Restate the ticket objective

Summarize in one or two sentences:

* current problem;
* desired change;
* expected result.

If this cannot be done confidently, that is itself a readiness problem.

---

## 3. Extract confirmed information

Identify only what is explicitly established.

Possible categories:

* actors;
* existing behavior;
* expected behavior;
* business rules;
* affected systems;
* acceptance criteria;
* constraints;
* dependencies.

---

## 4. Identify assumptions

List assumptions required to understand the ticket.

Example:

```text
ASM-01 — "Active user" is assumed to mean a user whose account status is ACTIVE.
```

Do not silently rely on assumptions when scoring readiness.

---

## 5. Evaluate ambiguity

Look for ambiguous terms such as:

* active;
* current;
* available;
* valid;
* owner;
* admin;
* recent;
* duplicate;
* cancelled;
* deleted;
* default;
* eligible;
* authorized;
* optional.

Also look for ambiguous phrases:

```text
should work
handle correctly
support multiple
improve performance
fix the issue
make it dynamic
as usual
same behavior
```

Determine whether ambiguity materially affects implementation.

---

## 6. Evaluate acceptance criteria

Ask:

* Can the expected outcome be observed?
* Can a test be written?
* Is success clearly distinguishable from failure?
* Are important error cases defined?
* Are relevant state changes visible?

Do not penalize the absence of formal acceptance-criteria syntax when the ticket is otherwise objectively verifiable.

---

## 7. Evaluate edge cases

Consider only cases relevant to the ticket.

Do not manufacture dozens of theoretical edge cases.

Focus on situations likely to affect correctness.

---

## 8. Evaluate scope

Determine:

* what must change;
* what may change;
* what should not change;
* whether another system or team is involved;
* whether linked work is required.

Detect scope phrases such as:

```text
and also
while we're here
for all other cases
everywhere
across the application
```

which may hide substantially larger work.

---

## 9. Evaluate dependencies

Identify dependencies such as:

* another ticket;
* another team;
* external API;
* missing design;
* unavailable data;
* infrastructure;
* migration;
* feature flag;
* product decision.

A dependency is not automatically blocking.

Determine whether implementation can begin without it.

---

## 10. Check existing system context

When codebase or project documentation is available, use it to verify:

* whether the requested feature already partially exists;
* whether terminology matches the project;
* whether ticket assumptions contradict current behavior;
* whether scope is larger than the ticket suggests.

Do not convert the readiness check into a full codebase audit.

Inspect only enough context to evaluate the ticket.

---

## 11. Identify contradictions

Look for contradictions between:

* title and description;
* description and acceptance criteria;
* ticket and linked documentation;
* expected behavior and current rules;
* multiple acceptance criteria.

Every contradiction that affects behavior should be explicitly reported.

---

## 12. Evaluate testability

Ask:

> Could a developer or QA engineer determine whether this ticket is complete?

If not, identify what information is missing.

Do not require automated testing.

This is about behavioral verifiability.

---

## 13. Score readiness

Score each of the five dimensions independently.

Every deduction should correspond to an identified issue.

Do not start at 10 and arbitrarily subtract points.

---

## 14. Produce the readiness decision

Return:

```text
READY
```

or:

```text
NEEDS CLARIFICATION
```

or:

```text
NOT READY
```

Explain the decision briefly.

---

# Feature ticket considerations

For a feature, consider whether the ticket establishes:

* actor;
* trigger;
* expected behavior;
* business rules;
* state changes;
* permissions;
* important errors;
* acceptance criteria.

---

# Bug ticket considerations

For a bug, readiness often requires different information.

Look for:

* observed behavior;
* expected behavior;
* reproduction steps;
* environment when relevant;
* frequency;
* known affected scope;
* evidence such as logs or screenshots when necessary.

A bug ticket does not always need full reproduction steps if the defect is already obvious from code or monitoring.

Do not mechanically penalize missing template fields.

The real question remains:

> Can the defect be reliably understood and verified?

---

# Technical ticket considerations

For technical work, evaluate:

* technical objective;
* reason for the change;
* boundaries;
* expected outcome;
* affected system;
* constraints;
* compatibility expectations.

Technical tickets do not need artificial business acceptance criteria.

Example:

```text
Upgrade PostgreSQL 15 to PostgreSQL 17.
```

may be ready when compatibility, environment scope, validation, and rollback expectations are clear.

---

# Refactoring ticket considerations

For refactoring work, look for:

* reason for refactoring;
* target area;
* expected structural outcome;
* behavioral invariants;
* explicit requirement not to change external behavior;
* success criteria.

Avoid accepting:

```text
Refactor UserService
```

as ready unless the desired improvement is actually established.

---

# Findings

Each meaningful readiness issue should use:

```markdown
### TR-01 — <Short title>

**Severity:** BLOCKING / IMPORTANT / MINOR

**Observed:**  
...

**Missing or unclear:**  
...

**Why it matters:**  
...

**Question / action required:**  
...
```

---

# Severity

## BLOCKING

Implementation should not begin without clarification.

Use when the missing information could significantly change the behavior or design.

## IMPORTANT

The issue should be clarified, but useful work may still begin.

## MINOR

The issue is worth documenting but does not materially block progress.

Do not report cosmetic ticket-writing issues.

---

# Do not grade writing quality

This skill evaluates delivery readiness, not how professionally the ticket was written.

Do not penalize:

* spelling;
* grammar;
* informal wording;
* short descriptions;
* formatting;
* missing headings;
* absence of Jira templates.

A badly written ticket may still contain everything required.

A beautifully formatted ticket may still be unusable.

---

# Do not require unnecessary documentation

Avoid bureaucratic readiness criteria.

Do not require every ticket to contain:

* detailed technical solution;
* UML diagrams;
* implementation steps;
* database schema;
* test plan;
* exhaustive edge cases;
* architectural decisions.

Those may belong to later analysis or design.

Ticket readiness is about having enough information to proceed safely.

---

# Handoff to other skills

When the ticket is sufficiently ready, recommend the next logical analysis stage without performing it automatically unless requested.

Typical flow:

```text
ticket-readiness
        ↓
conceptual-analysis
        ↓
technical-design
        ↓
implementation
```

Not every ticket needs every stage.

For example:

```text
simple technical ticket
        ↓
implementation
```

may be perfectly appropriate.

Use proportional reasoning.

---

# Markdown deliverable

When filesystem access is available, always generate a persistent Markdown readiness report.

Use:

```text
docs/ticket-readiness/
```

Create the directory if necessary.

---

## File naming

When a ticket identifier is available:

```text
docs/ticket-readiness/JIRA-142.readiness.md
docs/ticket-readiness/PROJ-381.readiness.md
```

A descriptive suffix may be added when helpful:

```text
docs/ticket-readiness/JIRA-142-primary-subscription.readiness.md
```

Without an identifier:

```text
docs/ticket-readiness/user-permission-delegation.readiness.md
```

Do not overwrite an unrelated report.

If the existing report concerns the same ticket, update it instead of creating unnecessary duplicates.

---

# Required report structure

Use the following structure.

Omit irrelevant sections instead of creating empty headings.

```markdown
# Ticket Readiness — <Ticket or feature>

**Ticket:** <identifier when available>
**Type:** <Feature | Bug | Technical | Refactoring | Migration | Integration | Other>
**Readiness Score:** X / 10
**Status:** READY | NEEDS CLARIFICATION | NOT READY

## Summary

<Short explanation of the requested work.>

## Readiness score

| Dimension | Score |
|---|---:|
| Intent and expected outcome | X / 2 |
| Business rules and behavior | X / 2 |
| Acceptance and verifiability | X / 2 |
| Scope and dependencies | X / 2 |
| Edge cases and operational completeness | X / 2 |
| **Total** | **X / 10** |

## Confirmed information

- ...

## Assumptions

- ASM-01 — ...

## Findings

### TR-01 — <Finding>

**Severity:** BLOCKING

**Observed:**  
...

**Missing or unclear:**  
...

**Why it matters:**  
...

**Question / action required:**  
...

## Acceptance criteria assessment

### Clear

- ...

### Missing or ambiguous

- ...

## Scope

### Known scope

- ...

### Unclear scope

- ...

## Dependencies

- ...

## Questions requiring clarification

### Blocking

1. ...
2. ...

### Non-blocking

1. ...
2. ...

## Suggested clarifications

<Concise list of information that should be added to the ticket.>

## Readiness decision

**Status:** READY / NEEDS CLARIFICATION / NOT READY

**Reason:**  
...

## Recommended next step

<Conceptual analysis, technical design, implementation, product clarification, etc.>
```

---

# Example

Input:

```text
JIRA-142

Allow customers to change their main subscription.

A customer can have multiple subscriptions.

Add an endpoint to update the main subscription.
```

Possible assessment:

```text
Readiness Score: 6.0 / 10
Status: NEEDS CLARIFICATION
```

Main findings:

```text
TR-01 — Eligibility of a main subscription is undefined.

Can an inactive or cancelled subscription become the main subscription?

TR-02 — Behavior when the current main subscription changes is unclear.

Must the previous one automatically lose its main status?

TR-03 — Zero-main-subscription state is undefined.

Is a customer allowed to have no main subscription?
```

The ticket should not be marked `NOT READY` simply because these questions exist.

Use the severity and importance of the missing information to determine the final status.

---

# Completion response

After generating the report, respond concisely.

Example:

```text
Ticket readiness completed: JIRA-142

Readiness: 6.5 / 10
Status: NEEDS CLARIFICATION

Main blocker:
- Eligibility rules for the main subscription are not defined.

Other important question:
- It is unclear whether a customer may temporarily have no main subscription.

Recommended next step:
- Clarify the two business rules above, then run conceptual-analysis.

Report:
docs/ticket-readiness/JIRA-142.readiness.md
```

Do not duplicate the full Markdown report in the conversation when it has been successfully written.

If filesystem access is unavailable, return the complete report directly.

---

# Quality checklist

Before completing the assessment, verify that:

* the ticket itself was actually read;
* the ticket type was considered;
* readiness was evaluated rather than writing quality;
* missing information was not invented;
* assumptions are explicit;
* ambiguities are concrete;
* acceptance criteria were evaluated based on verifiability;
* scope was considered;
* dependencies were considered;
* relevant edge cases were considered;
* blocking and non-blocking questions are separated;
* unnecessary bureaucracy was avoided;
* a short but sufficient ticket was not unfairly penalized;
* a long but vague ticket was not unfairly rewarded;
* the score is justified by evidence;
* the status matches the actual blockers;
* the skill did not drift into technical design;
* the recommended next step is proportional to the ticket.

The objective is not to make every ticket exhaustive.

The objective is to determine whether enough information exists for a developer to proceed without inventing important requirements.