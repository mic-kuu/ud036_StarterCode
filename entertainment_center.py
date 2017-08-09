import media
import website_generator

# This is the entry point for this project. It allows to dynamically define
# movies in the movies array, generate html/css/js and open it in the browser

blade_runner = media.Movie("Blade Runner",
                           "http://i.imgur.com/KykTdlk.jpg",
                           "https://www.youtube.com/embed/eogpIG53Cis?rel=0&amp;showinfo=0")  # noqa

fight_club = media.Movie("Fight Club",
                         "http://i.imgur.com/wyboozD.jpg",
                         "https://www.youtube.com/embed/BdJKm16Co6M?rel=0&amp;showinfo=0")  # noqa

kill_bill = media.Movie("Kill Bill",
                        "http://i.imgur.com/5AgF0Zi.jpg",
                        "https://www.youtube.com/embed/7kSuas6mRpk?rel=0&amp;showinfo=0")  # noqa

# Array of movies that will be used to generate website from
movies = [blade_runner, fight_club, kill_bill]

website_generator.generate_and_open(movies)
