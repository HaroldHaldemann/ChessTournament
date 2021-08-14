from Views import menus_view
from Views import tournaments_view
from Views import players_view

class MenuController():

	def main_menu(self, response):
		menu_view = menus_view.MenuView()
		if response not in [f"{i}" for i in range(5)]:
			print("\nCommande incorrect, veuillez entrer un numéro valide")
			menu_view.main_menu()
		tournament_view = tournaments_view.TournamentView()
		player_view = players_view.PlayerView()
		options = {
			'1': tournament_view.new_tournament,
			'2': tournament_view.load_tournament,
			'3': player_view.add_player_to_db,
			'4': menu_view.export_menu,
			'5': exit,
		}
		options[response]()

	def export_menu(self, response):
		menu_view = menus_view.MenuView()
		if response not in [f"{i}" for i in range(7)]:
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
