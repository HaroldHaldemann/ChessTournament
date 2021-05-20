class Tournament():

	def __init__(
			self,
			name, 
			place, 
			date, 
			number_turns=4, 
			tours, 
			players, 
			time_control, 
			description,
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
