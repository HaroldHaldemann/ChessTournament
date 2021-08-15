from tinydb import TinyDB, Query
from operator import itemgetter

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

	def remove_tournament_from_db(self, name):
		Tournament = Query()
		if self.TABLE.search(Tournament.name == name):
			self.TABLE.remove(Tournament.name == name)

	def get_name_tournaments(self):
		return [tournament['name'] for tournament in self.TABLE.all()]

	def get_all_tournament(self):
		Tournament = Query()
		tournaments = self.TABLE.all()
		dates = [tournament['date'] for tournament in tournaments]
		split_dates = [date.split("/") for date in dates]
		sorted_split_dates = sorted(
			split_dates,
			key=itemgetter(2, 1, 0)
		)
		sorted_dates = ['/'.join(split_date) for split_date in sorted_split_dates]
		sorted_tournaments = []
		for date in sorted_dates:
			sorted_tournaments += self.TABLE.search(Tournament.date == date)
		return sorted_tournaments
		
	def get_unfinished_tournaments(self):
		return [tournament for tournament in self.get_all_tournament() if not tournament['finished']]

	def get_finished_tournaments(self):
		Tournament = Query()
		return [tournament for tournament in self.get_all_tournament() if tournament['finished']]
