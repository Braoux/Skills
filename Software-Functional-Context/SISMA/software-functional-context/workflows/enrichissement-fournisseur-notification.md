# Enrichir un fournisseur à la Notification

## Finalité

Capitaliser automatiquement sur les achats réalisés afin d’associer aux fournisseurs les familles d’achat et CPV des consultations auxquelles ils ont participé.

## Acteurs

- gestionnaire qui valide la Notification ;
- système SIS Marchés ;
- fournisseurs représentés dans la Notification.

## Préconditions

- La Notification peut être validée.
- Le fournisseur possède une fiche entreprise identifiable.
- Le niveau porteur (consultation ou lot) est retrouvable dans la structure.
- Les familles disposent de leur identifiant de référentiel d’origine et les CPV sont résolvables.

## Déclencheur

Validation de l’étape **Notification**.

Une simple sauvegarde ou ouverture de l’écran ne déclenche pas l’enrichissement.

## Population traitée

**OBSERVED**

- Tous les rôles sont traités de la même façon.
- Les fournisseurs éliminés sont inclus.
- Les fournisseurs écartés à la candidature sont exclus.
- Les fournisseurs hors délai sont exclus.
- Le filtre d’affichage actif dans l’écran ne détermine pas la population métier.

## Flux fonctionnel

1. Charger la consultation et parcourir récursivement sa structure.
2. Identifier les fournisseurs éligibles de la Notification.
3. Pour chaque fournisseur, déterminer son niveau porteur : consultation ou lot.
4. Collecter les familles d’achat et CPV de ce niveau uniquement.
5. Charger les associations déjà présentes sur la fiche fournisseur.
6. Ajouter uniquement les associations manquantes.
7. Enregistrer les nouvelles associations avec **Principale = Non**.

## Règles métier

- Pas d’héritage consultation → lot dans ce traitement.
- Un lot imbriqué doit être retrouvé, pas seulement un enfant direct de la consultation.
- La famille ajoutée référence la famille d’origine, pas la copie locale du dossier.
- Une validation répétée séquentiellement ne crée pas de doublon.
- Une absence totale de famille/CPV ne modifie pas le fournisseur.
- Aucun historique fournisseur spécifique n’est créé.

## Restitution après enrichissement

Dans la fiche, les associations sont visibles comme non principales.

Dans la liste des fournisseurs :

- la valeur principale reste prioritaire ;
- si aucune principale n’existe, la première association est affichée ;
- le fournisseur devient recherchable par la famille ou le CPV ajouté.

## Dévalidation

Dévalider la Notification ne retire aucune association. La provenance n’étant pas stockée, une suppression automatique risquerait d’effacer une donnée ajoutée manuellement.

## Échecs et cas limites

- niveau porteur introuvable : le fournisseur ne peut pas être enrichi pour cette ligne ;
- famille sans identifiant d’origine : association ignorée et anomalie de donnée à signaler ;
- CPV inconnu : association impossible ;
- association déjà présente : aucun ajout ;
- deux transactions strictement concurrentes : risque résiduel de doublon, faute de contrainte unique en base ;
- échec d’une précondition de validation : aucune association ne devrait être persistée.

## Preuves

- `PassationSupplierEnrichmentServiceImpl`.
- `PassationNotificationServiceImpl.validate`.
- Repositories des associations fournisseur/famille et fournisseur/CPV.
- Tests `PassationSupplierEnrichmentServiceImplTest` et documentation `SM-17825`.

