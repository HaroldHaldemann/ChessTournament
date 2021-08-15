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
			args = {}
			player_view.add_player_to_db(args)
		tournament_view = tournaments_view.TournamentView()
		list_players = []
		tournament_view.add_player_to_tournament(all_players, list_players)
		

	def add_player_to_tournament(self, all_players, players):
		input_player = players[-1]
		tournament_view = tournaments_view.TournamentView()
		players.pop()
		if input_player == '0':
			player_view = players_view.PlayerView()
			args = {}
			player_view.add_player_to_db(args)
		if self.check_player(all_players, input_player):
			player = all_players[int(input_player)-1]
			players.append(player)
			all_players.pop(int(input_player)-1)
		if len(players) == 8:
			pass # TODO - Add round to tournament
		tournament_view.add_player_to_tournament(all_players, players)


	def load_tournament(self, list_tournaments=[], response="", finished=""):
		tournament = tournaments.Tournament()
		tournament_view = tournaments_view.TournamentView()
		if finished:
			options = {
				'1': tournament.get_unfinished_tournaments,
				'2': tournament.get_finished_tournaments,
			}
			list_tournaments = options[finished]()
			response = ""
			tournament_view.load_tournament(list_tournaments)
		if response == '0':
			args = {}
			tournament_view.new_tournament(args)
		if self.check_response_load(response, list_tournaments):
			loaded_tournament = list_tournaments[int(response)-1]
			if not loaded_tournament['finished']:
				if not loaded_tournament['players']:
					tournament_view.new_tournament({
						'name': loaded_tournament['name'],
						'place': loaded_tournament['place'],
						'date': loaded_tournament['date'],
						'time_control': loaded_tournament['time_control'],
						'description': loaded_tournament['description'],
						'number_rounds': loaded_tournament['number_rounds'],
					})
				else:
					pass # TODO - Add round to tournament



###############################################################
#  UTILS                                                      #
###############################################################

### NEW TOURNAMENT ###
	
	def check_args(self, args, **kwargs):
		key = list(kwargs.keys())[0]
		value = list(kwargs.values())[0]
		util = utils.Util()
		value = util.input_format(value)
		tournament_view = tournaments_view.TournamentView()
		options = {
			'name': self.check_name,
			'place': self.check_place,
			'date': util.check_date,
			'time_control': self.check_time_control,
			'description': self.check_description,
			'number_rounds': self.check_number_rounds,
			'response': self.check_response_new,
		}
		if options[key](value):
			value = options[key](value)
			args[key] = value
			if key == 'response':
				tournament = tournaments.Tournament()
				tournament.remove_tournament_from_db(args['name'])
				if value == '1':
					args = {}
					tournament_view.new_tournament(args)
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
		options = {
			'1': "bullet",
			'2': "blitz",
			'3': "coup rapide",
		}
		return options[time_control]

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


	def check_response_new(self, response):
		if response not in ['1', '2']:
			print("Réponse invalide")
			return False
		return response


### ADD PLAYER TO TOURNAMENT ###


	def check_player(self, all_players, input_player):
		if input_player not in [f"{index+1}" for index in range(len(all_players))]:
			print("Joueur invalide")
			return False
		return True


### LOAD TOURNAMENT ###


	def check_response_load(self, response, list_tournaments):
		if response not in [f"{index+1}" for index in range(len(list_tournaments))]:
			print("Réponse invalide")
			return False
		return True
			