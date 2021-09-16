from tinydb import TinyDB, Query
from operator import itemgetter
import json
import Models

DATABASE = TinyDB("database.json", encoding="utf-8")
TABLE = DATABASE.table("tournaments")


class Tournament:

    def __init__(
        self,
        name="",
        place="",
        date="",
        time_control="",
        description="",
        players=[],
        number_rounds=4,
        rounds=[],
    ):
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.description = description
        self.players = players
        self.number_rounds = number_rounds
        self.rounds = rounds
        self.finished = (len(self.rounds) == self.number_rounds)

    # ===== SERIALIZATION ===== #

    def serialize(self):
        return {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "time_control": self.time_control,
            "description": self.description,
            "players": [player.serialize() for player in self.players],
            "number_rounds": self.number_rounds,
            "rounds": [round.serialize() for round in self.rounds],
            "finished": self.finished,
        }

    @staticmethod
    def deserialize(serialized_tournament):
        return Tournament(
            serialized_tournament["name"],
            serialized_tournament["place"],
            serialized_tournament["date"],
            serialized_tournament["time_control"],
            serialized_tournament["description"],
            [
                Models.Player.deserialize(player)
                for player in serialized_tournament["players"]
            ],
            serialized_tournament["number_rounds"],
            [
                Models.Round.deserialize(round)
                for round in serialized_tournament["rounds"]
            ],
        )

    # ===== DATABASE ===== #

    def add_to_db(self):
        tournament = self.get_from_db(self.name)
        serialized_tournament = self.serialize()

        if tournament:
            Tournament = Query()

            if self.players != tournament.players:
                TABLE.update(
                    {"players": serialized_tournament["players"]},
                    Tournament.name == tournament.name,
                )
            if self.rounds != tournament.rounds:
                TABLE.update(
                    {
                        "rounds": serialized_tournament["rounds"],
                        "number_rounds": serialized_tournament["number_rounds"]
                    },
                    Tournament.name == tournament.name,
                )
            if self.finished != tournament.finished:
                TABLE.update(
                    {"finished": serialized_tournament["finished"]},
                    Tournament.name == tournament.name,
                )

        else:
            TABLE.insert(serialized_tournament)

    def remove_from_db(self):
        Tournament = Query()

        if self.get_from_db(self.name):
            TABLE.remove(Tournament.name == self.name)

    @classmethod
    def get_all_tournaments(cls):
        tournaments = TABLE.all()
        tournaments.sort(key=itemgetter("name"))

        return [
            cls.deserialize(tournament)
            for tournament in tournaments
        ]

    @classmethod
    def get_from_db(cls, name):
        Tournament = Query()
        serialized_tournament = TABLE.search(Tournament.name == name)

        if serialized_tournament:
            return cls.deserialize(serialized_tournament[0])

        else:
            return serialized_tournament

    # ===== UTILS ===== #

    def define_winners(self):
        round = self.rounds[-1]
        players = []

        for match in round.matches:
            players.append([match.player1, match.score1])
            players.append([match.player2, match.score2])

        players.sort(
            key=itemgetter(1, 0),
            reverse=True,
        )
        winners = []
        i = 0

        while players[0][1] == players[i][1]:
            winners.append(players[i])
            i += 1

        return winners

    @classmethod
    def get_unfinished_tournaments(cls):
        return [
            tournament
            for tournament in cls.get_all_tournaments()
            if not tournament.finished
        ]

    @classmethod
    def get_finished_tournaments(cls):
        return [
            tournament
            for tournament in cls.get_all_tournaments()
            if tournament.finished
        ]

    # ===== EXPORTS ===== #

    def export_players(self, sort):
        players = [
            player.serialize()
            for player in self.players
        ]
        if sort == "alphabetical":
            players.sort(
                key=itemgetter("last_name", "first_name"),
            )
        elif sort == "ranking":
            players.sort(
                key=itemgetter("ranking"),
                reverse=True,
            )
        file_name = f"./Exports/tournament_{self.name}_players_{sort}.json"
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(players, file, indent=2)

    def export_rounds(self):
        rounds = [
            round.serialize()
            for round in self.rounds
        ]
        for round in rounds:
            round.pop("met_players")
        
        file_name = f"./Exports/tournament_{self.name}_rounds.json"
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(rounds, file, indent=2)

    def export_matches(self):
        round_names = [
            round.name
            for round in self.rounds
        ]
        rounds = [
            round.serialize()
            for round in self.rounds
        ]
        all_matches = []
        for index in range(len(rounds)):
            round = rounds[index]
            round.pop("met_players")

            for match in round[round_names[index]]:
                all_matches.append((match[0][0], match[1][0]))

        file_name = f"./Exports/tournament_{self.name}_matches.json"
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(all_matches, file, indent=2)

    @classmethod
    def export_all_tournaments(cls):
        tournaments = cls.get_all_tournaments()
        all_tournaments = []

        for tournament in tournaments:
            tournament = tournament.serialize()
            tournament.pop("finished")

            for round in tournament["rounds"]:
                round.pop("met_players")

            all_tournaments.append(tournament)

        file_name = "./Exports/all_tournaments.json"
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(all_tournaments, file, indent=2)
