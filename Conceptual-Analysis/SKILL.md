````markdown
---
name: conceptual-analysis
description: Analyze business requirements conceptually before technical design and produce a persistent Markdown analysis.
---

# Conceptual Analysis

Analyze the business problem before proposing any technical solution.

The purpose of this skill is to make a requirement precise enough for technical design and implementation by identifying:

- domain concepts;
- relationships;
- business rules;
- invariants;
- lifecycle and states;
- ambiguities;
- assumptions;
- edge cases;
- consistency risks;
- unresolved business questions.

Do not jump directly to code or implementation details.

---

## Language

Write the analysis in the same language as the user's request unless another language is explicitly requested.

Keep domain terminology consistent with the terminology already used by the project, ticket, documentation, or user.

---

## When to use this skill

Use this skill when a request involves meaningful business or domain behavior, including:

- a new business feature;
- a Jira or issue-tracker ticket containing business rules;
- changes to an existing domain model;
- permissions or roles;
- ownership;
- validation rules;
- workflows;
- lifecycle or state transitions;
- relationships between business concepts;
- ambiguous requirements;
- behavior introducing constraints or invariants.

Examples:

- A customer can have several subscriptions but only one main subscription.
- Users can delegate approval rights to another employee.
- An invoice can be cancelled after validation under certain conditions.
- An administrator can temporarily suspend an account.
- A customer can have several delivery addresses.

Do not perform a full conceptual analysis for trivial or purely technical tasks such as:

- changing a button color;
- renaming a variable;
- updating a dependency;
- fixing CSS alignment;
- changing a log message;
- fixing a straightforward compilation error.

If an apparently simple task hides a domain decision, perform the analysis.

---

# Core rules

## Separate facts from assumptions

Never invent business rules.

Distinguish clearly between:

### Confirmed facts

Information explicitly stated by the requirement, ticket, documentation, existing system, or user.

### Deduced facts

Information that follows logically from confirmed facts without introducing additional assumptions.

### Assumptions

Reasonable interpretations that are not explicitly confirmed.

### Unknowns

Information that cannot currently be determined.

Never present an assumption as a confirmed fact.

If information is missing, expose the uncertainty instead of silently filling the gap.

---

## Stay implementation-independent

The conceptual analysis describes **what the domain means and requires**, not how the software will implement it.

Do not decide during this analysis:

- database tables;
- SQL constraints;
- indexes;
- ORM mappings;
- JPA annotations;
- REST endpoints;
- DTO structures;
- Java classes;
- Spring services;
- repositories;
- framework choices;
- caching strategies;
- message brokers;
- transaction strategies;
- locking mechanisms;
- infrastructure.

Technical consequences may be mentioned only at a high level when they expose an important constraint.

Good:

> The uniqueness of the main subscription must remain valid during concurrent changes.

Bad:

> Add a PostgreSQL unique partial index and use pessimistic locking.

Technical decisions belong to a later technical-design phase.

---

# Analysis process

Perform the following steps in order.

## 1. Understand the problem

Restate the requested behavior concisely.

Identify:

- what is changing;
- who is involved;
- what business outcome is expected;
- what existing behavior is affected.

Do not introduce a solution.

---

## 2. Extract confirmed facts

List the information explicitly established by the available sources.

Prefer short, precise statements.

Example:

- A customer may own several subscriptions.
- A subscription may be active or inactive.
- One subscription may be designated as the main subscription.

Do not include assumptions in this section.

---

## 3. Identify domain concepts

Extract the important business concepts involved.

For each significant concept, identify when relevant:

- its name;
- its definition;
- its meaning in the domain;
- its responsibilities;
- its relevant state.

Prefer domain vocabulary.

Good:

- Customer
- Subscription
- Delegation
- Approval
- Invoice

Avoid implementation terminology such as:

- CustomerEntity
- SubscriptionRepository
- ApprovalDTO
- InvoiceService

unless those terms are themselves part of the domain language.

---

## 4. Identify relationships

Describe how the concepts relate to one another.

When relevant, specify:

- ownership;
- dependency;
- cardinality;
- optionality;
- direction of the relationship.

Examples:

- A Customer may own zero or more Subscriptions.
- A Subscription belongs to exactly one Customer.
- An Employee may delegate permissions to another Employee.

Express relationships conceptually.

Do not translate them into ORM mappings.

---

## 5. Extract business rules

Identify the rules governing the behavior of the domain.

Give each relevant rule an identifier.

Example:

- BR-01 — A customer may own multiple subscriptions.
- BR-02 — Only an active subscription may be designated as main.
- BR-03 — A customer may have at most one main subscription.

Rules must remain independent from implementation choices.

---

## 6. Identify invariants

Identify conditions that must remain true regardless of which operation modifies the system.

