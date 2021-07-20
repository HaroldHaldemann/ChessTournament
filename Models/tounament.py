from tinydb import TinyDB

class Tournament():

	DATABASE = TinyDB('db.json')
	TOURNAMENT_TABLE = DATABASE.table('tournaments')

	def __init__(
			self,
			name,
			place,
			date,
			tours,
			players,
			time_control,
			description,
			number_turns=4,
		):
		self.name = name
		self.place = place
		self.date = date
		self.number_turns = number_turns
		self.tours = tours
		self.players = players
		self.time_control = time_control
		self.description = description


	def __str__(self):
		return (
			f"{self.name}\n"
			f"{self.place}\n"
			f"{str(self.date)}\n"
			f"{self.number_turns}\n"
			f"{self.tours}\n"
			f"{self.players}\n"
			f"{self.time_control}\n"
			f"{self.description}"
		)


	def add_tournament_to_db(tournament):
		serialized_tournament = {
			'name': tournament.name
			'place': tournament.place
			'date': tournament.date
			'number_tours': tournament.number_turns
			'tours': tournament.tours
			'players': tournament.players
			'time_control': tournament.time_control
			'description': tournament.description
		}
		TOURNAMENT_TABLE.insert(serialized_tournament)