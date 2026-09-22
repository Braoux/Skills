````markdown
---
name: architectural-audit
description: Audit the architectural cleanliness of a file or entire project, identify structural issues, and produce an explainable cleanliness score out of 10.
---

# Architectural Audit

Analyze the architectural quality of source code without focusing on formatting, linting, or cosmetic style rules.

This skill can operate at two levels:

1. **File audit** — audit one specific file in its architectural context.
2. **Project audit** — audit the architecture of an entire project or significant subsystem.

The file audit is the primary and preferred mode when a specific file is provided.

The purpose is to answer:

> Is this code structurally clean, well-placed, understandable, maintainable, and consistent with the architecture around it?

Every audit must produce an **Architectural Cleanliness Score from 0 to 10**.

---

# Core philosophy

Architecture is not about enforcing patterns for their own sake.

Do not penalize code merely because it:

- does not use a particular design pattern;
- does not follow textbook DDD;
- is not split into many classes;
- uses procedural code where procedural code is sufficient;
- contains a long method that remains conceptually coherent;
- does not introduce abstractions that are unnecessary.

Prefer simple, explicit, maintainable code over artificial architectural sophistication.

Do not reward abstraction merely because abstraction exists.

Do not recommend additional layers, interfaces, factories, wrappers, services, repositories, or patterns unless they solve an identified structural problem.

---

# Explicit exclusions

Ignore issues that belong primarily to a linter, formatter, or basic static-analysis tool.

Do NOT reduce the score because of:

- indentation;
- whitespace;
- formatting;
- line length;
- semicolons;
- quote style;
- import ordering;
- unused imports;
- trivial naming conventions;
- brace placement;
- blank lines;
- basic syntax style;
- Prettier differences;
- ESLint formatting rules;
- Checkstyle formatting rules;
- trivial compiler warnings;
- cosmetic code style.

Do not fill the report with these issues.

They are outside the scope of this skill.

However, a naming issue may be mentioned when it creates a genuine architectural misunderstanding.

Example:

A class named `UserService` that actually handles authentication, billing, notifications, persistence, and reporting may indicate an architectural responsibility problem.

That is relevant.

Whether the variable is named `userId` or `userID` is not.

---

# Audit modes

## File audit

Use this mode when the user provides or identifies a specific source file.

Examples:

