import main_menu_view


def export_menu():
	response = ""
	while response not in [f"{i}" for i in range(7)]:
		print("\nMENU GENERATION DE RAPPORT")
		print(" Veuillez selectionner l'action à réaliser en entrant le numéro correspondant:")
		print("1- Liste de tous les acteurs")
		print("2- Liste de tous les joueurs d'un tournoi")
		print("3- Liste de tous les tournois")
		print("4- Liste de tous les tours d'un tournoi")
		print("5- Liste de tous les matchs d'un tournoi")
		print("6- Revenir au menu principal\n")
		response = input("Veuillez entrer un numéro correspondant à une action et presser entrée\n")
		if response not in [f"{i}" for i in range(7)]:
			print("\nCommande incorrect, veuillez entrer un numéro valide")
		options = {
			'1': all_players,
			'2': list_players_tournament,
			'3': all_tournaments,
			'4': list_tours_tournament,
			'5': list_matches_tournament,
			'6': main_menu_view.main_menu,
		}
		options[response]()


def all_players():
	pass


def list_players_tournament():
	pass


def all_tournaments():
	pass


def list_tours_tournament():
	pass


def list_matches_tournament():
	pass