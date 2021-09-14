import Controllers

class RoundView():

  @staticmethod
  def def_number_rounds(tournament):
    print("Veuillez renseigner le nombre de tour")
    number_rounds = input("Format: nombre entre 1 et 7\n")

    Controllers.RoundController.check_number_rounds(tournament, number_rounds)

  @staticmethod
  def create_first_round(tournament):
    print("\nCREATION DES TOURS")
    print("1- Créer un nouveau tour")
    print("2- Revenir au menu principal")
    response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")

    Controllers.RoundController.create_first_round(tournament, response)

  @staticmethod
  def start_round(tournament, round):
    print("\nCREATION DES TOURS")
    print("\nListe des matchs")
    for match in round.matches:
      p1 = match[0][0]
      s1 = match[0][1]
      p2 = match[1][0]
      s2 = match[1][1]
      print(f"\n{p1.last_name} {p1.first_name} ({p1.birth_date}) \
      / Classement: {p1.ranking} / Score: {s1}")
      print("CONTRE")
      print(f"{p2.last_name} {p2.first_name} ({p2.birth_date}) \
      / Classement: {p2.ranking} / Score: {s2}\n")

    response = input("Veuillez entrer 0 pour commencer le tour\n")
    Controllers.RoundController.start_round(tournament, round, response)

  @staticmethod
  def end_round(tournament, round):
    print("\nCREATION DES TOURS")

    print("\nMatchs en cours\n")

    response = input("Veuillez entrer 0 pour terminer le tour\n")
    Controllers.RoundController.end_round(tournament, round, response)

  @staticmethod
  def results_round(tournament, round, step):
    print("\nRESULTAT DU TOUR")
    p1 = round.matches[step][0][0]
    s1 = round.matches[step][0][1]
    p2 = round.matches[step][1][0]
    s2 = round.matches[step][1][1]

    print("Veuillez determiner le vainqueur")
    print(f"\n1- {p1.last_name} {p1.first_name} ({p1.birth_date}) \
    / Classement: {p1.ranking} / Score: {s1}")
    print(f"2- {p2.last_name} {p2.first_name} ({p2.birth_date}) \
    / Classement: {p2.ranking} / Score: {s2}\n")
    print("3- Egalité")

    response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")
    Controllers.RoundController.results_round(tournament, round, step, response)

  @staticmethod
  def confirm_round(tournament, round):
    print("FINALISATION DU ROUND")
    for match in round.matches:
      p1 = match[0][0]
      s1 = match[0][1]
      p2 = match[1][0]
      s2 = match[1][1]
      print(f"{p1.last_name} {p1.first_name} ({p1.birth_date}) / Score: {s1}")
      print("CONTRE")
      print(f"{p2.last_name} {p2.first_name} ({p2.birth_date}) / Score: {s2}")

    print("1- Sauvegarder et continuer le tournoi")
    print("2- Sauvegarder et revenir au menu principal")
    print("3- Annuler et revenir au menu principal")
    response = input("Veuillez sélectionner une des options disponibles en entrant son numéro\n")

    Controllers.RoundController.confirm_rounds(tournament, round, response)