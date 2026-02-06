"""Module cours

Contient une petite classe Cours, pensée pour débutants.
Chaque cours a un code, un nom, un enseignant (optionnel) et une liste d'étudiants.
"""


class Cours:
    """Représente un cours.

    Args:
        code (str): code du cours (ex: MATH101)
        nom (str): nom du cours
        enseignant (Enseignant | None): enseignant responsable (peut être None)
    """

    def __init__(self, code, nom, enseignant=None):
        self.code = code
        self.nom = nom
        self.enseignant = enseignant  # peut être None
        self.etudiants = []  # liste d'objets Etudiant

    def ajouter_etudiant(self, etudiant):
        """Ajoute un étudiant au cours."""
        self.etudiants.append(etudiant)

    def afficher(self):
        """Retourne une chaîne lisible pour afficher le cours.

        Gère le cas où l'enseignant n'est pas défini (None).
        """
        nom_ens = self.enseignant.nom if self.enseignant else "N/A"
        return f"{self.code} - {self.nom} | Enseignant : {nom_ens}"