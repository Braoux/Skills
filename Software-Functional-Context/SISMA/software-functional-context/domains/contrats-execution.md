# Contrats et exécution

## Finalité

Ce domaine suit les marchés/contrats après attribution : données contractuelles, titulaires, actes, commandes, prestations, calculs, règlements et paiements.

## Contrats

**OBSERVED**

Un contrat peut être :

- créé depuis l’espace de suivi ;
- produit à partir d’une passation/notifiée ;
- importé depuis une procédure ;
- repris ou importé en liste selon les droits et modules actifs.

La fiche comporte des généralités, fournisseurs/titulaires, montants, délais, prix, index/formules, imputations, prévisions d’origine, documents et données d’exécution selon le type de contrat.

### Actions

Les droits distinguent consultation, création/saisie, validation, dévalidation, suppression et modification du numéro.

**INFERRED**

Les visas de contrat distinguent au minimum des états de saisie, à valider et validé. Des états plus détaillés existent pour les tranches/phases et variantes de reprise ; ils ne sont pas tous normalisés dans ce document.

## Actes

**OBSERVED**

Les actes représentent des événements d’exécution ou de modification du contrat. Le produit distingue au moins les actes d’exécution et les actes modificatifs, avec droits indépendants.

Exemples observés dans l’interface et les traitements :

- avenant ;
- reconduction ;
- affermissement de tranche ;
- événements de garantie ou d’état du marché selon les modules historiques.

Un acte peut être créé, consulté, validé, dévalidé et supprimé selon son type et les droits.

## Commandes

**OBSERVED**

Les bons de commande sont rattachés à un contrat. L’utilisateur autorisé peut consulter la liste, créer une commande, la valider, la supprimer et modifier son numéro.

Une commande peut porter ses propres prévisions d’origine lorsque le paramètre d’affichage correspondant est actif.

## Suivi opérationnel

**OBSERVED**

Lorsque le module est licencié, le produit gère notamment :

- prestations ;
- calculs ;
- règlements ;
- factures/demandes de paiement ;
- imports de montants consommés ;
- journaux de reprise.

Ces objets disposent de droits séparés pour consultation, création, validation, suppression et parfois forçage.

## Prévisions d’origine

Le rattachement de prévisions est disponible sur certains contrats, actes ou commandes lorsque le paramètre collectivité « affichage des prévisions d’origine » est actif.

Le bloc se trouve généralement dans les généralités du contrat/commande. Pour les actes, il n’est affiché que pour certains types, notamment avenant, reconduction et affermissement de tranche.

## Règles et contraintes

- Les contrats, actes et commandes ne partagent pas automatiquement tous leurs droits.
- La validation peut mettre à jour des statuts, historiques, échéanciers et documents.
- Les calculs et règlements comportent des contrôles de montants, pénalités, avances et révisions selon le type de contrat.
- Certaines fonctions sont spécifiques à une interface financière ou à une collectivité.
- Les imports doivent être traités comme des workflows distincts de la création manuelle.

## Effets de bord

- génération d’éditions et courriers ;
- mise à jour GED et métadonnées ;
- échanges avec systèmes financiers ;
- transmission éventuelle au parapheur ;
- création de paiements, calculs ou échéances ;
- mise à jour des montants consommés et indicateurs de pilotage.

## Cas limites

- Les actions visibles dépendent du type précis de contrat ou d’acte.
- Un bloc fonctionnel peut être absent uniquement parce qu’un paramètre collectivité est désactivé.
- Une intégration financière active peut ajouter des validations ou empêcher une opération incomplète.
- Les contrats importés/repris peuvent suivre des règles de visa différentes d’une création manuelle.

## Inconnues

**UNKNOWN**

- La totalité des types d’actes et leurs conséquences n’est pas consolidée ici.
- Le détail des calculs financiers par nature de marché nécessite une documentation dédiée avant une évolution de ce domaine.

## Preuves

- `suivi.js`, `suivi-actes.js`, `commandes.js`, modules `soweb`.
- `AuthoritiesEnum.java` — droits contrats, actes, commandes et opérationnel.
- Services sous `core/wmarche`, `modules/contractuel`, `modules/commande`, `modules/operationnel`.
- Tests sous `modules/commande`, `modules/contractuel`, `modules/operationnel`.

