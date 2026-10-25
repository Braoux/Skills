# Pricing & Offer Validation

[Skill instructions](SKILL.md)

**But :** tester l'intérêt payant avant de développer un abonnement. Ce skill n'exige ni Stripe, ni Google Analytics, ni API, ni accès à un compte marchand.

**À fournir (si disponible) :** retours utilisateurs anonymisés, offre gratuite actuelle, contraintes de coût, clics sur une annonce d'offre clairement signalée comme non disponible, et données de paiements déjà existants.

**Exemple :** `/pricing-offer-validation Compare une offre gratuite + premium à une offre par packs, mais ne mets aucun système de paiement en production.`

**Sortie :** hypothèses de prix étiquetées, mini-protocole de test éthique, signal observé et décision prudente. Différencier intention d'acheter et transaction réussie.

**Scénarios manuels :** (1) pas de testeur → aucun prix validé ; (2) 15 réponses « je paierais » mais aucune transaction → intérêt déclaré seulement ; (3) « acheter » mène à une liste d'attente transparente → qualifier d'intérêt, pas de vente ; (4) dépense par analyse élevée → réviser l'offre avant de lancer un forfait illimité.

**Liens métier :** `player-demand-evidence` et `analysis-unit-economics`.

## Sans nouvelle clé API

Exécuter ce skill avec l'agent IA déjà en cours et les fichiers ou observations locaux que l'utilisateur a le droit d'utiliser. Aucun `requires.env`, fournisseur payant, SDK cloud, compte analytique, scraping ou nouveau credential n'est requis. En cas de données manquantes, produire une méthode de collecte et signaler ce qui n'a pas été mesuré. Le moteur IA sous-jacent à l'agent peut avoir sa propre configuration indépendante du skill.
