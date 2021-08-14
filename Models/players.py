from tinydb import TinyDB, Query
from operator import itemgetter

class Player():

	DATABASE = TinyDB('database.json')
	TABLE = DATABASE.table('players')

	def add_player_to_db(self, last_name, first_name, birth_date, gender, ranking):
		serialized_player = {
			'last_name': last_name,
			'first_name': first_name,
			'birth_date': birth_date,
			'gender': gender,
			'ranking': ranking,
		}
		self.TABLE.insert(serialized_player)


	def get_all_players(self):
		return sorted(
			self.TABLE.all(), 
			key=itemgetter('last_name', 'first_name', 'birth_date'),
		)


	def get_player(self, last_name, first_name, birth_date):
		Player = Query()
		player = self.TABLE.search(
			Player['last_name'] == last_name and \
			Player['first_name'] == first_name and \
			Player['birth_date'] == birth_date
		)
		return player
