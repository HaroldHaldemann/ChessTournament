import exports_view
import tournaments_view

def main_menu():
	response = ""
	while response not in [f"{i}" for i in range(5)]:
		print("\nMENU PRINCIPAL")
		print(" Veuillez selectionner l'action à réaliser en entrant le numéro correspondant:")
		print("1- Créer un nouveau tournoi")
		print("2- Charger un tournoi existant")
		print("3- Générer un rapport")
		print("4- Quitter le programme\n")
		response = input("Veuillez entrer un numéro correspondant à une action et presser entrée\n")
		if response not in [f"{i}" for i in range(5)]:
			print("\nCommande incorrect, veuillez entrer un numéro valide")
	options = {
		'1': tournaments_view.new_tournament,
		'2': tournaments_view.load_tournament_menu,
		'3': exports_view.export_menu,
		'4': exit,
	}
	options[response]()

if __name__ == '__main__':
	main_menu()