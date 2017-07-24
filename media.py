"""
This module stores the class Movie, with its atributes, instances and methods.
"""

import webbrowser


class Movie():
    """Class that initializes the Instance for our Movies"""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This will open the movie's trailer url
    def show_trailer(self):
        """Method that allow us to open the Movie's Trailer url"""
        webbrowser.open(self.trailer_youtube_url)
