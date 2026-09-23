# Intégrations fonctionnelles

Les intégrations ci-dessous sont conditionnelles : leur code existe, mais leur activation dépend d’un serveur, d’une licence ou d’un paramètre de collectivité.

## Profils acheteurs et dématérialisation

### AWS-Achat / AWSolutions

**OBSERVED**

But : exporter une consultation et échanger des données de dématérialisation.

Comportements observés :

- export de données de consultation et de documents ;
- import planifié de registres de retraits, dépôts et candidatures ;
- rapprochement des lots externes avec les lots SIS ;
- création ou enrichissement de candidats à partir des registres ;
- refus fonctionnel d’un export déjà présent ou incohérent.

### Atexo

**OBSERVED**

But : exporter une consultation vers un profil acheteur Atexo et importer des registres.

L’export nécessite un profil acheteur compatible et des correspondances de procédure. L’application mémorise la référence et l’URL externes lorsqu’elles sont retournées.

### Safetender

**OBSERVED**

But : exporter une consultation et ses pièces DCE, puis exploiter les registres de retrait/dépôt.

Les erreurs de réponse sont restituées comme erreurs fonctionnelles d’export.

### BOAMP

**OBSERVED**

Le BOAMP apparaît comme support de publication et dans des flux d’avis. Le périmètre complet d’émission/réception n’a pas été reconstruit.

## GED : CMIS et SharePoint

**OBSERVED**

But : stocker et relire les documents associés aux objets métier.

L’application peut créer des dossiers, téléverser des documents et pousser des métadonnées. Le comportement varie selon que le serveur est CMIS ou SharePoint. Un paramétrage incomplet bloque l’opération avec un message fonctionnel.

## Parapheur / signature électronique

**OBSERVED**

But : transmettre des documents à un circuit de signature et récupérer les circuits/statuts.

Conséquences fonctionnelles :

- seuls les documents éligibles peuvent être transmis ;
- des traitements planifiés peuvent récupérer les retours ;
- des notifications applicatives peuvent être adressées au demandeur ;
- une réponse vide, HTML inattendue ou erreur HTTP est transformée en erreur métier lisible.

## Chorus Pro / CPP

**OBSERVED**

But : gérer des échanges liés aux factures et demandes de paiement, notamment des statuts et motifs de refus.

**UNKNOWN**

Le dépôt ne suffit pas, dans cette génération, à établir le workflow complet de bout en bout selon tous les cadres de facturation.

## Systèmes financiers et métiers

**OBSERVED**

Des interfaces spécifiques existent pour Cegid, Qualiac, Sytral, DGA et d’autres contextes de déploiement. Elles peuvent agir sur contrats, opérations, engagements, consommés ou propositions de liquidation.

**UNKNOWN**

Ces interfaces étant spécifiques à certaines installations, aucun comportement unique ne doit être supposé pour toutes les collectivités.

## SIRENE

**OBSERVED**

Une interface permet de rechercher ou compléter des informations d’entreprise à partir de données SIRENE. Son usage dépend du paramétrage et de la disponibilité du service.

## e-Attestations

**OBSERVED**

Le dépôt contient une intégration et des stubs liés à e-Attestations pour des informations documentaires fournisseur.

**UNKNOWN**

Les règles exactes de déclenchement et de rafraîchissement n’ont pas été établies avec assez de certitude.

## Preuves

- Packages `core/atexo`, `core/safetender`, `core/batch/demat/aws`.
- `GedIOCmisProcessor`, `GedServiceImpl`, `ParapheurConnectServiceImpl`.
- Contrôleurs `SafetenderController`, `CegidController`, `QualiacController`, `PaymentRequestController`, `SireneController`.
- Catalogue `ServerType` et configurations de serveurs.

