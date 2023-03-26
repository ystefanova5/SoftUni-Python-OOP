from project.library import Library

from unittest import TestCase, main


class Tests(TestCase):
    def test_01_init(self):
        library = Library("School Library")

        self.assertEqual("School Library", library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_02_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            library = Library("")

        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_03_add_book(self):
        library = Library("School Library")

        library.add_book("J. R. R. Tolkien", "The Hobbit")
        expected_result = {"J. R. R. Tolkien": ["The Hobbit"]}

        self.assertEqual(expected_result, library.books_by_authors)

        library.add_book("J. R. R. Tolkien", "The Hobbit")
        expected_result = {"J. R. R. Tolkien": ["The Hobbit"]}

        self.assertEqual(expected_result, library.books_by_authors)

        library.add_book("J. R. R. Tolkien", "The Silmarillion")
        expected_result = {"J. R. R. Tolkien": ["The Hobbit", "The Silmarillion"]}

        self.assertEqual(expected_result, library.books_by_authors)

        library.add_book("Test", "The Hobbit")
        expected_result = {"J. R. R. Tolkien": ["The Hobbit", "The Silmarillion"], "Test": ["The Hobbit"]}

        self.assertEqual(expected_result, library.books_by_authors)

    def test_04_add_reader_success(self):
        library = Library("School Library")

        library.add_reader("Boris")

        self.assertEqual({"Boris": []}, library.readers)

    def test_05_add_existing_reader(self):
        library = Library("School Library")
        library.add_reader("Boris")

        result = library.add_reader("Boris")
        self.assertEqual("Boris is already registered in the School Library library.", result)

    def test_06_rent_book_invalid_reader_name_message(self):
        library = Library("School Library")
        library.add_book("J. R. R. Tolkien", "The Hobbit")
        library.add_reader("Boris")

        result = library.rent_book("Ivan", "J. R. R. Tolkien", "The Hobbit")
        self.assertEqual("Ivan is not registered in the School Library Library.", result)

    def test_07_rent_book_invalid_author_message(self):
        library = Library("School Library")
        library.add_book("J. R. R. Tolkien", "The Hobbit")
        library.add_reader("Boris")

        result = library.rent_book("Boris", "Wrong Name", "The Hobbit")
        self.assertEqual("School Library Library does not have any Wrong Name's books.", result)

    def test_08_rent_book_invalid_title(self):
        library = Library("School Library")
        library.add_book("J. R. R. Tolkien", "The Hobbit")
        library.add_reader("Boris")

        result = library.rent_book("Boris", "J. R. R. Tolkien", "The Silmarillion")
        self.assertEqual("""School Library Library does not have J. R. R. Tolkien's "The Silmarillion".""", result)

    def test_09_rent_book_success(self):
        library = Library("School Library")
        library.add_book("J. R. R. Tolkien", "The Hobbit")
        library.add_book("J. R. R. Tolkien", "The Silmarillion")
        library.add_reader("Boris")

        library.rent_book("Boris", "J. R. R. Tolkien", "The Hobbit")

        self.assertEqual({'Boris': [{'J. R. R. Tolkien': 'The Hobbit'}]}, library.readers)
        self.assertEqual({'J. R. R. Tolkien': ['The Silmarillion']}, library.books_by_authors)


if __name__ == "__main__":
    main()