```text
Audit UserService.java
````

```text
Run an architectural audit on src/services/payment.ts
```

```text
Is this controller architecturally clean?
```

The target file is the unit being scored.

You may inspect surrounding code when available to understand its architectural context.

Relevant contextual files may include:

* directly imported project files;
* interfaces implemented by the target;
* parent or base classes;
* consumers of the target;
* closely related domain objects;
* adjacent services;
* tests;
* dependency injection configuration;
* module declarations;
* package structure.

Do not transform a file audit into an uncontrolled project-wide audit.

Contextual files exist to help evaluate the target file.

Only the requested file receives the score.

---

## Project audit

Use this mode when the user requests an audit of:

* an entire project;
* a repository;
* a module;
* a bounded subsystem;
* an application architecture.

Inspect enough of the project to understand:

* major modules;
* architectural layers;
* dependency directions;
* domain boundaries;
* entry points;
* infrastructure;
* persistence;
* external integrations;
* shared modules;
* cross-cutting concerns.

Do not assume that every directory must be inspected exhaustively.

Prioritize architecturally significant files and dependency boundaries.

---

# Determine the mode

If a specific file is explicitly provided, use:

```text
Mode: FILE
```

If a repository, project, module, or subsystem is provided without a specific file, use:

```text
Mode: PROJECT
```

If a file is provided as part of a broader project audit, evaluate it as project evidence rather than automatically switching to file mode.

---

# General audit rules

## Read before judging

Do not score architecture based only on filenames or directory names.

Inspect the relevant source.

When context is available, verify assumptions against the surrounding code.

---

## Distinguish evidence from inference

Separate:

* observed architectural facts;
* likely architectural implications;
* assumptions caused by missing context.

Do not treat an assumption as a confirmed defect.

If something cannot be determined from the available code, say so.

---

## Judge architecture in context

A file cannot always be evaluated correctly in isolation.

For example, a dependency on an interface may look unnecessary until its alternate implementations are inspected.

A controller may appear thin only because business logic has been correctly delegated elsewhere.

A service may appear coupled to persistence until the project's architecture shows that this is intentional.

Use surrounding code when necessary.

However, do not penalize the target for architectural problems that clearly belong elsewhere.

---

# File audit criteria

For a FILE audit, score five dimensions.

Each dimension is scored from **0 to 2**.

Total:

```text
10 points
```

---

## F1 — Responsibility and cohesion — /2

Evaluate whether the file has a clear reason to exist and whether its responsibilities belong together.

Look for:

* Single clear responsibility.
* Related behavior grouped coherently.
* Business concerns that belong together.
* Unrelated responsibilities accumulated in one file.
* "God class" or "God service" behavior.
* Controllers doing application or domain work.
* Domain objects handling infrastructure concerns.
* Utility files becoming dumping grounds.

### 2.0

Responsibility is clear and cohesive.

### 1.5

Mostly cohesive with minor responsibility leakage.

### 1.0

Several responsibilities are mixed but the file remains understandable.

### 0.5

Major responsibility confusion.

### 0.0

The file acts as an architectural dumping ground.

---

## F2 — Coupling and dependencies — /2

Evaluate what the file depends on and why.

Look for:

* number and nature of dependencies;
* dependency direction;
* unnecessary knowledge of unrelated components;
* direct infrastructure coupling;
* hidden dependencies;
* global state;
* static dependencies;
* circular dependency risks;
* excessive orchestration across unrelated components.

Do not penalize a file merely because it has several imports.

The important question is whether those dependencies are architecturally justified.

### 2.0

Dependencies are focused, explicit, and appropriate.

### 1.5

Some unnecessary or slightly awkward coupling exists.

### 1.0

The file depends on several things it should probably not know about.

### 0.5

Strong coupling makes changes risky.

### 0.0

The file is deeply entangled with unrelated parts of the system.

---

## F3 — Boundaries and abstraction level — /2

Evaluate whether the file respects architectural boundaries and operates at a coherent level of abstraction.

Look for mixtures such as:

* HTTP logic mixed with business logic;
* SQL mixed with application orchestration;
* domain logic mixed with framework behavior;
* persistence concerns leaking into domain objects;
* infrastructure details leaking into higher layers;
* high-level orchestration mixed with low-level implementation details.

Also detect unnecessary abstraction.

A direct implementation is preferable when an abstraction has no useful architectural purpose.

### 2.0

The file operates at a clear and coherent architectural level.

### 1.5

Small boundary leaks exist but remain controlled.

### 1.0

Several abstraction levels or architectural concerns are mixed.

### 0.5

Boundaries are poorly respected.

### 0.0

No meaningful architectural separation is visible.

---

## F4 — Changeability and testability — /2

Evaluate how safely the file can evolve.

Ask:

* Can behavior be changed without touching many unrelated concerns?
* Are important dependencies controllable?
* Can business behavior be tested without excessive infrastructure?
* Are changes likely to produce broad side effects?
* Is state management understandable?
* Are extension points present where they are genuinely useful?
* Does the design make common changes unnecessarily difficult?

Do not require interfaces or dependency injection mechanically.

A concrete dependency is not automatically bad.

Judge whether the current design creates actual change or testing friction.

### 2.0

The file is easy to change and its important behavior is easy to isolate.

### 1.5

Minor friction exists.

### 1.0

Common changes require touching several concerns or difficult setup.

### 0.5

The structure strongly resists change or isolated testing.

### 0.0

Changes are highly risky because responsibilities and dependencies cannot be isolated.

---

## F5 — Architectural coherence — /2

Evaluate whether the file fits naturally into the surrounding architecture.

Look for:

* consistency with project boundaries;
* consistency with existing domain concepts;
* appropriate package/module placement;
* duplication of architectural responsibilities;
* bypassing established abstractions;
* competing ways of performing the same architectural operation;
* unexpected dependency direction.

Do not reward blind conformity.

If the existing project architecture is poor, a file should not lose points merely because it improves on that architecture.

In that situation, explicitly explain the discrepancy.

### 2.0

The file fits cleanly into the surrounding architecture.

### 1.5

Minor inconsistencies exist.

### 1.0

The file partially bypasses or duplicates existing architectural structures.

### 0.5

The file significantly conflicts with the surrounding architecture.

### 0.0

Its role in the architecture is fundamentally unclear or contradictory.

---

# Project audit criteria

For a PROJECT audit, score five dimensions.

Each dimension is scored from **0 to 2**.

---

## P1 — Separation of responsibilities — /2

Evaluate whether the project has understandable architectural responsibilities.

Look for:

* modules with clear purposes;
* separation between business behavior and infrastructure;
* services with coherent responsibilities;
* concentration of unrelated functionality;
* dumping-ground modules;
* overly centralized components.

---

## P2 — Boundaries and dependency direction — /2

Evaluate:

* module boundaries;
* layer boundaries;
* dependency direction;
* circular dependencies;
* domain-to-infrastructure leakage;
* direct dependencies between unrelated areas;
* inappropriate shared modules.

Architecture does not need to be layered.

Judge the dependency model that actually exists.

---

## P3 — Domain and structural coherence — /2

Evaluate whether the project's concepts and modules form a coherent system.

Look for:

* clear domain concepts;
* duplicate representations of the same concept;
* inconsistent vocabulary;
* duplicated architectural responsibilities;
* competing patterns for equivalent operations;
* unclear ownership of functionality.

---

## P4 — Changeability and isolation — /2

Evaluate the likely impact of common changes.

Ask:

* Can one feature evolve without modifying unrelated areas?
* Are external systems isolated appropriately?
* Are business rules localized?
* Can modules be understood independently?
* Does shared code create hidden coupling?
* Does changing one concept ripple throughout the repository?

---

## P5 — Architectural simplicity — /2

Evaluate whether the architecture achieves its goals without unnecessary complexity.

Look for:

* unnecessary layers;
* abstraction without meaningful variation;
* excessive indirection;
* interfaces with single meaningless implementations;
* factories that provide no architectural value;
* generic frameworks built for hypothetical future needs;
* duplicated infrastructure abstractions;
* premature extensibility.

Also look for the opposite problem:

* giant modules;
* no meaningful boundaries;
* central services controlling everything.

The best architecture is not the architecture with the most patterns.

Prefer the simplest structure that preserves clear responsibilities and safe change.

---

# Scoring

Add the five dimension scores.

Example:

```text
Responsibility and cohesion     1.5 / 2
Coupling and dependencies       1.0 / 2
Boundaries and abstraction      1.5 / 2
Changeability and testability   1.5 / 2
Architectural coherence         2.0 / 2

