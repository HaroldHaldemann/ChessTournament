from Controllers import players_controller

class PlayerView():

	def add_player_to_db(self, args={}):
		step = 6-len(args)
		player_controller = players_controller.PlayerController()
		while step != 0:
			print("\nCREATION D'UN NOUVEAU JOUEUR")
			if step == 6:
				last_name = input("Veuillez renseigner le nom de ce joueur\n")
				player_controller.check_args(args, last_name=last_name)
			elif step == 5:
				first_name = input("Veuillez renseigner le prénom de ce joueur\n")
				player_controller.check_args(args, first_name=first_name)
			elif step == 4:
				print("Veuillez renseigner la date de naissance du joueur")
				birth_date = input("Format: JJ/MM/AAAA\n")
				player_controller.check_args(args, birth_date=birth_date)
			elif step == 3:
				print("Veuillez renseigner le sexe du joueur")
				print("1- Masculin")
				print("2- Féminin")
				gender = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
				player_controller.check_args(args, gender=gender)
			elif step == 2:
				print("Veuillez renseigner le classement du joueur")
				ranking = input("Le classement est un nombre positif\n")
				player_controller.check_args(args, ranking=ranking)
			elif step == 1:
				print("Résumé du joueur:")
				print(f"Nom: {args['last_name']}")
				print(f"Prénom: {args['first_name']}")
				print(f"Date de naissance: {args['birth_date']}")
				print(f"Sexe: {args['gender']}")
				print(f"Classemnt: {args['ranking']}")
				print("\nVoulez-vous continuer avec ces paramètres?")
				print("1- Modifier")
				print("2- Sauvegarder et ajouter un nouveau joueur")
				print("3- Sauvegarder et revenir au menu principal")
				response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
				player_controller.check_args(args, response=response)
		player_controller.add_player_to_db(args)


	def export_all_players(self):
		pass
