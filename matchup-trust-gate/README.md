# Matchup Trust Gate

[Skill instructions](SKILL.md)

**When to use:** before public alpha campaigns, after patch updates, when users flag bad advice, or when changes touch generation, repair or validation.

**Inputs:** locally available reports from golden runners, fact packs, validator diagnostics, production failure exports and voluntary anonymized player feedback. Use a human League of Legends reviewer for disputed tactical conclusions.

**Outputs:** auditable severity ledger, no invented accuracy scores, and release/hold recommendation. Favor blocking obviously harmful high-confidence tactical claims over adding more analysis sections.

**Example invocation:** `/matchup-trust-gate Audite ces échecs V2 et ces cas golden, sans appel à un LLM externe ni modification de production.`

**Manual verification scenarios:** (1) no gameplay facts → mark verdict unverified; (2) single person dislikes a trade plan → contested, not automatically false; (3) explicit known cooldown violation backed by current evidence → confirmed; (4) patch changes → mark stale fixtures.

**Related:** `player-demand-evidence` to see whether users find validated advice useful.

## No-key execution contract

Use this skill in an already-running agent by providing existing local files, public materials already available, or anonymized data. No `OPENAI_API_KEY`, `requires.env`, additional network API, integration or paid account is required. When evidence is absent, the skill produces a collection plan instead of imaginary conclusions. Any model credentials needed to operate the user's chosen AI agent are outside the skill and are never requested by this skill.
