import Views
import Models
from .utils import Util


class PlayerController:
    @staticmethod
    def add_player_to_db(player, response):
        """
        Add new player in db
        Check for redirection to chosen view
        """
        player.add_to_db()

        options = {
            "1": [Views.PlayerView.add_player_to_db, Models.Player(), 0],
            "2": Views.MenuView.main_menu,
        }
        Util.call_options(options, response)

    @staticmethod
    def load_player(all_players, response):
        """
        Check the response for the loading of a player
        """
        if response == "0":
            Views.MenuView.main_menu()

        if not Util.check_player(all_players, response):
            Views.PlayerView.load_player(all_players)

        player = all_players[int(response) - 1]
        Views.PlayerView.modify_player(all_players, player, response)

    @staticmethod
    def modify_player(all_players, player, response, input_player):
        """
        Check the response for the modification of the player
        Do the asked action of the corresponding view
        """
        options = {
            "1": [Views.PlayerView.add_player_to_db, player, 4],
            "2": player.remove_from_db,
            "3": Views.MenuView.main_menu,
        }
        if not Util.check_response(len(options), response):
            Views.PlayerView.modify_player(
                all_players,
                player,
                input_player,
            )
        Util.call_options(options, response)
        print("Le joueur a bien été supprimé")
        print("Retour au menu de chargement")
        all_players.pop(int(input_player) - 1)
        Views.PlayerView.load_player(all_players)

    # ===== UTILS ===== #

    @classmethod
    def check_args(cls, player, step, **kwargs):
        """
        Check the args of the add player to db view
        """
        key = list(kwargs.keys())[0]
        value = list(kwargs.values())[0]
        value = Util.input_format(value)

        options = {
            "last_name": cls.check_name,
            "first_name": cls.check_name,
            "birth_date": Util.check_date,
            "gender": cls.check_gender,
            "ranking": cls.check_ranking,
            "response": [Util.check_response, 3],
        }
        value = Util.call_options(options, key, value)

        if value:
            if key == "response":
                options = {
                    "1": [cls.add_player_to_db, player, value],
                    "2": [cls.add_player_to_db, player, value],
                    "3": Views.MenuView.main_menu,
                }
                Util.call_options(options, value)

            setattr(player, key, value)
            step += 1

        if step == 3:

            if Models.Player.get_from_db(
                player.last_name, player.first_name, player.birth_date
            ):
                print("Ce joueur existe déjà")
                player = Models.Player()
                step = 0

        Views.PlayerView.add_player_to_db(player, step)

    @staticmethod
    def check_name(name):
        """
        Check the last name and first name of the player
        """
        if name == "":
            print("Nom invalide: entrée vide")
            return False

        return name

    @staticmethod
    def check_gender(gender):
        """
        Check the gender of the player
        """
        if gender not in ["1", "2"]:
            print("Genre invalide")
            return False

        options = {
            "1": "masculin",
            "2": "feminin",
        }
        return options[gender]

    @staticmethod
    def check_ranking(ranking):
        """
        Check the ranking of the player
        """
        if not ranking.isdigit() or ranking == "0":
            print("Classement invalide")
            return False

        return int(ranking)

    # ===== EXPORTS ===== #

    @staticmethod
    def export_all_players(response):
        """
        Check the response of the corresponding view
        Calls the export all players function with given sorting
        """
        options = {
            "1": [Models.Player.export_all_players, "alphabetical"],
            "2": [Models.Player.export_all_players, "ranking"],
        }

        if not Util.check_response(len(options), response):
            Views.PlayerView.export_all_players()

        Util.call_options(options, response)
        print("La liste des joueurs vient d'être exporté vers Exports")
        Views.MenuView.export_menu()
