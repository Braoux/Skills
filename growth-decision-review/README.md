# Growth Decision Review

[Skill instructions](SKILL.md)

**But :** faire travailler les autres skills au service d'une seule décision : ce qui rapproche le produit de revenus viables, plutôt que multiplier les tickets.

**À fournir :** rapports locaux ou notes issus des skills `player-demand-evidence`, `activation-retention-audit`, `matchup-trust-gate`, `organic-acquisition-experiments`, `pricing-offer-validation` et `analysis-unit-economics`. Il peut fonctionner avec seulement une partie de ces documents.

**Exemple :** `/growth-decision-review Fais notre revue produit/business hebdomadaire. Maximum trois expériences, chacune avec mesure et condition d'arrêt, sans création automatique de ticket.`

**Résultat :** six signaux documentés, goulot d'étranglement, maximum trois décisions et ce qu'il faut arrêter de développer pour l'instant. Aucune donnée de marché ou chiffre d'affaires inventé.

**Scénarios manuels :** (1) aucun rapport → un plan de mesure, pas un business score inventé ; (2) acquisition élevée mais première analyse défaillante → priorité fiabilité ; (3) conversion payante mesurée mais marge négative → traiter coûts/prix avant croissance ; (4) deux rapports contradictoires → signaler la contradiction et proposer une mesure discriminante.

## Sans nouvelle clé API

Exécuter ce skill avec l'agent IA déjà en cours et les fichiers ou observations locaux que l'utilisateur a le droit d'utiliser. Aucun `requires.env`, fournisseur payant, SDK cloud, compte analytique, scraping ou nouveau credential n'est requis. En cas de données manquantes, produire une méthode de collecte et signaler ce qui n'a pas été mesuré. Le moteur IA sous-jacent à l'agent peut avoir sa propre configuration indépendante du skill.
