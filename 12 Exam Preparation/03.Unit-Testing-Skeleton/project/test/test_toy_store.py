from unittest import TestCase, main
from project.toy_store import ToyStore


class Tests(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_01_init(self):
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected_result, self.store.toy_shelf)

    def test_02_add_toy_invalid_shelf_raises(self):
        expected_result = "Shelf doesn't exist!"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("a", "Teddy Bear")

        self.assertEqual(expected_result, str(ex.exception))

    def test_03_add_toy_if_it_exists_on_shelf_raises(self):
        self.store.add_toy("A", "Teddy Bear")
        expected_result = "Toy is already in shelf!"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Teddy Bear")

        self.assertEqual(expected_result, str(ex.exception))

    def test_04_add_toy_if_shelf_is_occupied_raises(self):
        self.store.add_toy("A", "Teddy Bear")
        expected_result = "Shelf is already taken!"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Miss Piggy")

        self.assertEqual(expected_result, str(ex.exception))

    def test_05_add_toy_success(self):
        expected_result = "Toy:Teddy Bear placed successfully!"
        expected_result2 = {
            "A": "Teddy Bear",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        result = self.store.add_toy("A", "Teddy Bear")

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_result2, self.store.toy_shelf)

    def test_06_remove_toy_invalid_shelf_raises(self):
        self.store.add_toy("A", "Teddy Bear")
        expected_result = "Shelf doesn't exist!"
        expected_result2 = {
            "A": "Teddy Bear",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("a", "Teddy Bear")

        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_result2, self.store.toy_shelf)

    def test_07_remove_toy_with_invalid_name_raises(self):
        self.store.add_toy("A", "Teddy Bear")
        self.store.add_toy("B", "Miss Piggy")
        expected_result = "Toy in that shelf doesn't exists!"
        expected_result2 = {
            "A": "Teddy Bear",
            "B": "Miss Piggy",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("B", "Teddy Bear")

        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_result2, self.store.toy_shelf)

    def test_08_remove_toy_success(self):
        self.store.add_toy("A", "Teddy Bear")
        self.store.add_toy("B", "Miss Piggy")
        expected_result = "Remove toy:Teddy Bear successfully!"
        expected_result2 = {
            "A": None,
            "B": "Miss Piggy",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        result = self.store.remove_toy("A", "Teddy Bear")

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_result2, self.store.toy_shelf)


if __name__ == "__main__":
    main()
