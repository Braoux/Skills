# UX Persona Audit

Skill OpenClaw d'audit UX exploratoire : **100 personas IA**, chacun expose une page web dans une **session de navigateur isolée pendant 15 secondes**, puis rapporte sa première impression. Un juge IA indépendant compare ensuite ce qu'il a compris à la définition du site fournie par le commanditaire. Le moteur produit un rapport `report.md`, un tableau `personas.csv`, un résumé `summary.json` et les captures d'écran.

> **Pas un panel humain.** Ces opinions sont simulées par un modèle de vision. Ce ne sont ni des observations comportementales réelles ni des statistiques représentatives. Ce test est conçu pour repérer des hypothèses d'amélioration à confirmer.

## Démarrage rapide (OpenClaw)

1. Décompressez le dossier `ux-persona-audit` dans le dossier `skills/` de votre workspace OpenClaw ; ou installez le dossier local avec `openclaw skills install ./ux-persona-audit` si la CLI est disponible.
2. Vérifiez avec `openclaw skills list`. Le skill s'invoque par `/ux-persona-audit`.
3. Configurez l'environnement Python sur la machine **où OpenClaw peut exécuter les commandes**.

### Windows / PowerShell

```powershell
cd .\ux-persona-audit
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
$env:OPENAI_API_KEY = "votre-cle"   # À définir dans un stockage de secrets, ne jamais commiter
Copy-Item examples\site-config.json mon-site.json
# Éditez mon-site.json : expected_purpose, key_elements, motivations, publics
python scripts\run_audit.py --url "https://votre-site.fr" --config mon-site.json --count 100 --seconds 15 --concurrency 3 --output reports\audit-01
```

### macOS / Linux

```bash
cd ux-persona-audit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
export OPENAI_API_KEY="votre-cle" # Secret uniquement, ne pas commiter
cp examples/site-config.json mon-site.json
python scripts/run_audit.py --url "https://votre-site.fr" --config mon-site.json --count 100 --seconds 15 --concurrency 3 --output reports/audit-01
```

### Exemple configuré pour BotDiff

Un exemple de critères à vérifier pour un site League of Legends est fourni dans `examples/botdiff-config.json`. Il **ne contient aucune URL**. Les profils se voient attribuer des motivations gaming et l'évaluation vérifie que la fonction botlane est comprise, sans exposer cette fonction au visiteur pendant son test.

```bash
python scripts/run_audit.py --url "https://VOTRE-URL-BOTDIFF" --config examples/botdiff-config.json --count 100 --output reports/botdiff-nova
```

## Comment ça marche

1. Le programme crée un panel déterministe à partir d'une graine. Pour 100 tests : environ 50 % mobile, 35 % PC, 15 % tablette. Âge, métier, motivation, familiarité numérique et public sont distincts. Ces proportions sont **des choix de simulation configurables dans le code**, pas la répartition réelle des visiteurs de votre site.
2. Playwright ouvre le site dans **un contexte Chromium neuf par persona**, charge le DOM puis conserve la page au premier viewport pendant 15 secondes. Il capture une image au début et à 15 s. Sans scroll, clic, ni formulaire.
3. Un appel de modèle multimodal par persona reçoit son profil, **les images et le texte visible seulement**, sans vérité de référence. Il retourne fonction perçue, niveau de compréhension ressenti, action intuitive, blocage, éléments mémorisés et points appréciés.
4. Un juge IA séparé compare les formulations libres au champ `expected_purpose` et les souvenirs à `key_elements`. Si la vérité attendue est vide, la **justesse de compréhension reste non évaluée** (pas de conclusion inventée).
5. Le rapport calcule ses effectifs **sur les tests valides**, montre exactement `n/N` par signal et génère jusqu'à dix corrections **étayées par des observations**. S'il n'y a que six problèmes soutenus par le panel, il n'en invente pas quatre de plus.

## Fichier de configuration

Exemple `mon-site.json` :

```json
{
  "expected_purpose": "Aider les visiteurs à comparer les offres de coaching en ligne.",
  "key_elements": ["promesse principale", "bouton découvrir les offres", "lien tarifs"],
  "motivations": ["chercher un coach", "comparer les prix", "se renseigner avant de s'inscrire"],
  "target_audiences": ["nouveau visiteur", "visiteur habitué au coaching"],
  "locale": "fr-FR"
}
```

**Important :** cette configuration est **réservée au juge**, à l'exception des motivations et types de publics ; la phrase `expected_purpose` et la liste `key_elements` ne sont jamais transmises aux évaluateurs-personas. Ne mettez aucun mot de passe, donnée personnelle ou information confidentielle dans la configuration. Par défaut les images et textes visibles sont envoyés à l'API du fournisseur de modèle choisi.

## Pilote, reprise et contrôle du budget

