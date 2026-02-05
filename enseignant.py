"""Module enseignant

Classe très simple pour stocker les infos d'un enseignant.
"""


class Enseignant:
    """Représente un enseignant."""

    def __init__(self, id_enseignant, nom, specialite):
        self.id = id_enseignant
        self.nom = nom
        self.specialite = specialite

    def afficher(self):
        """Retourne une chaîne lisible pour afficher l'enseignant."""
        return f"{self.id} - {self.nom} ({self.specialite})"