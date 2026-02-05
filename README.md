Gestion Scolaire — Desktop (Tkinter)

Cette petite appli est conçue pour débutants. Elle permet d'ajouter des étudiants, des enseignants, de créer des cours et d'inscrire des étudiants à des cours. Le code est volontairement simple et commenté pour faciliter une présentation en séance.

## Prérequis

- Windows avec Python 3.8+ (Tkinter est inclus avec l'installateur officiel de Python).

## Lancer l'application (Windows PowerShell)

1. Ouvrir PowerShell.
2. Se placer dans le dossier du projet.

```powershell
cd "c:\Users\LenOvo\Desktop\desktop-application-school-management-"
# Optionnel : vérifier la syntaxe
python -m py_compile cours.py enseignant.py etudiant.py main.py
# Lancer l'appli
python main.py
```

## Présentation en séance (démo rapide)

- Cliquez sur le bouton "Remplir Données Démo" pour ajouter automatiquement quelques étudiants, enseignants et cours.
- Pour remettre à zéro, utilisez le bouton "Vider Données".
- Montrez les actions suivantes :
  1.  Ajouter un étudiant (ID + Nom + Prénom), puis regarder la liste mise à jour.
  2.  Ajouter un enseignant (ID + Nom).
  3.  Créer un cours (Code + Nom) et (optionnel) lier un enseignant via son ID.
  4.  Inscrire un étudiant à un cours (entrer l'ID étudiant et le code du cours).
- La zone de texte affiche en temps réel les listes (Étudiants, Enseignants, Cours et nombre d'inscrits).

### Interface (HD & propreté)

- La partie haute est séparée en deux colonnes par une ligne verticale :
  - À gauche : ajout d'Étudiants.
  - À droite : ajout d'Enseignants, création de Cours et Inscription.
- Une ligne horizontale sépare la partie haute (formulaires) de la partie basse (sortie texte).
- Les champs d'inscription (Étudiant, Cours) et le choix d'enseignant pour créer un cours utilisent des listes déroulantes (combobox) basées sur les données ajoutées.

## Fichiers

- `main.py` : interface Tkinter/ttk HD (séparateurs, frames), combobox pour sélections, avec commentaires.
- `etudiant.py` : classe `Etudiant`.
- `enseignant.py` : classe `Enseignant`.
- `cours.py` : classe `Cours` (enseignant optionnel, méthode `afficher` robuste).
- `ui_style.py` : style externe avec `UIStyle` (thème ttk, police agrandie, mise à l'échelle HD, style de bouton principal). Meilleure pratique: séparer style et logique.

## Idées d'amélioration

- Sauvegarde/chargement en JSON pour conserver les données.
- Export CSV ou impression.
- Petits tests unitaires sur les classes (afficher, ajout, etc.).

## Dépannage

- Erreur `import tkinter` : réinstaller Python en cochant "tcl/tk and IDLE".
- Lancez dans un terminal pour voir les messages : `python main.py`.

## Auteur

Projet pour TP/examen — livrable demandé par Pr. Salah-Eddine Mansour.
