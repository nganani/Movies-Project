import webbrowser


class Movie():
    # Documentation for the class in triple quotes:
    """ Class to store movie related data. play trailer and potentially much more"""

    # Constructor for class Movie
    def __init__(
            self, movie_title, movie_storyline,
            poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Play movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
