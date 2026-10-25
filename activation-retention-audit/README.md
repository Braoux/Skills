# Activation & Retention Audit

[Skill instructions](SKILL.md)

**When to use:** after an alpha has actual traffic, when a slow analysis might cause abandonment, and before paying for acquisition.

**Local-only inputs:** sanitized CSV/JSON, server logs, event schema documentation, anonymized SQL snapshots. No mandatory analytics service and no credentials in the skill.

**Minimal event fields:** `occurred_at,event_name,anonymous_visitor_id,session_id,device,source,analysis_status`. The sample template `templates/events.csv` contains headers only. Do not add email/IP/account names.

**Suggested event vocabulary:** `page_view,champion_select_started,champion_selection_complete,analysis_requested,analysis_usable,analysis_failed,return_visit`. An already streamed valid section counts as usable only if product confirms it offers real value.

**Example invocation:** `/activation-retention-audit Étudie mon export local des événements, avec les taux d'activation et des cohortes D7 si elles sont mûres.`

**Manual verification scenarios:** (1) only server logs with no visitor id → no per-user retention; (2) repeated events for one session → deduplicate; (3) all users registered yesterday → no D7 retention; (4) missing `analysis_usable` → instrument before claiming conversion.

**Related:** `player-demand-evidence` for why behavior matters and `growth-decision-review` for roadmap prioritization.

## No-key execution contract

Use this skill in an already-running agent by providing existing local files, public materials already available, or anonymized data. No `OPENAI_API_KEY`, `requires.env`, additional network API, integration or paid account is required. When evidence is absent, the skill produces a collection plan instead of imaginary conclusions. Any model credentials needed to operate the user's chosen AI agent are outside the skill and are never requested by this skill.
