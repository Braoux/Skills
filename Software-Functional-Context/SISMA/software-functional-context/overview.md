# Présentation fonctionnelle

## Finalité de l’application

**OBSERVED**

SIS Marchés est une application de gestion des achats et marchés publics. Elle couvre plusieurs moments du cycle de vie :

1. planifier un besoin sous forme de prévision d’achat ;
2. préparer une consultation et sa structure contractuelle ;
3. conduire la passation jusqu’à la notification ;
4. créer ou reprendre un contrat ;
5. suivre les actes, commandes et événements d’exécution ;
6. gérer les prestations, calculs, règlements et demandes de paiement lorsque le module de suivi opérationnel est actif ;
7. conserver et produire les documents associés ;
8. exploiter des référentiels partagés et des fonctions de pilotage.

## Utilisateurs

**OBSERVED**

L’application est utilisée par des agents d’une collectivité ou organisation. Les capacités sont découpées par domaine et par action : consulter, créer/saisir, modifier, valider, dévalider, supprimer, importer ou administrer.

Les profils et services organisationnels regroupent ces droits. Une installation peut limiter les modules visibles selon les licences et le paramétrage de la collectivité.

## Principaux espaces fonctionnels

### Accueil

L’accueil fournit une recherche transversale et peut restituer des consultations, contrats et prévisions selon les droits de l’utilisateur. Il expose aussi des liens, actualités, alertes ou tâches selon les modules actifs.

### Besoins

L’espace Besoins contient les prévisions d’achat et les projets de consultation. Une consultation peut être créée vide, comme marché subséquent ou depuis une prévision.

### Passation

La passation organise le traitement d’une consultation par étapes : candidature, lancement, ouverture, analyse, attribution et notification. Toutes les étapes ne sont pas nécessairement utilisées de façon identique selon la procédure.

### Fournisseurs

La bibliothèque fournisseurs centralise l’identité, les contacts, les adresses, les informations d’activité, les familles d’achat, les CPV, les mots-clés, les évaluations et les relations avec consultations et contrats.

### Suivi contractuel et opérationnel

Le suivi contractuel porte les contrats, actes et commandes. Le suivi opérationnel ajoute notamment prestations, calculs, règlements, factures ou demandes de paiement lorsqu’il est licencié et autorisé.

### Bibliothèques et paramétrage

Des bibliothèques administrent les familles d’achat, opérations, imputations, critères, justificatifs, pénalités, index, formules, articles, éditions, modèles documentaires, organisation, processus et paramètres divers.

## Frontières fonctionnelles importantes

**OBSERVED**

- Les données sont isolées par collectivité dans de nombreuses recherches et associations.
- Les droits sont évalués à la fois pour afficher les modules/actions et pour autoriser les opérations serveur.
- Les processus configurables peuvent ajouter des tâches et des contrôles aux validations.
- Les intégrations externes sont conditionnées par un serveur/configuration actif ; leur absence peut masquer l’action ou provoquer une erreur fonctionnelle de paramétrage.
- La GED et les éditions accompagnent plusieurs domaines sans constituer un cycle d’achat indépendant.

## Cycle de vie principal

**INFERRED**

Le parcours nominal est :

`Prévision → Projet de consultation → Passation → Notification → Contrat → Exécution`

Cette chaîne est appuyée par les écrans, les routes et les services de transformation. Elle n’est pas obligatoire dans tous les cas : un contrat peut être créé ou importé directement, et une consultation peut être créée sans prévision.

## Variabilité par installation

**OBSERVED**

Le produit contient des variantes activées par :

- licences fonctionnelles ;
- droits du profil ;
- paramètres collectivité ;
- serveurs externes actifs ;
- type de procédure ou de contrat ;
- processus configuré.

Il ne faut donc pas déduire qu’un écran présent dans le dépôt est visible pour tous les utilisateurs.

## Preuves principales

- Registre des modules AngularJS sous `sis-smw-webapp/src/main/html/src/sis-modules`.
- `AuthoritiesEnum.java` — catalogue fonctionnel des droits et licences.
- Contrôleurs REST sous `sis-smw-core/.../web/rest`.
- Services métier et tests sous `sis-smw-core/.../modules`.

