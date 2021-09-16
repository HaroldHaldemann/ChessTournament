from tinydb import TinyDB, Query
from operator import itemgetter

DATABASE = TinyDB("database.json")
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

    def serialize(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "ranking": self.ranking,
        }

    @staticmethod
    def deserialize(serialized_player):
        return Player(
            serialized_player["last_name"],
            serialized_player["first_name"],
            serialized_player["birth_date"],
            serialized_player["gender"],
            serialized_player["ranking"],
        )

    def add_to_db(self):
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
        Player = Query()
        if self.get_from_db(self.last_name, self.first_name, self.birth_date):
            TABLE.remove(
                (Player.last_name == self.last_name)
                & (Player.first_name == self.first_name)
                & (Player.birth_date == self.birth_date)
            )

    @classmethod
    def get_from_db(cls, last_name, first_name, birth_date):
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
        serialized_players = sorted(
            TABLE.all(),
            key=itemgetter("last_name", "first_name", "birth_date"),
        )
        return [cls.deserialize(player) for player in serialized_players]
