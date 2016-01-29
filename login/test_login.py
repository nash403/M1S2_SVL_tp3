"""
SVL 2016
TP login
Auteur: Honore Nintunze, antonin Durey

Tests
"""

# fonctionnalites

# creer user à la main
# - entre les param et ç cree un user
# - user deja existant -> erreur
# - login ne fait pas plus de 8 caracteres

# creer user auto
# - plan A -> max 8 lettres

import unittest
from mockito import mock, when, verify
from login import *

class TestCreerUserALaMain(unittest.TestCase):

    def test_user_est_cree(self):
        Bdd = mock()
        user  = mock()
        fabrique_user = mock()
        LOGIN = "log"
        when(fabrique_user).creer_user("nom", "prenom",LOGIN).thenReturn(user)
        login_manager = LoginManager(fabrique_user, Bdd)
        self.assertEqual(login_manager.create_user_manuel("nom", "prenom", LOGIN), user)

    def test_user_existe_deja(self):
        Bdd = mock()
        user  = mock()
        fabrique_user = mock()
        LOGIN = "log"
        when(fabrique_user).creer_user("nom", "prenom",LOGIN).thenRaise(LoginAlreadyExistsError)
        login_manager = LoginManager(fabrique_user, Bdd)
        self.assertRaises(LoginAlreadyExistsError, login_manager.create_user_manuel, "nom", "prenom", LOGIN)

    def test_login_trop_grand(self):
        Bdd = mock()
        user  = mock()
        fabrique_user = mock()
        LOGIN = "logloglog"
        when(fabrique_user).creer_user("nom", "prenom",LOGIN).thenRaise(LoginTooLongError)
        login_manager = LoginManager(fabrique_user, Bdd)
        self.assertRaises(LoginTooLongError, login_manager.create_user_manuel, "nom", "prenom", LOGIN)

    def test_login_pas_en_minuscule(self):
        Bdd = mock()
        user  = mock()
        fabrique_user = mock()
        LOGIN = "logRAkKB"
        when(fabrique_user).creer_user("nom", "prenom",LOGIN).thenRaise(LoginWrongFormatError)
        login_manager = LoginManager(fabrique_user, Bdd)
        self.assertRaises(LoginWrongFormatError, login_manager.create_user_manuel, "nom", "prenom", LOGIN)


class TestCreerUserAuto(unittest.TestCase):

    def test_nom_plus_grand_que_max(self):
        Bdd = mock()
        user = mock()
        fabrique_user = mock()
        nom = "duponchel"
        prenom = "alexandre"
        when(user).get_login().thenReturn("duponche")
        when(fabrique_user).creer_user(nom, prenom, "duponche").thenReturn(user)

        login_manager = LoginManager(fabrique_user, Bdd)

        self.assertEqual(login_manager.create_user_auto(nom, prenom).get_login(), "duponche")


    def test_nom_plus_petit_que_max(self):
        Bdd = mock()
        user = mock()
        fabrique_user = mock()
        nom = "dupont"
        prenom = "alexandre"
        when(user).get_login().thenReturn("dupont")
        when(fabrique_user).creer_user(nom, prenom, "dupont").thenReturn(user)

        login_manager = LoginManager(fabrique_user, Bdd)

        self.assertEqual(login_manager.create_user_auto(nom, prenom).get_login(), "dupont")


    def test_nom_plus_initiale_prenom(self):
        Bdd = mock()
        user = mock()
        fabrique_user = mock()
        nom = "dupont"
        prenom = "alexandre"
        when(user).get_login().thenReturn("duponta")
        when(fabrique_user).creer_user(nom, prenom, "duponta").thenReturn(user)
        when(Bdd).exist("dupont").thenReturn(True)


        login_manager = LoginManager(fabrique_user, Bdd)

        self.assertEqual(login_manager.create_user_auto(nom, prenom).get_login(), "duponta")

    def test_nom_plus_initiale_prenom_existe_donc_faix_au_mieux(self):
        Bdd = mock()
        user = mock()
        fabrique_user = mock()
        nom = "dupont"
        prenom = "alexandre"
        when(user).get_login().thenReturn("dupont1")
        when(fabrique_user).creer_user(nom, prenom, "dupont1").thenReturn(user)
        when(Bdd).exist("dupont").thenReturn(True)
        when(Bdd).exist("duponta").thenReturn(True)


        login_manager = LoginManager(fabrique_user, Bdd)

        self.assertEqual(login_manager.create_user_auto(nom, prenom).get_login(), "dupont1")
