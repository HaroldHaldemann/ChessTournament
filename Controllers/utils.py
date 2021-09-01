import datetime

class Util():

	@staticmethod
	def input_format(string_input):
		if type(string_input) == str:
			string_input = string_input.lower()

			split_input = string_input.split(" ")
			string_input = ''.join(split_input)

		return string_input


	@staticmethod
	def call_options(options, response, *args):
		if is_instance(option[response], list):

			params = options[response][1]
			options[response][0](params, *args)

		else:
			option[response](*args)


	@staticmethod
	def check_date(date):
		try:
			date = datetime.date.fromisoformat(date)

		except:
			print('Date invalide')
			return False

		else:
			return date


	@staticmethod
	def check_response(len_options, response):
		if response not in [f"{index + 1}" for index in range(len_options)]:
			print("Réponse invalide")
			return False

		return response


	@staticmethod
	def check_date_old(date):
		split_date = date.split('/')
		if len(split_date) != 3:
			print("Date invalide: format invalide")
			return False
		for day_month_year in split_date:
			if not day_month_year.isdigit():
				print("Date invalide: veuillez utiliser des nombres")
				return False
		sday = split_date[0]
		smonth = split_date[1]
		syear = split_date[2]
		if len(sday) == 1:
			sday = "0" + sday
		if len(smonth) == 1:
			smonth = "0" + smonth
		if len(syear) < 4:
			syear = ("0"*(4-len(syear))) + syear
		date = '/'.join([sday, smonth, syear])
		day = int(sday)
		month = int(smonth)
		year = int(syear)
		days_per_month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if year%4 == 0 and (year%100 != 0 or year%400 == 0):
			days_per_month[2] = 29
		if not (0 < month <= 12 and 0 < day <= days_per_month[month] and year < 10000):
			print("Date invalide: cette date n'existe pas")
			return False
		return date