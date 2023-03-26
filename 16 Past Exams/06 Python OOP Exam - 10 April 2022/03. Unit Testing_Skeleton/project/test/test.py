from project.movie import Movie
from unittest import TestCase, main


class Tests(TestCase):
    def test_01_init(self):
        movie = Movie("The Godfather", 1972, 9.2)

        self.assertEqual("The Godfather", movie.name)
        self.assertEqual(1972, movie.year)
        self.assertEqual(9.2, movie.rating)
        self.assertEqual([], movie.actors)

    def test_02_set_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie("", 1972, 9.2)

        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_03_invalid_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie("The Godfather", 1886, 9.2)

        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_04_add_valid_actor(self):
        movie = Movie("The Godfather", 1972, 9.2)

        movie.add_actor("Marlon Brando")
        movie.add_actor("Al Pacino")

        self.assertEqual(["Marlon Brando", "Al Pacino"], movie.actors)

    def test_05_add_invalid_actor_message(self):
        movie = Movie("The Godfather", 1972, 9.2)
        movie.add_actor("Marlon Brando")
        movie.add_actor("Al Pacino")

        result = movie.add_actor("Al Pacino")
        self.assertEqual("Al Pacino is already added in the list of actors!", result)
        self.assertEqual(["Marlon Brando", "Al Pacino"], movie.actors)

    def test_06_greater_than(self):
        movie = Movie("The Godfather", 1972, 9.2)
        other_movie = Movie("Fight Club", 1999, 8.7)

        result = movie > other_movie
        self.assertEqual('"The Godfather" is better than "Fight Club"', result)

    def test_07_greater_than(self):
        movie = Movie("The Godfather", 1972, 9.2)
        other_movie = Movie("The Shawshank Redemption", 1994, 9.21)

        result = movie > other_movie
        self.assertEqual('"The Shawshank Redemption" is better than "The Godfather"', result)

    def test_08_repr(self):
        movie = Movie("The Godfather", 1972, 9.2)
        movie.add_actor("Marlon Brando")
        movie.add_actor("Al Pacino")
        movie.add_actor("Diane Keaton")

        result = repr(movie)
        expected_result = "Name: The Godfather\n" \
                          "Year of Release: 1972\n" \
                          "Rating: 9.20\n" \
                          "Cast: Marlon Brando, Al Pacino, Diane Keaton"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
