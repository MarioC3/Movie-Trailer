# This file needs to be run, so the HTML can be generated for our website
"""
This module contains the movie's data, and executes
the function to build our HTML file.
"""
import fresh_tomatoes
import media

# Available movies
toy_story1 = media.Movie(
    'Toy Story 1',
    'A story of a boy and his toys that come to life',
    'http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg',
    'https://www.youtube.com/watch?v=4KPTXpQehio')

avatar = media.Movie(
    'Avatar',
    'A marine on an alien planet',
    'http://cafmp.com/wp-content/uploads/2012/12/Avatar-Neytiri.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

harry_potter1 = media.Movie(
    'Harry Potter 1',
    'A london kid finds out he is a wizard and goes to a Magical school',
    'https://fanart.tv/fanart/movies/671/movieposter/harry-potter-and-the-sorcerers-stone-5223553f8ce55.jpg',  # noqa
    'https://www.youtube.com/watch?v=VyHV0BRtdxo')

avengers = media.Movie(
    'Avengers',
    'Earths mightiest heroes must come together\
    and learn to fight as a team if they are to\
    stop the mischievous Loki and his alien army from enslaving humanity.',
    'http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/avengers-movie-poster-1.jpg',  # noqa
    'https://www.youtube.com/watch?v=eOrNdBpGMv8')

transformers = media.Movie(
    'Transformers',
    'An ancient struggle between two Cybertronian races,\
    the heroic Autobots and the evil Decepticons, comes to Earth,\
    with a clue to the ultimate power held by a teenager.',
    'http://www.impawards.com/2007/posters/transformers_ver8_xlg.jpg',
    'https://www.youtube.com/watch?v=CbX_SIz_9fk')

spiderman_homecoming = media.Movie(
    'Spiderman Homecoming',
    'Peter Parker, with the help of his mentor Tony Stark,\
    tries to balance his life as an ordinary high school student\
    in New York City while fighting crime as his superhero alter\
    ego Spider-Man when a new threat emerges.',
    'https://cdn.vox-cdn.com/uploads/chorus_asset/file/8571017/spider_man_poster.jpg',  # noqa
    'https://www.youtube.com/watch?v=DiTECkLZ8HM')

movies = [toy_story1, avatar, harry_potter1,
          avengers, transformers, spiderman_homecoming]

# Executes the function to build our html
fresh_tomatoes.open_movies_page(movies)
