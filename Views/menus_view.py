from Controllers import menus_controller
from Controllers import tournaments_controller

class MenuView():

	def main_menu(self):
		print("\nMENU PRINCIPAL")
		print("1- Créer un nouveau tournoi")
		print("2- Charger un tournoi")
		print("3- Ajouter des joueurs dans la base de données")
		print("4- Générer un rapport")
		print("5- Quitter le programme\n")
		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
		menu_controller = menus_controller.MenuController()
		menu_controller.main_menu(response)

	def export_menu(self):
		print("\nMENU GENERATION DE RAPPORT")
		print("1- Liste de tous les joueurs")
		print("2- Liste de tous les joueurs d'un tournoi")
		print("3- Liste de tous les tournois")
		print("4- Liste de tous les tours d'un tournoi")
		print("5- Liste de tous les matchs d'un tournoi")
		print("6- Revenir au menu principal\n")
		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
		menu_controller = menus_controller.MenuController()
		menu_controller.export_menu(response)

	def load_menu(self):
		print("\nCHARGEMENT D'UN TOURNOI")
		print("1- Charger un tournoi non complété")
		print("2- Charger un tournoi complété")
		print("3- Revenir au menu principal")
		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
		menu_controller = menus_controller.MenuController()
		menu_controller.load_menu(response)
