import tkinter as tk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from etudiant import Etudiant
from enseignant import Enseignant
from cours import Cours

etudiants = []
enseignants = []
cours_list = []


def add_student():
    sid = entry_st_id.get().strip()
    if not sid:
        messagebox.showwarning("Erreur", "ID étudiant requis")
        return
    e = Etudiant(sid, entry_st_nom.get().strip(), entry_st_prenom.get().strip(), entry_st_niveau.get().strip())
    etudiants.append(e)
    clear_student_fields()
    refresh_student_list()


def add_teacher():
    tid = entry_te_id.get().strip()
    if not tid:
        messagebox.showwarning("Erreur", "ID enseignant requis")
        return
    ens = Enseignant(tid, entry_te_nom.get().strip(), entry_te_spec.get().strip())
    enseignants.append(ens)
    clear_teacher_fields()
    refresh_teacher_list()


def add_course():
    code = entry_co_code.get().strip()
    name = entry_co_nom.get().strip()
    sel = teacher_listbox.curselection()
    if not code or not name:
        messagebox.showwarning("Erreur", "Code et nom du cours requis")
        return
    enseignant = None
    if sel:
        idx = sel[0]
        enseignant = enseignants[idx]
    c = Cours(code, name, enseignant)
    cours_list.append(c)
    clear_course_fields()
    refresh_course_list()


def enroll_student_in_course():
    ssel = student_listbox.curselection()
    csel = course_listbox.curselection()
    if not ssel or not csel:
        messagebox.showwarning("Erreur", "Sélectionnez un étudiant et un cours")
        return
    student = etudiants[ssel[0]]
    course = cours_list[csel[0]]
    course.ajouter_etudiant(student)
    refresh_course_list()


def clear_student_fields():
    entry_st_id.delete(0, tk.END)
    entry_st_nom.delete(0, tk.END)
    entry_st_prenom.delete(0, tk.END)
    entry_st_niveau.delete(0, tk.END)


def clear_teacher_fields():
    entry_te_id.delete(0, tk.END)
    entry_te_nom.delete(0, tk.END)
    entry_te_spec.delete(0, tk.END)


def clear_course_fields():
    entry_co_code.delete(0, tk.END)
    entry_co_nom.delete(0, tk.END)


def refresh_student_list():
    student_listbox.delete(0, tk.END)
    for s in etudiants:
        student_listbox.insert(tk.END, s.afficher())


def refresh_teacher_list():
    teacher_listbox.delete(0, tk.END)
    for t in enseignants:
        teacher_listbox.insert(tk.END, t.afficher())


def refresh_course_list():
    course_listbox.delete(0, tk.END)
    for c in cours_list:
        teacher_name = c.enseignant.nom if c.enseignant else "(aucun)"
        course_listbox.insert(tk.END, f"{c.code} - {c.nom} | {teacher_name} ({len(c.etudiants)} inscrits)")


root = tk.Tk()
root.title("Gestion Scolaire — Polished UI")
root.geometry("900x520")

style = ttk.Style(root)
style.theme_use('clam')
# color palette
BG = '#eaf4ff'        # main background
PANEL_BG = '#d6ecff'  # panel background
BTN_BG = '#3b82f6'    # button blue
BTN_FG = '#ffffff'
TEXT_FG = '#03254c'

style.configure('TFrame', background=BG)
style.configure('TLabelframe', background=BG)
style.configure('TLabelframe.Label', foreground=BTN_BG)
style.configure('TLabel', background=BG, foreground=TEXT_FG)
style.configure('TButton', background=BTN_BG, foreground=BTN_FG, padding=6)

root.configure(bg=BG)

main = ttk.Frame(root, padding=10)
main.pack(fill=tk.BOTH, expand=True)

# Panels
left = ttk.Frame(main)
left.grid(row=0, column=0, sticky='nsew', padx=(0, 10))
right = ttk.Frame(main)
right.grid(row=0, column=1, sticky='nsew')
bottom = ttk.Frame(main)
bottom.grid(row=1, column=0, columnspan=2, pady=(10,0), sticky='nsew')

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.rowconfigure(0, weight=1)

# Student panel
st_panel = ttk.Labelframe(left, text='Étudiants', padding=10)
st_panel.pack(fill=tk.BOTH, expand=True)

