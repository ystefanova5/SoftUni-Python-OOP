from project.truck_driver import TruckDriver
from unittest import TestCase, main


class Tests(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Boris", 1.50)

    def test_01_init(self):
        self.assertEqual("Boris", self.driver.name)
        self.assertEqual(1.50, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_02_negative_earned_money_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -1

        self.assertEqual("Boris went bankrupt.", str(ex.exception))

    def test_03_add_cargo_offer_for_existing_location_raises(self):
        self.driver.available_cargos["Sofia"] = 450

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 430)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))
        self.assertEqual({"Sofia": 450}, self.driver.available_cargos)

    def test_04_add_cargo_offer_success(self):
        expected_result = "Cargo for 450 to Sofia was added as an offer."
        result = self.driver.add_cargo_offer("Sofia", 450)

        self.assertEqual(expected_result, result)
        self.assertEqual({"Sofia": 450}, self.driver.available_cargos)

        expected_result = "Cargo for 120 to Burgas was added as an offer."
        result = self.driver.add_cargo_offer("Burgas", 120)

        self.assertEqual(expected_result, result)
        self.assertEqual({"Sofia": 450, "Burgas": 120}, self.driver.available_cargos)

    def test_05_drive_best_cargo_offer_no_offers_raises(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_06_drive_best_cargo_offer_success(self):
        self.driver.add_cargo_offer("Sofia", 450)
        self.driver.add_cargo_offer("Burgas", 120)

        result = self.driver.drive_best_cargo_offer()
        expected_result = "Boris is driving 450 to Sofia."

        self.assertEqual(expected_result, result)
        self.assertEqual(655, self.driver.earned_money)
        self.assertEqual(450, self.driver.miles)

        self.driver.add_cargo_offer("Hanoi", 10100)

        result = self.driver.drive_best_cargo_offer()
        expected_result = "Boris is driving 10100 to Hanoi."

        self.assertEqual(expected_result, result)
        self.assertEqual(4055, self.driver.earned_money)
        self.assertEqual(10550, self.driver.miles)

    def test_07_check_for_activities(self):
        self.driver.earned_money = 20000
        self.driver.check_for_activities(10500)

        self.assertEqual(7710, self.driver.earned_money)

    def test_08_repr(self):
        self.driver.add_cargo_offer("Sofia", 450)
        self.driver.add_cargo_offer("Burgas", 120)
        self.driver.drive_best_cargo_offer()

        result = repr(self.driver)
        expected_result = "Boris has 450 miles behind his back."

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
