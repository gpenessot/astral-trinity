.PHONY: install dev test lint format type-check clean run help

# Variables
PYTHON := uv run python
PYTEST := uv run pytest
RUFF := uv run ruff
TY := uv run ty

help: ## Affiche cette aide
	@echo "Commandes disponibles :"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Installe les dépendances
	uv venv
	uv pip install pandas numpy

dev: ## Installe les dépendances de développement
	uv venv
	uv pip install pandas numpy ruff ty pre-commit pytest pytest-cov
	uv run pre-commit install

test: ## Lance les tests
	$(PYTEST) -v

test-cov: ## Lance les tests avec couverture
	$(PYTEST) --cov=src --cov-report=html --cov-report=term

lint: ## Vérifie et corrige le code avec ruff
	$(RUFF) check --fix
	$(RUFF) format

type-check: ## Vérifie les types avec ty
	$(TY) check

check: lint type-check ## Lance toutes les vérifications

run: ## Lance l'exemple
	$(PYTHON) src/example.py

clean: ## Nettoie les fichiers temporaires
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

build: ## Construit le package
	uv build

pre-commit: ## Lance pre-commit sur tous les fichiers
	uv run pre-commit run --all-files

update: ## Met à jour les dépendances
	uv lock --upgrade

# Raccourcis
t: test
l: lint
r: run
c: check
