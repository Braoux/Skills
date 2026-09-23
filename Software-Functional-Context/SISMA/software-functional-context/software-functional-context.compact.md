# SIS Marchés — Contexte fonctionnel compact

## 1. Objet et niveaux de preuve

Ce document fournit une représentation fonctionnelle autonome de SIS Marchés. Il est destiné à l’analyse de tickets, anomalies et évolutions lorsque le lecteur ou l’IA ne dispose pas du dépôt source ni du package documentaire détaillé.

Il décrit le comportement existant, pas nécessairement l’intention produit future.

- **OBSERVED** : comportement directement démontré par les artefacts du logiciel.
- **INFERRED** : comportement fortement suggéré, mais non confirmé comme exigence produit.
- **UNKNOWN** : information que les éléments analysés ne permettent pas d’établir.
- **INCONSISTENCY** : sources ou comportements existants qui se contredisent.

**Contexte analysé :** branche `SM-17825`  
**Date de génération :** 23 septembre 2026

Sauf indication contraire, les comportements décrits dans les sections fonctionnelles sont **OBSERVED**.

## 2. Comment utiliser ce contexte

Lors de l’analyse d’un ticket :

- considérer **OBSERVED** comme le comportement existant ;
- utiliser **INFERRED** comme indication, jamais comme exigence produit ;
- transformer les **UNKNOWN** pertinents en questions de clarification ;
- signaler lorsqu’un ticket semble modifier ou contredire un comportement existant ;
- ne pas exiger la conservation d’un comportement existant si le ticket demande explicitement de le modifier ;
- se concentrer sur les sections pertinentes pour le ticket ;
- considérer toute information nécessaire mais absente de ce document comme inconnue, sans inventer le comportement manquant.

Ce contexte sert à comprendre l’existant. Il ne remplace pas les critères d’acceptation du ticket et ne doit pas imposer une solution technique.

## 3. Index de routage des tickets

| Si le ticket concerne… | Regarder principalement… |
|---|---|
| Besoin ou prévision d’achat | §5 — Prévisions et consultations |
| Consultation, lot ou règles d’achat | §5 — Prévisions et consultations |
| Candidature, lancement, ouverture, analyse, attribution ou notification | §6 — Passation |
| Fournisseur ou évaluation fournisseur | §7 — Fournisseurs |
| Contrat, acte ou commande | §8 — Contrats et exécution |
| Documents, éditions ou signature | §9 — Documents, éditions et référentiels |
| Interface externe | §10 — Intégrations externes |
| Permissions, licences ou paramétrage | §4 — Principes et acteurs ; §11 — Règles transverses |

## 4. Vue d’ensemble, principes et acteurs

### 4.1 Finalité du produit

**OBSERVED**

SIS Marchés gère le cycle des achats et marchés publics :

1. planifier un besoin avec une prévision d’achat ;
2. préparer et structurer une consultation ;
3. conduire la passation jusqu’à la notification ;
4. créer, reprendre ou importer un contrat ;
5. gérer les actes et commandes ;
6. suivre prestations, calculs, règlements et paiements lorsque le module opérationnel est actif ;
7. conserver, produire et signer des documents ;
8. exploiter des référentiels, processus, recherches et fonctions de pilotage.

Le parcours nominal est :

`Prévision → Consultation → Passation → Notification → Contrat → Exécution`

**INFERRED**

Cette chaîne représente le parcours principal, mais certaines étapes sont facultatives : une consultation peut être créée sans prévision et un contrat peut être créé ou importé directement.

### 4.2 Variabilité fonctionnelle

**OBSERVED**

La visibilité et le comportement dépendent :

- des permissions du profil ;
- des licences actives ;
- de la collectivité courante ;
- des paramètres de fonctionnement ;
- du type de procédure, consultation, contrat ou acte ;
- du processus configuré ;
- des interfaces externes actives.

Une fonctionnalité présente dans le produit n’est donc pas nécessairement disponible dans chaque installation.

### 4.3 Principes d’accès

