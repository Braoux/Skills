# Zero-key revenue skills — practical workflow

These seven skills are **reusable decision aids**. They do not require new API keys, OAuth connections, paid external tools, or new dependency installs. An already-running AI agent is still required to interpret their `SKILL.md` instructions; its own model configuration is separate.

## Priority by observed business constraint

| If the biggest unknown is… | Start here |
| --- | --- |
| Do players truly need this repeatedly? | [Player Demand Evidence](player-demand-evidence/SKILL.md) |
| Why do people quit before receiving value? | [Activation & Retention Audit](activation-retention-audit/SKILL.md) |
| Can the product be trusted to give correct advice? | [Matchup Trust Gate](matchup-trust-gate/SKILL.md) |
| How do we find qualified players without ads? | [Organic Acquisition Experiments](organic-acquisition-experiments/SKILL.md) |
| What will people actually pay for? | [Pricing & Offer Validation](pricing-offer-validation/SKILL.md) |
| Will revenue exceed the marginal cost of usage? | [Analysis Unit Economics](analysis-unit-economics/SKILL.md) |
| What are the next 3 decisions to make? | [Growth Decision Review](growth-decision-review/SKILL.md) |

## Usage

1. Copy an individual **complete directory** into the skill directory supported by your agent, or point it to the `SKILL.md`. The repository does not provide a universal installer.
2. Supply permitted **local**, anonymized inputs such as alpha-test notes, sanitized event CSVs, golden runner results, invoice summaries or previous reports.
3. Invoke the skill by natural language or by its canonical name if the agent supports invocation. Example: `/growth-decision-review Analyse les données anonymisées de BotDiff; ne propose que trois actions.`
4. Keep output under the **private project workspace**, never commit player data, finances, event logs or internal analysis to this public repository.
5. If a requested source is unavailable, say **NOT MEASURED** and give the next manual collection step. Never fabricate a conversion, market demand, keyword volume or pay intent.

## Sensible order for an early-stage game analytics product

**Demand → Trust → Activation → Acquisition → Price test → Unit margin**, re-evaluated weekly by **Growth Decision Review**. Iterate rather than treating this as a rigid waterfall. An obviously negative unit margin can be measured earlier and block additional spending.

**The existing [UX Persona Audit](UX%20Persona%20Audit/SKILL.md) is different:** its AI-analysis implementation currently requires `OPENAI_API_KEY`. Only its capture-only mode avoids that key. None of the seven skills in this page depend on that UX persona implementation.

## Hard safety boundaries

- Real behavior beats simulated personas. Do not treat synthetic users as proof of product-market fit.
- No spam, stealth marketing, bots generating fake traffic, unauthorized scraping, or invented policy approval.
- No processing of raw private player details, employer secrets or other restricted material in the public repository.
- No autonomously sending messages, creating public posts, activating paid plans, writing issues, merging or deploying without explicit permission.
- Treat all business outcomes as uncertain and revisit the evidence. These skills cannot guarantee revenue.
