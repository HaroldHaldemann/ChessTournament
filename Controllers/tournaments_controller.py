from Views import tournaments_view
from Views import players_view
from Models import tournaments
from Models import players
from . import utils

class TournamentController():

	def new_tournament(self, args):
		tournament = tournaments.Tournament()
		tournament.add_tournament_to_db(
			args['name'], 
			args['place'], 
			args['date'], 
			args['time_control'], 
			args['description'], 
			args['number_rounds']
		)
		player = players.Player()
		all_players = player.get_all_players()
		if len(all_players) < 8:
			print("\nATTENTION")
			print("Le nombre de joueur est insuffisant pour un tournoi")
			print("Vous allez être redirigé vers le menu d'ajout de joueur")
			print("Vous pourrez charger ce tournoi à partir du menu principal")
			player_view = players_view.PlayerView()
			player_view.add_player_to_db()
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
			'date': util.check_date,
			'time_control': self.check_time_control,
			'description': self.check_description,
			'number_rounds': self.check_number_rounds,
			'response': self.check_response,
		}
		if option[key](value):
			if key == 'response':
				if value == '1':
					tournament_view.new_tournament()
			value = option[key](value)
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
		return name


	def check_place(self, place):
		if place == "":
			print("Lieu invalide: entrée vide")
			return False
		return place


	def check_time_control(self, time_control):
		if time_control not in ['1', '2', '3']:
			print("Gestion de temps invalide")
			return False
		option = {
			'1': "bullet",
			'2': "blitz",
			'3': "coup rapide",
		}
		return option[time_control]

	def check_description(self, description):
		if description == "":
			description = " "
		return description

	def check_number_rounds(self, number_rounds):
		if type(number_rounds) == int:
			return number_rounds
		if not number_rounds.isdigit():
			print("Nombre de tours invalide")
			return False
		if not (0 < int(number_rounds) < 8):
			print("Nombre de tours invalide")
			return False
		return number_rounds


	def check_response(self, response):
		if response not in ['1', '2']:
			print("Réponse invalide")
			return False
		return response


	def check_player(self, all_players, input_player):
		if input_player not in [f"{index}" for index in range(1, len(all_players) + 1)]:
			print("Joueur invalide")
			return False
		return True