Pay particular attention to:

- uniqueness;
- ownership;
- permissions;
- quantities;
- consistency;
- ordering;
- mutually exclusive states;
- mandatory relationships.

Give each invariant an identifier.

Example:

- INV-01 — A customer cannot have more than one active main subscription.

An invariant should describe the state that must remain valid, not the mechanism used to enforce it.

---

## 7. Analyze lifecycle and states

When a concept has meaningful states, identify:

- known states;
- allowed transitions;
- known transition triggers;
- forbidden transitions;
- unclear transitions.

Example:

```text
CREATED
   |
   v
ACTIVE
  /   \
 v     v
SUSPENDED
       |
       v
CANCELLED
````

Only include states or transitions supported by available information.

Mark uncertain transitions as unresolved.

Do not invent a complete state machine from incomplete requirements.

---

## 8. Identify domain operations

List the business operations implied by the requirement.

Examples:

* designate a subscription as main;
* revoke a delegation;
* approve a request;
* cancel an invoice;
* suspend an account.

For each important operation, identify when known:

* actor;
* target;
* preconditions;
* business result;
* affected rules;
* affected invariants.

Do not describe controllers, endpoints, methods, database queries, or implementation algorithms.

---

## 9. Identify ambiguities and unknowns

Actively search for terms or behaviors whose interpretation could materially change the feature.

Pay particular attention to words such as:

* active;
* owner;
* current;
* main;
* available;
* administrator;
* authorized;
* cancelled;
* valid;
* temporary.

For each important ambiguity, provide:

* what is known;
* what is unclear;
* plausible interpretations;
* why the distinction matters.

Do not choose an interpretation without supporting evidence.

---

## 10. Identify assumptions

List every assumption required to continue reasoning despite missing information.

Give each assumption an identifier.

Example:

* ASM-01 — It is assumed that a customer may temporarily have no main subscription.

Assumptions must never silently become business rules.

---

## 11. Identify edge cases

Look for meaningful boundary cases, including when relevant:

* zero related objects;
* multiple related objects;
* deletion;
* expiration;
* disabled actors;
* missing relationships;
* repeated operations;
* conflicting states;
* retries;
* historical data;
* existing legacy data;
* migration implications;
* simultaneous modifications.

Give significant edge cases identifiers.

Example:

* EC-01 — The current main subscription is cancelled.
* EC-02 — A customer has no active subscriptions.
* EC-03 — Two actors attempt to change the main subscription simultaneously.

Do not generate artificial edge cases merely to make the analysis longer.

---

## 12. Identify consistency and concurrency risks

Only include this analysis when the domain rules make it relevant.

Identify situations where simultaneous operations could violate a business rule or invariant.

Example:

> Two operations could attempt to designate different subscriptions as main at the same time.

Describe the conceptual consistency requirement.

Do not prescribe locking, transaction, database, or infrastructure mechanisms.

---

## 13. Compare with the existing domain

When the codebase, documentation, existing analysis, or project files are accessible:

* inspect the existing domain vocabulary;
* search for equivalent concepts;
* reuse existing terminology when appropriate;
* identify overlapping concepts;
* detect contradictions with existing rules;
* identify existing behavior affected by the change.

Do not introduce a new concept when an equivalent already exists without explaining the distinction.

The conceptual model must remain consistent with the existing domain unless the requirement explicitly changes it.

---

## 14. Challenge the model

After completing the initial analysis, actively challenge it.

Consider:

* Are two concepts actually the same concept?
* Is one term being used with several meanings?
* Can another operation violate an identified invariant?
* Does deletion create an invalid domain state?
* What happens when there are no related objects?
* What happens when there are several?
* Is an apparently optional relationship actually mandatory?
* Is historical information expected to remain available?
* Are permissions attached to the correct actor?
* Can simultaneous operations produce contradictory states?
* Does the existing domain already provide an equivalent concept?
* Does a business rule contradict another rule?

Only report challenges that materially affect understanding of the requirement.

---

## 15. Determine blocking questions

Separate unresolved questions into:

### Blocking questions

Questions whose answer could materially alter:

* the conceptual model;
* a business rule;
* an invariant;
* the lifecycle;
* the expected behavior;
* the future technical design.

### Non-blocking questions

Questions that can safely be resolved later without materially changing the conceptual model.

Do not declare the analysis ready for technical design while important blocking questions remain.

---

# Markdown deliverable

Always produce a Markdown document containing the complete conceptual analysis.

When filesystem access is available, write the document to the project or workspace.

Use this directory by default:

```text
docs/conceptual-analysis/
```

Create the directory if necessary.

Do not overwrite an unrelated existing analysis.

---

## File naming

Use a descriptive kebab-case filename.

Examples:

```text
docs/conceptual-analysis/main-subscription-selection.md
docs/conceptual-analysis/user-permission-delegation.md
docs/conceptual-analysis/invoice-cancellation.md
```

When a ticket or issue identifier exists, include it.

Examples:

```text
docs/conceptual-analysis/JIRA-142-user-permission-delegation.md
docs/conceptual-analysis/PROJ-381-invoice-cancellation.md
```

Preserve the identifier exactly as provided by the source system.

Avoid generic filenames such as:

```text
analysis.md
concept.md
notes.md
```

unless no meaningful name can reasonably be inferred.

If the chosen filename already exists and corresponds to the same feature or ticket, update that analysis rather than creating unnecessary duplicate documents.

If it corresponds to another subject, choose another filename.

---

# Required document structure

The generated Markdown document should follow this structure.

Omit sections that are genuinely irrelevant rather than leaving empty headings.

```markdown
# Conceptual Analysis — <Feature or Ticket>

