class Movie():
    """ Movie class is a representation of a single movie

    An instance object of Movie class can be initialized
    using the following list of arguments:

    Args:
        movie_title (str): Title of the movie.
        poster_url (str): The url to the the poster graphics.
        trailer_url (str): The url to the youtube video.

    """
    def __init__(self, movie_tile, poster_url, trailer_url):
        self.title = movie_tile
        self.poster_image_url = poster_url
        self.trailer_youtu