# Analysis Unit Economics

[Skill instructions](SKILL.md)

**But :** savoir si le modèle économique tient réellement lorsque les utilisateurs et le nombre d'analyses augmentent. Fonctionne avec des fichiers CSV/Markdown locaux, sans accès API à Render, DeepSeek ou un service bancaire.

**Entrées :** dépenses réellement facturées, nombre de requêtes, cache HIT/MISS, réparations, analyses utilisables, frais fixes, prix testés et charges variables. `templates/cost-inputs.csv` fournit uniquement les en-têtes d'un format possible.

**Exemple :** `/analysis-unit-economics Calcule le coût par analyse utile et simule 50, 200 et 1 000 abonnés avec des hypothèses explicites.`

**Fichier de sortie :** table de coûts, équations reproductibles, trois scénarios et un plafond de risque. Aucune précision artificielle si les factures, les volumes ou les taux manquent.

**Scénarios manuels :** (1) coût 5 € et aucune analyse utile → division impossible ; (2) contribution unitaire négative → pas de point mort ; (3) 80 % cache HIT mais appels coûteux sur MISS → pondérer correctement ; (4) mêmes frais déjà compris dans le forfait → ne pas compter deux fois.

**Liens métier :** `pricing-offer-validation` et `growth-decision-review`.

## Sans nouvelle clé API

Exécuter ce skill avec l'agent IA déjà en cours et les fichiers ou observations locaux que l'utilisateur a le droit d'utiliser. Aucun `requires.env`, fournisseur payant, SDK cloud, compte analytique, scraping ou nouveau credential n'est requis. En cas de données manquantes, produire une méthode de collecte et signaler ce qui n'a pas été mesuré. Le moteur IA sous-jacent à l'agent peut avoir sa propre configuration indépendante du skill.
