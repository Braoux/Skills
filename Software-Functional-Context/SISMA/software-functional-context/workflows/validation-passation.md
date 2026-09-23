# Valider une étape de passation

## Finalité

Faire progresser une consultation dans la passation tout en contrôlant les données, droits et conditions de processus.

## Acteurs

- gestionnaire de l’étape ;
- valideur possédant le droit spécifique à l’étape ;
- processus système pour les tâches et historiques ;
- plateformes externes lorsque l’étape échange des données.

## Préconditions

- La consultation existe et se trouve dans un état compatible.
- L’utilisateur possède le droit de validation de l’étape.
- Les données obligatoires et décisions requises sont renseignées.
- Les conditions du processus configuré sont satisfaites.

## Déclencheur

L’utilisateur lance l’action **Valider** dans une étape de passation.

## Flux fonctionnel observé

1. Charger la consultation et les données de l’étape.
2. Contrôler l’autorisation et le processus.
3. Exécuter les validations propres à l’étape : dates, fournisseurs, offres, décisions, codes tiers, références contractuelles ou autres données requises.
4. Mettre à jour le visa/état de la consultation et des lots concernés.
5. Historiser la validation.
6. Mettre à jour les tâches et échéances de processus.
7. Préparer ou recopier les données utiles à l’étape suivante.
8. Exécuter les effets de bord propres à l’étape, notamment à la Notification.

## Variantes par étape

- **Candidature** : décisions de candidature, justificatifs et candidats retenus/écartés.
- **Lancement** : publication, dates et profil acheteur.
- **Ouverture** : plis/offres et participants.
- **Analyse** : notes, décisions et suivi d’analyse.
- **Attribution** : attributaires et références de contrat.
- **Notification** : dates/résultats notifiés, contrats et enrichissement fournisseur.

## Dévalidation

**OBSERVED**

Une action séparée de dévalidation existe pour chaque étape. Elle historise l’action et peut nettoyer des données de l’étape ou revenir à un état antérieur.

Les effets ne sont pas tous compensés. En particulier, les familles/CPV ajoutés aux fournisseurs par la Notification restent présents.

## Règles transactionnelles

**INFERRED comme exigence de sûreté, appuyée par un risque observé**

Les contrôles d’autorisation et de processus devraient précéder toute mutation. Une erreur après mutation ne doit pas laisser un visa ou un historique partiellement mis à jour.

Une analyse existante signale un risque spécifique dans l’ordre des opérations de validation Notification ; vérifier ce point avant toute modification de ce workflow.

## Échecs et cas limites

- utilisateur autorisé à l’ouverture mais plus au moment de la validation ;
- données modifiées concurremment ;
- filtre de processus devenu faux ;
- candidat/offre incomplet ;
- date incompatible ;
- référence de contrat dupliquée ou invalide ;
- erreur d’intégration externe ;
- validation répétée : les effets additifs doivent rester idempotents quand la règle le prévoit.

## Preuves

- `Passation*ServiceImpl` — méthodes `validate`, `submit`, `reject`, `devalidate`.
- `Passation*ValidationHelper` — contrôles par étape.
- `ProcessusTaskServiceImpl` — tâches et échéances.
- `docs/SM-17825-synthese-changements-points-attention.md` — risque transactionnel Notification.

