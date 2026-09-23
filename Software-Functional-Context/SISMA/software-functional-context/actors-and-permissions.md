# Acteurs et permissions

## Modèle général

**OBSERVED**

Les actions sont autorisées par des codes de permission associés aux profils. La visibilité d’un module et la disponibilité d’une action dépendent d’au moins un droit adapté, parfois aussi d’une licence ou d’un paramètre actif.

Le dépôt distingue trois niveaux fonctionnels récurrents :

- **consultation** : lecture et navigation ;
- **utilisateur actif** : création, saisie, modification, validation ou dévalidation ;
- **administration** : gestion des référentiels, paramètres, profils et organisation.

Ces niveaux sont des regroupements documentaires ; les autorisations effectives restent les codes individuels.

## Lecteur métier

Peut, selon son profil :

- consulter prévisions, consultations et contrats ;
- consulter les étapes de passation ;
- consulter les fournisseurs et référentiels ;
- consulter actes, commandes et données d’exécution ;
- exécuter certaines éditions.

Il ne peut pas être supposé qu’un lecteur puisse modifier ou valider un objet.

Exemples de droits techniques : `CNSBSN`, `PCOAFF`, `PCACON`, `MARCNS`, `ENTREC`.

## Gestionnaire des besoins

Peut, selon ses droits :

- créer, modifier, valider et supprimer une prévision ;
- importer des prévisions ;
- créer une consultation vide, depuis une prévision ou comme marché subséquent ;
- rédiger et valider des clauses ;
- lancer, modifier, valider ou supprimer une consultation.

La création depuis une prévision requiert un droit distinct de la simple création de consultation.

## Gestionnaire de passation

Les droits sont séparés par étape et par action. Pour chacune des étapes candidature, lancement, ouverture, analyse, attribution et notification, un profil peut disposer indépendamment des capacités suivantes :

- consulter ;
- traiter/saisir ;
- valider ;
- dévalider.

Des droits complémentaires existent pour les réunions et ordres du jour.

## Gestionnaire fournisseurs

Peut, selon son profil :

- consulter la bibliothèque fournisseurs ;
- créer ou mettre à jour une fiche ;
- activer un fournisseur ;
- valider ou supprimer une fiche ;
- consulter ou saisir des évaluations.

La gestion historique des IBAN/RIB possède des droits dédiés et comporte des fonctions signalées comme obsolètes dans le catalogue des droits.

## Gestionnaire contractuel

Les permissions distinguent :

- contrats : consulter, créer, valider, dévalider, supprimer, modifier le numéro ;
- actes d’exécution : consulter, créer, valider, dévalider, supprimer ;
- actes modificatifs : mêmes familles d’actions avec des droits distincts ;
- commandes : consulter, créer, valider, supprimer, modifier le numéro.

## Gestionnaire opérationnel

Lorsque le module est actif, des droits distincts contrôlent :

- prestations ;
- calculs ;
- règlements ;
- demandes de paiement ;
- imports de consommés et journaux de reprise.

La consultation, la création, la validation, le forçage et la suppression peuvent être accordés séparément.

## Administrateur fonctionnel

Peut administrer tout ou partie des éléments suivants :

- familles d’achat et opérations ;
- imputations, critères, justificatifs et pénalités ;
- articles, familles d’articles et unités ;
- index et formules ;
- éditions et modèles ;
- organisation, services, profils et utilisateurs ;
- processus et champs associés ;
- serveurs et paramètres divers.

## Processus système et traitements planifiés

**OBSERVED**

Des traitements techniques importent ou synchronisent des actualités, registres de dématérialisation, statuts de signature, données externes et reprises. Ils peuvent produire des notifications applicatives ou mettre à jour des dossiers sans interaction directe au moment de l’exécution.

## Inconnues

**UNKNOWN**

- La composition effective des profils de chaque déploiement n’est pas définie dans le code.
- Il n’est pas possible de garantir qu’un intitulé de rôle organisationnel correspond à un ensemble stable de permissions entre collectivités.

## Preuves

- `AuthoritiesEnum.java` — libellés fonctionnels, catégories de droits, licences et poids d’usage.
- Fichiers de module AngularJS — permissions nécessaires pour afficher modules et actions.
- Contrôleurs et services — contrôles serveur et opérations protégées.

