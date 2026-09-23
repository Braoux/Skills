# Prévisions et consultations

## Finalité

Ce domaine couvre l’expression d’un besoin d’achat puis la préparation d’un projet de consultation structuré et validable.

## Concepts principaux

### Prévision d’achat

**OBSERVED**

Une prévision peut contenir notamment : numéro, libellé, descriptif, montants estimés, nature, CPV, familles d’achat, opération/UF, imputations, contacts, fournisseurs potentiels, visibilité et caractère multi-service.

Elle dispose d’actions distinctes de création, consultation, validation, suppression et import.

### Consultation

**OBSERVED**

Une consultation est un projet d’achat structuré. Elle peut être créée :

- vide ;
- depuis une prévision ;
- comme marché subséquent d’un accord-cadre.

Elle regroupe caractéristiques, structure, règles d’achat, rédaction, montants, critères, justificatifs, documents et paramètres de procédure selon le type de dossier.

### Structure

**OBSERVED**

La structure est hiérarchique. La consultation racine peut contenir des lots et d’autres éléments tels que tranches, phases, postes ou périodes selon les options contractuelles.

Les règles d’achat et prévisions peuvent être portées par la consultation ou par un lot.

## Comportements fonctionnels

### Créer et gérer une prévision

Un utilisateur autorisé peut créer une prévision, la sauvegarder, la valider, la supprimer ou l’importer. La validation applique des contrôles dédiés sur les données du formulaire et les montants estimés HT/TTC.

La présence et le libellé de certains champs dépendent du paramétrage de la collectivité.

### Rechercher et sélectionner des prévisions

La bibliothèque de sélection est utilisée notamment pour créer une consultation depuis une prévision ou rattacher des prévisions à d’autres objets.

Les résultats exposent numéro, libellé, support achat, famille d’achat, opération/UF, nature et indicateur multi-service. Une famille et une opération absentes donnent une cellule vide.

### Créer une consultation depuis une prévision

La sélection d’une prévision déclenche la création d’une consultation alimentée depuis cette source. Le lien entre prévision et objet créé est conservé pour la restitution et le suivi.

### Préparer une consultation

Un utilisateur autorisé peut modifier la structure et les données tant que le visa et le processus le permettent. La sauvegarde et la validation appliquent des contrôles différents : une sauvegarde tolère davantage d’incomplétude qu’une validation.

### Valider, refuser, soumettre et dévalider

**OBSERVED**

Les services exposent des opérations séparées de soumission, validation, refus et dévalidation. Elles mettent à jour le visa et historisent l’action. La disponibilité dépend des droits et, le cas échéant, du processus configuré.

## Validations et contraintes observées

- cohérence de la structure et des identifiants des éléments ;
- unicité/cohérence du numéro selon le contexte ;
- montants HT, taux d’avance et seuils ;
- pondération des critères ;
- cohérence des formules et prix ;
- date limite de remise des plis ;
- imputations ;
- enveloppes d’opération/UF et de nomenclature d’achat ;
- processus autorisé.

La liste exacte des contrôles actifs dépend du type de consultation et de paramètres collectivité.

## Permissions

- Prévisions : consulter, créer, valider, supprimer, importer.
- Consultations : consulter, créer, créer à partir de, modifier, modifier le numéro, valider, lancer, supprimer.
- Rédaction : consulter, rédiger, modifier/ajouter des clauses, valider les clauses.

## Effets de bord

- Une consultation validée peut devenir disponible dans la passation.
- La création depuis une prévision conserve un rattachement au besoin d’origine.
- Les documents et éditions peuvent être générés à partir des données de consultation.
- Des tâches de processus peuvent être créées ou mises à jour.

## Cas limites

- Une consultation sans lot porte directement ses règles d’achat et fournisseurs.
- Dans une consultation allotie, certaines données sont portées au niveau du lot ; il ne faut pas supposer un héritage automatique pour tous les traitements.
- Les champs opération/UF, famille ou imputation peuvent être masqués par paramétrage.
- Une prévision sans famille ou opération reste sélectionnable ; la restitution correspondante est vide.

## Inconnues

**UNKNOWN**

- Toutes les combinaisons permises entre tranches, phases, postes et périodes ne sont pas synthétisées ici.
- Les règles réglementaires exactes par procédure et seuil peuvent évoluer via référentiels/configuration ; elles doivent être vérifiées dans le contexte d’un ticket concerné.

## Preuves

- `previsions.js`, `consultations.js` — routes, actions et permissions.
- `WAffaireElementServiceImpl` — création, sauvegarde, validation, soumission, refus et dévalidation.
- Package `modules/consultations/validator` — contrôles de structure et règles d’achat.
- `PrevisionValidationHelper` — contrôles des prévisions.