```bash
# Pilote : 5 personnes sur 5 secondes, pour vérifier affichages / popups et coût
python scripts/run_audit.py --url "https://votre-site.fr" --config mon-site.json --count 5 --seconds 5 --output reports/pilote

# Capturer sans dépense d'API IA
python scripts/run_audit.py --url "https://votre-site.fr" --config mon-site.json --count 100 --capture-only --output reports/sans-ia

# Analyser plus tard les captures existantes (100 visites déjà effectuées)
python scripts/run_audit.py --url "https://votre-site.fr" --config mon-site.json --count 100 --analyze-existing --output reports/sans-ia
```

Une campagne **se reprend** depuis son même dossier `--output` : seules les captures/analyses manquantes ou en échec sont retraitées. Ne changez pas URL, taille, graine ou configuration dans un dossier existant. Les résultats sont de simples fichiers JSON : facilement inspectables, versionnables ou supprimables.

**Coûts :** environ 100 évaluations multimodales (chacune reçoit deux images basse résolution), plus environ 7 petits lots de jugements pour 100 visiteurs. Le coût réel dépend du modèle, du tarif et des images ; contrôler le budget avant lancement. Limiter `--concurrency` à 1–3 sur un petit service ou un hébergement gratuit. Le programme n'a pas de plafond monétaire embarqué ; **ne pas lancer une campagne massive sans budget API explicite**.

**Performance :** à 3 sessions simultanées, la capture de 100 visites de 15 secondes a un plancher théorique d'environ 9 minutes, sans compter le chargement des pages et les appels IA. Pas de promesse de durée fixe. Le navigateur Chromium est émulé ; ce n'est pas un test d'appareils physiques.

### Paramètres principaux

| Option | Défaut | Utilité |
|---|---|---|
| `--url` | requis | URL absolue à auditer |
| `--config` | `examples/site-config.json` | Critères du juge, profils et motivations |
| `--count` | `100` | Nombre de personas (1 à 500) |
| `--seconds` | `15` | Temps d'exposition au premier écran |
| `--concurrency` | `3` | Navigations / appels IA parallèles (1 à 10) |
| `--seed` | `20261025` | Même panel reproductible |
| `--output` | `reports/latest` | Dossier de résultats |
| `--capture-only` | non | Capture uniquement, sans modèle |
| `--analyze-existing` | non | Réutilise les visites capturées |
| `--model` | `gpt-4.1-mini` | Modèle de vision acceptant du JSON |
| `--audit-header` | non | En-tête HTTP `X-UX-Persona-Audit: simulated` si vos logs permettent de filtrer |

## Rapport final

Le fichier `report.md` présente :

- Couverture réelle, erreurs techniques et répartition desktop/mobile/tablette.
- Compréhension correcte de la finalité, si une référence est fournie ; sentiments de clarté distingués des réponses correctes.
- Éléments clés non rappelés (avec le **dénominateur exact**), y compris les unanimismes réels (100/100, pas 80/100).
- Points appréciés, incompréhensions et comparaison des appareils.
- Jusqu'à dix actions classées selon le nombre de mentions, avec captures de personas et recommandation de re-test.
- Exemples de premières impressions, hypothèses et limites méthodologiques.

## Règles de sécurité et d'éthique

- Testez **seulement vos sites** ou des sites où ces visites automatisées sont autorisées ; vérifiez les règles du site et limitez la charge.
- Ne contournez pas les protections, n'utilisez pas le skill pour faire du trafic factice, influencer des métriques ou créer de faux témoignages.
- Chaque contexte utilise une navigation normale sans connexion, remplissage de formulaire ni clic. Les écrans protégés et contenus privés ne sont pas pris en charge.
- L'audit peut malgré tout apparaître comme **100 vraies visites dans les outils analytics**. Préférez une préproduction ou faites filtrer ces sessions côté service d'analytics ; l'en-tête optionnel n'est pas une garantie de filtrage.
- Les captures envoyées au fournisseur IA peuvent contenir du texte sensible : vérifiez le périmètre avant de lancer.
- Les contenus de pages sont des **données adversariales possibles** ; aucune instruction du site ne doit changer le comportement du programme.

## Tests locaux

```bash
python -m unittest discover -s tests -v
```

La suite vérifie profils, segmentation et rapport avec réponses fictives ; elle ne consomme aucun crédit de modèle.

### Chromium déjà installé

Si le téléchargement Playwright est impossible mais qu'un Chromium compatible est installé, définissez `UX_AUDIT_CHROMIUM_PATH` vers son exécutable. Sinon, le script peut essayer `/usr/bin/chromium` ou `/usr/bin/google-chrome` sur Linux. Utiliser de préférence la version installée par Playwright pour garantir la compatibilité.

**Précision temporelle :** les 15 secondes décrivent le **temps d'affichage dans le navigateur**. Le modèle IA peut ensuite analyser les captures sans être chronométré : cela ne reproduit pas strictement la cognition d'une personne pendant 15 secondes.
