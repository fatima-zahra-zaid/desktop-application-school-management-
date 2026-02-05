class Cours:
    def __init__(self, code, nom, enseignant):
        self.code = code
        self.nom = nom
        self.enseignant = enseignant
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def afficher(self):
        return f"{self.code} - {self.nom} | Enseignant : {self.enseignant.nom}"