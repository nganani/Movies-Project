import webbrowser


class Movie():
    # Documentation for the class in triple quotes:
    """ Class to store movie related data """

    # constant should be in upper case
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(
            self, movie_title, movie_storyline,
            poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