Architectural Cleanliness Score: 7.5 / 10
```

Scores may use increments of:

```text
0.5
```

Do not use fake precision such as:

```text
7.83 / 10
```

---

# Score interpretation

Use the following scale for explanation only.

Do not mechanically force the result into a category before analyzing the code.

## 9.0–10.0 — Very clean

Architecture is clear, focused, and easy to evolve.

Remaining issues are minor.

## 8.0–8.5 — Clean

Good architectural structure with a few meaningful improvements possible.

## 7.0–7.5 — Generally healthy

The architecture is workable and understandable but contains structural weaknesses worth addressing.

## 5.0–6.5 — Fragile

Several architectural issues create unnecessary coupling, unclear responsibilities, or difficult changes.

## 3.0–4.5 — Poor

Significant structural problems affect maintainability and reasoning.

## 0.0–2.5 — Critical

Responsibilities and dependencies are deeply entangled and substantial restructuring is likely required.

---

# Scoring principles

The score must be justified by evidence.

Never assign a score because the code merely "feels clean".

Every meaningful deduction should correspond to an observed structural issue.

Do not start from 10 and arbitrarily subtract points.

Evaluate each dimension independently.

Do not lower multiple dimensions for exactly the same problem unless it genuinely affects several architectural properties.

Example:

A service containing HTTP parsing, SQL queries, domain decisions, and email sending may legitimately affect:

* responsibility;
* coupling;
* boundaries;
* changeability.

Explain the impact instead of silently applying repeated penalties.

---

# Severity levels

Classify findings using:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Use these levels architecturally.

## CRITICAL

A structural issue threatens fundamental correctness or makes major parts of the architecture unsafe to evolve.

Use rarely.

## HIGH

A major architectural problem that creates substantial coupling, boundary violation, or responsibility confusion.

## MEDIUM

A real architectural weakness that increases maintenance cost but does not fundamentally compromise the design.

## LOW

A minor structural improvement.

Do not create LOW findings for cosmetic style.

---

# Findings

Every finding should contain:

```markdown
### A-01 — <Short title>

**Severity:** HIGH

**Evidence:**  
<What was observed and where.>

**Why it matters:**  
<Architectural consequence.>