- Les données, référentiels et paramètres sont fréquemment isolés par collectivité.
- Consulter ne donne pas implicitement le droit de créer, modifier, valider, dévalider ou supprimer.
- Une action autorisée par le profil peut encore être refusée par un processus configuré.
- Une validation peut produire des effets de bord dans plusieurs domaines.

### 4.4 Acteurs

| Acteur | Capacités principales selon permissions |
|---|---|
| Lecteur métier | Consulter besoins, consultations, passations, fournisseurs, contrats et référentiels. |
| Gestionnaire des besoins | Créer et valider des prévisions ; préparer et rédiger des consultations. |
| Gestionnaire de passation | Traiter et valider les différentes étapes de mise en concurrence. |
| Gestionnaire fournisseurs | Gérer les fiches, l’activité, les nomenclatures et les évaluations. |
| Gestionnaire contractuel | Gérer contrats, actes, commandes et leurs validations. |
| Gestionnaire opérationnel | Gérer prestations, calculs, règlements et paiements lorsque le module est actif. |
| Administrateur fonctionnel | Gérer référentiels, organisation, profils, processus, modèles et paramètres. |
| Processus système | Importer et synchroniser des données ou statuts de manière planifiée. |

**UNKNOWN**

La composition effective des profils dépend de chaque collectivité. Un intitulé de rôle ne garantit pas le même ensemble de permissions entre installations.

## 5. Prévisions et consultations

### 5.1 Prévisions d’achat

**OBSERVED**

Une prévision représente un besoin planifié. Elle peut contenir numéro, libellé, descriptif, montants estimés, nature, CPV, familles d’achat, opération/UF, imputations, contacts, fournisseurs potentiels, visibilité et caractère multi-service.

Elle peut être créée, importée, consultée, sauvegardée, validée ou supprimée selon les droits.

La validation applique des contrôles plus stricts que la sauvegarde, notamment sur les données obligatoires et les montants HT/TTC. Certains champs sont visibles uniquement lorsque le paramétrage de la collectivité les active.

### 5.2 Sélection des prévisions

La bibliothèque de prévisions permet notamment de créer une consultation depuis une prévision ou de rattacher une prévision à un autre objet.

La restitution peut inclure numéro, libellé, support achat, famille d’achat, opération/UF, nature et indicateur multi-service. Une donnée non renseignée apparaît vide.

### 5.3 Consultations

Une consultation peut être créée :

- vide ;
- depuis une prévision ;
- comme marché subséquent d’un accord-cadre.

Elle peut contenir une structure hiérarchique avec lots et autres niveaux contractuels. Elle regroupe notamment règles d’achat, montants, critères, justificatifs, rédaction, documents et paramètres de procédure.

La création depuis une prévision reprend des informations du besoin et conserve le rattachement à son origine.

### 5.4 Contrôles et transitions

Les contrôles observés portent notamment sur la structure, les identifiants, le numéro, les montants, les seuils, la pondération, les prix/formules, les dates, les imputations, les nomenclatures et le processus.

Les actions de soumission, validation, refus et dévalidation sont distinctes. Elles modifient l’état et historisent l’action.

### 5.5 Cas limites

- Une consultation sans lot porte directement ses règles et fournisseurs.
- Dans une consultation allotie, certaines données appartiennent au lot ; aucun héritage universel ne doit être supposé.
- Les champs famille d’achat, opération/UF ou imputation peuvent être masqués par paramétrage.

## 6. Passation

### 6.1 Étapes disponibles

**OBSERVED**

Le modèle prévoit les étapes suivantes :

1. Candidature (`PCA`)
2. Lancement (`PLA`)
3. Ouverture (`POU`)
4. Analyse (`PAN`)
5. Attribution (`PAT`)
6. Notification (`PNO`)

**INFERRED**

Le chemin exact dépend de la procédure. Toutes les étapes ne sont pas nécessairement obligatoires ou ordonnées de manière identique dans chaque dossier.

### 6.2 Rôle des étapes

