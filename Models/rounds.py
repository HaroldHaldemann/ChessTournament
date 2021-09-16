from operator import itemgetter
import Models
from copy import deepcopy


class Round:
    def __init__(
        self,
        name="",
        matches=[],
        met_players={},
        date_start="Not informed",
        date_end="Not informed",
    ):
        self.name = name
        self.matches = matches
        self.met_players = met_players
        self.date_start = date_start
        self.date_end = date_end

    def serialize(self):
        met_players = {}
        for str_player in list(self.met_players.keys()):
            met_players[str_player] = [
                player.serialize()
                for player in self.met_players[str_player]
            ]
        return {
            f"{self.name}": [match.serialize() for match in self.matches],
            "met_players": met_players,
            "start": self.date_start,
            "end": self.date_end,
        }

    @staticmethod
    def deserialize(serialized_round):
        keys = list(serialized_round.keys())
        met_players_keys = list(serialized_round["met_players"].keys())

        serialized_met_players = {}
        for str_player in met_players_keys:
            serialized_met_players[str_player] = [
                Models.Player.deserialize(player)
                for player in serialized_round["met_players"][str_player]
            ]
        return Round(
            keys[0],
            [
                Models.Match.deserialize(match)
                for match in serialized_round[keys[0]]
            ],
            serialized_met_players,
            serialized_round["start"],
            serialized_round["end"],
        )

    def create_first_round(PLAYERS):
        players = sorted(PLAYERS, reverse=True)
        demi_len = int(len(players) / 2)

        round = Round()
        round.name = "Round 1"

        for index in range(demi_len):
            player = players[index]
            sym_player = players[index + demi_len]

            round.met_players[str(player)] = [sym_player]
            round.met_players[str(sym_player)] = [player]

            match = Models.Match(
                player,
                0,
                sym_player,
                0,
            )
            round.matches.append(match)

        return round

    def create_new_round(self):
        scored_players = []

        for match in self.matches:
            player_1 = match.player1
            player_2 = match.player2
            scored_players.extend((
                [player_1, match.score1],
                [player_2, match.score2],
            ))
            self.met_players[str(player_1)].append(player_2)
            self.met_players[str(player_2)].append(player_1)

        print(scored_players)
        scored_players.sort(
            key=itemgetter(1, 0),
            reverse=True,
        )
        self.matches = self.define_pairs(scored_players, self.met_players)

    @classmethod
    def define_pairs(cls, scored_players, met_players):
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

            while j < len(scored_players):
                player_i = scored_players[i][0]
                player_j = scored_players[j][0]

                if player_i in met_players[str(player_i)] or j in set_indexes:
                    j += 1

                else:
                    match = Models.Match(
                        player_i,
                        scored_players[i][1],
                        player_j,
                        scored_players[j][1],
                    )
                    matches.append(match)
                    set_indexes.extend([i, j])
                    i += 1
                    j = i + 1
                    break

            if len(matches) == 4:
                if cls.check_count(scored_players, met_players, matches):
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
    def check_count(players, met_players, matches):
        non_met = {}
        count = {}

        for player in players:
            key_player = str(player[0])
            non_met[key_player] = [
                PLAYER[0]
                for PLAYER in players
                if PLAYER[0] not in met_players[key_player]
            ]
            count[key_player] = 0

        for match in matches:
            non_met[str(match.player1)] = [
                player
                for player in non_met[str(match.player1)]
                if player != match.player2
            ]
            non_met[str(match.player2)] = [
                player
                for player in non_met[str(match.player2)]
                if player != match.player1
            ]

        for player in players:
            key_player = str(player[0])
            for PLAYER in players:
                if non_met[key_player] == non_met[str(PLAYER[0])]:
                    count[key_player] += 1

            if (count[key_player] % 2 != 0) and (count[key_player] > 1):
                return True

        return False
