import Views
import Models
from .utils import Util


class MenuController:
    @staticmethod
    def main_menu(response):
        all_players = Models.Player.get_all_players()
        options = {
            "1": [Views.TournamentView.new_tournament, Models.Tournament(), 0],
            "2": Views.MenuView.load_menu,
            "3": [Views.PlayerView.add_player_to_db, Models.Player(), 0],
            "4": [Views.PlayerView.load_player, all_players],
            "5": Views.MenuView.export_menu,
            "6": exit,
        }
        if not Util.check_response(len(options), response):
            Views.MenuView.main_menu()

        Util.call_options(options, response)

    @staticmethod
    def export_menu(response):
        options = {
            "1": Views.PlayerView.export_all_players,
            "2": Views.TournamentView.export_players,
            "3": Views.TournamentView.export_all_tournaments,
            "4": Views.TournamentView.export_rounds,
            "5": Views.TournamentView.export_matches,
            "6": Views.MenuView.main_menu,
        }
        if not Util.check_response(len(options), response):
            Views.MenuView.export_menu()

        Util.call_options(options, response)

    @staticmethod
    def load_menu(response):
        options = {
            "1": [
                Views.TournamentView.load_tournament,
                Models.Tournament.get_unfinished_tournaments(),
            ],
            "2": [
                Views.TournamentView.load_tournament,
                Models.Tournament.get_finished_tournaments(),
            ],
            "3": Views.MenuView.main_menu,
        }
        if not Util.check_response(len(options), response):
            Views.MenuView.load_menu()

        Util.call_options(options, response)
