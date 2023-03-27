from unittest import TestCase, main

from project.train.train import Train


class Tests(TestCase):
    def test_01_init(self):
        train = Train("Express", 100)

        self.assertEqual("Express", train.name)
        self.assertEqual(100, train.capacity)
        self.assertEqual([], train.passengers)
        self.assertEqual("Train is full", train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", train.PASSENGER_ADD)
        self.assertEqual("Removed {}", train.PASSENGER_REMOVED)
        self.assertEqual(0, train.ZERO_CAPACITY)

    def test_02_add_passenger_if_train_full_raises(self):
        train = Train("Express", 1)
        train.passengers.append("Boris")

        with self.assertRaises(ValueError) as ex:
            train.add("Ivan")

        self.assertEqual("Train is full", str(ex.exception))
        self.assertEqual(["Boris"], train.passengers)

    def test_03_add_invalid_passenger(self):
        train = Train("Express", 100)
        train.passengers.append("Boris")

        with self.assertRaises(ValueError) as ex:
            train.add("Boris")

        self.assertEqual("Passenger Boris Exists", str(ex.exception))
        self.assertEqual(["Boris"], train.passengers)

    def test_04_add_success(self):
        train = Train("Express", 100)

        result = train.add("Boris")
        self.assertEqual("Added passenger Boris", result)
        self.assertEqual(["Boris"], train.passengers)

        result = train.add("Ivan")
        self.assertEqual("Added passenger Ivan", result)
        self.assertEqual(["Boris", "Ivan"], train.passengers)

    def test_05_remove_invalid_passenger_raises(self):
        train = Train("Express", 100)
        result = train.add("Boris")

        with self.assertRaises(ValueError) as ex:
            train.remove("Ivan")

        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(["Boris"], train.passengers)

    def test_06_remove_passenger_success(self):
        train = Train("Express", 100)
        result = train.add("Boris")
        result = train.add("Ivan")

        result = train.remove("Boris")

        self.assertEqual("Removed Boris", result)
        self.assertEqual(["Ivan"], train.passengers)

        result = train.remove("Ivan")

        self.assertEqual("Removed Ivan", result)
        self.assertEqual([], train.passengers)


if __name__ == "__main__":
    main()
