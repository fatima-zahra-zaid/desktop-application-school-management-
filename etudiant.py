class Etudiant:
    def __init__(self, id_etudiant, nom, prenom, niveau):
        self.id = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.niveau = niveau

    def afficher(self):
        return f"{self.id} - {self.nom} {self.prenom} ({self.niveau})"