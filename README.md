````markdown
# OpenClaw Skills

A collection of reusable OpenClaw skills designed to improve how AI agents analyze problems, reason about software, and execute development-related tasks.

This repository serves as a shared library of specialized skills that can be reused across multiple OpenClaw agents and workspaces.

---

## Purpose

Instead of embedding every behavior directly inside an agent prompt, this repository separates reusable capabilities into dedicated skills.

The general idea is:

```text
Agent
  |
  +-- Skill: Conceptual Analysis
  +-- Skill: Technical Design
  +-- Skill: Code Review
  +-- Skill: Ticket Analysis
  +-- ...
````

Each skill focuses on one responsibility and can evolve independently.

This makes agents easier to maintain, extend, test, and reuse.

---

## Repository structure

```text
Skills/
├── README.md
│
├── conceptual-analysis/
│   ├── SKILL.md
│   └── README.md
│
├── technical-design/
│   ├── SKILL.md
│   └── README.md
│
├── code-review/
│   ├── SKILL.md
│   └── README.md
│
└── ...
```

Each skill lives in its own directory.

The main skill definition is always stored in:

```text
SKILL.md
```

A skill may also contain additional resources such as:

```text
README.md
examples/
templates/
scripts/
references/
```

when they are useful.

---

## Available skills

### Conceptual Analysis

Location:

```text
conceptual-analysis/
```

Purpose:

Analyze a business requirement before technical design or implementation.

It identifies:

* domain concepts;
* relationships;
* business rules;
* invariants;
* states and lifecycle;
* ambiguities;
* assumptions;
* edge cases;
* consistency risks;
* blocking questions.

It can also produce a persistent Markdown analysis under:

```text
docs/conceptual-analysis/
```

See:

```text
conceptual-analysis/README.md
```

for complete documentation.

---

## Planned skills

This repository is intended to grow progressively.

Possible future skills include:

### Technical Design

Transform a validated conceptual analysis into an implementation-oriented technical design.

Potential topics:

* architecture;
* components;
* data model;
* APIs;
* persistence;
* transactions;
* concurrency;
* integration points;
* technical risks.

### Code Review

Review a code change with a consistent methodology.

Potential topics:

* correctness;
* readability;
* maintainability;
* performance;
* security;
* test coverage;
* architectural consistency.

### Ticket Analysis

Analyze an issue-tracker ticket and determine what information is required before implementation.

Potential topics:

* acceptance criteria;
* missing information;
* affected areas;
* dependencies;
* risks;
* required analysis.

### Codebase Analysis

Explore an existing project before making changes.

Potential topics:

* architecture;
* modules;
* domain concepts;
* dependencies;
* conventions;
* existing implementations;
* likely impact areas.

These skills are not necessarily implemented yet.

The repository should favor useful, well-defined skills over creating a large number of overlapping ones.

---

## Design principles

Skills in this repository should follow several principles.

### One clear responsibility

A skill should solve a specific category of problem.

Avoid large skills that attempt to handle the entire software-development lifecycle.

Prefer:

```text
conceptual-analysis
technical-design
implementation
code-review
```

over:

```text
do-everything-developer
```

---

### Reusable

Skills should avoid unnecessary assumptions about:

* a specific project;
* company-specific processes;
* one programming language;
* one framework;
* one issue tracker.

Project-specific behavior should generally live in the agent or workspace configuration rather than inside a reusable skill.

---

### Explicit boundaries

A skill should clearly state what it does and what it does not do.

For example, a conceptual-analysis skill should not silently become a technical-design skill.

Clear boundaries reduce unpredictable agent behavior.

---

### Facts before assumptions

Skills should distinguish between:

* confirmed facts;
* deductions;
* assumptions;
* unknowns.

Missing information should be exposed rather than silently invented.

---

### Proportional reasoning

The depth of the analysis should match the complexity of the task.

A simple problem should not generate unnecessary documentation.

A complex domain problem should receive deeper analysis when required.

---

### Persistent artifacts when useful

When a task produces information that should survive beyond the current conversation, the skill should prefer generating a reusable artifact.

For example:

```text
docs/conceptual-analysis/
docs/technical-design/
```

This allows future developers and agents to reuse previous work.

---

## Language

Skill definitions are written in English.

Generated outputs should generally use the same language as the user's request unless explicitly instructed otherwise.

This keeps the skills portable while preserving a natural user experience.

---

## Adding a new skill

Create a new directory:

```text
my-new-skill/
```

Then add at minimum:

```text
my-new-skill/
└── SKILL.md
```

Recommended structure:

```text
my-new-skill/
├── SKILL.md
├── README.md
└── examples/
```

The `SKILL.md` should clearly define:

* the purpose of the skill;
* when it should be used;
* when it should not be used;
* its analysis or execution process;
* expected outputs;
* important constraints;
* quality criteria.

Avoid duplicating responsibilities already covered by another skill.

---

## Naming conventions

Use lowercase kebab-case for skill directories.

Good:

```text
conceptual-analysis
technical-design
code-review
ticket-analysis
```

Avoid:

```text
ConceptualAnalysis
technical_design
CodeReviewSkill
skill-v2-final
```

Skill names should describe the capability rather than the implementation technology.

---

## Versioning

Changes to skills should be committed through Git so their evolution remains traceable.

Useful examples:

```text
feat: add conceptual analysis skill
feat: add technical design skill
fix: prevent conceptual analysis from inventing business rules
docs: document skill structure
refactor: simplify code review workflow
```

When changing an existing skill, preserve its intended responsibility unless the change explicitly introduces a breaking behavioral change.

---

## Security

Never commit secrets or environment-specific credentials to this repository.

Do not include:

```text
.env
API keys
access tokens
passwords
credentials
private certificates
cookies
session data
```

Runtime state from OpenClaw should also remain outside the repository unless explicitly required and safe to version.

---

## Contributing

When adding or modifying a skill:

1. Keep the responsibility narrow.
2. Avoid unnecessary overlap with existing skills.
3. Define clear triggering conditions.
4. Define clear boundaries.
5. Make assumptions explicit.
6. Keep outputs deterministic where practical.
7. Add documentation when the behavior is not self-explanatory.
8. Prefer examples that demonstrate realistic usage.

---

## Status

This repository is under active development.

The first available skill is:

```text
conceptual-analysis
```

Additional skills will be added as reusable agent workflows are identified and refined.

```