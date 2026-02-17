
def data_validation_title():

    while True:
        title_input = input("Bitte geben Sie einen Film titel ein (max. 200 Zeichen: ")
        if 0 < len(title_input) <= 200:
            break
        else:
            print("Titel zu lange. Bitte erneut eingeben")

    return title_input

def data_validation_genre():
    genre_input_new = []
    while True:
        ingredient_input = input("Genre (Leer Enter um zu Beenden)\n(Max 100 Zeichen): ")
        if ingredient_input == '':
            break
        if 0 < len(ingredient_input) <= 100:
            genre_input_new.append(ingredient_input)
        else:
            print("Genre zu lange. Bitte erneut eingeben")

    return genre_input_new


def data_validation_release_year():
    release_year_input_new = input("Geben Sie ein Erscheinungsdatum an:")


    return release_year_input_new


def data_validation_availability():
    availability_input_new = input("Geben Sie die Verfügbarkeit an(1. für Vorhanden, 2. für Nicht vorhanden :")

    if availability_input_new == "1":
        availability_input_new = True
    else:
        availability_input_new = False

    return availability_input_new