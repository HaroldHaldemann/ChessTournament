from Views import menus_view
from Views import tournaments_view
from Views import players_view
from . import tournaments_controller

class MenuController():

	def main_menu(self, response):
		menu_view = menus_view.MenuView()
		if response not in [f"{i+1}" for i in range(5)]:
			print("\nCommande incorrect, veuillez entrer un numéro valide")
			menu_view.main_menu()
		tournament_view = tournaments_view.TournamentView()
		tournament_controller = tournaments_controller.TournamentController()
		player_view = players_view.PlayerView()
		options = {
			'1': tournament_view.new_tournament,
			'2': menu_view.load_menu,
			'3': player_view.add_player_to_db,
			'4': menu_view.export_menu,
			'5': exit,
		}
		options[response]()

	def export_menu(self, response):
		menu_view = menus_view.MenuView()
		if response not in [f"{i+1}" for i in range(7)]:
			print("\nCommande incorrect, veuillez entrer un numéro valide")
			menu_view.main_menu()
		tournament_view = tournaments_view.TournamentView()
		player_view = players_view.PlayerView()
		options = {
			'1': player_view.export_all_players,
			'2': tournament_view.export_players,
			'3': tournament_view.export_all_tournaments,
			'4': tournament_view.export_rounds,
			'5': tournament_view.export_matches,
			'6': menu_view.main_menu,
		}
		options[response]()

	def load_menu(self, response):
		menu_view = menus_view.MenuView()
		if response not in [f"{i+1}" for i in range(3)]:
			print("\nCommande incorrect, veuillez entrer un numéro valide")
			menu_view.main_menu()
		tournament_controller = tournaments_controller.TournamentController()
		options = {
			'1': [tournament_controller.load_tournament, response],
			'2': [tournament_controller.load_tournament, response],
			'3': [menu_view.main_menu, None],
		}
		args = options[response][1]
		if args:
			options[response][0](finished=args)
		options[response][0]()