- **Lancement** : publication, supports, dates et dématérialisation.
- **Candidature** : candidats, dépôts, décisions et justificatifs.
- **Ouverture** : plis, offres et participants.
- **Analyse** : notes, évaluations et décisions.
- **Attribution** : attributaires, offres retenues et références contractuelles.
- **Notification** : résultats notifiés, dates et préparation contractuelle.

### 6.3 Comportement fonctionnel

Un fournisseur de passation peut porter un rôle, une décision, des offres, des lots, des justificatifs et des contacts. Les données utiles sont reprises ou transformées entre les étapes.

Les retraits, dépôts et candidatures peuvent être importés depuis un fichier ou une plateforme de dématérialisation. L’import peut créer ou rapprocher les fournisseurs et les lots.

Chaque étape propose une combinaison d’actions : enregistrer, soumettre, valider, refuser/rejeter et dévalider. Selon l’étape, une validation peut historiser l’action, mettre à jour les tâches, préparer l’étape suivante, générer des documents ou alimenter les contrats.

Les réunions de passation possèdent leurs propres participants, ordres du jour et actions de soumission/validation.

### 6.4 Cas limites et risque connu

- La procédure détermine les étapes et contrôles applicables.
- Les décisions prises en candidature influencent la population des étapes suivantes.
- Un lot externe non rapproché peut empêcher une reprise complète de registre.
- Une plateforme externe peut refuser un export déjà existant ou incohérent.
- **Risque connu :** la validation Notification présente un risque lié à l’ordre entre contrôle du processus et changement d’état.

## 7. Fournisseurs

### 7.1 Fiche et bibliothèque

**OBSERVED**

Une fiche fournisseur peut regrouper identité, identifiants légaux, coordonnées, contacts, type, statut, données bancaires selon les droits, mots-clés, familles d’achat, CPV, évaluations et liens avec les consultations ou contrats.

Les droits distinguent consultation, création/mise à jour, activation, validation et suppression.

La bibliothèque est paginée. Les filtres sont appliqués côté serveur avant tri et pagination afin de conserver des résultats et compteurs cohérents.

### 7.2 Recherche et restitution

La recherche peut porter sur les mots-clés, les familles d’achat et les CPV. Les résultats observés ne dupliquent pas un fournisseur lorsqu’il possède plusieurs associations.

Dans la liste, la famille d’achat ou le CPV principal est affiché lorsqu’il existe ; sinon la première association est affichée. La colonne reste vide si aucune association n’existe.

### 7.3 Alimentation depuis la passation

La validation Notification peut ajouter à la fiche fournisseur les familles d’achat et CPV du niveau de consultation ou de lot auquel il est rattaché.

Cet enrichissement est additif : il conserve les associations existantes, évite les doublons lors des validations séquentielles et crée les nouvelles associations comme non principales. La dévalidation de la Notification ne les retire pas.

### 7.4 Évaluations et imports

Le produit permet de définir et renseigner des évaluations fournisseur avec des permissions dédiées.

Des fournisseurs peuvent être créés ou mis à jour par import. Les formats, colonnes et règles de mise à jour sont des contrats fonctionnels à vérifier pour tout ticket portant sur l’import.

### 7.5 Cas limites

- Les données proposées sont limitées par la collectivité et l’état des référentiels.
- Un identifiant de famille ou un CPV incohérent peut empêcher une association automatique.
- La fusion complète des doublons d’entreprise n’est pas établie dans ce contexte.

## 8. Contrats et exécution

### 8.1 Contrats

**OBSERVED**

Un contrat peut être créé dans l’espace de suivi, produit depuis la passation, importé depuis une procédure ou repris en liste.

Il peut contenir généralités, titulaires, montants, délais, prix, index/formules, imputations, prévisions d’origine, documents et données d’exécution.

Les permissions distinguent consultation, création/saisie, validation, dévalidation, suppression et modification du numéro.

### 8.2 Actes

Les actes représentent des événements d’exécution ou de modification du contrat. Le produit distingue au moins actes d’exécution et actes modificatifs, avec des droits séparés.

Des exemples observés sont l’avenant, la reconduction et l’affermissement d’une tranche. Les actions disponibles dépendent du type d’acte et de son état.

