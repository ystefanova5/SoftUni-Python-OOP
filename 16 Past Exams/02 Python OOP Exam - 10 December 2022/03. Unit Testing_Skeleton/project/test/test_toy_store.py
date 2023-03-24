from project.toy_store import ToyStore

from unittest import TestCase, main


class ToyStoreTests(TestCase):
    def test_01_init(self):
        store = ToyStore()
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected, store.toy_shelf)

    def test_02_add_toy_invalid_shelf_raises(self):
        store = ToyStore()

        with self.assertRaises(Exception) as ex:
            store.add_toy("H", "Teddy Bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_03_add_toy_with_same_toy_already_on_shelf_raises(self):
        store = ToyStore()
        store.add_toy("A", "Teddy Bear")

        with self.assertRaises(Exception) as ex:
            store.add_toy("A", "Teddy Bear")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_04_add_toy_with_different_toy_already_on_shelf_raises(self):
        store = ToyStore()
        store.add_toy("A", "Teddy Bear")

        with self.assertRaises(Exception) as ex:
            store.add_toy("A", "Miss Piggy")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_05_add_toy_success(self):
        store = ToyStore()

        result = store.add_toy("A", "Teddy Bear")
        self.assertEqual({
            "A": "Teddy Bear",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, store.toy_shelf)
        self.assertEqual("Toy:Teddy Bear placed successfully!", result)

        result = store.add_toy("B", "Miss Piggy")
        self.assertEqual({
            "A": "Teddy Bear",
            "B": "Miss Piggy",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, store.toy_shelf)
        self.assertEqual("Toy:Miss Piggy placed successfully!", result)

    def test_06_remove_toy_invalid_shelf_raises(self):
        store = ToyStore()
        store.add_toy("A", "Teddy Bear")

        with self.assertRaises(Exception) as ex:
            store.remove_toy("h", "Teddy Bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_07_remove_toy_invalid_toy_raises(self):
        store = ToyStore()
        store.add_toy("A", "Teddy Bear")

        with self.assertRaises(Exception) as ex:
            store.remove_toy("A", "Miss Piggy")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_08_remove_toy_success(self):
        store = ToyStore()
        store.add_toy("A", "Teddy Bear")
        store.add_toy("B", "Miss Piggy")

        result1 = store.remove_toy("A", "Teddy Bear")
        self.assertEqual("Remove toy:Teddy Bear successfully!", result1)
        self.assertEqual(None, store.toy_shelf["A"])
        self.assertEqual("Miss Piggy", store.toy_shelf["B"])

        result2 = store.remove_toy("B", "Miss Piggy")
        self.assertEqual("Remove toy:Miss Piggy successfully!", result2)
        self.assertEqual(None, store.toy_shelf["B"])


if __name__ == "__main__":
    main()
