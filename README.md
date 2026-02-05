Gestion Scolaire — Desktop (Tkinter)

Description
- Petite application desktop pour gérer Étudiants, Enseignants et Cours.
- Interface graphique en `tkinter` / `ttk` (file: `main.py`).

Fonctionnalités
- Ajouter / lister Étudiants et Enseignants.
- Créer des Cours et inscrire des étudiants.
- Interface simple et theme bleu.

Prerequis
- Python 3.8+ (Windows). `tkinter` inclus avec l'installateur officiel.

Lancer l'application
1. Ouvrir PowerShell dans le dossier du projet.

```powershell
cd "c:\Users\Computer\OneDrive\Bureau\ALL\GIIA\PYHTON\TP EXAM"
python -m py_compile *.py   # optionnel : vérifie la syntaxe
python main.py
```

Fichiers principaux
- `main.py` : interface graphique (ajout/liste/inscription).
- `etudiant.py` : classe `Etudiant`.
- `enseignant.py` : classe `Enseignant`.
- `cours.py` : classe `Cours`.

Améliorations possibles
- Persistance JSON (save/load).
- Export CSV / impression.
- Tests unitaires pour les classes métier.

Aide & dépannage
- Erreur `import tkinter` : réinstaller Python en cochant "tcl/tk and IDLE".
- Voir les erreurs en lançant `python main.py` depuis un terminal.

Auteur
- Projet pour TP/examen — livrable demandé par Pr. Salah-Eddine Mansour.

Thanks