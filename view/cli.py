
from model.movie import Movie
from controller.search_movie import  search_menu
from controller.movie_handler import show_movie_from_json, write_movie_to_json, rent_movie
import json

def menu_user_input():
    return """
Bitte wählen Sie eine Option:
1. Alle Filme anzeigen
2. Neuen Film hinzufügen  # build / check / done
3. Film suchen
4. Film ausleihen / zurückgeben  # build / check / done
5. Programm beenden
"""

#global recipe json dict import from file
def load_from_json(recipe_data_new):
    try:
        with open("./movies.json", 'r', encoding='utf-8') as from_json:
            moviebase_data = json.load(from_json)

        return moviebase_data

    except FileNotFoundError:
        print("error")

def show_menu():
    moviebase_data = {}
    moviebase_data = load_from_json(moviebase_data) #set global json dict variable

# menu structure
    while True:
        print(menu_user_input())
        user_option = input("Wählen Sie eine Option (1-5): ")

# show all recipes
        if user_option == '1':
            if not moviebase_data:
                print("Kein Rezept gefunden.")
            else:
                show_movie_from_json(moviebase_data)

# add new recipe
        elif user_option == '2':
            new_movie = Movie()
            new_movie.fill_movie()

            write_movie_to_json(new_movie, moviebase_data)

# search movie
        elif user_option == '3':
            search_menu(moviebase_data)

# rent movie
        elif user_option == '4':
            rent_movie(moviebase_data)

# close program
        elif user_option == '5':
            print("Programm beendet.")
            break

        else:
            print("Falsche Eingabe!")
