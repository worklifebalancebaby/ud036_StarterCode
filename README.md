#Movie Trailer Website
This is a python program that launches a page in your web browser displaying movie posters as links to pop-up windows showing the movie trailer. The program uses bootstrap and and html format to create this web browser page. 
#Install
- you will need to have python installed on your computer to run this program
- the `entertainment_center.py` file contains the instances of the class Movie that will be displayed on the web page. 
	- the Movie class data structure is described in `media.py`. It's attributes are the movie title, the url to the movie box art, and the url to the youtube trailer. 
	- therefore, to change the menu of movies displayed on the web page you will have to go into the `entertainment_center.py` file and manually type out or delete instances of `media.Movie()`.
#Run
Launch the web page by running the `entertainment_center.py` module. The last line in the module: 
`fresh_tomatoes.open_movies_page(movies)`
contains the `open_movies_page()` function which will take in the list of movies and generate the HTML file as a web page in a new browser window.  
