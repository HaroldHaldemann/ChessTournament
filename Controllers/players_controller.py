import Views
import Models
from .utils import Util

class PlayerController():


	@staticmethod
	def add_player_to_db(args):
		player = Models.Player(
			args['last_name'],
			args['first_name'],
			args['birth_date'],
			args['gender'],
			args['ranking'],
		)
		player.remove_from_db()
		player.add_to_db()

		options = {
			'2': [Views.PlayerView.add_player_to_db, {}],
			'3': [Views.MenuView.main_menu, None],
		}
		response = args['response']
		Util.call_options(options, response)


#############################################
# 									UTILS 									#
#############################################

	
	@classmethod
	def check_args(cls, args, **kwargs):
		key = list(kwargs.keys())[0]
		value = list(kwargs.values())[0]
		value = Util.input_format(value)

		options = {
			'last_name': cls.check_name,
			'first_name': cls.check_name,
			'birth_date': Util.check_date,
			'gender': cls.check_gender,
			'ranking': cls.check_ranking,
			'response': Util.check_response,
		}
		value = options[key](value)

		if value:
			args[key] = value

			if key == 'response':
				options = {
					'1': [Views.PlayerView.add_player_to_db, {}],
					'2': [cls.add_player_to_db, args],
					'3': [cls.add_player_to_db, args],
					'4': [Views.MenuView.main_menu, None],
				}
				Util.call_options(options, response)
		
		if len(args) == 3:

			if Models.Player.get_from_db(args['last_name'], args['first_name'], args['birth_date']):
				print("Ce joueur existe déjà")
				args = {}

		Views.PlayerView.add_player_to_db(args)


	@staticmethod
	def check_name(name):
		if name == "":
			print("Nom invalide: entrée vide")
			return False

		return name


	@staticmethod
	def check_gender(gender):
		if gender not in ['1', '2']:
			print("Genre invalide")
			return False

		options = {
			'1': "masculin",
			'2': "féminin",
		}
		return options[gender]


	@staticmethod
	def check_ranking(ranking):
		if not ranking.isdigit():
			print("Classement invalide")
			return False

		return ranking
