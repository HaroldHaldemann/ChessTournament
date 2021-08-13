from tinydb import TinyDB

class Tournament():

	DATABASE = TinyDB('database.json')
	TABLE = DATABASE.table('tournaments')

	def add_tournament_to_db(
			self,
			name,
			place,
			date,
			time_control,
			description,
			number_rounds=4,
			players=[],
			rounds=[],
		):
		serialized_tournament = {
			'name': name,
			'place': place,
			'date': date,
			'number_rounds': number_rounds,
			'time_control': time_control,
			'description': description,
			'players': players,
			'rounds': rounds,
			'finished': (len(rounds) == number_rounds),
		}
		self.TABLE.insert(serialized_tournament)

	def get_name_tournaments(self):
		return [tournament['name'] for tournament in self.TABLE]