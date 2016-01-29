"""
SVL 2016
TP login
Auteur: Honore Nintunze, antonin Durey

Classes
"""

class LoginManager:
    """docstring for LoginManager"""
    def __init__(self, fabrique, Bdd):
        self.fabrique_user = fabrique
        self.BDD = Bdd

    def create_user_manuel(self, nom, prenom, login):
        return self.fabrique_user.creer_user(nom, prenom, login)

    def create_user_auto(self, nom, prenom):

        login = nom[:8].lower()

        if not self.BDD.exist(login):
            return self.fabrique_user.creer_user(nom, prenom, login)
        else:
            login = (nom[:7] + prenom[0]).lower()
            if not self.BDD.exist(login):
                return self.fabrique_user.creer_user(nom, prenom, login)
            cpt = 1
            login = nom[:7].lower() + str(cpt)
            while self.BDD.exist(login):
                cpt += 1
                login = nom[:7].lower() + cpt

        return self.fabrique_user.creer_user(nom, prenom, login)

class BDD:

    # def exists(self,login):
    #    pass
    pass

class LoginAlreadyExistsError(Exception):
    pass

class LoginTooLongError(Exception):
    pass

class LoginWrongFormatError(Exception):
    pass
