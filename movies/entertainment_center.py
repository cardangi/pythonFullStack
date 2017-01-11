import media
import fresh_tomatoes


#Movies that point to the media file under the Movie class
#Each movie has a title, summary, title page, and trailer link
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


kung_pow = media.Movie("Kung Pow", "A man trying to avenge his families death",
                       "https://upload.wikimedia.org/wikipedia/en/5/54/Kungpow.jpg",
                       "https://www.youtube.com/watch?v=GXrAYdSeWY8")

#puts movies in array so that the fresh tomatoes can read them
movies = [toy_story, avatar, kung_pow]
fresh_tomatoes.open_movies_page(movies)

      
