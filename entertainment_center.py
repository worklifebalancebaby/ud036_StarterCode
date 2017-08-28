import fresh_tomatoes
import media

# instantiate movie objects using class Movie from media module
alien_covenant = media.Movie("Alien Covenant",
                             "https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
                             "https://www.youtube.com/watch?v=svnAD0TApb8")

blade_runner = media.Movie("Blade Runner",
                           "https://upload.wikimedia.org/wikipedia/en/2/27/Blade_Runner_2049_logo.png",
                           "https://www.youtube.com/watch?v=Dgank1Rk32E")

it = media.Movie("It",
                 "https://upload.wikimedia.org/wikipedia/en/a/a2/It_%282017%29_logo.jpg",
                 "https://www.youtube.com/watch?v=IT-r51CbcKY")

star_wars_the_last_jedi = media.Movie("Star Wars: The Last Jedi",
                                      "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                                      "https://www.youtube.com/watch?v=zB4I68XVPzQ")

# put movie objects into a list to run through the open_movies_page() function
movies = [alien_covenant, blade_runner, it, star_wars_the_last_jedi]

# build html file from movies list to open in a webbrowser
fresh_tomatoes.open_movies_page(movies)
