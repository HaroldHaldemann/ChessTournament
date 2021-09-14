from tinydb import TinyDB, Query
from typing import List

from tinydb.utils import V
import Models

DATABASE = TinyDB('database.json')
TABLE = DATABASE.table('tournaments')

class Tournament():

	def __init__(
			self,
			name = "",
			place = "",
			date = "",
			time_control = "",
			description = "",
			players = [],
			number_rounds = 4,
			rounds = [],
		):
		self.name = name
		self.place = place
		self.date = date
		self.time_control = time_control
		self.description = description
		self.players = players
		self.number_rounds = number_rounds
		self.rounds = rounds

	def serialize(self):
		return {
				'name': self.name,
				'place': self.place,
				'date': self.date,
				'time_control': self.time_control,
				'description': self.description,
				'players': self.players,
				'number_rounds': self.number_rounds,
				'rounds': self.rounds,
				'finished': (len(self.rounds) == self.number_rounds + 1),
			}

	@staticmethod
	def deserialize(serialized_tournament):
		tournament= Tournament()
		tournament.name = serialized_tournament['name']
		tournament.place = serialized_tournament['place']
		tournament.date = serialized_tournament['date']
		tournament.time_control = serialized_tournament['time_control']
		tournament.description = serialized_tournament['description']
		tournament.players = \
			[Models.Player.deserialize(player) for player in serialized_tournament['players']]
		tournament.number_rounds = serialized_tournament['number_rounds']
		tournament.rounds = serialized_tournament['rounds']
		tournament.finished = serialized_tournament['finished']
		return tournament

	def add_to_db(self):
		tournament = self.get_from_db(self.name)

		if tournament:
			Tournament = Query()

			if self.number_rounds != 4:
				TABLE.update(
						{'number_rounds': self.rounds},
						Tournament.name == tournament.name,
					)
			if self.rounds != tournament.rounds:
				TABLE.update(
					{'rounds': self.rounds},
					Tournament.name == tournament.name,
				)
			if self.players != tournament.players:
				serialized_players = [player.serialize() for player in self.players]
				TABLE.update(
						{'players': serialized_players},
						Tournament.name == tournament.name,
					)
		else:
			TABLE.insert(self.serialize())


	def remove_from_db(self):
		Tournament = Query()

		if self.get_from_db(self.name):
			TABLE.remove(Tournament.name == self.name)


	@classmethod
	def get_all_tournament(cls):
		Tournament = Query()
		tournaments = TABLE.all()

		sorted_dates = sorted(
			[tournament['date'] for tournament in tournaments],
			reverse=True,
		)
		sorted_tournaments = []

		for date in sorted_dates:
			sorted_tournaments += TABLE.search(Tournament.date == date)
			
		return [cls.deserialize(tournament) for tournament in sorted_tournaments]
	
	@classmethod
	def get_from_db(cls, name):
		Tournament = Query()
		serialized_tournament = TABLE.search(Tournament.name == name)
		if serialized_tournament:
			return cls.deserialize(serialized_tournament[0])
		else:
			return serialized_tournament

	@classmethod
	def get_unfinished_tournaments(cls):
		return [tournament for tournament in cls.get_all_tournament() if not tournament.finished]

	@classmethod
	def get_finished_tournaments(cls):
		return [tournament for tournament in cls.get_all_tournament() if tournament.finished]
