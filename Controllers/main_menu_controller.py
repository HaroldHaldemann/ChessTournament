import Views as view

def main_menu_controller(response):
	if response not in [f"{i}" for i in range(5)]:
		print("\nCommande incorrect, veuillez entrer un numéro valide")
		view.main_menu_view()
	options = {
		'1': view.tv.new_tournament,
		'2': view.tv.load_tournament_menu,
		'3': view.ev.export_menu_view,
		'4': exit,
	}
	options[response]()