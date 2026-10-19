# Ticket Readiness

Canonical skill name: **`ticket-readiness`**. The containing directory `Ticket-Readyness` retains an older spelling for compatibility.

[Read the skill instructions](SKILL.md).

Use it to determine whether a Jira ticket, GitHub issue or other development request is sufficiently clear and verifiable **before implementation**. The output includes a justified score out of ten, a readiness status, blockers and optional Markdown report.

~~~text
Review ticket ABC-142 for implementation readiness.
Identify missing acceptance criteria, assumptions and blocking questions.
Do not implement or design the solution.
~~~

This is not a writing-quality score. For deeper business modelling use [Conceptual Analysis](../Conceptual-Analysis/SKILL.md); once requirements are clear use [Technical Design](../Technical-Design/SKILL.md).
