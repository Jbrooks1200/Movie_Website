import media #importing the media.py subfolder in the media main folder.
import fresh_tomatoes 


def main():
	super_troopers2 = media.Movie("Super Troopers2","A comedy about 5 highway partol officers in a dispute with Canada.",
							"https://upload.wikimedia.org/wikipedia/en/3/30/Super_Troopers_2_poster.png",
							"https://www.youtube.com/watch?v=H2ehN-WeGAo",
							media.Movie.VALID_RATINGS[3])


	snatch = media.Movie("Snatch", "A english comedy about an 86 caret diamond.", 
						 "https://upload.wikimedia.org/wikipedia/en/a/a7/Snatch_ver4.jpg",
						 "https://www.youtube.com/watch?v=9Jar2XkBboo",
						 media.Movie.VALID_RATINGS[3])


	deadpool = media.Movie("Deadpool", "A superhero taking out bad guys.", 
						   "https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg",
						   "https://www.youtube.com/watch?v=_aov5GCcTVE",
						   media.Movie.VALID_RATINGS[3])


	out_cold = media.Movie("Out cold", "A group of snowboarders save their mountian from being sold.",
						  "https://upload.wikimedia.org/wikipedia/en/5/5a/Out_cold_poster.jpg",
						  "https://www.youtube.com/watch?v=4_7nVDz0tUE&t=58s",
						  media.Movie.VALID_RATINGS[2])


	john_wick = media.Movie("John Wick", "John Wick advenges people who killed his dog.",
							"https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
							"https://www.youtube.com/watch?v=2AUmvWm5ZDQ",
							media.Movie.VALID_RATINGS[3])


	cutting_edge = media.Movie("Cutting Edge", "A story about a hockey playeer that does figure skating.",
							   "https://upload.wikimedia.org/wikipedia/en/b/be/The_Cutting_Edge_Poster.jpg",
							   "https://www.youtube.com/watch?v=QratAk_OUuc",
							   media.Movie.VALID_RATINGS[1])

	movies = [super_troopers2, snatch, deadpool, out_cold, john_wick, cutting_edge]

	fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
	main()

	
	#print (media.Movie.VALID_RATINGS)
	#print media.Movie.__doc__
#print (deadpool.title)