# 🚀 Template Python Moderne : uv + ruff + ty

Un template de projet Python utilisant les outils les plus rapides et modernes de 2025.

## ⚡ Le trio magique

- **[uv](https://github.com/astral-sh/uv)** : Gestionnaire de packages et d'environnements ultra-rapide
- **[ruff](https://github.com/astral-sh/ruff)** : Linter et formatter écrit en Rust (remplace black + flake8 + isort)
- **[ty](https://github.com/astral-sh/ruff/tree/main/crates/red_knot_python_semantic)** : Type checker statique ultra-rapide par Astral

## 🏁 Setup en 3 commandes

```bash
# 1. Cloner le template
git clone https://github.com/votre-username/python-modern-template.git
cd python-modern-template

# 2. Installer les dépendances
uv sync --dev

# 3. Configurer pre-commit (hooks automatiques)
uv run pre-commit install
```

**C'est tout !** Votre environnement de développement moderne est prêt.

## 💡 Utilisation

### Lancer l'exemple
```bash
uv run python src/example.py
```

### Lancer les tests
```bash
uv run pytest
```

### Vérifier le code manuellement
```bash
# Linter + fixes automatiques
uv run ruff check --fix

# Formatage
uv run ruff format

# Vérification des types
uv run ty check
```

## 🎯 Ce qui se passe automatiquement

À chaque `git commit`, pre-commit vérifie automatiquement :
- ✅ Code formaté avec ruff
- ✅ Erreurs de linting corrigées
- ✅ Types vérifiés avec ty
- ✅ Fichiers propres (trailing whitespace, etc.)

Si des erreurs sont trouvées, le commit est annulé et les corrections sont appliquées automatiquement.

## 📁 Structure du projet

```
python-modern-template/
├── src/
│   └── example.py          # Exemples avec type hints avancés
├── tests/
│   └── test_example.py     # Tests unitaires
├── pyproject.toml          # Configuration uv + ruff
├── .pre-commit-config.yaml # Hooks automatiques
├── .gitignore              # Fichiers à ignorer
└── README.md               # Ce fichier
```

## 🔧 Configuration

### ruff
La configuration dans `pyproject.toml` active :
- Vérifications PEP 8
- Import sorting (comme isort)
- Détection de bugs courants
- Suggestions de modernisation du code

### ty
ty est le type checker statique d'Astral, conçu pour être :
- **Ultra-rapide** : écrit en Rust comme ruff et uv
- **Précis** : diagnostics détaillés et informatifs
- **Moderne** : support des dernières fonctionnalités Python

Exemples de ce que ty peut détecter :
```python
# Types Literal pour des valeurs spécifiques
Style = Literal["italic", "bold", "underline"]

def with_style(text: str, style: Style) -> str:
    if style == "italic":
        return f"*{text}*"
    # ty détecte si vous oubliez des cas
```

## 🚀 Avantages

**Rapidité :**
- uv : 10-100x plus rapide que pip
- ruff : 10-100x plus rapide que black + flake8
- ty : type checking ultra-rapide par Astral

**Qualité :**
- Code toujours formaté
- Types vérifiés statiquement
- Bugs détectés avant commit
- Trio d'outils cohérent d'Astral

**Simplicité :**
- Une seule configuration
- Outils qui se complètent parfaitement
- Setup en 3 commandes

## 📦 Ajouter des dépendances

```bash
# Dépendance de production
uv add pandas matplotlib

# Dépendance de développement
uv add --dev pytest-mock

# Dépendance optionnelle
uv add --optional viz plotly
```

## 🤝 Contribution

Ce template évolue avec les meilleures pratiques Python modernes.

N'hésitez pas à :
- Ouvrir des issues pour suggestions
- Proposer des améliorations via PR
- Partager vos retours d'expérience

## 📚 Pour aller plus loin

- [Documentation uv](https://docs.astral.sh/uv/)
- [Documentation ruff](https://docs.astral.sh/ruff/)
- [Documentation ty](https://docs.astral.sh/ty/) (à venir)
- [Type hints Python](https://docs.python.org/3/library/typing.html)

---

**Ce template vous fait gagner du temps ?** ⭐ N'oubliez pas de star le repo !

**Problème ou question ?** 💬 Ouvrez une issue, on vous aide !
