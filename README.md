# TP Intégration Continue - Pipeline CI/CD

## Description
Ce projet implémente une application Python permettant de gérer des produits (CRUD) en mémoire, accompagnée d'une chaîne CI/CD complète.

## Prérequis
- Python 3
- Docker & Docker Compose
- Un compte GitHub/GitLab

## Installation et Utilisation Locale
1. Cloner le dépôt : `git clone https://github.com/Mooodrix/tp-ci-cd.git`
2. Installer les dépendances : `pip install -r requirements.txt`
3. Lancer les tests manuellement : `pytest test_product_manager.py`

## Infrastructure CI/CD
L'infrastructure s'appuie sur `docker-compose` pour faire tourner Jenkins et SonarQube localement.
1. Lancer les serveurs : `docker-compose up -d`
2. Jenkins est accessible sur le port `8080`.
3. SonarQube est accessible sur le port `9000`.

Le fichier `Jenkinsfile` automatise l'installation de l'environnement, l'exécution des tests (avec `coverage.py` et `radon`), et l'envoi du rapport vers SonarQube.