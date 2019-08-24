import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/pt/thumb/d/dc/Movie_poster_toy_story.jpg/250px-Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet,",
                     'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")
#print(avatar.storyline)
#avatar.show_trailer()

school_of_Rock = media.Movie("School of Rock",
                             "A rock musician passes as a middle school teacher",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatuille = media.Movie("Ratatuille",
                         "A mouse who dreamed of cooking",
                         "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                         "https://www.youtube.com/watch?v=nTTxc1Vf2pQ")

fight_club = media.Movie("Fight Club",
                         "After losing everything a man starts a boxing club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=Y6cwmHL2tFI")

hunger_games = media.Movie("Hunger Games",
                           "A deadly reality show in the future",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/3/39/The_Hunger_Games_cover.jpg/220px-The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_Rock, ratatuille, fight_club, hunger_games]
fresh_tomatoes.open_movies_page(movies)