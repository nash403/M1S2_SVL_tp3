"""
SVL 2016
TP bibliotheque de livre
Auteur: Honore Nintunze

Classes
"""
class ServiceEmprunt:

    def __init__(self, les_emprunts):
        self.fabrique_emprunts = les_emprunts
        self.service_litige = ServiceLitige()

    def emprunter(self, livre, membre):
        if not livre.est_empruntable():
            raise LivreNonEmpruntableError()
        if not membre.peut_emprunter():
            raise QuotaAtteintError()
        # emprunt = Emprunt(livre, membre)
        # JAMAIS ! SURTOUT PAS !
        return self.fabrique_emprunts.creer_emprunt(livre, membre)

    def rendre(self,emprunt):
        if not membre.est_dans_les_temps():
            self.service_litige.signaler(emprunt)

        emprunt.cloture()

class LivreNonEmpruntableError(Exception):
    pass

class QuotaAtteintError(Exception):
    pass

class Livre:
    """
    >>> livre = Livre()
    >>> livre.est_empruntable()
    True
    """
    pass

class Membre:
    """
    >>> membre = Membre()
    >>> membre.peut_emprunter()
    True
    """
    pass

class FabriqueEmprunts:
    """
    Permet de créer des emprunts.
    >>> fabrique = FabriqueEmprunts()
    >>> livre = Livre()
    >>> membre = membre()
    >>> emprunt = fabrique.creer_emprunt(livre, membre)
    """
    pass

class ServiceLitige:
    """
    Permet de gerer les litiges des emprunts
    >>> litiges = ServiceLitige()
    >>> fabrique = FabriqueEmprunts()
    >>> livre = Livre()
    >>> membre = membre()
    >>> emprunt = fabrique.creer_emprunt(livre, membre)
    >>> litiges.signaler(emprunt)
    """
    pass
