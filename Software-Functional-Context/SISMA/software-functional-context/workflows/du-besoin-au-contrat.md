# Du besoin au contrat

## Finalité

Décrire le parcours fonctionnel principal qui transforme un besoin planifié en contrat suivi.

## Acteurs

- gestionnaire des besoins ;
- rédacteur de consultation ;
- gestionnaire de passation ;
- valideurs selon le processus ;
- gestionnaire contractuel ;
- fournisseurs/candidats en tant que parties externes représentées dans le système.

## Préconditions

- L’utilisateur dispose des droits adaptés à chaque étape.
- Les licences nécessaires sont actives.
- Les référentiels et paramètres requis sont configurés.

## Déclencheur

Un besoin d’achat est créé/importé, ou une consultation est créée directement.

## Flux fonctionnel

### 1. Préparer le besoin

1. Créer ou importer une prévision.
2. Renseigner objet, montants, nomenclatures, opération/UF, imputations et acteurs utiles.
3. Sauvegarder puis valider selon les contrôles applicables.

Cette étape est facultative lorsqu’une consultation est créée directement.

### 2. Créer la consultation

L’utilisateur choisit l’un des parcours observés :

- consultation vide ;
- consultation depuis une prévision ;
- marché subséquent depuis un accord-cadre.

La création depuis une prévision recopie des informations du besoin et conserve le rattachement.

### 3. Structurer et rédiger

1. Définir la consultation et ses lots/autres niveaux.
2. Renseigner règles d’achat, montants, CPV, familles, opérations, critères et justificatifs.
3. Rédiger ou sélectionner clauses et documents.
4. Enregistrer jusqu’à ce que les contrôles de validation soient satisfaits.

### 4. Valider et lancer

La consultation est soumise/validée selon les droits et le processus. Elle devient disponible dans la passation.

### 5. Conduire la passation

Le dossier traverse les étapes applicables : lancement/candidature, ouverture, analyse, attribution et notification.

À chaque étape, les acteurs saisissent candidats, offres, décisions, dates, justificatifs et réunions, puis soumettent ou valident.

### 6. Notifier

La Notification finalise les fournisseurs et offres concernés. Sa validation peut :

- créer ou compléter les contrats ;
- générer des courriers/éditions ;
- mettre à jour l’historique et les tâches ;
- enrichir les fiches fournisseurs avec familles et CPV.

### 7. Suivre le contrat

Le gestionnaire contractuel complète et valide le contrat, puis gère actes, commandes et données d’exécution. Les modules opérationnels peuvent ensuite traiter prestations, calculs, règlements et paiements.

## États et transitions

**OBSERVED**

Les principaux objets supportent des opérations séparées de sauvegarde, soumission, validation, refus et dévalidation.

**INFERRED**

Le schéma générique est souvent :

`En saisie → Soumis/à valider → Validé`

avec possibilité de refus ou dévalidation. Les codes exacts et transitions autorisées varient selon l’objet ; ce schéma ne doit pas remplacer les règles spécifiques.

## Règles importantes

- La validation est plus contraignante que la sauvegarde.
- Les droits sont vérifiés à chaque domaine, pas une seule fois pour l’ensemble du cycle.
- Le niveau consultation/lot détermine plusieurs reprises de données.
- Une intégration externe n’est utilisée que si elle est configurée et active.
- Les effets de bord doivent appartenir à la même transaction fonctionnelle lorsqu’un échec doit tout annuler.

## Échecs et cas limites

- contrôle de processus devenu faux entre ouverture et validation ;
- donnée obligatoire ou référentiel manquant ;
- plateforme externe indisponible ;
- lot externe impossible à rapprocher ;
- document non éligible à la signature ;
- objet déjà validé ou modifié concurremment ;
- consultation sans prévision ou contrat créé directement, qui court-circuite une partie du flux.

## Preuves

- Modules `previsions`, `consultations`, `passation`, `suivi`.
- Services de validation correspondants.
- Routes de création depuis une prévision et de création/import de contrat.

