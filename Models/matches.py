from dataclasses import dataclass
import Models


@dataclass
class Match():

    player1: Models.Player
    score1: float
    player2: Models.Player
    score2: float

    def serialize(self):
        return (
            [self.player1.serialize(), self.score1],
            [self.player2.serialize(), self.score2],
        )

    @staticmethod
    def deserialize(serialized_match):
        return Match(
            Models.Player.deserialize(serialized_match[0][0]),
            serialized_match[0][1],
            Models.Player.deserialize(serialized_match[1][0]),
            serialized_match[1][1],
        )
