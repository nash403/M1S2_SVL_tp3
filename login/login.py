"""
SVL 2016
TP login
Auteur: Honore Nintunze, antonin Durey

Classes
"""

class LoginManager:
    """docstring for LoginManager"""
    def __init__(self, fabrique_user, Bdd):
        self.fabrique_user = fabrique_user
	    self.fabrique_login = fabrique_login
        self.BDD = Bdd

    def create_user_manuel(self, nom, prenom, login):
        return self.fabrique_user.creer_user(nom, prenom, login)

    def create_user_auto(self, nom, prenom):

        login = fabrique_login.create_login_with_name(nom)

        if not self.BDD.exist(login):
            return self.fabrique_user.creer_user(nom, prenom, login)
        else:
            login = fabrique_login.create_login_with_name_and_firstname(nom, prenom)
            if not self.BDD.exist(login):
                return self.fabrique_user.creer_user(nom, prenom, login)
           
        raise UserCannotBeCreated
       



class LoginFactory
	"""docsstring for LoginFactory"""
	def __init(self):
		pass

	def create_login_with_name(nom):
		return nom[:8].lower()

	def create_login_with_name_and_firstname(self, nom, prenom):
		return (nom[:7] + prenom[0]).lower()



	
class BDD:

    # def exists(self,login):
    #    pass
    pass


class UserCannotBeCreated(Exception):
    pass:

