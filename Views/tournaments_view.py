from Controllers import tournaments_controller

class TournamentView():

	def new_tournament(self, args={}):
		step = 7-len(args)
		tournament_controller = tournaments_controller.TournamentController()
		while step != 0:
			print("\nCREATION D'UN NOUVEAU TOURNOI")
			if step == 7:
				name = input("Veuillez renseigner le nom de ce tournoi\n")
				tournament_controller.check_args(args, name=name)
			elif step == 6:
				place = input("Veuillez renseigner le lieu de ce tournoi\n")
				tournament_controller.check_args(args, place=place)
			elif step == 5:
				print("Veuillez renseigner la date de ce tournoi")
				date = input("Format: JJ/MM/AAAA\n")
				tournament_controller.check_args(args, date=date)
			elif step == 4:
				print("Veuillez renseigner votre controle du temps")
				print("1- Bullet")
				print("2- Blitz")
				print("3- Coup rapide")
				time_control = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
				tournament_controller.check_args(args, time_control=time_control)
			elif step == 3:
				print("Vous pouvez renseigner des remarques pour ce tournoi")
				description = input("Laissez vide dans le cas contraire\n")
				tournament_controller.check_args(args, description=description)
			elif step == 2:
				print("Veuillez renseigner le nombre de tours de ce tournoi")
				number_rounds = input("Nombre entre 1 et 7 compris (Par défault: 4)\n") or 4
				tournament_controller.check_args(args, number_rounds=number_rounds)
			elif step == 1:
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
				tournament_controller.check_args(args, response=response)
		tournament_controller.new_tournament(args)


	def add_player_to_tournament(self, all_players, players=[]):
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
		tournament_controller = tournaments_controller.TournamentController()
		tournament_controller.add_player_to_tournament(all_players, players)


	def load_tournament(self, list_tournaments):
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
		tournament_controller = tournaments_controller.TournamentController()
		tournament_controller.load_tournament(list_tournaments, response=response, finished="")

	def export_players(self):
		pass

	def export_all_tournaments(self):
		pass

	def export_rounds(self):
		pass

	def export_matches(self):
		pass
