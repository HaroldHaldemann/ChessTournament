import Views
import Controllers
import Models
from .utils import Util
from copy import deepcopy


class TournamentController:

    # ====== NEW TOURNAMENT ====== #

    @staticmethod
    def new_tournament(tournament, value):
        tournament.players = []
        tournament.rounds = []
        tournament.add_to_db()

        if value == "2":
            Views.MenuView.main_menu()

        all_players = Models.Player.get_all_players()

        if len(all_players) < 8:
            print("\nATTENTION")
            print("Le nombre de joueur est insuffisant pour un tournoi")
            print("Vous allez être redirigé(e) vers le menu d'ajout de joueur")
            print("Vous pourrez charger ce tournoi à partir du menu principal")

            Views.PlayerView.add_player_to_db(Models.Player(), 0)

        list_players = []
        Views.TournamentView.add_player_to_tournament(
            all_players, list_players, tournament
        )

    # ===== ADD PLAYER TO TOURNAMENT ===== #

    @staticmethod
    def add_player_to_tournament(all_players, players, tournament):
        input_player = players[-1]
        players.pop()

        if input_player == "0":
            Views.PlayerView.add_player_to_db(Models.Player(), 0)

        if Util.check_player(all_players, input_player):
            player = all_players[int(input_player) - 1]
            players.append(player)
            all_players.pop(int(input_player) - 1)

        if len(players) == 8:
            Views.TournamentView.confirm_players(
                all_players,
                players,
                tournament,
            )
        Views.TournamentView.add_player_to_tournament(
            all_players,
            players,
            tournament,
        )

    @staticmethod
    def confirm_players(all_players, players, response, tournament):
        if response == "1":
            tournament.players = players
            tournament.add_to_db()
            Views.RoundView.def_number_rounds(tournament)

        elif response == "2":
            players = []
            Views.TournamentView.add_player_to_tournament(
                all_players,
                players,
                tournament,
            )
        else:
            print("Réponse invalide")
            Views.TournamentView.confirm_players(
                all_players,
                players,
                tournament,
            )

    # ====== LOAD TOURNAMENT ====== #

    @staticmethod
    def load_tournament(list_tournaments, response):
        options = {}
        if response in ["0", "00"]:
            options = {
                "0": [
                    Views.TournamentView.new_tournament,
                    Models.Tournament(),
                    0,
                ],
                "00": Views.MenuView.load_menu,
            }
            Util.call_options(options, response)

        for index in range(len(list_tournaments)):
            tournament = list_tournaments[index]
            options[f"{index + 1}"] = [
                Views.TournamentView.load_step_tournament,
                tournament,
            ]
        if not Util.check_response(len(options), response):
            Views.TournamentView.load_tournament(list_tournaments)

        Util.call_options(options, response)

    @classmethod
    def load_step_tournament(cls, tournament, response):
        options = {
            "1": None,
            "2": tournament.remove_from_db,
            "3": Views.MenuView.load_menu,
        }
        if not Util.check_response(len(options), response):
            Views.TournamentView.load_step_tournament(tournament)

        if tournament.finished and response == "1":
            print("Le tournoi est déjà terminé")
            winners = tournament.define_winners()
            Views.RoundView.end_tournament(tournament, winners)

        if not tournament.rounds:

            if not tournament.players:
                options["1"] = [
                    cls.new_tournament,
                    tournament,
                    0,
                ]
            else:
                options["1"] = [
                    Views.RoundView.def_number_rounds,
                    tournament,
                ]
        else:
            round = deepcopy(tournament.rounds[-1])
            options["1"] = [
                Controllers.RoundController.create_new_round,
                tournament,
                round,
            ]
        Util.call_options(options, response)
        print("Le tournoi a bien été supprimé")
        print("Retour au menu de chargement")
        Views.MenuView.load_menu()

    # =========================================== #
    #                   UTILS                     #
    # =========================================== #

    # ====== NEW TOURNAMENT ====== #

    @classmethod
    def check_args(cls, tournament, step, **kwargs):
        key = list(kwargs.keys())[0]
        value = list(kwargs.values())[0]
        value = Util.input_format(value)

        options = {
            "name": cls.check_name,
            "place": cls.check_place,
            "date": Util.check_date,
            "time_control": cls.check_time_control,
            "description": cls.check_description,
            "response": [Util.check_response, 3],
        }
        value = Util.call_options(options, key, value)

        if value:

            if key == "response":
                options = {
                    "1": [cls.new_tournament, tournament, value],
                    "2": [cls.new_tournament, tournament, value],
                    "3": Views.MenuView.main_menu,
                }
                Util.call_options(options, value)

            setattr(tournament, key, value)
            step += 1

        Views.TournamentView.new_tournament(tournament, step)

    @staticmethod
    def check_name(name):
        if name == "":
            print("Nom invalide: entrée vide")
            return False

        if Models.Tournament.get_from_db(name):
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
        if time_control not in ["1", "2", "3"]:
            print("Gestion de temps invalide")
            return False

        options = {
            "1": "bullet",
            "2": "blitz",
            "3": "coup rapide",
        }
        return options[time_control]

    @staticmethod
    def check_description(description):
        if description == "":
            description = "Aucun commentaire"

        return description
