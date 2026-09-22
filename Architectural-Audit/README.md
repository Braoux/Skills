````markdown
# Architectural Audit

Skill OpenClaw dédié à l’audit architectural d’un fichier, d’un module ou d’un projet complet.

Son objectif est d’évaluer la propreté structurelle du code sans tomber dans les contrôles de style, de formatage ou de linting.

Le skill produit systématiquement une note de propreté architecturale sur 10.

---

## Objectif

Ce skill cherche à répondre à une question simple :

> Est-ce que ce code est propre d’un point de vue architectural ?

Il s’intéresse notamment à :

- la responsabilité des fichiers et modules ;
- la cohésion ;
- le couplage ;
- les dépendances ;
- les frontières entre couches ;
- la séparation des responsabilités ;
- la testabilité ;
- la facilité d’évolution ;
- la cohérence avec l’architecture existante ;
- la complexité structurelle inutile.

Il ne cherche pas à juger la qualité cosmétique du code.

---

## Deux modes d’audit

Le skill peut être utilisé à deux niveaux.

### Audit d’un fichier

C’est le mode principal.

Exemples :

```text
Audite architecturalement UserService.java
````

```text
Analyse src/services/payment.ts
```

```text
Donne-moi la note de propreté architecturale de ce contrôleur.
```

Le fichier demandé est l’unité évaluée.

Le skill peut néanmoins consulter du code autour afin de comprendre son contexte :

* dépendances directes ;
* interfaces ;
* classes parentes ;
* consommateurs ;
* services associés ;
* configuration ;
* tests ;
* organisation du module.

Le score final concerne uniquement le fichier demandé.

---

### Audit d’un projet

Le skill peut également analyser :

* un repository complet ;
* une application ;
* un module ;
* un sous-système ;
* une partie significative d’un projet.

Dans ce mode, il cherche notamment à comprendre :

* les principaux modules ;
* les responsabilités ;
* les dépendances entre modules ;
* les frontières architecturales ;
* l’organisation du domaine ;
* les accès à l’infrastructure ;
* les intégrations externes ;
* les zones de fort couplage ;
* la complexité inutile.

---

## Ce qui est volontairement ignoré

Ce skill n’est pas un linter.

Il ne pénalise pas :

* l’indentation ;
* les espaces ;
* le formatage ;
* les points-virgules ;
* les guillemets ;
* la longueur des lignes ;
* l’ordre des imports ;
* les règles Prettier ;
* les règles ESLint de style ;
* les règles Checkstyle cosmétiques ;
* les imports inutilisés ;
* les différences triviales de nommage ;
* la position des accolades.

Ces contrôles doivent être laissés aux outils spécialisés.

Le skill ne doit pas remplir son rapport avec des remarques qu’un linter peut déjà produire automatiquement.

---

## Ce qui est réellement évalué

Pour un fichier, la note repose sur cinq dimensions.

### 1. Responsabilité et cohésion — /2

Le fichier a-t-il une responsabilité claire ?

Ses différentes parties ont-elles une raison logique d’être regroupées ?

Le skill cherche notamment :

* les classes ou services fourre-tout ;
* les responsabilités sans rapport entre elles ;
* les contrôleurs contenant du métier ;
* les objets métier gérant directement de l’infrastructure ;
* les fichiers utilitaires devenus des dépotoirs.

---

### 2. Couplage et dépendances — /2

Le fichier dépend-il uniquement de ce qu’il devrait connaître ?

Le skill observe :

* la nature des dépendances ;
* la direction des dépendances ;
* les dépendances inutiles ;
* le couplage fort ;
* l’état global ;
* les risques de dépendances circulaires ;
* la connaissance excessive d’autres parties du système.

Le nombre brut d’imports n’est pas un critère en soi.

---

### 3. Frontières et niveau d’abstraction — /2

Le fichier mélange-t-il des responsabilités appartenant à des couches différentes ?

Exemples de mélanges problématiques :

```text
HTTP + métier
SQL + orchestration applicative
framework + domaine
persistance + règles métier
```

Le skill cherche à vérifier que le fichier reste à un niveau d’abstraction cohérent.

---

### 4. Facilité d’évolution et testabilité — /2

Le code peut-il évoluer sans provoquer des effets de bord disproportionnés ?

Le skill cherche à déterminer :

* si les dépendances importantes peuvent être isolées ;
* si la logique métier peut être testée correctement ;
* si un changement oblige à modifier plusieurs responsabilités ;
* si l’état du fichier reste compréhensible ;
* si les changements futurs sont localisés.

Le skill ne pénalise pas automatiquement l’absence d’interfaces ou d’injection de dépendances.

Il juge leur utilité réelle.

---

### 5. Cohérence architecturale — /2

Le fichier s’intègre-t-il correctement dans l’architecture existante ?

Le skill vérifie notamment :

* sa place dans les modules ;
* le respect des frontières existantes ;
* la cohérence avec le vocabulaire du projet ;
* les responsabilités dupliquées ;
* les contournements d’abstractions existantes ;
* les différentes façons de résoudre le même problème.

---

## Note de propreté

Chaque dimension reçoit une note sur 2.

La somme produit la note finale :

```text
Responsabilité et cohésion      1.5 / 2
Couplage et dépendances         1.0 / 2
Frontières et abstraction       1.5 / 2
Évolution et testabilité        1.5 / 2
Cohérence architecturale        2.0 / 2

