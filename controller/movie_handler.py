
import json
from controller.search_movie import *

def show_movie_from_json(moviebase_data_new):

        for title, book in moviebase_data_new.items():
            print(f"\nFilm: {title}")
            print("Genre:")
            for genre in book["genre"]:
                print(f"- {genre}")
            print("Erschienen:")

            release = book["erscheinungsjahr"]
            print(f"- {release}")

            print("Verfügbar:")
            available = book["verfuegbar"]
            if available:
                print("Ja")
            else:
                print("Nein")

def write_movie_to_json(new_movie, moviebase_data):

    moviebase_data[new_movie.title] = new_movie.do_dict()

    with open("./movies.json", 'w', encoding='utf-8') as db:
        json.dump(moviebase_data, db, ensure_ascii=False, indent=4)
        print(f"Titel {new_movie.title}: Erfolgreich gespeichert")

def rent_movie(moviebase_data, title, book ,rent_input):
    if rent_input == "y":

        moviebase_data[title]["verfuegbar"] = False

        with open("./movies.json", 'w', encoding='utf-8') as db:
            json.dump(moviebase_data, db, ensure_ascii=False, indent=4)
            print(f"Film {title} geliehen!")
    else:
        print("Buch nicht geliehen")

def return_movie(moviebase_data):
    return_movie_name = input("Welchen film wollen Sie zurückgeben?").lower()
    found = False

    for title, book in moviebase_data.items():
        if return_movie_name.lower() == title.lower() or return_movie_name in str(title.lower()):
            found = True
            print(f"Film {title} gefunden!")
            back_input = input("Wollen Sie den Film zurückgeben?. (y/n): ")
            if back_input.lower() == "y":
                moviebase_data[title]["verfuegbar"] = True

                with open("./movies.json", 'w', encoding='utf-8') as db:
                    json.dump(moviebase_data, db, ensure_ascii=False, indent=4)
                    print(f"Film {title} zurückgegeben!")
            else:
                print("Film nicht zurückgeben!")


    if not found:
        print("Kein Film gefunden!.")
    pass