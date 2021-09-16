import Controllers


class MenuView:
    @staticmethod
    def main_menu():
        """
        View corresponding to the main menu
        """
        print("\nMENU PRINCIPAL")
        print("1- Créer un nouveau tournoi")
        print("2- Charger un tournoi")
        print("3- Ajouter des joueurs dans la base de données")
        print("4- Charger un joueur")
        print("5- Générer un rapport")
        print("6- Quitter le programme\n")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.MenuController.main_menu(response)

    @staticmethod
    def export_menu():
        """
        View corresponding to the export menu
        """
        print("\nMENU GENERATION DE RAPPORT")
        print("1- Liste de tous les joueurs")
        print("2- Liste de tous les joueurs d'un tournoi")
        print("3- Liste de tous les tournois")
        print("4- Liste de tous les tours d'un tournoi")
        print("5- Liste de tous les matchs d'un tournoi")
        print("6- Revenir au menu principal\n")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.MenuController.export_menu(response)

    @staticmethod
    def load_menu():
        """
        View corresponding to the loading menu
        """
        print("\nCHARGEMENT D'UN TOURNOI")
        print("1- Charger un tournoi non complété")
        print("2- Charger un tournoi complété")
        print("3- Revenir au menu principal")

        response = input("Veuillez entrer le numéro de l'option choisie\n")
        Controllers.MenuController.load_menu(response)
