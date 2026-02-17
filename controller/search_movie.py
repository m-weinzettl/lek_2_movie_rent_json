
import json
from controller.movie_handler import rent_movie
def search_menu(moviebase_data):


    while True:
        print("""
        Film suchen:
        1. Film Titel
        2. Abbrechen
        """)
        choice = input("Option auswählen?")
        if choice == "1":
            search_by_name(moviebase_data)
        elif choice == "2":
            break

def search_by_name(moviebase_data):
    search_title = input("Bitte Film Titel eingebene: ").lower()
    found = False

    for title, book in moviebase_data.items():
        if search_title.lower() == title.lower() or search_title in str(title.lower()):
            found = True
            search_title_for_rent = title
            print(f"Film {title} gefunden!")
            show = input("Wollen Sie die Verfügbarkeit anzeigen. (y/n): ")
            if show.lower() == "y":
                print("Verfügbar:")
                available = book["verfuegbar"]
                if available:
                    print("Ja")

                    rent_movie_input = input("Wollen Sie den Film ausleihen? (y/n): ")
                    if rent_movie_input.lower() == "y" and available == True:
                        rent_movie(moviebase_data, search_title_for_rent, book, rent_movie_input)
                        break

                    else:
                        print("Film ist verliehen!")


                else:
                    print("Nein")

            elif show.lower() == "n":
                break
            else:
                break

    if not found:
        print("Kein Film gefunden!.")