### 8.3 Commandes

Les bons de commande sont rattachés à un contrat et possèdent leurs propres actions de consultation, création, validation, suppression et modification du numéro.

### 8.4 Suivi opérationnel

Lorsque le module est licencié, il couvre notamment :

- prestations ;
- calculs ;
- règlements ;
- factures et demandes de paiement ;
- imports de montants consommés ;
- journaux de reprise.

Les contrôles peuvent dépendre des montants, pénalités, avances, révisions, types de contrats et interfaces financières actives.

### 8.5 Effets de bord et variantes

Les validations peuvent mettre à jour états, historiques, échéanciers, documents, paiements et indicateurs de pilotage.

Le rattachement de prévisions d’origine à certains contrats, actes ou commandes dépend d’un paramètre de collectivité. Les contrats importés ou repris peuvent suivre des règles différentes d’une création manuelle.

## 9. Documents, éditions et référentiels

### 9.1 GED et signature

**OBSERVED**

Des documents peuvent être rattachés aux prévisions, consultations, passations, contrats et actes.

Les fonctions observées incluent ajout, téléchargement, remplacement, suppression selon droits/états, métadonnées, import de plis et préparation pour signature.

Le stockage peut être local ou externe. Les documents envoyés à la signature doivent avoir le format et l’état attendus ; sinon l’envoi est refusé.

### 9.2 Éditions et modèles

L’application produit des documents de consultation, courriers de candidature ou d’offre, notifications, contrats, actes et états de suivi.

Certaines éditions sont générées par fournisseur et peuvent être regroupées. Les modèles, thèmes et clauses sont administrables et réutilisables.

### 9.3 Référentiels

Les référentiels principaux comprennent familles d’achat, CPV, opérations/UF, imputations, critères, justificatifs, pénalités, index, formules, articles, contacts, processus, tâches et modèles d’édition.

Une valeur inactive peut rester présente dans l’historique sans être proposée pour une nouvelle sélection. L’activation/désactivation est souvent distincte de la suppression.

### 9.4 Organisation et paramétrage

La bibliothèque Organisation gère organismes, services, utilisateurs et profils.

Le paramétrage couvre notamment modes de fonctionnement, numérotation, TVA, jours fériés, correspondances externes, serveurs, GED et personnalisation de l’accueil.

## 10. Intégrations externes

**OBSERVED**

Les intégrations sont conditionnées par une configuration, une licence ou un serveur actif.

| Intégration | Comportement fonctionnel observé |
|---|---|
| AWS-Achat / AWSolutions | Export des consultations et documents ; import de registres ; rapprochement de lots. |
| Atexo | Export vers le profil acheteur ; import de registres ; conservation des références externes. |
| Safetender | Export consultation et DCE ; exploitation de registres. |
| BOAMP | Support de publication et flux d’avis ; périmètre complet non établi. |
| CMIS / SharePoint | Stockage documentaire, dossiers et métadonnées. |
| Parapheur | Circuits de signature et récupération des statuts. |
| Chorus Pro / CPP | Échanges liés aux factures, demandes de paiement, statuts et refus. |
| Cegid / Qualiac / Sytral / DGA | Interfaces financières ou métiers propres à certains déploiements. |
| SIRENE | Recherche ou complément des informations d’entreprise. |
| e-Attestations | Informations documentaires fournisseur ; règles détaillées non établies. |

Une intégration absente ou mal paramétrée peut masquer l’action ou produire une erreur fonctionnelle. Aucun comportement uniforme ne doit être supposé pour les interfaces spécifiques à une collectivité.

## 11. Règles transverses essentielles

Les identifiants restent alignés sur ceux du package détaillé. Les numéros absents de cette sélection compacte sont volontairement réservés ; ils ne signalent pas un contenu manquant dans ce document.

