# Passation

## Finalité

La passation conduit une consultation depuis sa mise en concurrence jusqu’à la notification des résultats et la préparation des contrats.

## Étapes

**OBSERVED**

Le modèle définit les étapes suivantes :

1. Candidature (`PCA`)
2. Lancement (`PLA`)
3. Ouverture (`POU`)
4. Analyse (`PAN`)
5. Attribution (`PAT`)
6. Notification (`PNO`)

**INFERRED**

Cette liste représente le cycle fonctionnel global, mais le chemin exact varie selon la procédure. Une procédure restreinte traite notamment la candidature distinctement ; toutes les étapes ne doivent pas être supposées obligatoires dans chaque dossier.

## Concepts principaux

### Candidat/fournisseur de passation

Une entreprise intervient dans une étape avec un rôle, une décision, des offres, des lots, des justificatifs et éventuellement des contacts. Les informations pertinentes sont recopiées ou transformées entre étapes.

### Offre

Une offre peut comporter montants, notes, variantes, décisions et rattachement à un lot. L’analyse et l’attribution exploitent ces informations.

### Réunion

Le module permet de créer une réunion, gérer participants et ordres du jour, puis soumettre, valider, refuser ou dévalider la réunion.

### Registre

Les retraits, dépôts et candidatures peuvent être importés depuis un fichier ou une plateforme de dématérialisation. L’import peut créer ou rapprocher des fournisseurs et rattacher leurs lots.

## Workflow fonctionnel

### Lancement

Prépare la publication, les journaux/supports, les dates et la dématérialisation. Une consultation peut être exportée vers un profil acheteur configuré.

### Candidature

Gère les candidats, dépôts, décisions de candidature, justificatifs et éventuels registres externes.

### Ouverture

Gère l’ouverture des plis/offres et les participants associés. Les fournisseurs et offres peuvent être repris des étapes précédentes.

### Analyse

Gère l’évaluation des offres, notes, décisions et suivi d’analyse. Elle prépare les données nécessaires à l’attribution.

### Attribution

Enregistre les décisions d’attribution, fournisseurs retenus ou non retenus et références de contrat. Elle prépare les données de Notification.

### Notification

Finalise les fournisseurs/offres notifiés, dates et contrats. La validation peut créer ou mettre à jour des éléments de contrat et enrichir les fiches fournisseurs avec les familles d’achat et CPV du niveau porteur.

## Actions et états

**OBSERVED**

Chaque étape principale expose une combinaison d’actions : enregistrer, soumettre, valider, refuser/rejeter et dévalider. Les services historisent ces actions et nettoient ou reconstruisent certaines données lors d’une dévalidation.

La validation peut copier les fournisseurs, offres et justificatifs vers l’étape suivante.

## Règles importantes

- Les permissions sont distinctes par étape et action.
- Le processus configuré peut refuser une transition même si l’utilisateur possède le droit.
- La date de remise des plis et certains délais sont calculés ou contrôlés selon la procédure et l’étape.
- Les décisions de candidature influencent la population reprise dans les étapes suivantes.
- Les fournisseurs hors délai ou écartés à la candidature ne sont pas enrichis lors de la Notification.
- Une revalidation doit rester idempotente pour l’enrichissement des nomenclatures fournisseur.

## Effets de bord

- historique fonctionnel ;
- mise à jour des tâches de processus ;
- import/export de registres ;
- génération de courriers et éditions par fournisseur ;
- création ou alimentation contractuelle ;
- enrichissement des familles/CPV fournisseur à la Notification ;
- notifications applicatives pour certains traitements externes.

## Cas limites

- Un fournisseur peut être porté par la consultation ou un lot.
- Un fournisseur éliminé peut rester présent fonctionnellement en Notification même s’il est masqué par un filtre d’écran.
- Un lot sans correspondance avec un registre externe nécessite un rapprochement ou peut empêcher une reprise complète.
- Les plateformes externes peuvent refuser un export déjà existant ou mal paramétré.

## Inconnues et contradiction

**UNKNOWN**

La matrice complète des transitions autorisées pour chaque type de procédure n’est pas explicitée dans une seule source.

**INCONSISTENCY / risque connu**

Une analyse du dépôt signale que le contrôle de processus de la Notification peut intervenir après un changement de visa. Toute évolution de la validation doit vérifier l’ordre transactionnel des préconditions et mutations.

## Preuves

- `PassationStepTypes.java` — étapes et codes.
- `Passation*ServiceImpl` — sauvegarde, soumission, validation, rejet et dévalidation.
- `Passation*ValidationHelper` — validations par étape.
- Contrôleurs `Passation*Controller` — actions exposées.
- Tests du package `modules/passation`.

