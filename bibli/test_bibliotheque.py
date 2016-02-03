"""
SVL 2016
TP bibliotheque de livre
Auteur: Honore Nintunze

Tests
"""
# emprunter un livre
# - si le livre n'est que consultable  l'emprunt échoue
# - si le membre a atteint son quota l'emprunt échoue
# - sinon un emprunt est créé et disponible pour affichage

# rendre un livre
# - le membre a depasse les 30 jours, on notifie le service des litiges
# - sinon l'emprunt est cloturé

import unittest
from mockito import *
from bibliotheque import *

class TestEmprunterUnLivre(unittest.TestCase):

    def test_livre_consultable_uniquement_l_emprunt_echoue(self):
        livre = mock()
        when(livre).est_empruntable().thenReturn(False)
        membre = mock()
        fabrique_emprunts = mock()

        service_emprunts = ServiceEmprunt(fabrique_emprunts)
        self.assertRaises(LivreNonEmpruntableError,service_emprunts.emprunter,livre, membre)


    def test_le_membre_a_atteint_son_quota_l_emprunt_echoue(self):
        livre = mock()
        when(livre).est_empruntable().thenReturn(True)
        membre = mock()
        when(membre).peut_emprunter().thenReturn(False)
        fabrique_emprunts = mock()

        service_emprunts = ServiceEmprunt(fabrique_emprunts)
        self.assertRaises(QuotaAtteintError,service_emprunts.emprunter,livre, membre)

    def test_l_emprunt_est_cree(self):
        livre = mock()
        membre = mock()
        when(livre).est_empruntable().thenReturn(True)
        when(membre).peut_emprunter().thenReturn(True)
        emprunt = mock()
        fabrique_emprunts = mock()
        when(fabrique_emprunts).creer_emprunt(livre, membre).thenReturn(emprunt)

        service_emprunts = ServiceEmprunt(fabrique_emprunts)

        self.assertEqual(service_emprunts.emprunter(livre, membre), emprunt)

class TestRendreUnLivre(unittest.TestCase):

    def test_membre_a_depasse_duree_emprunt_genere_un_signalement(self):
        emprunt = mock()
        fabrique_emprunts = mock()
        service_emprunts = ServiceEmprunt(fabrique_emprunts)
        service_litige = mock()

        service_emprunts.rendre(emprunt)

        verify(service_litige).signaler(emprunt)

    def test_emprunt_est_cloture(self):
        emprunt = mock()
        fabrique_emprunts = mock()
        service_emprunts = ServiceEmprunt(fabrique_emprunts)

        service_emprunts.rendre(emprunt)

        verify(emprunt).cloture()
