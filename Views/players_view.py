import Controllers

class PlayerView():

##### ADD PLAYER TO DATABASE #####


	@classmethod
	def add_player_to_db(cls, args={}):
		step = len(args)
		print("\nCREATION D'UN NOUVEAU JOUEUR")

		options = [
			cls.add_player_last_name,
			cls.add_player_first_name,
			cls.add_player_birth_date,
			cls.add_player_gender,
			cls.add_player_ranking,
			cls.add_player_response,
		]
		options[step](args)


	@staticmethod
	def add_player_last_name(args):
		last_name = input("Veuillez renseigner le nom de ce joueur\n")

		Controllers.PlayerController.check_args(args, last_name=last_name)


	@staticmethod
	def add_player_first_name(args):
		first_name = input("Veuillez renseigner le prénom de ce joueur\n")

		Controllers.PlayerController.check_args(args, first_name=first_name)


	@staticmethod
	def add_player_birth_date(args):
		print("Veuillez renseigner la date de naissance du joueur")
		birth_date = input("Format: JJ/MM/AAAA\n")

		Controllers.PlayerController.check_args(args, birth_date=birth_date)


	@staticmethod
	def add_player_gender(args):
		print("Veuillez renseigner le sexe du joueur")
		print("1- Masculin")
		print("2- Féminin")

		gender = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")

		Controllers.PlayerController.check_args(args, gender=gender)


	@staticmethod
	def add_player_ranking(args):
		print("Veuillez renseigner le classement du joueur")
		ranking = input("Le classement est un nombre positif\n")

		Controllers.PlayerController.check_args(args, ranking=ranking)


	@staticmethod
	def add_player_response(args):
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
		print("4- Annuler et revenir au menu principal")

		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")

		Controllers.PlayerController.check_args(args, response=response)


##### EXPORTS #####


	def export_all_players(self):
		pass
