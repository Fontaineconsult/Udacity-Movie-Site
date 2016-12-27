# Welcome to the Media module.
# This module hosts the class constructor needed to instantiate the movie objects used by fresh_tomatoes.py

class Video():
	"""
	
	The tmdb3 module is an API that queries movie data from the database, 'themovieDB.org'.
	The parent video class's primary purposed is to contain the searchMovie function.
	The title variable is used as a search keyword for the searchMovie function. Searching a 
	movie usually returns a list of multiple titles. The title_modifier variable is used to
	specificy which search result to use. 

	Make sure to have tmdb3 installed before use. 

	"""
	

	def __init__(self, title, title_modifier, trailer_modifier):
		from tmdb3 import set_key 
		from tmdb3 import set_cache
		from tmdb3 import searchMovie
		from tmdb3 import Movie, Collection, Person, Series
		set_cache('null')
		set_key('a7b2a24af9fbe91fc6003d4d111b3b37')
		self.search_results = searchMovie(title) #self.search_results is a list returned by the searchMovie function after passing in the title variable. 
		self.video_id = self.search_results[title_modifier].id # to use any of the provided methods from tmdb3 we need to get the movie's ID.
		self.title = Movie(self.video_id).title # method to return movies title.

class Movie(Video):

	""" Store movie related info in this class"""
	
	def __init__(self, title, title_modifier, trailer_modifier):
		Video.__init__(self, title, title_modifier, trailer_modifier)
		# was having trouble with inhereting the imported tmbd3 module from class video. So reimported it. 
		from tmdb3 import set_key
		from tmdb3 import set_cache
		from tmdb3 import searchMovie
		from tmdb3 import Movie, Collection, Person, Series
		set_cache('null')
		set_key('a7b2a24af9fbe91fc6003d4d111b3b37')
		self.tagline = Movie(self.video_id).tagline # returns short 'tagline' description of movie.
		self.storyline = Movie(self.video_id).overview # returns longer description of movie.
		self.runtime = Movie(self.video_id).runtime # total runtime in minutes
		self.poster_image_url = Movie(self.video_id).poster.geturl() # returns url of .jpg of the movie poster
		self.trailer_youtube_url = Movie(self.video_id).youtube_trailers[trailer_modifier].geturl() # youtube trailer. 
		self.release_date = Movie(self.video_id).releasedate