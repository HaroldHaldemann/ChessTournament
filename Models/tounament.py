from tinydb import TinyDB

class Tournament():

	DATABASE = TinyDB('db.json')
	TOURNAMENT_TABLE = DATABASE.table('tournaments')

	def __init__(
			self,
			name,
			place,
			date,
			time_control,
			description,
			number_rounds=4,
		):
		self.name = name
		self.place = place
		self.date = date
		self.time_control = time_control
		self.description = description
		self.number_rounds = number_rounds


	def __str__(self):
		return (
			f"{self.name}\n"
			f"{self.place}\n"
			f"{self.date}\n"
			f"{self.number_rounds}\n"
			f"{self.rounds}\n"
			f"{self.players}\n"
			f"{self.time_control}\n"
			f"{self.description}"
		)


	def add_tournament_to_db(self):
		serialized_tournament = {
			'name': self.name,
			'place': self.place,
			'date': self.date,
			'number_rounds': self.number_rounds,
			'rounds': self.rounds,
			'players': self.players,
			'time_control': self.time_control,
			'description': self.description,
			'finished': (len(self.rounds) == number_rounds),
		}
		self.TOURNAMENT_TABLE.insert(serialized_tournament)