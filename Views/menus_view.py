from Controllers import menus_controller

class MenuView():

	def main_menu(self):
		print("\nMENU PRINCIPAL")
		print("1- Créer un nouveau tournoi")
		print("2- Charger un tournoi existant")
		print("3- Générer un rapport")
		print("4- Quitter le programme\n")
		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
		menu_controller = menus_controller.MenuController()
		menu_controller.main_menu(response)

	def export_menu(self):
		print("\nMENU GENERATION DE RAPPORT")
		print("1- Liste de tous les acteurs")
		print("2- Liste de tous les joueurs d'un tournoi")
		print("3- Liste de tous les tournois")
		print("4- Liste de tous les tours d'un tournoi")
		print("5- Liste de tous les matchs d'un tournoi")
		print("6- Revenir au menu principal\n")
		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
		menu_controller = menus_controller.MenuController()
		menu_controller.export_menu(response)
