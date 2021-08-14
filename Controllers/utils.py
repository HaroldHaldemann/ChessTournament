class Util():

	def input_format(self, string_input):
		if type(string_input) == str:
			string_input = string_input.lower()
			split_input = string_input.split(" ")
			string_input = ''.join(split_input)
		return string_input


	def check_date(self, date):
		split_date = date.split('/')
		if len(split_date) != 3:
			print("Date invalide: format invalide")
			return False
		for day_month_year in split_date:
			if not day_month_year.isdigit():
				print("Date invalide: veuillez utiliser des nombres")
				return False
		day = int(split_date[0])
		month = int(split_date[1])
		year = int(split_date[2])
		days_per_month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if year%4 == 0 and (year%100 != 0 or year%400 == 0):
			days_by_month[2] = 29
		if not (month <= 12 and day <= days_per_month[month]):
			print("Date invalide: cette date n'existe pas")
			return False
		return date