"""

@author: Rad George-Ciprian

This is a Movie Manager Application. This app can:
I1: Create a movie object/entity and load it in a list of movie
I2: Display the list of movies
I3: Delete a specified movie from the list
I4: Update a movie from the list

This code:

I5: has been tested completely
I6: is using a menu-based UI

"""

from ro.ubb.movieapp.operations.movieoperations import MovieOperations
from ro.ubb.movieapp.ui.console import Console

if __name__ == '__main__':

    movie_operations = MovieOperations()
    console = Console(movie_operations)
    console.run_menu()