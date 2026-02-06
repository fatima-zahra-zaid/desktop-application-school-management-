# Gestion Scolaire — Application de bureau (Tkinter)

## Résumé

Ce document présente une description académique et technique de l'application "Gestion Scolaire" — une application de bureau développée en Python avec `tkinter` destinée à la gestion basique des étudiants, des enseignants et des cours. L'objectif du projet est pédagogique : fournir un prototype fonctionnel pour des travaux pratiques et des évaluations.

## Mots-clés

Gestion scolaire, application de bureau, Python, Tkinter, architecture logicielle, enseignement.

## Contexte et objectifs

L'application a été conçue comme support de TP pour un cours d'informatique. Elle permet d'aborder des notions de programmation orientée objet, de conception d'interface utilisateur et de gestion de données en mémoire. Les objectifs principaux sont :

- Illustrer la modélisation d'entités scolaires (Étudiant, Enseignant, Cours).
- Présenter une interface graphique simple pour les opérations CRUD élémentaires.
- Servir de base pour extensions (persistance, tests, export).

## Fonctionnalités principales

- Création, consultation et listing d'étudiants.
- Création, consultation et listing d'enseignants.
- Création de cours et inscription d'étudiants aux cours.
- Interface graphique minimaliste basée sur `tkinter`/`ttk`.

## Architecture et conception

Le projet adopte une structure modulaire simple :

- `main.py` — point d'entrée et interface graphique (views/controllers simples).
- `etudiant.py` — définition de la classe métier `Etudiant` et comportements associés.
- `enseignant.py` — définition de la classe métier `Enseignant`.
- `cours.py` — définition de la classe métier `Cours` et gestion des inscriptions.

Le modèle suit une séparation claire entre la logique métier (classes) et la présentation (interface). Aucun framework extérieur n'est requis.

## Modèle de données (aperçu)

- `Etudiant` : identifiant, nom, prénom, année, liste des cours inscrits.
- `Enseignant` : identifiant, nom, prénom, discipline.
- `Cours` : code/nom du cours, enseignant référent, liste d'étudiants.

Les structures sont en mémoire (objets Python) et ne persistent pas automatiquement entre exécutions dans la version actuelle.

## Prérequis

- Python 3.8 ou supérieur.
- `tkinter` (inclus par défaut dans les distributions officielles de Python pour Windows). Pour Linux/macOS, installer le paquet `python3-tk` si nécessaire.

## Installation et exécution

1. Cloner ou télécharger le dépôt dans un répertoire local.
2. (Optionnel) Créer un environnement virtuel :

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Lancer l'application depuis le répertoire du projet :

```powershell
python -m py_compile *.py   # optionnel : vérifie la syntaxe
python main.py
```

Remarque : adaptez le chemin et la méthode d'activation de l'environnement selon votre shell et système d'exploitation.

## Tests et validation

La base actuelle ne contient pas de suite de tests unitaires formelle. Pour ajouter des tests :

- Créer des fichiers `test_*.py` en utilisant `unittest` ou `pytest`.
- Tester les comportements des classes dans `etudiant.py`, `enseignant.py` et `cours.py`.

Exemple rapide :

```powershell
pip install pytest
pytest -q
```

## Limitations et perspectives d'amélioration

- Persistance : ajouter sauvegarde/chargement JSON ou base SQLite.
- Tests automatisés : couverture des cas métier (inscription, suppression, validations).
- Internationalisation et amélioration ergonomique de l'interface.
- Export/Import CSV pour échanges avec d'autres outils.

## Réutilisation et citation

Pour réutiliser ou citer ce travail dans un contexte académique, mentionner l'auteur et l'année, et indiquer que le code est un prototype pédagogique.

## Auteurs

- Auteur principal : Projet TP/examen (voir en-tête des fichiers sources pour crédits spécifiques).

## Contact

Pour questions ou contributions, ouvrir une issue dans le dépôt ou contacter l'équipe enseignante responsable du cours.
