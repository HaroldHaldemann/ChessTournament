from Controllers import tournaments_controller

class TournamentView():

	def new_tournament(self, args={}):
		step = 8-len(args)
		tournament_controller = tournaments_controller.TournamentController()
		while step != 0:
			if step == 8:
				print("\nCREATION D'UN NOUVEAU TOURNOI")
				step += 1
			elif step == 7:
				name = input("\nVeuillez renseigner le nom de ce tournoi\n")
				tournament_controller.check_args(step, args, name=name)
			elif step == 6:
				place = input("\nVeuillez renseigner le lieu de ce tournoi\n")
				tournament_controller.check_args(step, args, place=place)
			elif step == 5:
				print("\nVeuillez renseigner la date de ce tournoi")
				date = input("Format: JJ/DD/AAAA\n")
				tournament_controller.check_args(step, args, date=date)
			elif step == 4:
				print("\nVeuillez renseigner votre controle du temps")
				print("1- Bullet")
				print("2- Blitz")
				print("3- Coup rapide")
				time_control = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
				tournament_controller.check_args(step, args, time_control=time_control)
			elif step == 3:
				print("\nVous pouvez renseigner des remarques pour ce tournoi")
				description = input("Laissez vide dans le cas contraire\n")
				tournament_controller.check_args(step, args, description=description)
			elif step == 2:
				print("\nVeuillez renseigner le nombre de tours de ce tournoi")
				number_rounds = input("Nombre entre 1 et 7 compris (Par défault: 4)\n") or 4
				tournament_controller.check_args(step, args, number_rounds=number_rounds)
			elif step == 1:
				print("\nRESUME DU TOURNOI")
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
				tournament_controller.check_args(step, args, response=response)
		tournament_controller.new_tournament(
			name=args['name'],
			place=args['place'],
			date=args['date'],
			time_control=args['time_control'],
			description=args['description'],
			number_rounds=args['number_roundsm'],
		)


	def add_player_to_tournament(self, all_players, players=[]):
		print(f"Veuillez ajouter {8-len(players)} joueurs dans le tournoi")
		for index, player in enumerate(all_players):
			print(
				f"{index}- " \
				f"Nom: {player['last_name']} " \
				f"Prénom: {player['first_name']}, " \
				f"Date de naissance: {player['bitrth_date']}, " \
				f"Genre: {player['gender']}, " \
				f"Classement: {player['ranking']}" 
			)
		player = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")




	def load_tournament():
		pass

	def export_players():
		pass

	def export_all_tournaments():
		pass

	def export_rounds():
		pass

	def export_matches():
		pass
