import webbrowser


class Movie():
    """Thic class provides a way to store movie related information."""

    def __init__(self, movie_title, poster, trailer):
        self.title = movie_title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
