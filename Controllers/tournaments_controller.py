from Views import tournaments_view
from Views import players_view
from Models import tournaments
from Models import players
from . import utils

class TournamentController():

	def new_tournament(self, name, place, date, time_control, description, number_rounds):
		tournament = tournaments.Tournament()
		tournament.add_tournament_to_db(name, place, date, time_control, description, number_rounds)
		player = players.Player()
		all_players = player.get_all_players()
		tournament_view = tournaments_view.TournamentView()
		tournament_view.add_player_to_tournament(all_players)


	def add_player_to_tournament(self, all_players, players):
		input_player = players[-1]
		tournament_view = tournaments_view.TournamentView()
		players.pop()
		if input_player == '0':
			player_view = players_view.PlayerView()
			player_view.add_player_to_db()
		if self.check_player(all_players, input_player):
			player = all_players[int(input_player)]
			players.append(player)
		tournament_view.add_player_to_tournament(all_players, players)


###############################################################
#  UTILS                                                      #
###############################################################

	
	def check_args(self, args, **kwargs):
		key = list(kwargs.keys())[0]
		value = list(kwargs.values())[0]
		util = utils.Util()
		value = util.input_format(value)
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
					tournament_view.new_tournament(args={})
			args[key] = value
		tournament_view.new_tournament(args)


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
		for day_month_year in split_date:
			if not day_month_year.isdigit():
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


	def check_player(self, all_players, input_player):
		if input_player not in [f"{index}" for index in range(1, len(all_players) + 1)]:
			print("Joueur invalide")
			return False
		return True
