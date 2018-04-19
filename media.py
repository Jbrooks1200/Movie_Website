import webbrowser

class Movie():
	"""testing out the doc pre-defined variable"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"] # class variables that do not change should be done in all caps.
	#function that initializes inputs
	def __init__ (self, movie_title, movie_storyline, poster_image, trail_youtube, rating):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trail_youtube
		self.rating = rating
		

	def show_trailer(self):#function to show movie trailer
		webbrowser.open(self.trailer_youtube_url)
	def show_poster(self):#function that produces the movie cover art
		webbrowser.open(self.poster_image_url)



