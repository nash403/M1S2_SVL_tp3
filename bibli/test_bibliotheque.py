"""
SVL 2016
TP bibliotheque de livre
Auteur: Honore Nintunze

Tests
"""

# fonctionnalites

# emprunter livre
# - si le livre que consultable, emrpunt echoue
# - si le membre a atteint quota, emprunt echoue
# - sinon emprunt cree et disponible pour affichage

# rendre livre

import unittest
import mockito
from bibliotheque import *

class TestEmprunterUnLivre(unittest.TestCase):

    def test_livre_consultable_uniquement_alors_emprunt_echoue(self):
        livre = mock()
        when(livre).est_empruntable().thenReturn(False)
        fabrique_emprunts = mock()
        service_emprunt = ServiceEmprunt(fabrique_emprunts)
        self.assertRaises(LivreNonEmpruntableError,service_emprunt.emprunter,livre)

    def test_membre_a_atteint_son_quota_emprunt_echoue(self):
        livre = mock()
        membre = mock()
        when(membre).peut_emprunter().thenReturn(False)
        fabrique_emprunts = mock()
        service_emprunt = ServiceEmprunt(fabrique_emprunts)
        self.assertRaises(QuotaAtteintError,service_emprunt.emprunter,livre, membre)

    def test_l_emprunt_est_cree(self):
        livre = mock()
        membre = mock()
        when(livre).est_empruntable().thenReturn(True)
        when(membre).peut_emprtunter().thenReturn(True)
        emprunt = mock()
        fabrique_emprunts = mock()
        when(fabrique_emprunts).creer_emprunt(livre,membre).thenReturn(emprunt)
        service_emprunt = ServiceEmprunt(fabrique_emprunts)

        self.assertEqual(...)
