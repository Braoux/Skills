# Contexte fonctionnel portable de SIS Marchés

## Objet

Ce package décrit le comportement fonctionnel actuellement observable de SIS Marchés. Il est destiné à des agents ou lecteurs qui doivent analyser une évolution sans disposer du dépôt source.

Il ne constitue ni une spécification produit future, ni un manuel utilisateur exhaustif. Les constats sont qualifiés comme suit :

- **OBSERVED** : démontré directement par le dépôt ;
- **INFERRED** : fortement suggéré par plusieurs éléments, sans règle métier explicite ;
- **UNKNOWN** : non déterminable avec les preuves disponibles.

**Généré le :** 23 septembre 2026  
**Branche analysée :** `SM-17825`

## SIS Marchés en bref

SIS Marchés accompagne le cycle des achats publics : expression et planification du besoin, préparation des consultations, passation, gestion des fournisseurs, création et suivi des contrats, actes, commandes, prestations, calculs, règlements, paiements, documents et pilotage.

Le comportement disponible dépend des droits du profil, des licences actives et de paramètres propres à la collectivité.

## Navigation

### Version compacte

- [Contexte fonctionnel agrégé](software-functional-context.compact.md)

### Vue globale

- [Présentation fonctionnelle](overview.md)
- [Glossaire](glossary.md)
- [Acteurs et permissions](actors-and-permissions.md)
- [Règles métier transverses](business-rules.md)
- [Intégrations](integrations.md)

### Domaines

- [Prévisions et consultations](domains/previsions-consultations.md)
- [Passation](domains/passation.md)
- [Fournisseurs](domains/fournisseurs.md)
- [Contrats et exécution](domains/contrats-execution.md)
- [Documents, éditions et référentiels](domains/documents-referentiels.md)

### Workflows

- [Du besoin au contrat](workflows/du-besoin-au-contrat.md)
- [Valider une étape de passation](workflows/validation-passation.md)
- [Enrichir un fournisseur à la Notification](workflows/enrichissement-fournisseur-notification.md)

## Guide d’utilisation pour un ticket

- Ticket sur les besoins, prévisions, lots, familles d’achat ou opérations/UF : commencer par `domains/previsions-consultations.md`.
- Ticket sur les candidats, offres, attribution ou notification : lire `domains/passation.md` et `workflows/validation-passation.md`.
- Ticket sur la recherche ou la fiche fournisseur : lire `domains/fournisseurs.md`.
- Ticket sur un marché, acte, commande ou paiement : lire `domains/contrats-execution.md`.
- Ticket sur la GED, les éditions ou une plateforme externe : lire `domains/documents-referentiels.md` et `integrations.md`.
- Toujours consulter `business-rules.md` pour les effets transverses et `actors-and-permissions.md` pour les contrôles d’accès.

## Limites connues de cette génération

- Le dépôt contient des fonctions historiques « Version 7 » et des modules optionnels ; leur présence dans le code ne prouve pas leur activation dans une installation donnée.
- Les libellés fonctionnels des droits sont documentés, mais la composition réelle des profils dépend des données de chaque collectivité.
- Certains états sont portés par des codes provenant de dépendances ou de tables de référence ; seuls les états et transitions directement observables ont été retenus.
- Les comportements décrits sont ceux du code analysé, pas nécessairement l’intention produit cible.