| ID | Règle existante |
|---|---|
| BR-001 | L’accès dépend des droits, licences et paramètres actifs. |
| BR-002 | Les données et référentiels sont fréquemment isolés par collectivité. |
| BR-003 | Consulter, saisir, valider, dévalider et supprimer sont des capacités distinctes. |
| BR-004 | Une validation peut produire des effets dans plusieurs domaines. |
| BR-005 | Un processus configuré peut ajouter des contrôles et tâches. |
| BR-006 | Une consultation possède une structure hiérarchique ; les données peuvent appartenir à un niveau précis. |
| BR-008 | Les enrichissements additifs observés évitent les doublons lors d’exécutions séquentielles. |
| BR-010 | Une dévalidation ne compense pas nécessairement tous les effets déjà produits. |
| BR-012 | Dans les listes paginées observées, les filtres sont appliqués avant pagination. |
| BR-015 | La visibilité et la sélection des référentiels dépendent de leur activation et du paramétrage. |
| BR-016 | Une interface externe requiert une configuration active et cohérente. |
| BR-017 | Seuls les documents éligibles peuvent être transmis à la signature. |
| BR-018 | Les actions structurantes sont généralement historisées. |

## 12. Cas limites et risques majeurs

- Une donnée peut appartenir au lot plutôt qu’à la consultation ; ne pas supposer un héritage automatique.
- Un écran ou champ absent peut résulter d’un droit, d’une licence ou d’un paramètre.
- Une validation répétée doit être examinée pour son idempotence.
- Une dévalidation ne supprime pas nécessairement les effets produits dans d’autres domaines.
- Une plateforme externe peut refuser une donnée dupliquée, incomplète ou non rapprochée.
- Les documents non éligibles ne peuvent pas être envoyés à la signature.
- Les contrats importés ou repris peuvent différer des créations manuelles.
- Les fonctions historiques présentes dans le produit ne sont pas nécessairement actives.
- La validation Notification présente un risque connu lié à l’ordre entre contrôle du processus et changement d’état.

## 13. Inconnues importantes

**UNKNOWN**

- Matrice exhaustive des transitions pour chaque type de procédure.
- Toutes les combinaisons autorisées de lots, tranches, phases, postes et périodes.
- Détail complet des types d’actes et de leurs conséquences.
- Règles exhaustives des calculs financiers par nature de marché.
- Politiques de rétention et de suppression physique des documents externes.
- Workflow Chorus Pro complet selon tous les cadres de facturation.
- Comportement uniforme des interfaces financières spécifiques entre collectivités.
- Règles complètes de fusion des doublons fournisseur.
- Composition effective des profils dans chaque déploiement.

Ces inconnues doivent devenir des questions de clarification lorsqu’elles sont nécessaires à l’analyse d’un ticket.

## 14. Glossaire minimal

- **Affaire** : terme générique historique pour un dossier et sa structure.
- **Prévision** : expression planifiée d’un besoin d’achat.
- **Consultation** : projet d’achat soumis à une procédure de passation.
- **Lot** : niveau de consultation pouvant porter règles, fournisseurs et nomenclatures.
- **Passation** : traitement de la consultation jusqu’à la Notification.
- **Notification** : étape finale modélisée, avec résultats et préparation contractuelle.
- **Fournisseur / entreprise** : opérateur économique enregistré dans la bibliothèque.
- **Famille d’achat** : classification achat propre à une collectivité.
- **CPV** : nomenclature commune des marchés publics.
- **Opération / UF** : référence opérationnelle ou unité fonctionnelle du besoin.
- **Contrat / marché** : objet de suivi contractuel.
- **Acte** : événement d’exécution ou de modification d’un contrat.
- **Visa** : code d’état d’un objet dans son workflow.
- **GED** : gestion électronique des documents.
- **Collectivité** : périmètre principal d’isolation des données et paramètres.

## 15. Portée et informations absentes

Ce document est autonome : il contient les informations retenues comme essentielles pour raisonner sur le produit.

Lorsque les informations nécessaires à l’analyse d’un ticket ne sont pas présentes dans ce document, elles doivent être considérées comme inconnues. Ne pas inventer le comportement manquant.

Si le package détaillé est disponible, il peut être consulté pour approfondir le domaine concerné, mais il n’est pas requis pour utiliser ce contexte compact.
