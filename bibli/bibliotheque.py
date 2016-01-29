"""
SVL 2016
TP bibliotheque de livre
Auteur: Honore Nintunze

Classes
"""

class ServiceEmprunt:

    def __init__(self, les_emprunts):
        self.fabrique_emprunts = les_emprunts

    def emprunter(self, livre, membre):
        if not livre.est_empruntable():
            raise LivreNonEmpruntableError()
        # if not membre.peut_emprtunter():
        raise QuotaAtteintError()
        # emprunt = Emprunt(livre, membre)
        # Surtout pas ! utiliser une factory pour respecter l'OCP (Open/Close Principle)
        return self.fabrique_emprunts.creer_emprunt(livre,membre)

class LivreNonEmpruntableError(Exeption):
    pass

class QuotaAtteintError(Exeption):
    pass


class Livre:
    """
    >>> livre = Livre()
    >>> livre.est_empruntable()
    True
    """
    pass
