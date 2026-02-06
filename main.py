"""Mini application Tkinter pour gestion scolaire (débutants).

Fonctions disponibles :
- Ajouter des étudiants
- Ajouter des enseignants
- Créer des cours (enseignant optionnel)
- Inscrire un étudiant à un cours

Interface et code volontairement simples, avec quelques commentaires.
"""

import tkinter as tk
from tkinter import messagebox

from etudiant import Etudiant
from enseignant import Enseignant
from cours import Cours
from ui_style import UIStyle


# Very small, beginner-friendly UI
students = []
teachers = []
courses = []


# Helpers très simples pour retrouver par ID / code (boucles for, faciles à lire)
def find_student_by_id(sid):
    for s in students:
        if s.id == sid:
            return s
    return None


def find_teacher_by_id(tid):
    for t in teachers:
        if t.id == tid:
            return t
    return None


def find_course_by_code(code):
    for c in courses:
        if c.code == code:
            return c
    return None


def add_student():
    sid = ent_id.get().strip()
    nom = ent_nom.get().strip()
    prenom = ent_prenom.get().strip()
    if not sid or not nom:
        messagebox.showwarning('Erreur', 'ID et nom requis')
        return
    students.append(Etudiant(sid, nom, prenom, ''))
    # Nettoyage des champs
    ent_id.delete(0, tk.END)
    ent_nom.delete(0, tk.END)
    ent_prenom.delete(0, tk.END)
    update_comboboxes(); show()


def add_teacher():
    tid = ent_tid.get().strip(); tnom = ent_tnom.get().strip()
    if not tid or not tnom:
        messagebox.showwarning('Erreur', 'ID et nom requis')
        return
    teachers.append(Enseignant(tid, tnom, ''))
    ent_tid.delete(0, tk.END)
    ent_tnom.delete(0, tk.END)
    update_comboboxes(); show()


def add_course():
    code = ent_code.get().strip(); name = ent_cname.get().strip()
    if not code or not name:
        messagebox.showwarning('Erreur', 'Code et nom requis')
        return
    # enseignant optionnel : on peut taper l'ID, sinon laisser vide
    tid = cmb_teacher_for_course.get().strip()
    teacher = find_teacher_by_id(tid) if tid else None
    courses.append(Cours(code, name, teacher))
    ent_code.delete(0, tk.END)
    ent_cname.delete(0, tk.END)
    cmb_teacher_for_course.set("")
    update_comboboxes(); show()


def enroll():
    sid = ent_enroll_sid.get().strip(); code = ent_enroll_code.get().strip()
    s = next((x for x in students if x.id == sid), None)
    c = next((x for x in courses if x.code == code), None)
    if not s or not c:
        messagebox.showwarning('Erreur', 'Étudiant ou cours non trouvé')
        return

    c.ajouter_etudiant(s)
    cmb_enroll_sid.set("")
    cmb_enroll_code.set("")
    show()


def fill_demo_data():
    """Ajoute rapidement des données de démonstration (pour présentation)."""
    # Évite de dupliquer si on clique plusieurs fois
    if not students:
        students.extend([
            Etudiant('S1', 'Ali', 'Karim', 'L1'),
            Etudiant('S2', 'Sara', 'Zaid', 'L2'),
        ])
    if not teachers:
        teachers.extend([
            Enseignant('T1', 'Pr. Mansour', 'Math'),
            Enseignant('T2', 'Pr. Nadia', 'Info'),
        ])
    if not courses:
        courses.extend([
            Cours('C1', 'Algèbre', find_teacher_by_id('T1')),
            Cours('C2', 'Programmation', find_teacher_by_id('T2')),
        ])
        # Inscrire un étudiant à un cours pour montrer
        courses[0].ajouter_etudiant(students[0])
    update_comboboxes(); show()


def show():
    """Actualise la zone de texte avec les listes."""
    text.delete(1.0, tk.END)
    text.insert(tk.END, 'Étudiants:\n')
    for s in students:
        text.insert(tk.END, s.afficher() + '\n')

    text.insert(tk.END, '\nEnseignants:\n')
    for t in teachers:
        text.insert(tk.END, t.afficher() + '\n')

    text.insert(tk.END, '\nCours:\n')
    for c in courses:
        # nombre d'inscrits pour visualiser
        text.insert(tk.END, f"{c.code} - {c.nom} ({len(c.etudiants)} inscrits)\n")