Note de propreté architecturale : 7.5 / 10
```

Les notes utilisent des pas de :

```text
0.5
```

Le skill évite les fausses précisions du type :

```text
7.83 / 10
```

---

## Interprétation des notes

### 9 à 10 — Très propre

Architecture claire, cohérente et facile à faire évoluer.

Les améliorations restantes sont mineures.

### 8 à 8.5 — Propre

Bonne structure globale avec quelques améliorations possibles.

### 7 à 7.5 — Globalement sain

Le code reste compréhensible et maintenable, mais certaines faiblesses structurelles méritent d’être corrigées.

### 5 à 6.5 — Fragile

Plusieurs problèmes de couplage, de responsabilité ou de frontière augmentent le coût des évolutions.

### 3 à 4.5 — Mauvais

Les problèmes structurels deviennent significatifs et pénalisent clairement la maintenabilité.

### 0 à 2.5 — Critique

Le code est fortement entremêlé et une restructuration importante est probablement nécessaire.

---

## Pas de dogmatisme

Le skill ne juge pas l’architecture en fonction du nombre de patterns utilisés.

Il ne pénalise pas un projet simplement parce qu’il n’utilise pas :

* DDD ;
* Clean Architecture ;
* architecture hexagonale ;
* CQRS ;
* Repository Pattern ;
* Factory Pattern ;
* SOLID à la lettre.

Ces notions peuvent aider à raisonner, mais elles ne sont pas des objectifs en soi.

Le skill privilégie :

```text
simplicité
+
responsabilités claires
+
dépendances maîtrisées
+
facilité d’évolution
```

Il ne récompense pas l’abstraction pour l’abstraction.

---

## Exemple

Un fichier de 500 lignes peut obtenir :

```text
9 / 10
```

s’il reste cohérent, concentré sur une responsabilité claire et simple à faire évoluer.

À l’inverse, un fichier de 80 lignes peut obtenir :

```text
4 / 10
```

s’il mélange :

* logique métier ;
* requêtes SQL ;
* appels HTTP ;
* envoi d’emails ;
* gestion de cache ;
* orchestration applicative.

La taille du fichier n’est donc pas directement utilisée pour calculer la note.

---

## Méthodes longues

Une méthode longue n’est pas automatiquement considérée comme mauvaise.

Le skill cherche plutôt à savoir si elle :

* reste conceptuellement cohérente ;
* mélange plusieurs responsabilités ;
* change constamment de niveau d’abstraction ;
* contient de nombreux effets de bord ;
* devient difficile à faire évoluer.

L’objectif est d’éviter de transformer l’audit architectural en simple revue de Clean Code.

---

## Duplication

La duplication n’est pas automatiquement considérée comme un défaut architectural.

Deux portions de code similaires peuvent parfois être préférables à une mauvaise abstraction partagée.

La duplication devient pertinente lorsqu’elle révèle :

* plusieurs implémentations divergentes d’une même règle métier ;
* plusieurs représentations du même concept ;
* plusieurs composants portant la même responsabilité ;
* un risque de comportement incohérent.

---

## Tests

Les tests peuvent être utilisés pour comprendre l’architecture.

Ils peuvent aider à identifier :

* les responsabilités réelles ;
* les frontières ;
* les dépendances ;
* les comportements exposés ;
* la difficulté à isoler le code.

En revanche, le taux de couverture n’entre pas directement dans la note.

Un manque de tests n’est pas un problème architectural en soi.

Une architecture qui rend les tests inutilement difficiles, en revanche, est pertinente pour l’audit.

---

## Forces et problèmes

Le rapport contient à la fois :

### Les forces

Exemples :

* responsabilités bien séparées ;
* dépendances maîtrisées ;
* domaine bien isolé ;
* architecture simple ;
* bonne cohésion ;
* modules clairement définis.

### Les problèmes

Chaque problème contient :

```text
Sévérité
Preuve
Impact
Recommandation
```

Les sévérités possibles sont :

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Les problèmes cosmétiques ne doivent jamais apparaître comme des findings architecturaux.

---

## Priorisation

Le skill essaie de ne pas générer une liste interminable de refactorings.

Il privilégie les changements ayant le plus fort impact architectural.

Exemple :

```text
Priorité 1
Séparer les règles métier des accès à la persistance.

