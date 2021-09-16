import datetime


class Util:
    @staticmethod
    def input_format(string_input):
        if type(string_input) == str:
            string_input = string_input.lower()

            for caracter in ["à", "â", "ä"]:
                string_input.replace(caracter, "a")

            for caracter in ["é", "è", "ê", "ë"]:
                string_input.replace(caracter, "e")

            for caracter in ["î", "ï"]:
                string_input.replace(caracter, "i")

            for caracter in ["ô", "ö"]:
                string_input.replace(caracter, "o")

            for caracter in ["ù", "û", "ü"]:
                string_input.replace(caracter, "u")
            
            split_input = string_input.split(" ")
            string_input = "".join(split_input)

        return string_input

    @staticmethod
    def call_options(options, response, *args):
        if isinstance(options[response], list):
            new_args = args
            params = options[response][1:]

            for param in reversed(params):
                new_args = (param,) + new_args

            result = options[response][0](*new_args)

        else:
            result = options[response](*args)

        return result

    @staticmethod
    def check_date(date):
        try:
            date = datetime.date.fromisoformat(date)

        except ValueError:
            print("Date invalide")
            return False

        else:
            return date.isoformat()

    @staticmethod
    def check_response(len_options, response):
        if response not in [f"{i + 1}" for i in range(len_options)]:
            print("Réponse invalide")
            return False

        return response

    @staticmethod
    def check_player(all_players, input_player):
        if input_player not in [f"{i + 1}" for i in range(len(all_players))]:
            print("Joueur invalide")
            return False

        return input_player
