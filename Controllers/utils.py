class Util():

	def input_format(self, string_input):
		if type(string_input) == str:
			string_input = string_input.lower()
			split_input = string_input.split(" ")
			string_input = ''.join(split_input)
		return string_input