Priorité 2
Réduire les dépendances directes vers les services externes.

Priorité 3
Clarifier la responsabilité du module partagé.
```

L’objectif est de proposer quelques changements structurants plutôt qu’une longue liste de micro-améliorations.

---

## Rapport Markdown

Lorsque l’environnement permet d’écrire sur le système de fichiers, le skill génère un rapport Markdown.

Par défaut :

```text
docs/architecture-audit/
```

Pour un fichier :

```text
docs/architecture-audit/UserService.audit.md
```

Pour un projet :

```text
docs/architecture-audit/project.audit.md
```

Pour un module :

```text
docs/architecture-audit/payment-module.audit.md
```

---

## Exemple de rapport

```markdown
# Architectural Audit — UserService.java

**Mode:** File
**Target:** `src/main/java/com/example/user/UserService.java`
**Architectural Cleanliness Score:** 7.5 / 10

## Résumé

Le service possède une responsabilité globalement claire,
mais mélange orchestration métier et effets de bord infrastructurels.

## Score

| Dimension | Score |
|---|---:|
| Responsabilité et cohésion | 1.5 / 2 |
| Couplage et dépendances | 1.0 / 2 |
| Frontières et abstraction | 1.5 / 2 |
| Évolution et testabilité | 1.5 / 2 |
| Cohérence architecturale | 2.0 / 2 |
| **Total** | **7.5 / 10** |

## Forces

- Bonne centralisation du cas d’usage.
- Modèle métier cohérent avec le reste du projet.

## Problèmes

### A-01 — Effets de bord infrastructurels

**Sévérité:** HIGH

**Preuve:**

Le service orchestre le cas d’usage mais déclenche également
directement les notifications et la persistance.

**Impact:**

Ces responsabilités évoluent indépendamment et augmentent
le couplage du service.

**Recommandation:**

Séparer les effets de bord infrastructurels de l’orchestration
principale du cas d’usage.
```

---

## Structure du skill

```text
architectural-audit/
├── SKILL.md
└── README.md
```

Le comportement de l’agent est défini dans :

```text
SKILL.md
```

Le présent fichier décrit l’objectif et le fonctionnement général du skill.

---

## Utilisation

Exemple d’audit ciblé :

```text
Fais un audit architectural de UserService.java.
```

Exemple d’audit avec contexte :

```text
Audite PaymentController.java et utilise le reste du projet
uniquement pour comprendre son rôle architectural.
```

Exemple d’audit global :

```text
Fais un audit architectural de ce projet.
```

Le skill détermine automatiquement s’il doit fonctionner en mode :

```text
FILE
```

ou :

```text
PROJECT
```

---

## Philosophie

Le but de ce skill n’est pas de vérifier si le code ressemble à un exemple de livre.

Il cherche plutôt à déterminer :

> Est-ce que l’organisation actuelle du code rend le système facile à comprendre, à modifier et à faire évoluer sans créer de couplage inutile ?

Une bonne architecture n’est pas nécessairement complexe.

Dans de nombreux cas :

```text
moins de couches
+
moins d’abstractions
+
responsabilités claires
```

est préférable à une architecture plus sophistiquée mais plus difficile à comprendre.

---

## Statut

Première version.

Le skill est actuellement spécialisé dans l’évaluation de la qualité architecturale des fichiers et projets logiciels.

```