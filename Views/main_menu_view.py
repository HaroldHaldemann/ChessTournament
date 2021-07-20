def main_menu():
	response = ""
	while response not in range(5):
		print(" \nVeuillez selectionner l'action à réaliser en entrant le numéro correspondant:")
		print("1- Créer un nouveau tournoi")
		print("2- Charger un tournoi existant")
		print("3- Générer un rapport")
		print("4- Quitter le programme\n")
		response = input("Veuillez entrer un numéro correspondant à une action et presser entrée")

