import Views
import Models
from .utils import Util
from datetime import datetime
from copy import deepcopy


class RoundController:
    @staticmethod
    def check_number_rounds(tournament, number_rounds):
        if number_rounds == "":
            number_rounds = 4

        if not number_rounds.isdigit():
            print("Nombre de tours invalide")
            Views.RoundView.def_number_rounds(tournament)

        if not (0 < int(number_rounds) < 8):
            print("Nombre de tours invalide")
            Views.RoundView.def_number_rounds(tournament)

        tournament.number_rounds = int(number_rounds)
        Views.RoundView.create_first_round(tournament)

    @staticmethod
    def create_first_round(tournament, response):
        options = {
            "1": [Models.Round.create_first_round, tournament.players],
            "2": Views.MenuView.main_menu,
        }
        if not Util.check_response(len(options), response):
            Views.RoundView.create_first_round(tournament)

        round = Util.call_options(options, response)
        Views.RoundView.start_round(tournament, round)

    @staticmethod
    def create_new_round(tournament, round):
        round.create_new_round()
        Views.RoundView.start_round(tournament, round)

    @staticmethod
    def start_round(tournament, round, response):
        options = {
            "0": [datetime.now().strftime, "%Y-%m-%d, %H:%M:%S"],
        }
        if not Util.check_response(len(options), response):
            Views.RoundView.start_round(tournament, round)

        round.date_start = Util.call_options(options, response)
        Views.RoundView.end_round(tournament, round)

    @staticmethod
    def end_round(tournament, round, response):
        options = {
            "0": [datetime.now().strftime, "%Y-%m-%d, %H:%M:%S"],
        }
        if not Util.check_response(len(options), response):
            Views.RoundView.end_round(tournament, round)

        round.date_end = Util.call_options(options, response)
        Views.RoundView.results_round(tournament, round, 0)

    @staticmethod
    def results_round(tournament, round, step, response):
        options = {
            "1": (1, 0),
            "2": (0, 1),
            "3": (0.5, 0.5),
        }
        if not Util.check_response(len(options), response):
            Views.RoundView.results_round(tournament, round, step)

        round.matches[step][0][1] += options[response][0]
        round.matches[step][1][1] += options[response][1]
        step += 1

        if step == 4:
            Views.RoundView.new_round(tournament, round)

        Views.RoundView.results_round(tournament, round, step)

    @classmethod
    def confirm_round(cls, tournament, ROUND, response):
        options = {
            "1": [tournament.rounds.append, ROUND],
            "2": [tournament.rounds.append, ROUND],
            "3": Views.MenuView.main_menu,
        }
        if not Util.check_response(len(options), response):
            Views.RoundView.confirm_round(tournament, ROUND)

        Util.call_options(options, response)

        tournament.add_to_db()

        if response == "2":
            Views.MenuView.main_menu()

        if len(tournament.rounds) == tournament.number_rounds:
            Views.RoundView.end_tournament(tournament)

        else:
            round = deepcopy(ROUND)
            cls.create_new_round(tournament, round)
