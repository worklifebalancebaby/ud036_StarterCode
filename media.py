import webbrowser


'''This class initializes the Movie object with important attributes'''
 
class Movie():
    ''' the contructor method makes space for the attributes movie title, poster iamge url, and youtube trailer url'''
    def __init__(self, movie_title, poster, trailer):
        self.title = movie_title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
