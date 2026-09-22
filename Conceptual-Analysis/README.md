````markdown
# Conceptual Analysis Skill

A reusable OpenClaw skill for analyzing business requirements before technical design or implementation.

The skill helps transform an incomplete requirement, feature request, or issue-tracker ticket into a structured conceptual analysis focused on the business domain.

It deliberately avoids premature technical decisions.

---

## Purpose

Developers and AI coding agents often move too quickly from:

```text
Requirement
    ↓
Implementation
````

This skill introduces an explicit conceptual analysis step:

```text
Requirement
    ↓
Conceptual Analysis
    ↓
Technical Design
    ↓
Implementation
```

The goal is to understand **what the system must represent and guarantee** before deciding how it should be implemented.

---

## What the skill analyzes

The skill identifies and documents:

* domain concepts;
* relationships between concepts;
* business rules;
* invariants;
* states and lifecycle;
* domain operations;
* ambiguities;
* assumptions;
* edge cases;
* consistency and concurrency risks;
* blocking and non-blocking questions.

It also challenges the resulting model to detect contradictions, missing rules, and unclear domain behavior.

---

## Example

Given a requirement such as:

> A customer may have several subscriptions but only one main subscription.

The skill may identify:

### Concepts

* Customer
* Subscription
* Main subscription

### Relationships

```text
Customer
  |
  | owns 0..N
  v
Subscription
```

### Business rules

* A customer may own multiple subscriptions.
* A subscription belongs to one customer.
* A subscription may be designated as the main subscription.

### Invariant

```text
For a given customer, no more than one active subscription may be marked as main.
```

### Open questions

* Can a customer have no main subscription?
* Can an inactive subscription remain the main subscription?
* What happens when the current main subscription is cancelled?
* Can two concurrent operations attempt to select different main subscriptions?

The skill exposes these questions before implementation begins.

---

## What this skill does not do

This skill intentionally avoids technical design.

It does not decide:

* database schemas;
* SQL constraints;
* ORM mappings;
* JPA annotations;
* REST endpoints;
* DTO structures;
* Java classes;
* Spring services;
* repository implementations;
* caching;
* message brokers;
* locking strategies;
* infrastructure.

For example:

Good conceptual analysis:

```text
The uniqueness of the main subscription must remain valid during concurrent changes.
```

Too technical:

```text
Use a PostgreSQL partial unique index and pessimistic locking.
```

Implementation decisions belong to a later technical-design phase.

---

## Markdown output

The skill generates a persistent Markdown document containing the complete analysis.

By default, analyses are stored under:

```text
docs/conceptual-analysis/
```

Example:

```text
docs/conceptual-analysis/JIRA-142-user-permission-delegation.md
```

If a ticket identifier is available, it is included in the filename.

The generated analysis contains sections such as:

```text
Problem summary
Confirmed facts
Domain concepts
Relationships
Business rules
Invariants
States and lifecycle
Domain operations
Ambiguities and unknowns
Assumptions
Edge cases
Consistency and concurrency risks
Questions requiring clarification
Conceptual model
Analysis status
```

---

## Analysis status

The generated document indicates whether the conceptual analysis is ready to move to technical design.

Possible states:

```text
Partial
```

Important business questions are still unresolved.

or:

```text
Ready for technical design
```

The main concepts, relationships, rules, invariants, and expected behavior are sufficiently defined.

The skill distinguishes between:

* **blocking questions**, which may change the conceptual model;
* **non-blocking questions**, which can safely be resolved later.

---

## Language

The skill instructions are written in English.

The generated analysis uses the same language as the user's request unless another language is explicitly requested.

For example:

```text
Analyse conceptuellement ce ticket :
un utilisateur peut déléguer ses droits à un autre utilisateur.
```

will produce the analysis in French.

---

## When to use it

This skill is useful for:

* new business features;
* Jira or issue-tracker tickets;
* domain-model changes;
* permissions and roles;
* workflows;
* ownership rules;
* state transitions;
* validation rules;
* relationships between domain concepts;
* unclear or incomplete business requirements.

It is especially useful when a feature appears simple but may hide important business decisions.

---

## When not to use it

A full conceptual analysis is usually unnecessary for purely technical or trivial tasks such as:

* changing a button color;
* renaming a variable;
* fixing CSS alignment;
* updating a dependency;
* changing a log message;
* fixing a straightforward compilation error.

If the task contains a hidden business decision, however, the skill may still be relevant.

---

## Project structure

```text
conceptual-analysis/
├── SKILL.md
└── README.md
```

The actual OpenClaw skill definition is contained in:

```text
SKILL.md
```

---

## Usage

Install or place the skill in an OpenClaw workspace so that OpenClaw can discover the `SKILL.md`.

Then invoke it when a requirement needs conceptual analysis.

Example request:

```text
Analyze conceptually:

A company administrator can delegate invoice approval rights
to another employee for a limited period.
```

The skill will analyze the domain and generate the corresponding Markdown document.

---

## Design principles

The skill follows a few core principles:

### Domain before implementation

Understand the business model before designing the software solution.

### Facts before assumptions

Missing information must be exposed instead of invented.

### Explicit invariants

Important consistency rules should be clearly identified.

### Ambiguity is useful information

An unclear requirement should remain visible until it is resolved.

### Proportional analysis

Simple requirements should produce concise analyses.

Complex domains should receive deeper analysis.

The objective is not to generate the longest possible document.

The objective is to make the requirement precise enough for technical design to begin with minimal ambiguity.

---

## Status

Initial version.

This skill is currently focused exclusively on conceptual and domain analysis.

```