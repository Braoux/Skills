# Documents, éditions et référentiels

## Finalité

Ce domaine fournit les ressources partagées qui structurent les achats : documents, modèles, éditions, référentiels, organisation, processus et paramètres.

## GED et documents

**OBSERVED**

Des documents peuvent être rattachés aux prévisions, consultations, passations, contrats et actes. Selon la configuration, ils sont stockés localement ou via un serveur CMIS/SharePoint.

Fonctions observées :

- créer des dossiers métier ;
- ajouter, télécharger, remplacer ou supprimer des documents selon les droits/états ;
- associer des métadonnées métier ;
- importer des pièces de plis ;
- préparer des documents pour signature ;
- vérifier le format et l’état avant transmission.

## Éditions

**OBSERVED**

L’application produit des éditions standards et configurables : documents de consultation, courriers de candidature/offre, notification, contrat, actes et états de suivi.

Certaines éditions sont générées une fois par fournisseur et peuvent être regroupées dans une archive.

Les modèles, thèmes et clauses sont administrables et réutilisés dans la rédaction des consultations et contrats.

## Référentiels d’achat

### Familles d’achat

Référentiel propre à la collectivité, utilisé par prévisions, consultations/lots, fournisseurs et recherche. Les valeurs peuvent être activées/désactivées.

### CPV

Référentiel de classification externe/commun utilisé pour qualifier les achats et fournisseurs. Les recherches peuvent porter sur le code ou le libellé.

### Opérations / unités fonctionnelles

Référentiel opérationnel utilisé pour rattacher et contrôler des besoins et enveloppes. Son affichage peut dépendre du paramétrage.

### Autres bibliothèques

**OBSERVED**

Le produit contient notamment :

- imputations ;
- critères ;
- justificatifs ;
- pénalités ;
- index et valeurs d’index ;
- formules ;
- articles, familles d’articles et unités ;
- contacts/intervenants ;
- tâches et processus ;
- états et modèles d’édition ;
- liens utiles.

## Organisation et sécurité fonctionnelle

La bibliothèque Organisation administre collectivités/organismes, services, utilisateurs et profils. Les profils regroupent les permissions utilisées dans tous les modules.

## Processus configurables

**OBSERVED**

Des workflows/processus peuvent associer des tâches, champs et conditions aux dossiers. Ils influencent la disponibilité ou la validation d’une étape et peuvent mettre à jour des échéances.

## Paramétrage

Les paramètres divers couvrent notamment :

- modes de fonctionnement ;
- numérotation ;
- TVA ;
- jours fériés ;
- correspondances externes ;
- serveurs ;
- GED ;
- personnalisation de l’accueil.

Les variations doivent être documentées pour tout ticket dépendant d’un paramètre.

## Règles et contraintes

- Les référentiels sont généralement isolés par collectivité.
- Une valeur inactive peut rester liée à des données historiques sans être proposée pour une nouvelle sélection.
- Les suppressions de référentiel peuvent être empêchées lorsqu’une valeur est utilisée ; l’activation/désactivation est souvent distincte de la suppression.
- Un serveur externe doit être actif et cohérent avec son contexte d’utilisation.
- Les modèles et éditions sont soumis à des droits d’administration distincts de leur simple exécution.

## Inconnues

**UNKNOWN**

- Les politiques exactes de rétention documentaire ne sont pas définies de manière suffisamment explicite.
- Le comportement de suppression physique dans chaque stockage externe nécessite une analyse dédiée.

## Preuves

- Modules frontend `ged`, `document-models`, `editions`, `libraries`.
- `GedServiceImpl`, processeurs GED et intégration parapheur.
- `EditionServiceImpl` et types d’éditions.
- `AuthoritiesEnum.java` — droits d’administration des bibliothèques.
- `assets/libraries/libraries.json` — catalogue de bibliothèques.

