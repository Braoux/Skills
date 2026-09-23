# Fournisseurs

## Finalité

La bibliothèque fournisseurs centralise les opérateurs économiques utilisés dans les prévisions, consultations, passations et contrats.

## Informations principales

**OBSERVED**

Une fiche fournisseur peut regrouper :

- identité et identifiants légaux ;
- coordonnées, adresses et contacts ;
- statut actif/référencé et type ;
- données financières ou bancaires selon les droits ;
- mots-clés ;
- familles d’achat et CPV, avec notion de valeur principale ;
- évaluations ;
- liens vers consultations, contrats et autres historiques d’activité.

## Bibliothèque et recherche

### Onglets et pagination

La bibliothèque utilise une liste paginée et des catégories de fournisseurs, notamment les fournisseurs référencés. Les filtres doivent être appliqués côté serveur avant pagination.

### Mots-clés

Le champ est facultatif et limité à 400 caractères. Une recherche contient est insensible à la casse. Plusieurs expressions séparées par `,` sont combinées par ET.

Exemple : `plomberie, chauffage` retient une fiche dont le champ contient les deux expressions.

### Famille d’achat et CPV

Les filtres sélectionnent les fournisseurs possédant l’association choisie, même s’ils en possèdent plusieurs. La recherche ne doit pas dupliquer le fournisseur.

### Colonnes de restitution

Pour Famille d’achat et CPV :

1. afficher la valeur principale si elle existe ;
2. sinon afficher la première association créée ;
3. sinon laisser vide.

## Création et mise à jour

Un utilisateur autorisé peut créer ou modifier une fiche. Des droits distincts existent pour consulter, activer, valider et supprimer.

L’import CSV peut créer ou mettre à jour des fournisseurs. L’ordre des colonnes est significatif et le séparateur est `;`. `mots_cles` est la dernière colonne ; son absence conserve la compatibilité avec les anciens fichiers.

## Enrichissement automatique à la Notification

À la validation de Notification, la fiche peut recevoir les familles d’achat et CPV du niveau de consultation/lot auquel le fournisseur est rattaché.

Règles :

- ajout uniquement des associations absentes ;
- associations créées comme non principales ;
- pas de doublon lors d’une revalidation séquentielle ;
- pas de retrait lors d’une dévalidation ;
- pas d’historique fournisseur spécifique ;
- fournisseurs éliminés inclus ; fournisseurs hors délai ou écartés à la candidature exclus ;
- niveau consultation et niveau lot traités strictement, y compris dans une structure imbriquée.

## Évaluations

Le produit permet de définir des modèles/questions d’évaluation et d’évaluer des fournisseurs selon des droits distincts de consultation, saisie, activation et suppression.

## Contraintes et cas limites

- La collectivité limite les données et référentiels disponibles.
- Une association automatique sans principale doit malgré tout être visible dans la liste grâce à la règle de repli.
- La déduplication automatique est applicative ; une concurrence transactionnelle stricte conserve un risque résiduel.
- Une famille rattachée à une consultation utilise l’identifiant de la famille d’origine pour enrichir le fournisseur. Une source incohérente peut être ignorée.
- Un CPV absent du référentiel ne peut pas être associé normalement.

## Inconnues

**UNKNOWN**

- Les règles complètes de fusion de doublons d’entreprise ne sont pas synthétisées ici.
- Le détail des synchronisations e-Attestations/SIRENE dépend du paramétrage et nécessite une analyse dédiée pour un ticket concerné.

## Preuves

- `fournisseurs.js`, `fournisseur-grid.js` — écrans, actions et colonnes.
- `EntrepriseList.java` — restitution des Familles/CPV.
- Services et critères sous `modules/entreprise` — recherche et fiche.
- `PassationSupplierEnrichmentServiceImpl` — enrichissement Notification.
- `FournisseurJobConfiguration` — import CSV.
- Tests sous `modules/entreprise` et `modules/passation`.

