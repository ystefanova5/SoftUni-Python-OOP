from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    @staticmethod
    def find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def register_user(self, username: str, age: int):
        if username in [x.username for x in self.users_collection]:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if username not in [x.username for x in self.users_collection]:
            raise Exception("This user does not exist!")

        user = self.find_object(username, "username", self.users_collection)

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.find_object(username, "username", self.users_collection)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute, new_value in kwargs.items():
            if attribute == "title":
                movie.title = new_value
            elif attribute == "year":
                movie.year = new_value
            elif attribute == "age_restriction":
                movie.age_restriction = new_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.find_object(username, "username", self.users_collection)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.find_object(username, "username", self.users_collection)

        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie.title in [x.title for x in user.movies_liked]:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_object(username, "username", self.users_collection)

        if movie.title not in [x.title for x in user.movies_liked]:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        return '\n'.join(x.details() for x in sorted_movies)

    def __str__(self):
        result = []

        if self.users_collection:
            result.append(f"All users: {', '.join(x.username for x in self.users_collection)}")
        else:
            result.append("All users: No users.")

        if self.movies_collection:
            result.append(f"All movies: {', '.join(x.title for x in self.movies_collection)}")
        else:
            result.append("All movies: No movies.")

        return '\n'.join(result)
