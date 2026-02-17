
import json

def search_menu(moviebase_data):
    print("""
Rezept suchen:
1. Film Titel
2. Abbrechen
""")

    while True:
        choice = input("Option auswählen?")
        if choice == "1":
            search_by_name(moviebase_data)
        elif choice == "2":
            break

def search_by_name(moviebase_data):
    search_name = input("Bitte Rezeptname eingbene: ").lower()
    found = False

    for titel, book in moviebase_data.items():
        if search_name.lower() == titel.lower():
            found = True
            print(f"Film {titel} gefunden!")
            show = input("Wollen Sie die Verfügbarkeit anzeigen. (y/n): ")
            if show.lower() == "y":
                for availability in book["verfuegbar"]:
                    print(f" - {availability}")
            elif show.lower() == "n":
                break
            else:
                break

    if not found:
        print("Kein Film gefunden!.")


def recipe_search_by_ingredient(recipe_data_new):
    search_ingredient = input("Bitte Zutat eingeben: ").lower()
    found = False

    for name, book in recipe_data_new.items():
        for ingredient in book["ingredients"]:
            if search_ingredient in ingredient.lower():
                found = True
                print(f"Zutat '{ingredient}' im Rezept '{name}' gefunden!")
                show = input("Rezept anzeigen? (y/n): ")
                if show.lower() == "y":
                    print(f"\nRezept: {name}")
                    print("Zutaten:")
                    for ing in book["ingredients"]:
                        print(f" - {ing}")
                    print("Anleitung:")
                    for instr in book["instructions"]:
                        print(f" - {instr}")
                break

    if not found:
        print("Keine Rezepte mit dieser Zutat gefunden.")


def delete_recipe(recipe_data_new):
    search_name = input("Bitte Rezeptname eingbene: ").lower()
    found = False
    recipe_found = None
    for name, book in recipe_data_new.items():
         if search_name.lower() == name.lower():
            recipe_found = name
            break

    print(f"Rezept {recipe_found} gefunden!")
    delete_yn = input("Wollen Sie das Rezept löschen?")
    if delete_yn.lower() == "y":
        del recipe_data_new[recipe_found]
    with open("./db_json.json", 'w', encoding='utf-8') as db:
        json.dump(recipe_data_new, db, ensure_ascii=False, indent=4)
        print(f"Rezept {recipe_found} gelöscht!")

    return recipe_data_new

