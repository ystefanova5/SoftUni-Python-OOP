from project.bookstore import Bookstore
from unittest import TestCase, main


class Tests(TestCase):
    def test_01_init(self):
        bookstore = Bookstore(10)

        self.assertEqual(10, bookstore.books_limit)
        self.assertEqual({}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore._Bookstore__total_sold_books)

    def test_02_set_valid_book_limit(self):
        bookstore = Bookstore(10)
        bookstore.books_limit = 1

        self.assertEqual(1, bookstore.books_limit)

    def test_03_set_invalid_book_limit_raises(self):
        bookstore = Bookstore(10)

        with self.assertRaises(ValueError) as ex:
            bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            bookstore.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))

    def test_04_len_returns_correct_value(self):
        bookstore = Bookstore(10)
        bookstore.availability_in_store_by_book_titles = {
            "The Hobbit": 2,
            "The Lord of the Rings": 3,
            "The Silmarillion": 1}

        self.assertEqual(6, len(bookstore))

    def test_05_receive_book_if_not_enough_space(self):
        bookstore = Bookstore(10)

        with self.assertRaises(Exception) as ex:
            bookstore.receive_book("The Hobbit", 11)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_06_receive_book_if_enough_space(self):
        bookstore = Bookstore(10)
        bookstore.receive_book("The Hobbit", 2)
        bookstore.receive_book("The Hobbit", 2)
        bookstore.receive_book("The Lord of the Rings", 3)

        expected_availability = {"The Hobbit": 4, "The Lord of the Rings": 3}

        self.assertEqual(expected_availability, bookstore.availability_in_store_by_book_titles)

    def test_07_receive_book_returns_correct_message(self):
        bookstore = Bookstore(10)
        bookstore.receive_book("The Hobbit", 2)

        result = bookstore.receive_book("The Hobbit", 3)
        expected_message = "5 copies of The Hobbit are available in the bookstore."

        self.assertEqual(expected_message, result)

    def test_08_sell_invalid_book_raises(self):
        bookstore = Bookstore(10)
        bookstore.receive_book("The Hobbit", 2)

        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("The Silmarillion", 2)

        self.assertEqual("Book The Silmarillion doesn't exist!", str(ex.exception))

    def test_09_sell_book_with_insufficient_quantity_raise(self):
        bookstore = Bookstore(10)
        bookstore.receive_book("The Hobbit", 2)

        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("The Hobbit", 3)

        self.assertEqual("The Hobbit has not enough copies to sell. Left: 2", str(ex.exception))

    def test_10_sell_book_success(self):
        bookstore = Bookstore(10)
        bookstore.receive_book("The Hobbit", 3)

        result = bookstore.sell_book("The Hobbit", 1)
        bookstore.sell_book("The Hobbit", 1)
        bookstore.sell_book("The Hobbit", 1)

        self.assertEqual("Sold 1 copies of The Hobbit", result)
        self.assertEqual({"The Hobbit": 0}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, bookstore.total_sold_books)

    def test_11_str_method_returns_correct_data(self):
        bookstore = Bookstore(10)
        bookstore.receive_book("The Hobbit", 4)
        bookstore.receive_book("The Lord of the Rings", 3)
        bookstore.receive_book("The Silmarillion", 2)
        bookstore.sell_book("The Hobbit", 1)
        bookstore.sell_book("The Lord of the Rings", 1)
        bookstore.sell_book("The Silmarillion", 2)

        expected_result = "Total sold books: 4\n" \
                          "Current availability: 5\n" \
                          " - The Hobbit: 3 copies\n" \
                          " - The Lord of the Rings: 2 copies\n" \
                          " - The Silmarillion: 0 copies"

        self.assertEqual(expected_result, str(bookstore))


if __name__ == "__main__":
    main()
