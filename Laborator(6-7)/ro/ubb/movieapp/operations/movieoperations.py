from ro.ubb.movieapp.domain.movieentity import Movie

class MovieOperations:
    def __init__(self):
        self.__all_movies = []

    @property
    def all_movies(self):
        return self.__all_movies

    def find_by_id(self, movie_id):
        for movie in self.__all_movies:
            if movie.movie_id == movie_id:
                return movie
        else:
            return None


    def add_movie(self, movie_id, title, description, genre):
        if self.find_by_id(movie_id) is not None:
            raise ValueError("Movie with this id already exists")
        else:
            movie = Movie()
            movie.movie_id = movie_id
            movie.title = title
            movie.description = description
            movie.genre = genre
            self.__all_movies.append(movie)

    # this function does not work because movie is a NoneType, and it does not have attributes to be changed
    # def add_movie(self, movie_id, title, description, genre):
    #     movie = self.find_by_id(movie_id)
    #     if movie is not None:
    #         raise ValueError("Movie already exists")
    #     else:
    #         if title is not None:
    #             movie.title = title
    #         if description is not None:
    #             movie.description = description
    #         if genre is not None:
    #             movie.genre = genre
    #     self.__all_movies.append(movie)

    def read_all_movies(self):
        if not self.__all_movies:
            raise ValueError("No movies added.")
        else:
            return self.__all_movies

    # def delete_movie(self, movie_id):
    #     for movie in self.__all_movies:
    #         if self.find_by_id(movie_id) is None:
    #             raise ValueError("Movie with this id does not exist")
    #         else:
    #             self.__all_movies.remove(movie)

    def delete_movie(self, movie_id):
        movie = self.find_by_id(movie_id)
        if movie is None:
            raise ValueError("Movie with this id does not exist.")
        self.__all_movies.remove(movie)

    # def update_movie(self, movie_id, title = None, description = None, genre = None):
    #     if self.find_by_id(movie_id) is not None:
    #          for movie in self.__all_movies:
    #              if movie.id == movie_id:
    #                 if title: movie.title = title
    #                 if description: movie.description = description
    #                 if genre: movie.genre = genre
    #     return ValueError("Movie with this id does not exist")

    def update_movie(self, movie_id, title=None, description=None, genre=None):
        movie = self.find_by_id(movie_id)
        if movie is None:
            raise ValueError("Movie with this id does not exist.")

        if title is not None:
            movie.title = title
        if description is not None:
            movie.description = description
        if genre is not None:
            movie.genre = genre

