from dataclasses import dataclass
import Models


@dataclass
class Match():

    player1: Models.Player
    score1: float
    player2: Models.Player
    score2: float

    def serialize(self):
        """
        Return a serialized version of a given match
        i.e. a dictionnary-like version of a match
        """
        return (
            [self.player1.serialize(), self.score1],
            [self.player2.serialize(), self.score2],
        )

    @staticmethod
    def deserialize(serialized_match):
        """
        Return a match version of a given serialized match
        i.e. a match which attributes correspond to
        the keys and the values of the serialized match
        """
        return Match(
            Models.Player.deserialize(serialized_match[0][0]),
            serialized_match[0][1],
            Models.Player.deserialize(serialized_match[1][0]),
            serialized_match[1][1],
        )
