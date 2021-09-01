from tinydb import TinyDB, Query
from dataclasses import dataclass, field
import datetime
from typing import List

DATABASE = TinyDB('database.json')
TABLE = DATABASE.table('tournaments')


@dataclass
class Tournament():

	name: str
	place: str
	date: datetime.date
	time_control: str
	description: str
	players: List
	rounds: List
	number_rounds: int = 4


	def add_to_db(self):
		tournament = self.is_in_db(self.name)

		if tournament:
			Tournament = Query()

			if self.number_rounds != 4:
				TABLE.update(
						{'number_rounds': self.rounds},
						Tournament.name == tournament['name'],
					)
			if len(self.rounds) > len(tournament['rounds']):
				TABLE.update(
					{'rounds': self.rounds},
					Tournament.name == tournament['name'],
				)
			if len(self.players) > len(tournament['players']):
				TABLE.update(
						{'players': self.players},
						Tournament.name == tournament['name'],
					)
		else:
			serialized_tournament = {
				'name': self.name,
				'place': self.place,
				'date': self.date.isoformat(),
				'number_rounds': self.number_rounds,
				'time_control': self.time_control,
				'description': self.description,
				'players': self.players,
				'rounds': self.rounds,
				'finished': (len(self.rounds) == self.number_rounds),
			}
			TABLE.insert(serialized_tournament)


	def remove_from_db(self):
		Tournament = Query()

		if self.is_in_db(self.name):
			TABLE.remove(Tournament.name == self.name)


	@staticmethod
	def get_all_tournament():
		Tournament = Query()
		tournaments = TABLE.all()

		sorted_dates = sorted(
			[tournament['date'] for tournament in tournaments],
			reverse=True,
		)
		sorted_tournaments = []

		for date in sorted_dates:
			sorted_tournaments += TABLE.search(Tournament.date == date)
			
		return sorted_tournaments

	
	@staticmethod
	def is_in_db(name):
		Tournament = Query()
		return TABLE.search(Tournament.name == name)

	@classmethod
	def get_unfinished_tournaments(cls):
		return [tournament for tournament in cls.get_all_tournament() if not tournament['finished']]


	@classmethod
	def get_finished_tournaments(cls):
		Tournament = Query()
		return [tournament for tournament in cls.get_all_tournament() if tournament['finished']]
