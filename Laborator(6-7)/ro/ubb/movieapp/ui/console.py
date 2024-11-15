class Console:
    def __init__(self, movie_operations):
        self.__movie_operations = movie_operations

    @property
    def movie_operations(self):
        return self.__movie_operations

    @staticmethod
    def show_menu():
        print("1. Add a new movie: ")
        print("2. Delete a movie: ")
        print("3. Show the movies: ")
        print("4. Update Movie: ")
        print("5. Quit: ")

    def run_menu(self):
        while True:
            self.show_menu()
            command = input("Please enter an option from the menu above: ")
            if command == "1":
                self.ui_add_movie()
            elif command == "2":
                self.ui_delete_movie()
            elif command == "3":
                self.ui_read_movie()
            elif command == "4":
                self.ui_update_movie()
            elif command == "5":
                print("Thank you for using the application.")
                break
            else:
                print("Invalid input! Insert an integer from the menu above.")

    def ui_add_movie(self):
        try:
            movie_id = int(input("Please enter the movie ID: "))
            title = input("Please enter the movie title: ")
            description = input("Please enter the movie description: ")
            genre = input("Please enter the movie genre: ")
            self.movie_operations.add_movie(movie_id, title, description, genre)
        except ValueError:
            print("Please enter valid inputs: ")

    def ui_delete_movie(self):
        try:
            movie_id = int(input("Please enter the movie ID: "))
            self.movie_operations.delete_movie(movie_id)
        except ValueError:
            print("Please enter valid inputs: ")

    def ui_read_movie(self):
        movies = self.movie_operations.read_all_movies()
        if not movies or len(movies) == 0:
            print("No movies found.")
        for movie in movies:
            print(movie)

    def ui_update_movie(self):
        try:
            id = int(input("Please enter the movie ID: "))
            title = input("Please enter a new movie title: ")
            description = input("Please enter a new movie description: ")
            genre = input("Please enter a new movie genre: ")
            self.movie_operations.update_movie(id, title, description, genre)
        except ValueError:
            print("Please enter valid inputs: ")
