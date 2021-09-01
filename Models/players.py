from tinydb import TinyDB, Query
from operator import itemgetter
from dataclasses import dataclass
import datetime

DATABASE = TinyDB('database.json')
TABLE = DATABASE.table('players')


@dataclass
class Player():

	last_name: str
	first_name: str
	birth_date: datetime.date
	gender: str = ""
	ranking: int = 0

	def add_to_db(self):
		serialized_player = {
			'last_name': self.last_name,
			'first_name': self.first_name,
			'birth_date': self.birth_date,
			'gender': self.gender,
			'ranking': self.ranking,
		}
		TABLE.insert(serialized_player)


	def remove_from_db(self):
		Playert = Query()
		if self.get_player(last_name, first_name, birth_date):
			TABLE.remove(
				(Player['last_name'] == self.last_name) & \
				(Player['first_name'] == self.first_name) & \
				(Player['birth_date'] == self.birth_date)
			)


	@staticmethod
	def get_from_db(self, last_name, first_name, birth_date):
		Player = Query()
		player = TABLE.search(
			(Player['last_name'] == last_name) & \
			(Player['first_name'] == first_name) & \
			(Player['birth_date'] == birth_date)
		)
		return player


	@staticmethod
	def get_all_players():
		return sorted(
			TABLE.all(), 
			key=itemgetter('last_name', 'first_name', 'birth_date'),
		)
