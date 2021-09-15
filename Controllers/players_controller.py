import Views
import Models
from .utils import Util


class PlayerController:
    @staticmethod
    def add_player_to_db(player, response):
        player.add_to_db()

        options = {
            "1": [Views.PlayerView.add_player_to_db, Models.Player(), 0],
            "2": Views.MenuView.main_menu,
        }
        Util.call_options(options, response)

    @staticmethod
    def load_player(all_players, response):
        if response == "0":
            Views.MenuView.main_menu()

        if not Util.check_player(all_players, response):
            Views.PlayerView.load_player(all_players)

        player = all_players[int(response) - 1]
        Views.PlayerView.modify_player(all_players, player, response)

    @staticmethod
    def modify_player(all_players, player, response, input_player):
        options = {
            "1": [Views.PlayerView.add_player_to_db, player, 4],
            "2": player.remove_from_db,
            "3": Views.MenuView.main_menu,
        }
        Util.call_options(options, response)
        print("Le joueur a bien été supprimé")
        print("Retour au menu de chargement")
        all_players.pop(int(input_player) - 1)
        Views.PlayerView.load_player(all_players)

    # =========================================== #
    #                    UTILS                    #
    # =========================================== #

    @classmethod
    def check_args(cls, player, step, **kwargs):
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
        if name == "":
            print("Nom invalide: entrée vide")
            return False

        return name

    @staticmethod
    def check_gender(gender):
        if gender not in ["1", "2"]:
            print("Genre invalide")
            return False

        options = {
            "1": "masculin",
            "2": "féminin",
        }
        return options[gender]

    @staticmethod
    def check_ranking(ranking):
        if not ranking.isdigit() or ranking == "0":
            print("Classement invalide")
            return False

        return int(ranking)
