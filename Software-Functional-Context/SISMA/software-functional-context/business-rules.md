# Règles métier transverses

## BR-001 — Accès conditionné par droits et licences

**Statut : OBSERVED**

Un écran ou une action n’est disponible que si l’utilisateur possède une permission adaptée. Certains droits sont en outre rattachés à une licence fonctionnelle ; un module présent dans le produit peut donc être absent d’un déploiement.

S’applique à : tous les domaines.

## BR-002 — Isolation par collectivité

**Statut : OBSERVED**

Les fournisseurs, référentiels, paramètres, serveurs et nombreuses recherches sont filtrés par la collectivité de l’utilisateur. Une association ou une autocomplétion ne doit pas mélanger des données de collectivités différentes.

S’applique à : fournisseurs, référentiels, consultations, contrats, intégrations.

## BR-003 — Séparation consulter / saisir / valider / dévalider

**Statut : OBSERVED**

La lecture d’un objet n’accorde pas implicitement le droit de le modifier ou de le valider. Les validations et dévalidations utilisent des permissions distinctes dans les principaux workflows.

S’applique à : prévisions, consultations, passation, contrats, actes, commandes, exécution.

## BR-004 — Une validation peut déclencher des effets de bord

**Statut : OBSERVED**

Valider ne se limite pas à changer un état. Selon le domaine, l’opération peut historiser l’action, mettre à jour des tâches de processus, recopier des données vers l’étape suivante, créer des éléments contractuels, enrichir des fournisseurs ou déclencher des échanges documentaires.

S’applique à : consultations, passation, contrats, documents, fournisseurs.

## BR-005 — Processus configurables

**Statut : OBSERVED**

Un processus configuré peut imposer des contrôles et des tâches supplémentaires. Une action autorisée par le profil peut encore être refusée si les conditions du processus ne sont plus satisfaites.

S’applique à : consultations, passation, réunions et autres formulaires processés.

## BR-006 — Structure hiérarchique d’une consultation

**Statut : OBSERVED**

Une consultation possède une structure hiérarchique pouvant contenir des lots et d’autres niveaux. Les règles, nomenclatures, fournisseurs et futurs contrats peuvent être portés par un niveau précis.

S’applique à : consultations, passation, contrats, fournisseurs.

## BR-007 — Niveau porteur des nomenclatures fournisseur

**Statut : OBSERVED**

Lors de l’enrichissement d’un fournisseur à la Notification :

- un fournisseur porté par la consultation reçoit les familles et CPV de la consultation ;
- un fournisseur porté par un lot reçoit les familles et CPV de ce lot ;
- il n’existe pas d’héritage automatique consultation → lot pour cet enrichissement.

Le niveau peut se trouver dans une structure imbriquée.

## BR-008 — Enrichissement fournisseur additif et idempotent

**Statut : OBSERVED**

La validation Notification ajoute seulement les familles et CPV absents de la fiche fournisseur. Une revalidation séquentielle ne doit pas créer de doublon. Les associations ajoutées sont non principales.

Limite observée : aucune contrainte unique en base ne garantit le cas de deux validations strictement concurrentes.

## BR-009 — Population fournisseur de la Notification

**Statut : OBSERVED**

L’enrichissement traite les fournisseurs présents dans la population métier de la Notification, quel que soit leur rôle. Les fournisseurs éliminés restent inclus ; les fournisseurs écartés à la candidature ou hors délai sont exclus.

## BR-010 — Dévalidation sans compensation fournisseur

**Statut : OBSERVED**

Dévalider la Notification ne retire pas les familles ou CPV ajoutés aux fournisseurs. Le modèle ne conserve pas leur provenance de façon suffisante pour distinguer un ajout automatique d’un ajout manuel.

## BR-011 — Restitution principale sinon première association

**Statut : OBSERVED**

Dans la liste des fournisseurs, les colonnes Famille d’achat et CPV affichent l’association marquée principale lorsqu’elle existe. Sinon, elles affichent la première association créée. Elles restent vides en l’absence d’association.

## BR-012 — Recherche fournisseur filtrée avant pagination

**Statut : OBSERVED**

Les critères Mots-clés, Famille d’achat et CPV sont appliqués côté serveur avant tri et pagination. Les filtres Famille/CPV utilisent une logique d’existence afin qu’un fournisseur ne soit pas dupliqué lorsqu’il possède plusieurs associations.

## BR-013 — Mots-clés fournisseur

**Statut : OBSERVED**

Le champ Mots-clés fournisseur est facultatif et limité à 400 caractères. La recherche est partielle et insensible à la casse. Plusieurs expressions séparées par une virgule sont combinées avec un ET.

## BR-014 — Import CSV fournisseur compatible

**Statut : OBSERVED**

Le format CSV fournisseur utilise `;`. La colonne `mots_cles` est la dernière colonne attendue. Une cellule vide conserve la valeur existante et un ancien fichier sans cette dernière colonne reste accepté.

## BR-015 — Référentiels actifs et paramétrés

**Statut : OBSERVED**

Les sélections proposées dans les formulaires peuvent être limitées aux valeurs actives et au périmètre de la collectivité. La visibilité de certains champs, notamment opération/UF, famille ou imputation, dépend du paramétrage.

## BR-016 — Données externes conditionnées par configuration

**Statut : OBSERVED**

Les exports vers un profil acheteur, le stockage GED externe, la signature et les autres interfaces nécessitent un serveur actif et un paramétrage cohérent. En cas d’absence ou d’incompatibilité, l’application retourne une erreur fonctionnelle de configuration ou rend l’action indisponible.

## BR-017 — Documents envoyés à la signature

**Statut : OBSERVED**

Les documents transmis au parapheur doivent être au format et dans l’état requis ; sinon l’envoi complet est refusé avec la liste des documents incompatibles.

## BR-018 — Historisation des actions structurantes

**Statut : OBSERVED**

Les sauvegardes, soumissions, validations, refus et dévalidations de plusieurs workflows créent des entrées d’historique. L’enrichissement automatique des nomenclatures fournisseur ne crée toutefois pas d’historique fournisseur spécifique.

## Incohérence connue — contrôle du processus à la Notification

**Statut : OBSERVED dans la documentation d’analyse du dépôt**

Une analyse existante signale que la validation Notification peut modifier le visa avant d’exécuter le contrôle de processus. Si un filtre dépend de l’étape courante, ce changement peut invalider le contrôle après mutation. Ce point doit être revalidé avant toute évolution de cette transaction.

Preuve : `docs/SM-17825-synthese-changements-points-attention.md`.

