import Controllers


class PlayerView:

    # ===== ADD PLAYER TO DATABASE ===== #

    @classmethod
    def add_player_to_db(cls, player, step):
        """
        View corresponding to the addition of a new player in the database
        """
        print("\nCREATION D'UN NOUVEAU JOUEUR")

        options = {
            0: cls.add_player_last_name,
            1: cls.add_player_first_name,
            2: cls.add_player_birth_date,
            3: cls.add_player_gender,
            4: cls.add_player_ranking,
            5: cls.add_player_response,
        }
        Controllers.Util.call_options(options, step, player, step)

    @staticmethod
    def add_player_last_name(player, step):
        """
        View asking the last name of the new player
        """
        last_name = input("Veuillez renseigner le nom de ce joueur\n")
        Controllers.PlayerController.check_args(
            player,
            step,
            last_name=last_name,
        )

    @staticmethod
    def add_player_first_name(player, step):
        """
        View asking the first name of the new player
        """
        first_name = input("Veuillez renseigner le prénom de ce joueur\n")
        Controllers.PlayerController.check_args(
            player,
            step,
            first_name=first_name,
        )

    @staticmethod
    def add_player_birth_date(player, step):
        """
        View asking the birth date of the new player
        """
        print("Veuillez renseigner la date de naissance du joueur")

        birth_date = input("Format: AAAA-MM-JJ\n")
        Controllers.PlayerController.check_args(
            player,
            step,
            birth_date=birth_date,
        )

    @staticmethod
    def add_player_gender(player, step):
        """
        View asking the gender of the new player
        """
        print("Veuillez renseigner le sexe du joueur")
        print("1- Masculin")
        print("2- Féminin")

        gender = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.PlayerController.check_args(
            player,
            step,
            gender=gender,
        )

    @staticmethod
    def add_player_ranking(player, step):
        """
        View asking the ranking of the new player
        """
        print("Veuillez renseigner le classement du joueur")

        ranking = input("Le classement est un nombre positif\n")
        Controllers.PlayerController.check_args(
            player,
            step,
            ranking=ranking,
        )

    @staticmethod
    def add_player_response(player, step):
        """
        View corresponding to the confirmation of the player creation
        Redirect to the chosen view
        """
        print("Résumé du joueur:")
        print(f"Nom: {player.last_name}")
        print(f"Prénom: {player.first_name}")
        print(f"Date de naissance: {player.birth_date}")
        print(f"Sexe: {player.gender}")
        print(f"Classement: {player.ranking}")

        print("\nVoulez-vous continuer avec ces paramètres?")
        print("1- Sauvegarder et ajouter un nouveau joueur")
        print("2- Sauvegarder et revenir au menu principal")
        print("3- Annuler et revenir au menu principal")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.PlayerController.check_args(
            player,
            step,
            response=response,
        )

    # ===== LOAD PLAYERS ===== #

    @staticmethod
    def load_player(all_players):
        """
        View corresponding to the loading of a player
        """
        print("\nLISTE DES JOUEURS")
        print("0- Revenir au menu principal")

        for index, player in enumerate(all_players):
            print(
                f"{index+1}- {player.last_name} {player.first_name} "
                f"({player.birth_date}) / Classement: {player.ranking}"
            )
        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.PlayerController.load_player(all_players, response)

    @staticmethod
    def modify_player(all_players, player, input_player):
        """
        View asking what to do with the chosen player
        """
        print("\nRésumé du joueur:")
        print(f"Nom: {player.last_name}")
        print(f"Prénom: {player.first_name}")
        print(f"Date de naissance: {player.birth_date}")
        print(f"Sexe: {player.gender}")
        print(f"Classement: {player.ranking}\n")

        print("1- Modifier le classement du joueur")
        print("2- Supprimer le joueur")
        print("3- Annuler et revenir au menu principal")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.PlayerController.modify_player(
            all_players,
            player,
            response,
            input_player,
        )

    # ===== EXPORTS ===== #

    @staticmethod
    def export_all_players():
        """
        View to chose the sorting of the list of all players
        """
        print("Veuillez choisir l'ordonnement de votre rapport")
        print("1- Par ordre alphabétique")
        print("2- Par classement")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.PlayerController.export_all_players(response)
