import webbrowser

class Movie() :
    def __init__(self, movie_title, movie_sotyrline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_sotyrline
        self.poster_image_url = poster_image
        self.youtube_trailer_url = trailer_youtube
    
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)