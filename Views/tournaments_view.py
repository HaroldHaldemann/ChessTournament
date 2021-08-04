from Controllers import tournaments_controller

class TournamentView():

	def new_tournament(self, step):
		tournament_controller = tournaments_controller.TournamentController()
		while step < 7:
			if step == 0:
				print("\nCREATION D'UN NOUVEAU TOURNOI")
				step += 1
			elif step == 1:
				name = input("\nVeuillez renseigner le nom de ce tournoi\n")
				tournament_controller.check_args(step, name=name)
			elif step == 2:
				place = input("\nVeuillez renseigner le lieu de ce tournoi\n")
				tournament_controller.check_args(step, place=place)
			elif step == 3:
				print("\nVeuillez renseigner la date de ce tournoi")
				date = input("Format: JJ/DD/AAAA\n")
				tournament_controller.check_args(step, date=date)
			elif step == 4:
				print("\nVeuillez selectionner une des options disponibles")
				print("1 - Bullet")
				print("2 - Blitz")
				print("3 - Coup rapide")
				time_control = input("Veuillez renseigner le numéro correspondant à vorte choix\n")
				tournament_controller.check_args(step, time_control=time_control)
			elif step == 5:
				print("\nVous pouvez renseigner des remarques pour ce tournoi")
				description = input("Laissez vide dans le cas contraire\n")
				tournament_controller.check_args(step, description=description)
			elif step == 6:
				print("\nVeuillez renseigner le nombre de tours de ce tournoi")
				number_rounds = input("Nombre entre 1 et 7 compris (Par défault: 4)\n") or 4
				tournament_controller.check_args(step, number_rounds=number_rounds)
		print("OK")
		exit()


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
