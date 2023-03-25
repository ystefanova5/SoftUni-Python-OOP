from project.plantation import Plantation

from unittest import TestCase, main


class Tests(TestCase):
    def test_01_init(self):
        plantation = Plantation(10)

        self.assertEqual(10, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_02_set_invalid_size_raises(self):
        plantation = Plantation(10)
        with self.assertRaises(ValueError) as ex:
            plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_03_hire_valid_worker(self):
        plantation = Plantation(10)

        result = plantation.hire_worker("Boris")

        self.assertEqual("Boris successfully hired.", result)
        self.assertEqual(["Boris"], plantation.workers)

    def test_04_hire_invalid_worker_raises(self):
        plantation = Plantation(10)
        plantation.hire_worker("Boris")
        plantation.hire_worker("Ivan")

        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker("Boris")

        self.assertEqual("Worker already hired!", str(ex.exception))
        self.assertEqual(["Boris", "Ivan"], plantation.workers)

    def test_05_len(self):
        plantation = Plantation(10)
        plantation.plants["Boris"] = ["Corn", "Spelt"]
        plantation.plants["Ivan"] = ["Barley"]

        self.assertEqual(3, len(plantation))

    def test_06_planting_invalid_worker_raises(self):
        plantation = Plantation(10)
        plantation.hire_worker("Boris")

        with self.assertRaises(ValueError) as ex:
            plantation.planting("Ivan", "Barley")

        self.assertEqual("Worker with name Ivan is not hired!", str(ex.exception))

    def test_07_planting_if_plantation_is_full_raises(self):
        plantation = Plantation(1)
        plantation.hire_worker("Boris")
        plantation.planting("Boris", "Corn")

        with self.assertRaises(ValueError) as ex:
            plantation.planting("Boris", "Spelt")

        self.assertEqual("The plantation is full!", str(ex.exception))
    def test_08_planting_success(self):
        plantation = Plantation(10)
        plantation.hire_worker("Boris")
        plantation.hire_worker("Ivan")

        result_first = plantation.planting("Boris", "Spelt")
        result_second = plantation.planting("Boris", "Corn")
        result_third = plantation.planting("Ivan", "Barley")

        self.assertEqual("Boris planted it's first Spelt.", result_first)
        self.assertEqual("Boris planted Corn.", result_second)
        self.assertEqual("Ivan planted it's first Barley.", result_third)
        self.assertEqual({'Boris': ['Spelt', 'Corn'], 'Ivan': ['Barley']}, plantation.plants)

    def test_09_str_return_correct_data(self):
        plantation = Plantation(10)
        plantation.hire_worker("Boris")
        plantation.hire_worker("Ivan")
        plantation.planting("Boris", "Spelt")
        plantation.planting("Boris", "Corn")
        plantation.planting("Ivan", "Barley")

        expected_result = "Plantation size: 10\n" \
                          "Boris, Ivan\n" \
                          "Boris planted: Spelt, Corn\n" \
                          "Ivan planted: Barley"

        self.assertEqual(expected_result, str(plantation))

    def test_10_repr(self):
        plantation = Plantation(10)
        plantation.hire_worker("Boris")
        plantation.hire_worker("Ivan")

        result_first = plantation.planting("Boris", "Spelt")
        result_second = plantation.planting("Boris", "Corn")
        result_third = plantation.planting("Ivan", "Barley")

        expected_result = "Size: 10\nWorkers: Boris, Ivan"

        self.assertEqual(expected_result, plantation.__repr__())

if __name__ == "__main__":
    main()
