from Models import players
from Views import players_view
from Views import menus_view
from . import utils

class PlayerController():

	def add_player_to_db(self, args):
		player = players.Player()
		player.add_player_to_db(
			args['last_name'],
			args['first_name'],
			args['birth_date'],
			args['gender'],
			args['ranking'],
		)
		player_view = players_view.PlayerView()
		menu_view = menus_view.MenuView()
		options = {
			'2': [player_view.add_player_to_db, {}],
			'3': [menu_view.main_menu, None],
		}
		response = args['response']
		args = options[response][1]
		if args != None:
			options[response][0](args)
		options[response][0]()


###############################################################
#  UTILS                                                      #
###############################################################

	
	def check_args(self, args, **kwargs):
		key = list(kwargs.keys())[0]
		value = list(kwargs.values())[0]
		util = utils.Util()
		value = util.input_format(value)
		options = {
			'last_name': self.check_name,
			'first_name': self.check_name,
			'birth_date': util.check_date,
			'gender': self.check_gender,
			'ranking': self.check_ranking,
			'response': self.check_response,
		}
		player_view = players_view.PlayerView()
		if options[key](value):
			if key == 'response':
				if value == '1':
					args = {}
					player_view.add_player_to_db(args)
				if value == '4':
					menu_view = menus_view.MenuView()
					menu_view.main_menu()
			value = options[key](value)
			args[key] = value
		if len(args) == 3:
			player = players.Player()
			if player.get_player(args['last_name'], args['first_name'], args['birth_date']):
				print("Ce joueur existe déjà")
				args = {}
		player_view.add_player_to_db(args)


	def check_name(self, name):
		if name == "":
			print("Nom invalide: entrée vide")
			return False
		return name


	def check_gender(self, gender):
		if gender not in ['1', '2']:
			print("Genre invalide")
			return False
		options = {
			'1': "masculin",
			'2': "féminin",
		}
		return options[gender]


	def check_ranking(self, ranking):
		if not ranking.isdigit():
			print("Classement invalide")
			return False
		return ranking


	def check_response(self, response):
		if response not in ['1', '2', '3', '4']:
			print("Réponse invalide")
			return False
		return response
