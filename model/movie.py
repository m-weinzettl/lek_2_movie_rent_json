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


#code edit for json export
    def do_dict(self):
        return {
            "title": self.title,
            "genre":  self.genre,
            "erscheinungsjahr": self.release_date,
            "verfuegbar": self.availability}