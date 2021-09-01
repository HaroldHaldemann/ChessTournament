import Views
import Models
from .utils import Util

class TournamentController():

	@staticmethod
	def new_tournament(args):
		tournament = Models.Tournament(
			args['name'], 
			args['place'], 
			args['date'], 
			args['time_control'], 
			args['description'], 
			args['number_rounds'],
			[],
			[],
		)
		tournament.remove_from_db()
		tournament.add_to_db()

		all_players = Models.Player.get_all_players()	

		if len(all_players) < 8:
			print("\nATTENTION")
			print("Le nombre de joueur est insuffisant pour un tournoi")
			print("Vous allez être redirigé(e) vers le menu d'ajout de joueur")
			print("Vous pourrez charger ce tournoi à partir du menu principal")
			
			args = {}
			Views.PlayerView.add_player_to_db(args)

		list_players = []
		Views.TournamentView.add_player_to_tournament(all_players, list_players)
		

	@classmethod
	def add_player_to_tournament(cls, all_players, players):
		input_player = players[-1]
		players.pop()

		if input_player == '0':
			args = {}
			Views.PlayerView.add_player_to_db(args)

		if cls.check_player(all_players, input_player):
			player = all_players[int(input_player)-1]
			players.append(player)
			all_players.pop(int(input_player)-1)

		if len(players) == 8:
			Views.TournamentView.confirm_players(all_players, players)

		Views.TournamentView.add_player_to_tournament(all_players, players)

	@classmethod
	def confirm_players(cls, all_players, players, response):
		pass


	@classmethod
	def load_tournament(cls, list_tournaments, response):
		args = {}
		options = {
			'0': Views.TournamentView.new_tournament(args),
		}
		for index in range(len(list_tournaments)):
			options[f"{index + 1}"] = list_tournaments[index]

		if Util.check_response(response, options) or response != '0':
			loaded_tournament = options[response]

			if not loaded_tournament['finished']:

				if not loaded_tournament['players']:
					Views.TournamentView.new_tournament({
						'name': loaded_tournament['name'],
						'place': loaded_tournament['place'],
						'date': loaded_tournament['date'],
						'time_control': loaded_tournament['time_control'],
						'description': loaded_tournament['description'],
						'number_rounds': loaded_tournament['number_rounds'],
					})
				else:
					pass # TODO - Add round to tournament


	def add_round_to_tournament():
		pass



#############################################
# 									UTILS 									#
#############################################


##### NEW TOURNAMENT #####

	
	@classmethod
	def check_args(cls, args, **kwargs):
		key = list(kwargs.keys())[0]
		value = list(kwargs.values())[0]
		value = Util.input_format(value)

		options = {
			'name': cls.check_name,
			'place': cls.check_place,
			'date': Util.check_date,
			'time_control': cls.check_time_control,
			'description': cls.check_description,
			'number_rounds': cls.check_number_rounds,
			'response': [Util.check_response, 2],
		}
		value = Util.call_option(options, key, value)
		if key == 'response':

		value = options[key](value)

		if value:
			args[key] = value

			if key == 'response':
					options = {
						'1': ,
						'2': ,
					}
				if value == '1':
					args = {}
				else:
					cls.new_tournament(args)

		Views.TournamentView.new_tournament(args)


	@staticmethod
	def check_name(name):
		if name == "":
			print("Nom invalide: entrée vide")
			return False

		if name in Models.Tournament.get_name_tournaments():
			print("Nom invalide: nom déjà existant")
			return False

		return name


	@staticmethod
	def check_place(place):
		if place == "":
			print("Lieu invalide: entrée vide")
			return False

		return place


	@staticmethod
	def check_time_control(time_control):
		if time_control not in ['1', '2', '3']:
			print("Gestion de temps invalide")
			return False

		options = {
			'1': "bullet",
			'2': "blitz",
			'3': "coup rapide",
		}
		return options[time_control]


	@staticmethod
	def check_description(description):
		if description == "":
			description = "Aucun commentaire"

		return description


	@staticmethod
	def check_number_rounds(number_rounds):
		if type(number_rounds) == int:
			return number_rounds

		if not number_rounds.isdigit():
			print("Nombre de tours invalide")
			return False

		if not (0 < int(number_rounds) < 8):
			print("Nombre de tours invalide")
			return False

		return number_rounds


##### ADD PLAYER TO TOURNAMENT #####


	@staticmethod
	def check_player(all_players, input_player):
		if input_player not in [f"{index+1}" for index in range(len(all_players))]:
			print("Joueur invalide")
			return False

		return input_player
			