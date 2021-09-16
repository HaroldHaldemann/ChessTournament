from tinydb import TinyDB, Query
from operator import itemgetter
import json

DATABASE = TinyDB("database.json", encoding="utf-8")
TABLE = DATABASE.table("players")


class Player:
    def __init__(
        self,
        last_name="",
        first_name="",
        birth_date="",
        gender="",
        ranking=0,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def __lt__(self, other):
        if isinstance(other, Player):
            return self.ranking < other.ranking
        return False

    def __eq__(self, other):
        return (self.last_name == other.last_name) \
            & (self.first_name == other.first_name) \
            & (self.birth_date == other.birth_date)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.birth_date}"

    # ===== SERIALIZATION ===== #

    def serialize(self):
        """
        Return a serialized version of a given player
        i.e. a dictionnary-like version of a player
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "ranking": self.ranking,
        }

    @staticmethod
    def deserialize(serialized_player):
        """
        return a player version of a given serialized player
        i.e. a player which attributes correspond to
        the keys and the values of the serialized player
        """
        return Player(
            serialized_player["last_name"],
            serialized_player["first_name"],
            serialized_player["birth_date"],
            serialized_player["gender"],
            serialized_player["ranking"],
        )

    # ===== DATABASE ===== #

    def add_to_db(self):
        """
        Add the given player to the database
        or update the existing player
        """
        if self.get_from_db(self.last_name, self.first_name, self.birth_date):
            Player = Query()
            TABLE.update(
                {"gender": self.gender, "ranking": self.ranking},
                (Player.last_name == self.last_name)
                & (Player.first_name == self.first_name)
                & (Player.birth_date == self.birth_date),
            )
        else:
            TABLE.insert(self.serialize())

    def remove_from_db(self):
        """
        Remove a given tournament from database
        """
        Player = Query()
        if self.get_from_db(self.last_name, self.first_name, self.birth_date):
            TABLE.remove(
                (Player.last_name == self.last_name)
                & (Player.first_name == self.first_name)
                & (Player.birth_date == self.birth_date)
            )

    @classmethod
    def get_from_db(cls, last_name, first_name, birth_date):
        """
        Return the player from database with the given
        last name, first name and birth date
        The player is deserialized
        """
        Player = Query()
        serialized_player = TABLE.search(
            (Player.last_name == last_name)
            & (Player.first_name == first_name)
            & (Player.birth_date == birth_date)
        )
        if serialized_player:
            return cls.deserialize(serialized_player[0])
        else:
            return serialized_player

    @classmethod
    def get_all_players(cls):
        """
        Return a list of all players in the database
        The players are deserialized
        """
        serialized_players = sorted(
            TABLE.all(),
            key=itemgetter("last_name", "first_name", "birth_date"),
        )
        return [cls.deserialize(player) for player in serialized_players]

    # ===== EXPORTS ===== #

    @classmethod
    def export_all_players(cls, sort):
        """
        Create a file json in ./Exports and
        put in it the list of all the players in the database
        """
        players = cls.get_all_players()
        all_players = [
            player.serialize()
            for player in players
        ]
        if sort == "alphabetical":
            all_players.sort(
                key=itemgetter("last_name", "first_name"),
            )
        elif sort == "ranking":
            all_players.sort(
                key=itemgetter("ranking"),
                reverse=True,
            )

        file_name = f"./Exports/all_players_{sort}.json"
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(all_players, file, indent=2)
