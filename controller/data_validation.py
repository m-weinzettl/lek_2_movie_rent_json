
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


def data_validation_availability():
    availability_input_new = []
    while True:
        instructions_input = input("Anleitung (Leer Enter um zu Beenden)\n(Max 100 Zeichen): ")
        if instructions_input == '':
            break
        if 0 < len(instructions_input) <= 100:
            availability_input_new.append(instructions_input)
        else:
            print("Anleitung zu lange. Bitte erneut eingeben")

    return availability_input_new