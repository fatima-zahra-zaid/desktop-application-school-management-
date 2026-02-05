import tkinter as tk
from tkinter import messagebox

from etudiant import Etudiant
from enseignant import Enseignant
from cours import Cours

# Very small, beginner-friendly UI
students = []
teachers = []
courses = []


def add_student():
    sid = ent_id.get().strip()
    nom = ent_nom.get().strip()
    prenom = ent_prenom.get().strip()
    if not sid or not nom:
        messagebox.showwarning('Erreur', 'ID et nom requis')
        return
    students.append(Etudiant(sid, nom, prenom, ''))
    ent_id.delete(0, tk.END); ent_nom.delete(0, tk.END); ent_prenom.delete(0, tk.END)
    show()


def add_teacher():
    tid = ent_tid.get().strip(); tnom = ent_tnom.get().strip()
    if not tid or not tnom:
        messagebox.showwarning('Erreur', 'ID et nom requis')
        return
    teachers.append(Enseignant(tid, tnom, ''))
    ent_tid.delete(0, tk.END); ent_tnom.delete(0, tk.END)
    show()


def add_course():
    code = ent_code.get().strip(); name = ent_cname.get().strip()
    if not code or not name:
        messagebox.showwarning('Erreur', 'Code et nom requis')
        return
    # teacher assignment optional: use teacher id field
    tid = ent_teacher_for_course.get().strip()
    teacher = next((t for t in teachers if t.id == tid), None) if tid else None
    courses.append(Cours(code, name, teacher))
    ent_code.delete(0, tk.END); ent_cname.delete(0, tk.END); ent_teacher_for_course.delete(0, tk.END)
    show()


def enroll():
    sid = ent_enroll_sid.get().strip(); code = ent_enroll_code.get().strip()
    s = next((x for x in students if x.id == sid), None)
    c = next((x for x in courses if x.code == code), None)
    if not s or not c:
        messagebox.showwarning('Erreur', 'Étudiant ou cours non trouvé')
        return
    c.ajouter_etudiant(s)
    show()


def show():
    text.delete(1.0, tk.END)
    text.insert(tk.END, 'Étudiants:\n')
    for s in students:
        text.insert(tk.END, s.afficher() + '\n')
    text.insert(tk.END, '\nEnseignants:\n')
    for t in teachers:
        text.insert(tk.END, t.afficher() + '\n')
    text.insert(tk.END, '\nCours:\n')
    for c in courses:
        text.insert(tk.END, f"{c.code} - {c.nom} ({len(c.etudiants)} inscrits)\n")


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

# Enroll inputs
tk.Label(root, text='Inscrire: Étudiant ID').grid(row=6, column=0)
ent_enroll_sid = tk.Entry(root); ent_enroll_sid.grid(row=6, column=1)
tk.Label(root, text='Code cours').grid(row=6, column=2)
ent_enroll_code = tk.Entry(root); ent_enroll_code.grid(row=6, column=3)
tk.Button(root, text='Inscrire', command=enroll).grid(row=7, column=0, columnspan=4, pady=6)

# Output
text = tk.Text(root, width=60, height=12)
text.grid(row=8, column=0, columnspan=4, pady=8)

show()

root.mainloop()