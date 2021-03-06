import Views
import Controllers
import Models


class TournamentView:

    # ====== NEW TOURNAMENT ====== #

    @classmethod
    def new_tournament(cls, tournament, step):
        """
        View corresponding to the addition of a new tournament in the database
        """
        print("\nCREATION D'UN NOUVEAU TOURNOI")

        options = {
            0: cls.new_tournament_name,
            1: cls.new_tournament_place,
            2: cls.new_tournament_date,
            3: cls.new_tournament_time_control,
            4: cls.new_tournament_description,
            5: cls.new_tournament_response,
        }
        Controllers.Util.call_options(options, step, tournament, step)

    @staticmethod
    def new_tournament_name(tournament, step):
        """
        View asking the name of the new tournament
        """
        name = input("Veuillez renseigner le nom de ce tournoi\n")
        Controllers.TournamentController.check_args(
            tournament,
            step,
            name=name,
        )

    @staticmethod
    def new_tournament_place(tournament, step):
        """
        View asking the place of the new tournament
        """
        place = input("Veuillez renseigner le lieu de ce tournoi\n")
        Controllers.TournamentController.check_args(
            tournament,
            step,
            place=place,
        )

    @staticmethod
    def new_tournament_date(tournament, step):
        """
        View asking the date of the new tournament
        """
        print("Veuillez renseigner la date de ce tournoi")

        date = input("Format: AAAA-MM-JJ\n")
        Controllers.TournamentController.check_args(
            tournament,
            step,
            date=date,
        )

    @staticmethod
    def new_tournament_time_control(tournament, step):
        """
        View asking the time control of the new tournament
        """
        print("Veuillez renseigner votre controle du temps")
        print("1- Bullet")
        print("2- Blitz")
        print("3- Coup rapide")
        time_control = input("Veuillez entrer le num??ro de l'option choisie\n")

        Controllers.TournamentController.check_args(
            tournament,
            step,
            time_control=time_control,
        )

    @staticmethod
    def new_tournament_description(tournament, step):
        """
        View asking the description of the new tournament
        """
        print("Vous pouvez renseigner des remarques pour ce tournoi")

        description = input("Laissez vide dans le cas contraire\n")
        Controllers.TournamentController.check_args(
            tournament,
            step,
            description=description,
        )

    @staticmethod
    def new_tournament_response(tournament, step):
        """
        View corresponding to the confirmation of the tournament creation
        Redirect to the chosen view
        """
        print("R??sum?? du tournoi")
        print(f"Nom: {tournament.name}")
        print(f"Lieu: {tournament.place}")
        print(f"Date: {tournament.date}")
        print(f"Gestion du temps: {tournament.time_control}")
        print(f"Remarques: {tournament.description}")

        print("\nVoulez-vous continuer avec ces param??tres?")
        print("1- Sauvegarder et continuer")
        print("2- Sauvegarder et revenir au menu principal")
        print("3- Annuler et revenir au menu principal")

        response = input("Veuillez entrer le num??ro de l'option choisie\n")
        Controllers.TournamentController.check_args(
            tournament,
            step,
            response=response,
        )

    # ===== ADD PLAYER TO TOURNAMENT ===== #

    @staticmethod
    def add_player_to_tournament(all_players, players, tournament):
        """
        View asking which player to add to the given tournament
        """
        print("\nAJOUT DE JOUEURS")
        print(f"Veuillez ajouter {8-len(players)} joueurs dans le tournoi")

        print("\n0- Ajouter de nouveaux joueurs ?? la base de donn??es")
        print("\nListe des joueurs:")

        for index, player in enumerate(all_players):
            print(f"\n{index + 1}- ")
            print(f"Nom: {player.last_name} {player.first_name}")
            print(f"Date de naissance: {player.birth_date}")
            print(f"Genre: {player.gender}")
            print(f"Classement: {player.ranking}")

        player = input("Veuillez entrer le num??ro de l'option choisie\n")
        players.append(player)
        Controllers.TournamentController.add_player_to_tournament(
            all_players,
            players,
            tournament,
        )

    @staticmethod
    def confirm_players(all_players, players, tournament):
        """
        Views asking for the confirmation for the given players
        """
        print("\nAJOUT DE JOUEURS")
        print("\nListe des joueurs:")

        for index, player in enumerate(players):
            print(f"\n{index + 1}- ")
            print(f"Nom: {player.last_name} {player.first_name}")
            print(f"Date de naissance: {player.birth_date}")
            print(f"Genre: {player.gender}")
            print(f"Classement: {player.ranking}")

        print("\nVoulez-vous ces joueurs pour le tournoi?")
        print("1- Confimer et sauvegarder")
        print("2- Modifier la s??l??ction")

        response = input("Veuillez entrer le num??ro de l'option choisie\n")
        Controllers.TournamentController.confirm_players(
            all_players,
            players,
            response,
            tournament,
        )

    # ====== LOAD TOURNAMENT ====== #

    @staticmethod
    def load_tournament(list_tournaments):
        """
        View asking which tournament to load
        """
        print("\nCHARGEMENT D'UN TOURNOI")
        print("0- Cr??er un nouveau tournoi")
        print("00- Annuler et revenir au menu pr??c??dent")
        print("Liste des tournois:")

        for index, tournament in enumerate(list_tournaments):
            print(
                f"{index+1}- "
                f"Nom: {tournament.name}, "
                f"Lieu: {tournament.place}, "
                f"Date: {tournament.date}, "
                f"Gestion du temps: {tournament.time_control}"
            )

        response = input("Veuillez entrer le num??ro de l'option choisie\n")
        Controllers.TournamentController.load_tournament(
            list_tournaments,
            response,
        )

    @staticmethod
    def load_step_tournament(tournament):
        """
        View asking what to do whith the given tournament
        """
        print("\nCHARGEMENT D'UN TOURNOI")
        print("1- Continuer le tournoi")
        print("2- Supprimer le tournoi")
        print("3- Annuler et revenir au menu de chargement")

        response = input("Veuillez entrer le num??ro de l'option choisie\n")
        Controllers.TournamentController.load_step_tournament(
            tournament,
            response,
        )

    # ====== EXPORTS ====== #

    @staticmethod
    def export_all_tournaments():
        """
        View to display the list of all tournaments in the database
        """
        Models.Tournament.export_all_tournaments()
        print("L'ensemble des tournois vient d'??tre export?? vers Exports")
        Views.MenuView.export_menu()

    @staticmethod
    def select_tournament(export):
        """
        View asking which tournament to export
        """
        tournaments = Models.Tournament.get_all_tournaments()
        print("\nLISTE DES TOURNOIS")
        print("Veuillez choisir le tournoi dont vous souhaitez le rapport\n")
        print("0- Revenir au menu pr??c??dent")
        for index, tournament in enumerate(tournaments):
            print(
                f"{index+1}- "
                f"Nom: {tournament.name}, "
                f"Lieu: {tournament.place}, "
                f"Date: {tournament.date}, "
                f"Gestion du temps: {tournament.time_control}"
            )

        response = input("Veuillez entrer le num??ro de l'option choisie\n")
        Controllers.TournamentController.select_tournament(
            export,
            tournaments,
            response,
        )

    @staticmethod
    def export_players(tournament):
        """
        View to chose the sorting of the list of all tournaments
        """
        print("Veuillez choisir l'ordonnement de votre rapport")
        print("1- Par ordre alphab??tique")
        print("2- Par classement")

        response = input("Veuillez entrer le num??ro de l'option choisie\n")
        Controllers.TournamentController.export_players(tournament, response)
