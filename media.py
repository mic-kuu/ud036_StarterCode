# The movie class definition
class Movie():
    def __init__(self, movie_tile, poster_url, trailer_url):
        self.title = movie_tile
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url