frm = ttk.Frame(st_panel)
frm.pack(fill=tk.X)
ttk.Label(frm, text='ID').grid(row=0, column=0, sticky='w')
entry_st_id = ttk.Entry(frm)
entry_st_id.grid(row=0, column=1, sticky='ew', padx=5)
ttk.Label(frm, text='Nom').grid(row=1, column=0, sticky='w')
entry_st_nom = ttk.Entry(frm)
entry_st_nom.grid(row=1, column=1, sticky='ew', padx=5)
ttk.Label(frm, text='Prénom').grid(row=2, column=0, sticky='w')
entry_st_prenom = ttk.Entry(frm)
entry_st_prenom.grid(row=2, column=1, sticky='ew', padx=5)
ttk.Label(frm, text='Niveau').grid(row=3, column=0, sticky='w')
entry_st_niveau = ttk.Entry(frm)
entry_st_niveau.grid(row=3, column=1, sticky='ew', padx=5)
frm.columnconfigure(1, weight=1)

ttk.Button(st_panel, text='Ajouter Étudiant', command=add_student).pack(fill=tk.X, pady=6)

student_listbox = tk.Listbox(st_panel, height=10, bg='#f0f8ff', fg=TEXT_FG, selectbackground='#3b82f6', activestyle='none')
student_listbox.pack(fill=tk.BOTH, expand=True)

# Teacher panel
te_panel = ttk.Labelframe(right, text='Enseignants', padding=10)
te_panel.pack(fill=tk.BOTH, expand=True)

frm2 = ttk.Frame(te_panel)
frm2.pack(fill=tk.X)
ttk.Label(frm2, text='ID').grid(row=0, column=0, sticky='w')
entry_te_id = ttk.Entry(frm2)
entry_te_id.grid(row=0, column=1, sticky='ew', padx=5)
ttk.Label(frm2, text='Nom').grid(row=1, column=0, sticky='w')
entry_te_nom = ttk.Entry(frm2)
entry_te_nom.grid(row=1, column=1, sticky='ew', padx=5)
ttk.Label(frm2, text='Spécialité').grid(row=2, column=0, sticky='w')
entry_te_spec = ttk.Entry(frm2)
entry_te_spec.grid(row=2, column=1, sticky='ew', padx=5)
frm2.columnconfigure(1, weight=1)

ttk.Button(te_panel, text='Ajouter Enseignant', command=add_teacher).pack(fill=tk.X, pady=6)

teacher_listbox = tk.Listbox(te_panel, height=10, bg='#f0f8ff', fg=TEXT_FG, selectbackground='#3b82f6', activestyle='none')
teacher_listbox.pack(fill=tk.BOTH, expand=True)

# Bottom: Courses
co_panel = ttk.Labelframe(bottom, text='Cours & Inscriptions', padding=10)
co_panel.pack(fill=tk.BOTH, expand=True)

frm3 = ttk.Frame(co_panel)
frm3.pack(fill=tk.X)
ttk.Label(frm3, text='Code').grid(row=0, column=0, sticky='w')
entry_co_code = ttk.Entry(frm3)
entry_co_code.grid(row=0, column=1, sticky='ew', padx=5)
ttk.Label(frm3, text='Nom').grid(row=1, column=0, sticky='w')
entry_co_nom = ttk.Entry(frm3)
entry_co_nom.grid(row=1, column=1, sticky='ew', padx=5)
frm3.columnconfigure(1, weight=1)

btns = ttk.Frame(co_panel)
btns.pack(fill=tk.X, pady=6)
ttk.Button(btns, text='Ajouter Cours (sélectionner enseignant à droite)', command=add_course).pack(side=tk.LEFT, padx=4)
ttk.Button(btns, text='Inscrire Étudiant au Cours', command=enroll_student_in_course).pack(side=tk.LEFT, padx=4)

course_listbox = tk.Listbox(co_panel, height=6, bg='#f0f8ff', fg=TEXT_FG, selectbackground='#3b82f6', activestyle='none')
course_listbox.pack(fill=tk.BOTH, expand=True)

refresh_student_list()
refresh_teacher_list()
refresh_course_list()

root.mainloop()
tk.Label(root, text="Nom Enseignant").grid(row=1, column=2)
entry_nom_ens = tk.Entry(root)
entry_nom_ens.grid(row=1, column=3)

tk.Label(root, text="Spécialité").grid(row=2, column=2)
entry_spec = tk.Entry(root)
entry_spec.grid(row=2, column=3)

tk.Button(root, text="Ajouter Enseignant", command=ajouter_enseignant).grid(row=3, column=3)
tk.Button(root, text="Afficher Enseignants", command=afficher_enseignants).grid(row=4, column=3)

text = tk.Text(root, height=10, width=40)
text.grid(row=6, column=0, columnspan=2)

root.mainloop()