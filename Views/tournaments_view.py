import Controllers

class TournamentView():

##### NEW TOURNAMENT #####

	@classmethod
	def new_tournament(cls, args):
		step = len(args)
		print("\nCREATION D'UN NOUVEAU TOURNOI")

		options = {
			1: cls.new_tournament_name,
			2: cls.new_tournament_place,
			3: cls.new_tournament_date,
			4: cls.new_tournament_time_control,
			5: cls.new_tournament_description,
			6: cls.new_tournament_number_rounds,
			7: cls.new_tournament_response,
		}
		Controllers.Util.call_options(options, step)


	@staticmethod
	def new_tournament_name(args):
		name = input("Veuillez renseigner le nom de ce tournoi\n")

		Controllers.TournamentController.check_args(args, name=name)


	@staticmethod
	def new_tournament_place(args):
		place = input("Veuillez renseigner le lieu de ce tournoi\n")

		Controllers.TournamentController.check_args(args, place=place)


	@staticmethod
	def new_tournament_date(args):
		print("Veuillez renseigner la date de ce tournoi")
		date = input("Format: AAAA-MM-JJ\n")

		Controllers.TournamentController.check_args(args, date=date)


	@staticmethod
	def new_tournament_time_control(args):
		print("Veuillez renseigner votre controle du temps")
		print("1- Bullet")
		print("2- Blitz")
		print("3- Coup rapide")

		time_control = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")

		Controllers.TournamentController.check_args(args, time_control=time_control)


	@staticmethod
	def new_tournament_description(args):
		print("Vous pouvez renseigner des remarques pour ce tournoi")
		description = input("Laissez vide dans le cas contraire\n")

		Controllers.TournamentController.check_args(args, description=description)


	@staticmethod
	def new_tournament_number_rounds(args):
		print("Veuillez renseigner le nombre de tours de ce tournoi")
		number_rounds = input("Nombre entre 1 et 7 compris (Par défault: 4)\n") or 4

		Controllers.TournamentController.check_args(args, number_rounds=number_rounds)


	@staticmethod
	def new_tournament_response(args):
		print("Résumé du tournoi")
		print(f"Nom: {args['name']}")
		print(f"Lieu: {args['place']}")
		print(f"Date: {args['date']}")
		print(f"Gestion du temps: {args['time_control']}")
		print(f"Remarques: {args['description']}")
		print(f"Nombre de tours: {args['number_rounds']}")

		print("\nVoulez-vous continuer avec ces paramètres?")
		print("1- Modifer")
		print("2- Sauvegarder et continuer")

		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
		Controllers.TournamentController.check_args(args, response=response)


##### ADD PLAYER TO TOURNAMENT #####


	@staticmethod
	def add_player_to_tournament(all_players, players):
		print("\nAJOUT DE JOUEURS")
		print(f"Veuillez ajouter {8-len(players)} joueurs dans le tournoi")

		print("\n0- Ajouter de nouveaux joueurs à la base de données")
		print("\nListe des joueurs:")

		for index, player in enumerate(all_players):
			print(f"\n{index + 1}- Nom: {player['last_name']} {player['first_name']}")
			print(f"Date de naissance: {player['birth_date']}")
			print(f"Genre: {player['gender']}")
			print(f"Classement: {player['ranking']}")
			
		player = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
		players.append(player)

		Controllers.TournamentController.add_player_to_tournament(all_players, players)


	@staticmethod
	def confirm_players(all_players, players):
		print("\nAJOUT DE JOUEURS")
		print("\nListe des joueurs:")

		for index, player in enumerate(players):
			print(f"\n{index + 1}- Nom: {player['last_name']} {player['first_name']}")
			print(f"Date de naissance: {player['birth_date']}")
			print(f"Genre: {player['gender']}")
			print(f"Classement: {player['ranking']}")

		print("\nVoulez-vous ces joueurs pour le tournoi?")
		print("1- Confimer et sauvegarder")
		print("2- Modifier la séléction")
		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")

		Controllers.TournamentController.confirm_players(all_players, players, response)


##### LOAD TOURNAMENT #####


	@staticmethod
	def load_tournament(list_tournaments):
		print("\nCHARGEMENT D'UN TOURNOI")
		print("0- Créer un nouveau tournoi")
		print("Liste des tournois:")

		for index, tournament in enumerate(list_tournaments):
			print(
				f"{index+1}- " \
				f"Nom: {tournament['name']}, " \
				f"Lieu: {tournament['place']}, " \
				f"Date: {tournament['date']}, " \
				f"Gestion du temps: {tournament['time_control']}"
			)
		response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")

		Controllers.TournamentController.load_tournament(list_tournaments, response=response)


##### EXPORTS #####


	def export_players(self):
		pass

	def export_all_tournaments(self):
		pass

	def export_rounds(self):
		pass

	def export_matches(self):
		pass
