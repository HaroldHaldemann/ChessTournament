class Player():

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