
from model.movie import Movie
from controller.search_movie import  search_menu
from app.services import recipe_service
from controller.movie_handler import show_movie_from_json, write_movie_to_json
import json

def menu_user_input():
    return """
Bitte wählen Sie eine Option:
1. Alle Filme anzeigen # build / check / done
2. Neuen Film hinzufügen  # build / check / done
3. Film suchen # check / done
4. Film ausleihen / zurückgeben  # build / check / done
5. Programm beenden  # build / check / done
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
        user_option = input("Wählen Sie eine Option (1-4): ")

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

# edit recipe name
        elif user_option == '4':
            recipe_service.edit_recipe(recipe_data_new)

# show all hidden recipe ids
        elif user_option == '5':
            for name, book in recipe_data_new.items():
                print(f"\nRezept {name}: ID: {book['id']}")

# close program
        elif user_option == '5':
            print("Programm beendet.")
            break

        else:
            print("Falsche Eingabe!")