**Recommendation:**  
<Concrete structural improvement.>
```

Recommendations must address the architectural problem rather than merely changing its appearance.

Bad recommendation:

```text
Rename this method.
```

unless the name itself creates architectural ambiguity.

Good recommendation:

```text
Move invoice eligibility decisions out of the controller and into the existing invoice domain/application component so that HTTP handling no longer owns business rules.
```

---

# Avoid dogmatic pattern enforcement

Do not report an issue merely because a known principle appears to be violated.

Examples include:

* SOLID;
* DRY;
* DDD;
* Clean Architecture;
* Hexagonal Architecture;
* CQRS;
* Repository pattern;
* Factory pattern.

These concepts may be used as reasoning tools.

They are not goals by themselves.

For example:

Do not say:

```text
This violates SRP.
```

Prefer:

```text
This class has three independent reasons to change: pricing rules, persistence orchestration, and notification delivery. A pricing change therefore risks affecting infrastructure behavior.
```

Explain the concrete consequence.

---

# Duplication

Do not automatically treat duplication as an architectural defect.

Some duplication may be preferable to creating inappropriate coupling.

Report duplication only when it reveals:

* duplicated business rules;
* duplicated architectural responsibilities;
* multiple competing representations of the same concept;
* repeated logic that creates consistency risk.

---

# File size

Do not score based on raw line count.

A 500-line cohesive parser may be architecturally cleaner than five fragmented classes with unnecessary indirection.

File size is relevant only when it reflects responsibility accumulation or poor separation.

---

# Method size

Do not penalize a long method solely because it is long.

Evaluate:

* conceptual coherence;
* number of responsibilities;
* abstraction levels;
* hidden side effects;
* changeability.

Do not turn architectural audits into clean-code style reviews.

---

# Comments and documentation

Do not lower architectural cleanliness merely because comments or documentation are missing.

Mention missing documentation only when architectural intent cannot reasonably be understood from the project and that uncertainty creates maintenance risk.

---

# Tests

Tests may be inspected as architectural evidence.

Use them to understand:

* public responsibilities;
* dependency boundaries;
* coupling;
* expected behavior;
* changeability.

Do not reduce the architectural score merely because test coverage is low.

Test coverage is not the purpose of this skill.

Poor testability caused by architecture is relevant.

Missing tests themselves are not.

---

# Framework usage

Do not penalize framework-specific code simply because it depends on a framework.

Framework coupling becomes relevant when it:

* leaks into domain concepts unnecessarily;
* prevents isolation of important business behavior;
* spreads infrastructure concerns across unrelated layers;
* significantly increases the cost of change.

---

# File audit process

When auditing one file:

1. Read the complete target file.
2. Identify its apparent responsibility.
3. Identify its dependencies.
4. Identify the architectural layer or role it appears to belong to.
5. Inspect enough surrounding code to verify that role when available.
6. Identify business, application, infrastructure, transport, persistence, and orchestration concerns present in the file.
7. Detect responsibility mixing.
8. Detect inappropriate coupling.
9. Detect boundary leaks.
10. Evaluate changeability and testability.
11. Compare it with surrounding architecture.
12. Identify findings.
13. Score each of the five FILE dimensions.
14. Calculate the final score.
15. Produce the audit report.

Do not modify source code unless explicitly asked.

The audit is read-only by default.

---

# Project audit process

When auditing a project:

1. Identify the project structure.
2. Identify primary entry points.
3. Identify major modules or packages.
4. Identify dependency direction.
5. Identify business/domain areas.
6. Identify infrastructure boundaries.
7. Inspect representative architecturally significant files.
8. Inspect suspicious dependency hotspots.
9. Identify cross-module coupling.
10. Identify duplicated architectural responsibilities.
11. Identify unnecessary complexity.
12. Identify missing or weak boundaries.
13. Identify strengths worth preserving.
14. Score each PROJECT dimension.
15. Calculate the final score.
16. Produce the audit report.

Do not attempt to read every generated, vendor, build, or dependency file.

Ignore when appropriate:

```text
node_modules/
target/
build/
dist/
coverage/
vendor/
generated/
.git/
```

Also ignore generated source unless it materially affects the architecture being evaluated.

---

# Positive observations

An audit must not consist only of criticism.

Identify architectural decisions that are working well.

Examples:

* clear dependency direction;
* cohesive domain service;
* good isolation of infrastructure;
* simple design without unnecessary abstraction;
* consistent module boundaries;
* clear orchestration;
* appropriate use of interfaces;
* business rules located in a stable place.

This helps distinguish intentional strengths from accidental structure.

---

# Prioritization

After findings, identify the most valuable improvements.

Use:

```text
Priority 1
Priority 2
Priority 3
```

Priorities are based on architectural impact, not implementation ease.

Do not generate a large refactoring backlog for minor issues.

Prefer the smallest set of changes that would materially improve the architecture.

---

# Markdown deliverable

Always produce a persistent Markdown audit when filesystem access is available.

Use:

```text
docs/architecture-audit/
```

Create the directory if necessary.

---

## File audit naming

For a target such as:

```text
src/main/java/com/example/user/UserService.java
```

prefer:

```text
docs/architecture-audit/UserService.audit.md
```

If filename collisions are possible, include meaningful path context:

```text
docs/architecture-audit/user-UserService.audit.md
```

---

## Project audit naming

Prefer:

```text
docs/architecture-audit/project.audit.md
```

For a subsystem:

```text
docs/architecture-audit/payment-module.audit.md
```

Do not overwrite an unrelated existing audit.

---

# File audit report format

Use this structure:

```markdown
# Architectural Audit — <filename>

