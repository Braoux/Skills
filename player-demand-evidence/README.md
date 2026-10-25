# Player Demand Evidence

[Skill instructions](SKILL.md)

**When to use:** before feature expansion, after alpha player tests, or when engagement seems weak. Use anonymized interview notes, screenshots of consented test observations, and event exports where available. No API key or browser automation required.

**Suggested minimum note per participant:** participant code; consenting segment; test date; last real incident described; task attempted; completion observed; perceived usefulness; actual return (if measurable); trust objections; source evidence. Avoid collecting summoner names, emails or other personal identifiers by default.

**Outputs:** evidence-led recommendation, no fake sample sizes. A 5-person exploratory round can reveal problems but does not establish market representativeness.

**Example invocation:** `/player-demand-evidence Analyse ces 7 retours anonymisés, distingue ce qui est observé de ce qui est déclaré, et prépare nos prochains tests.`

**Manual verification scenarios:** (1) Only feature ideas supplied → mark demand unmeasured; (2) three friendly interviews → flag selection bias; (3) repeat visits available for a known cohort → compute eligibility and observed returns; (4) contradictory feedback from ADC vs support → segment rather than averaging.

**Related:** `activation-retention-audit` (quantitative behavior) and `pricing-offer-validation` (actual payment intent).

## No-key execution contract

Use this skill in an already-running agent by providing existing local files, public materials already available, or anonymized data. No `OPENAI_API_KEY`, `requires.env`, additional network API, integration or paid account is required. When evidence is absent, the skill produces a collection plan instead of imaginary conclusions. Any model credentials needed to operate the user's chosen AI agent are outside the skill and are never requested by this skill.
