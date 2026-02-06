class Enseignant:

    def __init__(self, id_enseignant, nom, specialite):
        self.id = id_enseignant
        self.nom = nom
        self.specialite = specialite

    def afficher(self):
        return f"{self.id} - {self.nom} ({self.specialite})"