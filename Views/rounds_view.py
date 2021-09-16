import Controllers


class RoundView:
    @staticmethod
    def def_number_rounds(tournament):
        """
        View asking the number of rounds of the given tournament
        """
        print("Veuillez renseigner le nombre de tour (4 par défaut)")

        number_rounds = input("Format: nombre entre 1 et 7\n")
        Controllers.RoundController.check_number_rounds(
            tournament,
            number_rounds,
        )

    @staticmethod
    def create_first_round(tournament):
        """
        View asking if create a first round or going back to main menu
        """
        print("\nCREATION DU TOUR")
        print("1- Créer un nouveau tour")
        print("2- Revenir au menu principal")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.RoundController.create_first_round(
            tournament,
            response,
        )

    @staticmethod
    def start_round(tournament, round):
        """
        View asking to start the new round
        for round.date_start
        """
        print("\nDEBUT DU TOUR")
        print("\nListe des matchs")
        for match in round.matches:
            p1 = match.player1
            s1 = match.score1
            p2 = match.player2
            s2 = match.score2

            print(
                f"\n1- {p1.last_name} {p1.first_name} ({p1.birth_date})"
                f" / Classement: {p1.ranking} / Score: {s1}"
            )
            print("CONTRE")
            print(
                f"2- {p2.last_name} {p2.first_name} ({p2.birth_date})"
                f" / Classement: {p2.ranking} / Score: {s2}\n"
            )

        response = input("Veuillez entrer 1 pour commencer le tour\n")
        Controllers.RoundController.start_round(
            tournament,
            round,
            response,
        )

    @staticmethod
    def end_round(tournament, round):
        """
        View asking to end the new round
        for round.date_end
        """
        print("\nMATCH EN COURS\n")

        response = input("Veuillez entrer 1 pour terminer le tour\n")
        Controllers.RoundController.end_round(
            tournament,
            round,
            response,
        )

    @staticmethod
    def results_round(tournament, round, step):
        """
        Views asking the results of the given round matches
        """
        print("\nRESULTAT DU TOUR")
        p1 = round.matches[step].player1
        s1 = round.matches[step].score1
        p2 = round.matches[step].player2
        s2 = round.matches[step].score2

        print("Veuillez determiner le vainqueur")
        print(
            f"1- {p1.last_name} {p1.first_name} ({p1.birth_date})"
            f" / Classement: {p1.ranking} / Score: {s1}\n"
        )
        print(
            f"2- {p2.last_name} {p2.first_name} ({p2.birth_date})"
            f" / Classement: {p2.ranking} / Score: {s2}\n"
        )
        print("3- Egalité")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.RoundController.results_round(
            tournament,
            round,
            step,
            response
        )

    @staticmethod
    def confirm_round(tournament, round):
        """
        Views asking confirmation of the round and
        asking what to do next
        """
        print("\nFINALISATION DU TOUR\n")
        for match in round.matches:
            p1 = match.player1
            s1 = match.score1
            p2 = match.player2
            s2 = match.score2

            print(
                f"\n{p1.last_name} {p1.first_name} "
                f"({p1.birth_date}) / Score: {s1}"
            )
            print("CONTRE")
            print(
                f"{p2.last_name} {p2.first_name} "
                f"({p2.birth_date}) / Score: {s2}\n"
            )
        print("1- Sauvegarder et continuer le tournoi")
        print("2- Sauvegarder et revenir au menu principal")
        print("3- Annuler et revenir au menu principal")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.RoundController.confirm_round(
            tournament,
            round,
            response,
        )

    @staticmethod
    def end_tournament(tournament, winners):
        """
        View displaying the winner(s) of the tournament and
        asking what to do next
        """
        print("FIN DU TOURNOI")
        if len(winners) == 1:
            player = winners[0][0]
            score = winners[0][1]
            print("Le vainqueur est:")
            print(
                f"{player.last_name} {player.first_name}"
                f"({player.birth_date})"
            )
        else:
            print("Les vainqueurs sont:")
            for winner in winners:
                player = winner[0]
                score = winner[1]
                print(
                    f"{player.last_name} {player.first_name}"
                    f"({player.birth_date})"
                )
        print(f"Avec un score de: {score}")

        print("Voulez-vous modifier le classement des joueurs?")
        print("1- Aller au menu de chargement des joueurs")
        print("2- Revenir au menu principal")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.RoundController.end_tournament(
            tournament,
            winners,
            response,
        )