**Mode:** File  
**Target:** `<path>`  
**Architectural Cleanliness Score:** X / 10

## Executive summary

<Short assessment of the architectural state of the file.>

## Architectural role

**Observed responsibility:**  
...

**Likely layer / role:**  
...

**Relevant dependencies:**  
...

## Score

| Dimension | Score |
|---|---:|
| Responsibility and cohesion | X / 2 |
| Coupling and dependencies | X / 2 |
| Boundaries and abstraction level | X / 2 |
| Changeability and testability | X / 2 |
| Architectural coherence | X / 2 |
| **Total** | **X / 10** |

## Strengths

- ...
- ...

## Findings

### A-01 — <Finding>

**Severity:** HIGH

**Evidence:**  
...

**Why it matters:**  
...

**Recommendation:**  
...

## Priority improvements

### Priority 1

...

### Priority 2

...

### Priority 3

...

## Final assessment

<Explain what mainly determines the score and what would most improve it.>
```

Do not force three priority items if fewer meaningful changes exist.

---

# Project audit report format

Use this structure:

```markdown
# Architectural Audit — <project>

**Mode:** Project  
**Target:** `<project or module>`  
**Architectural Cleanliness Score:** X / 10

## Executive summary

...

## Architecture observed

<Describe the architecture that actually exists rather than the architecture you expected to find.>

## Score

| Dimension | Score |
|---|---:|
| Separation of responsibilities | X / 2 |
| Boundaries and dependency direction | X / 2 |
| Domain and structural coherence | X / 2 |
| Changeability and isolation | X / 2 |
| Architectural simplicity | X / 2 |
| **Total** | **X / 10** |

## Strengths

- ...
- ...

## Findings

### A-01 — <Finding>

**Severity:** HIGH

**Evidence:**  
...

**Why it matters:**  
...

**Recommendation:**  
...

## Architectural hotspots

- ...
- ...

## Priority improvements

### Priority 1

...

### Priority 2

...

### Priority 3

...

## Final assessment

...
```

---

# User-facing completion response

After producing the report, respond concisely.

For a file audit:

```text
Architectural audit completed: UserService.java

Cleanliness: 7.5 / 10

Main strength:
- Business orchestration is clearly centralized.

Main issue:
- Persistence and notification responsibilities leak into the service.

Highest-priority improvement:
- Separate infrastructure side effects from the core use-case orchestration.

Report:
docs/architecture-audit/UserService.audit.md
```

For a project audit:

```text
Architectural audit completed.

Cleanliness: 6.5 / 10

Main strengths:
- Clear module organization.
- Domain logic is mostly isolated.

Main issue:
- Several modules depend directly on infrastructure implementations.

Highest-priority improvement:
- Restore a clear dependency boundary around persistence and external integrations.

Report:
docs/architecture-audit/project.audit.md
```

Do not duplicate the complete report in the conversation when the Markdown file has been successfully created.

If filesystem access is unavailable, provide the complete audit directly instead.

---

# Quality checklist

Before completing an audit, verify that:

* the correct audit mode was used;
* the target source was actually inspected;
* relevant architectural context was inspected when available;
* the score measures architecture rather than formatting;
* lint issues were ignored;
* findings are supported by evidence;
* assumptions are clearly identified;
* no design pattern was imposed dogmatically;
* unnecessary abstraction was not rewarded;
* simplicity was considered a positive quality;
* test coverage itself was not scored;
* actual testability was considered;
* strengths were identified;
* findings were prioritized;
* every score dimension is justified;
* the final score is consistent with the detailed scores;
* recommendations address architectural causes rather than cosmetic symptoms;
* the generated report is understandable by a developer who did not perform the audit.

The goal is not to enforce a theoretical ideal architecture.

The goal is to determine how cleanly the code separates responsibilities, controls dependencies, preserves understandable boundaries, and supports safe future change.

```

J’ai notamment fait en sorte qu’un **fichier de 500 lignes puisse avoir 9/10 s’il est cohérent**, tandis qu’un fichier de 80 lignes plein d’abstractions inutiles puisse se faire descendre. C’est important pour éviter que le skill se transforme en pseudo-Sonar déguisé.