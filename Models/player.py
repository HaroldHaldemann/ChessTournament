from tinydb import TinyDB

class Player():

	DATABASE = TinyDB('db.json')
	PLAYER_TABLE = DATABASE.table('players')

	def __init__(
			self,
			last_name,
			first_name,
			birth_date,
			gender,
			elo_rating,
		):
		self.last_name = last_name
		self.first_name =first_name
		self.birth_date = birth_date
		self.gender = gender
		self.elo_rating = elo_rating

	def __str__():
		return (
			f"{self.last_name}\n"
			f"{self.first_name}\n"
			f"{self.birth_date}\n"
			f"{self.gender}\n"
			f"{self.elo_rating}"
		)

	def add_player_to_db(player):
		serialized_player = {
			'first_name': player.first_name
			'last_name': player.last_name
			'birth_date': player.birth_date
			'gender': player.gender
			'elo_rating': player.elo_rating
		}
		PLAYER_TABLE.insert(serialized_player)


	