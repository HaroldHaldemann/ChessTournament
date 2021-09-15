from operator import itemgetter
import Models
from random import randint
from copy import deepcopy


class Round:
    def __init__(
        self,
        matches=[],
        met_players={},
        players_with_id={},
        date_start="Not informed",
        date_end="Not informed",
    ):
        self.matches = matches
        self.met_players = met_players
        self.players_with_id = players_with_id
        self.date_start = date_start
        self.date_end = date_end

    def serialize(self):
        num_round = len(list(self.met_players.values())[0])
        serialized_matches = [
            (
                [self.players_with_id[match[0][0]].serialize(), match[0][1]],
                [self.players_with_id[match[1][0]].serialize(), match[1][1]],
            )
            for match in self.matches
        ]
        return {
            f"Round {num_round}": serialized_matches,
            "Start": self.date_start,
            "End": self.date_end,
        }

    def create_first_round(PLAYERS):
        players = sorted(PLAYERS, reverse=True)
        demi_len = int(len(players) / 2)

        round = Round()

        for index in range(len(players)):
            round.players_with_id[f"P{index}"] = players[-index - 1]
            round.met_players[f"P{index}"] = []

            if index < demi_len:
                round.matches.append(
                    (
                        [f"P{index}", 0],
                        [f"P{index + demi_len}", 0],
                    )
                )
        return round

    def create_new_round(self):
        players = []

        for match in self.matches:
            players.extend(match)

        players.sort(
            key=itemgetter(1, 0),
            reverse=True,
        )
        self.matches = self.define_pairs(players, self.met_players)

    @classmethod
    def define_pairs(cls, players, met_players):
        matches = []
        set_indexes = []
        i = 0
        j = 1
        while len(matches) < 4:
            while i in set_indexes:
                i += 1
                j = i + 1

            if j == 8:
                i, j = cls.back_to_previous_match(matches, set_indexes)

            while j < len(players):
                player_i = players[i]
                player_j = players[j]
                if player_i[0] in met_players[player_i[0]] or j in set_indexes:
                    j += 1

                else:
                    matches.append((player_i, player_j))
                    set_indexes.extend([i, j])
                    i += 1
                    j = i + 1
                    break

            if len(matches) == 4:
                if cls.check_pb_non_binary(players, met_players, matches):
                    i, j = cls.back_to_previous_match(matches, set_indexes)

        return matches

    @staticmethod
    def back_to_previous_match(matches, set_indexes):
        i = set_indexes[-2]
        j = set_indexes[-1] + 1
        matches.pop()
        del set_indexes[-2:]
        return i, j

    @staticmethod
    def add_points_to_matches(round):

        for match in round.matches:
            r = randint(1, 3)
            if r == 1:
                match[0][1] += 1.0
            elif r == 2:
                match[1][1] += 1.0
            else:
                match[0][1] += 0.5
                match[1][1] += 0.5
            round.met_players[f"{match[0][0]}"].append(f"{match[1][0]}")
            round.met_players[f"{match[1][0]}"].append(f"{match[0][0]}")

    @staticmethod
    def check_pb_non_binary(players, met_players, matches):
        list_players = [f"P{index}" for index in range(len(players))]
        non_met = {}
        count = {}

        for i in range(len(players)):
            non_met[f"P{i}"] = set(list_players) - set(met_players[f"P{i}"])
            count[f"P{i}"] = 0

        for match in matches:
            non_met[match[0][0]] -= set([match[1][0]])
            non_met[match[1][0]] -= set([match[0][0]])

        for i in range(len(players)):
            for j in range(len(players)):
                if non_met[f"P{i}"] == non_met[f"P{j}"]:
                    count[f"P{i}"] += 1

            if (count[f"P{i}"] % 2 != 0) and (count[f"P{i}"] > 1):
                return True

        return False

    @classmethod
    def test(cls):
        tournament = Models.Tournament.get_from_db("test")
        round = cls.create_first_round(tournament.players)
        cls.add_points_to_matches(round)

        tournament.rounds.append(round)

        for i in range(1, 7):

            ROUND = deepcopy(round)
            round = Round(
                ROUND.matches,
                ROUND.met_players,
                ROUND.players_with_id,
            )
            cls.create_new_round(round)
            cls.add_points_to_matches(round)

            tournament.rounds.append(round)

        for R in tournament.rounds:
            print(R.serialize())