# Bouton pour vider toutes les données (réinitialiser)
def clear_data():
    """Efface toutes les listes et nettoie les champs d'entrée."""
    students.clear()
    teachers.clear()
    courses.clear()

    # Nettoyer tous les champs de saisie
    for e in [ent_id, ent_nom, ent_prenom, ent_tid, ent_tnom, ent_code, ent_cname]:
        e.delete(0, tk.END)
    # Réinitialiser les combobox
    cmb_teacher_for_course.set("")
    cmb_enroll_sid.set("")
    cmb_enroll_code.set("")

    update_comboboxes(); show()
    messagebox.showinfo('Info', 'Données vidées avec succès')


def update_comboboxes():
    """Synchronise les valeurs des combobox avec les listes en mémoire."""
    # Étudiants pour inscription
    sid_values = [s.id for s in students]
    cmb_enroll_sid['values'] = sid_values

    # Codes de cours
    code_values = [c.code for c in courses]
    cmb_enroll_code['values'] = code_values

    # Enseignants pour création de cours (optionnel)
    teacher_ids = [t.id for t in teachers]
    cmb_teacher_for_course['values'] = [""] + teacher_ids


"""
# --- Interface avec séparation en frames et séparateurs ---
"""
root = tk.Tk()
root.title('Gestion Scolaire - Beginner')

# Student inputs
tk.Label(root, text='Étudiant ID').grid(row=0, column=0)
ent_id = tk.Entry(root); ent_id.grid(row=0, column=1)
tk.Label(root, text='Nom').grid(row=1, column=0)
ent_nom = tk.Entry(root); ent_nom.grid(row=1, column=1)
tk.Label(root, text='Prénom').grid(row=2, column=0)
ent_prenom = tk.Entry(root); ent_prenom.grid(row=2, column=1)
tk.Button(root, text='Ajouter Étudiant', command=add_student).grid(row=3, column=0, columnspan=2, pady=4)

# Teacher inputs
tk.Label(root, text='Enseignant ID').grid(row=0, column=2)
ent_tid = tk.Entry(root); ent_tid.grid(row=0, column=3)
tk.Label(root, text='Nom enseignant').grid(row=1, column=2)
ent_tnom = tk.Entry(root); ent_tnom.grid(row=1, column=3)
tk.Button(root, text='Ajouter Enseignant', command=add_teacher).grid(row=3, column=2, columnspan=2, pady=4)

# Course inputs
tk.Label(root, text='Code cours').grid(row=4, column=0)
ent_code = tk.Entry(root); ent_code.grid(row=4, column=1)
tk.Label(root, text='Nom cours').grid(row=5, column=0)
ent_cname = tk.Entry(root); ent_cname.grid(row=5, column=1)
tk.Label(root, text='ID enseignant (optionnel)').grid(row=4, column=2)
ent_teacher_for_course = tk.Entry(root); ent_teacher_for_course.grid(row=4, column=3)
tk.Button(root, text='Ajouter Cours', command=add_course).grid(row=5, column=2, columnspan=2, pady=4)

# Inscription
ttk.Separator(right_group, orient='horizontal').grid(row=7, column=0, columnspan=2, sticky='ew', pady=6)
ttk.Label(right_group, text='Inscrire: Étudiant').grid(row=8, column=0, sticky='w', padx=6, pady=4)
cmb_enroll_sid = ttk.Combobox(right_group, state='readonly')
cmb_enroll_sid.grid(row=8, column=1, sticky='ew')

ttk.Label(right_group, text='Dans le cours').grid(row=9, column=0, sticky='w', padx=6, pady=4)
cmb_enroll_code = ttk.Combobox(right_group, state='readonly')
cmb_enroll_code.grid(row=9, column=1, sticky='ew')

ttk.Button(right_group, text='Inscrire', style='Primary.TButton', command=enroll).grid(row=10, column=0, columnspan=2, pady=8, sticky='ew')

# Boutons démo / clear
ttk.Button(right_group, text='Remplir Données Démo', command=fill_demo_data).grid(row=11, column=0, pady=6, sticky='ew')
ttk.Button(right_group, text='Vider Données', command=clear_data).grid(row=11, column=1, pady=6, sticky='ew')

right_group.columnconfigure(0, weight=1)
right_group.columnconfigure(1, weight=1)

# Zone sortie (bottom)
text = tk.Text(bottom_frame, width=100, height=20)
scroll = ttk.Scrollbar(bottom_frame, orient='vertical', command=text.yview)
text.configure(yscrollcommand=scroll.set)
text.grid(row=0, column=0, sticky='nsew')
scroll.grid(row=0, column=1, sticky='ns')

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=0)
bottom_frame.rowconfigure(0, weight=1)

update_comboboxes(); show()

root.mainloop()