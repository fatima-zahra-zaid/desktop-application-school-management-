"""Module etudiant

Classe très simple pour stocker les infos d'un étudiant.
"""


class Etudiant:
    """Représente un étudiant."""

    def __init__(self, id_etudiant, nom, prenom, niveau):
        self.id = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.niveau = niveau

    def afficher(self):
        """Retourne une chaîne lisible pour afficher l'étudiant."""
        return f"{self.id} - {self.nom} {self.prenom} ({self.niveau})"
    