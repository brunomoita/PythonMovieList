import webbrowser

class Movie() :
    """This class provides a way store movie related information"""
    
    valid_ratings = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_sotyrline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_sotyrline
        self.poster_image_url = poster_image
        self.youtube_trailer_url = trailer_youtube
    
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)