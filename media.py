import webbrowser


class Movie():
    # Documentation for the class is done in triple quotes:
    """ Class to store movie related data, play trailer and potentially much more. 

    Attributes:
        title (str): Title of the movie
        storyline (str): Movie storyline 
        poster_image_url (str): URL to Movie poster picture (jpg or other)
        trailer_youtube_url (str): YouTUBE video URL featuring movie trailer

    Methods:
        show_trailer: opens default browser and play trailer on YouTUBE
    """

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
        webbrowser.open_new_tab(self.trailer_youtube_url)
