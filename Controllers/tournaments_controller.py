from Views import tournaments_view
from Models import tournaments

class TournamentController():

	def new_tournament(self, name, place, date, time_control, description, number_rounds):
		pass


###############################################################
#  UTILS                                                      #
###############################################################


	def check_name(self, name):
		if name == "":
			print("Nom invalide: entrée vide")
			return False
		tournament = tournaments.Tournament()
		if name in tournament.get_name_tournaments():
			print("Nom invalide: nom déjà existant")
			return False
		return True


	def check_place(self, place):
		if place == "":
			print("Lieu invalide: entrée vide")
			return False
		return True


	def check_date(self, date):
		split_date = date.split('/')
		if len(split_date) != 3:
			print("Date invalide: format invalide")
			return False
		for e in split_date:
			if not e.isdigit():
				print("Date invalide: veuillez utiliser des nombres")
				return False
		day = int(split_date[0])
		month = int(split_date[1])
		year = int(split_date[2])
		days_by_month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if year%4 == 0 and (year%100 != 0 or year%400 == 0):
			days_by_month[2] = 29
		if not (0 < month < 13 and 0 < day <= days_by_month[month]):
			print("Date invalide: cette date n'existe pas")
			return False
		return True


	def check_time_control(self, time_control):
		if time_control not in ['1', '2', '3']:
			print("Gestion de temps invalide")
			return False
		return True


	def check_number_rounds(self, number_rounds):
		if type(number_rounds) == int:
			return True
		if not number_rounds.isdigit():
			print("Nombre de tours invalide")
			return False
		if not (0 < int(number_rounds) < 8):
			print("Nombre de tours invalide")
			return False
		return True


	def check_response(self, response):
		if response not in ['1', '2']:
			print("Réponse invalide")
			return False
		return True


	def check_args(self, step, args, **kwargs):
		key = list(kwargs.keys())[0]
		value = list(kwargs.values())[0]
		tournament_view = tournaments_view.TournamentView()
		option = {
			'name': self.check_name,
			'place': self.check_place,
			'date': self.check_date,
			'time_control': self.check_time_control,
			'description': lambda x: True,
			'number_rounds': self.check_number_rounds,
			'response': self.check_response,
		}
		if option[key](value):
			if key == 'response':
				if value == '1':
					tournament_view.new_tournament(step=1, args={})
				if value == '2':
					self.new_tournament(
						args['name'],
						args['place'],
						args['date'],
						args['time_control'],
						args['description'],
						args['number_rounds'],
					)
			step += 1
			args[key] = value
		tournament_view.new_tournament(step, args)

	