from tinydb import TinyDB, Query
from operator import itemgetter

class Player():

	DATABASE = TinyDB('database.json')
	TABLE = DATABASE.table('players')

	def __init__(
			self,
			last_name,
			first_name,
			birth_date,
			gender,
			ranking,
		):
		self.last_name = last_name
		self.first_name =first_name
		self.birth_date = birth_date
		self.gender = gender
		self.ranking = ranking

	def __str__(self):
		return (
			f"{self.last_name}\n"
			f"{self.first_name}\n"
			f"{self.birth_date}\n"
			f"{self.gender}\n"
			f"{self.ranking}"
		)

	def add_player_to_db(self):
		serialized_player = {
			'first_name': player.first_name,
			'last_name': player.last_name,
			'birth_date': player.birth_date,
			'gender': player.gender,
			'ranking': player.ranking,
		}
		self.TABLE.insert(serialized_player)

	def get_all_players(self):
		return sorted(
			self.TABLE.all(), 
			key=itemgetter('last_name', 'first_name', 'birth_date', 'ranking'),
		)

	def get_player(self, last_name, first_name, birth_date, gender, ranking):
		Player = Query()
		player = self.TABLE.search(
			Player['last_name'] == last_name and \
			Player['first_name'] == first_name and \
			Player['birth_date'] == birth_date and \
			Player['gender'] == gender and \
			Player['ranking'] == ranking
		)
		return player

player = Player("a", "a", "11/11/1111", "A", 1000)
print(player.TABLE.all())
test = player.get_player("a", "a", "11/11/1111", "A", 1000)
print(test)