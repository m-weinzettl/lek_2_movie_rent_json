
import json

def show_movie_from_json(moviebase_data_new):

        for title, book in moviebase_data_new.items():
            print(f"\nFilm {title}:")
            print("Genre:")
            for genre in book["genre"]:
                print(f"- {genre}")
            print("Verfügbarkeit:")
            for availability in book["verfuegbar"]:
                print(f"- {availability}")

def write_movie_to_json(new_movie, moviebase_data):

    moviebase_data[new_movie.title] = new_movie.do_dict()

    with open("./movies.json", 'w', encoding='utf-8') as db:
        json.dump(moviebase_data, db, ensure_ascii=False, indent=4)
        print(f"Titel {new_movie.title}: Erfolgreich gespeichert")

def edit_recipe(recipe_data_new):
    search_name = input("Bitte Rezeptname eingbene: ").lower()
    found = False
    recipe_found = None
    for name, book in recipe_data_new.items():
         if search_name.lower() == name.lower():
            recipe_found = name
            break
    if recipe_found:
        print(f"Rezept {recipe_found} gefunden!")
        edit_yn = input("Wollen Sie den Rezeptnamen ändern?")

        if edit_yn.lower() == "y":
            new_name = input("Bitte neuen Rezeptnamen eingeben.")

            book = recipe_data_new.pop(recipe_found)
            book["name"] = new_name
            recipe_data_new[new_name] = book

            with open("./movies.json", 'w', encoding='utf-8') as db:
                json.dump(recipe_data_new, db, ensure_ascii=False, indent=4)
                print(f"Rezept {recipe_found} geändert!")

    return recipe_data_new
