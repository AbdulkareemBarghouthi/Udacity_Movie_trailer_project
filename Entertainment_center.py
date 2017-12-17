import media
import fresh_tomatoes
import webbrowser

# Those are the instances for the movie class. each instance contains Movie title,a url poster and a url to the trailer on youtube`
forrest_gump = media.Movie("Forrest Gump",
	"https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
	"https://www.youtube.com/watch?v=bLvqoHBptjg")

Mr_nobody = media.Movie("Mr. Nobody",
	"https://upload.wikimedia.org/wikipedia/en/3/32/Mr._Nobody_%28film_poster%29.jpg",
	"https://www.youtube.com/watch?v=vXf3gVYXlHg")

dumb_and_dumber = media.Movie("Dumb and dumber",
	"https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
	"https://www.youtube.com/watch?v=l13yPhimE3o")

cheech_and_chong = media.Movie("Cheech and Chong: next movie",
	"https://upload.wikimedia.org/wikipedia/en/e/ed/Cheech_%26_Chong%27s_Next_Movie.jpg",
	"https://www.youtube.com/watch?v=RslItmJlPcY")

the_invention_of_lying = media.Movie("The invention of lying",
	"https://upload.wikimedia.org/wikipedia/en/2/2b/Invention_of_lying_ver2.jpg",
	"https://www.youtube.com/watch?v=vn71hYvyqCA")

napoleon_dynamite = media.Movie("Napoleon Dynamite",
	"https://upload.wikimedia.org/wikipedia/en/8/87/Napoleon_dynamite_post.jpg",
	"https://www.youtube.com/watch?v=ZHDi_AnqwN4")

movies= [forrest_gump,Mr_nobody,dumb_and_dumber,cheech_and_chong,the_invention_of_lying,napoleon_dynamite]

fresh_tomatoes.open_movies_page(movies)
