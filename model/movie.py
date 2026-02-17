from controller.data_validation import *


class Movie:
    def __init__(self, title=None, genre=None, release_date=None, availability=None):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.availability = availability


    def fill_movie(self):

        self.title = data_validation_title()
        self.genre = data_validation_genre()
        self.release_date = data_validation_release_year()
        self.availability = data_validation_availability()

    def is_valid(self):
        checks = [
            self.title is not None and self.title != "",
            self.genre is not None and len(self.genre) > 0,
            self.release_date is not None,
            self.availability is not None
        ]
        return all(checks)


#code edit for json export
    def do_dict(self):
        if not self.title:
            raise ValueError("Zugriff verweigert: Movie-Instanz wurde noch nicht befüllt!")

        return {
            "genre": self.genre,
            "erscheinungsjahr": self.release_date,
            "verfuegbar": self.availability
        }