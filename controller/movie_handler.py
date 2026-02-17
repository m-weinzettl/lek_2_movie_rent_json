
import json

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

def rent_movie(moviebase_data):
    pass