**Status:** Draft
**Source:** <ticket, requirement, request, or other source>
**Ticket:** <identifier, when available>
**Completeness:** <Partial | Ready for technical design>

## Problem summary

<Concise description of the business problem and expected behavior.>

## Confirmed facts

- ...

## Domain concepts

### <Concept>

**Definition:**  
...

**Meaning / responsibility:**  
...

**Relevant state:**  
...

## Relationships

- ...

## Business rules

- BR-01 — ...
- BR-02 — ...

## Invariants

- INV-01 — ...
- INV-02 — ...

## States and lifecycle

...

## Domain operations

### <Operation>

**Actor:**  
...

**Target:**  
...

**Preconditions:**

- ...

**Result:**  
...

**Affected rules / invariants:**

- ...

## Ambiguities and unknowns

### A-01 — <Title>

**Known:**  
...

**Unclear:**  
...

**Possible interpretations:**

- ...
- ...

**Impact:**  
...

## Assumptions

- ASM-01 — ...

## Edge cases

- EC-01 — ...
- EC-02 — ...

## Consistency and concurrency risks

- ...

## Questions requiring clarification

### Blocking

1. ...
2. ...

### Non-blocking

1. ...
2. ...

## Conceptual model

<Compact textual or Mermaid representation of the resulting domain model.>

## Analysis status

**Ready for technical design:** Yes / No

**Reason:**  
...
```

---

# Conceptual model

End the analysis with a compact representation of the resulting model.

Use a simple textual model when that is clearer.

Example:

```text
Customer
  |
  | owns 0..N
  v
Subscription
  |
  +-- status
  +-- main

Invariant:
For a given Customer, no more than one active Subscription may be main.
```

A Mermaid diagram may be used when it materially improves readability.

Keep the diagram conceptual.

Do not expose classes, tables, repositories, controllers, DTOs, or framework-specific objects.

---

# Completeness decision

Set:

```text
Completeness: Partial
```

when unresolved blocking questions remain.

Set:

```text
Completeness: Ready for technical design
```

only when the available information is sufficient to establish the important:

* concepts;
* relationships;
* rules;
* invariants;
* lifecycle;
* expected behavior.

Minor non-blocking questions do not necessarily prevent technical design.

---

# Completion response

After writing the Markdown file, respond concisely with:

* what was analyzed;
* the most important concepts;
* the most important invariants;
* any blocking questions;
* whether the analysis is ready for technical design;
* the path of the generated Markdown file.

Example:

```text
Conceptual analysis completed.

Main concepts:
- Customer
- Subscription
- Main subscription

Critical invariant:
- A customer cannot have more than one active main subscription.

Blocking question:
- It is unclear whether a customer may have no main subscription.

Ready for technical design: No

Analysis:
docs/conceptual-analysis/JIRA-142-main-subscription.md
```

Do not duplicate the entire Markdown analysis in the conversation after successfully writing the file.

If filesystem access is unavailable, return the complete Markdown document directly and clearly state that it could not be persisted.

---

# Quality criteria

Before completing the task, verify that the analysis:

* uses domain vocabulary rather than implementation vocabulary;
* clearly separates facts, deductions, assumptions, and unknowns;
* does not invent business rules;
* identifies important concepts and relationships;
* identifies significant business rules;
* identifies important invariants;
* exposes meaningful ambiguities;
* identifies relevant edge cases;
* identifies consistency risks when applicable;
* distinguishes blocking from non-blocking questions;
* does not prematurely design the implementation;
* remains proportional to the complexity of the requirement;
* is understandable without reading the source code;
* is useful to both a human developer and another agent;
* has been saved to the expected Markdown file when filesystem access is available.

The objective is not to maximize the amount of analysis.

The objective is to make the business problem precise enough that technical design can begin with minimal ambiguity.

```