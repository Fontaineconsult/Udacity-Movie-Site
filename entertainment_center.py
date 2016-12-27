import Media # Import Media module containing class constructors for movies using tmdb3 API. 
import fresh_tomatoes
import time

#Since we are using an API, all that is needed to make a new movie is to instantiate a Media.Movie class with the movie title plus two integers specifying 
#the location in a list of the correct movie and the correct youtube video. 

The_Fifth_Element = Media.Movie("The Fifth Element", 0, 1)
time.sleep(1)
Ferris_Bueller = Media.Movie("Ferris Bueller's Day Off", 0, 1)
time.sleep(1)
Futurama = Media.Movie("Bender's Big Score", 0, 0)
time.sleep(1)
LOTR_FOTR = Media.Movie('The Fellowship of the Ring', 0, 0)
time.sleep(1)
Rogue_One = Media.Movie('Rogue One', 0, 0)
time.sleep(1)
XXX = Media.Movie("xXx", 0, 0) 


movies = [The_Fifth_Element, Ferris_Bueller, Futurama, LOTR_FOTR, Rogue_One, XXX] #list of movies to be passed into fresh_tomatoes.
fresh_tomatoes.open_movies_page(movies)


