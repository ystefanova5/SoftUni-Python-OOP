from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTests(TestCase):
    def test_01_class_initializes_with_correct_data(self):
        driver = TruckDriver("Boris", 5)

        self.assertEqual("Boris", driver.name)
        self.assertEqual(5, driver.money_per_mile)
        self.assertEqual({}, driver.available_cargos)
        self.assertEqual(0, driver.earned_money)
        self.assertEqual(0, driver.miles)

    def test_02_negative_earned_money_raises(self):
        driver = TruckDriver("Boris", 5)
        expected_message = "Boris went bankrupt."

        with self.assertRaises(ValueError) as ex:
            driver.earned_money = -10

        self.assertEqual(expected_message, str(ex.exception))

    def test_03_add_cargo_offer_for_existing_location_raises(self):
        driver = TruckDriver("Boris", 5)
        driver.available_cargos["Rome"] = 1000
        expected_message = "Cargo offer is already added."

        self.assertEqual({"Rome": 1000}, driver.available_cargos)

        with self.assertRaises(Exception) as ex:
            driver.add_cargo_offer("Rome", 1100)

        self.assertEqual(expected_message, str(ex.exception))

    def test_04_add_cargo_offer_adds_cargo_and_returns_message(self):
        driver = TruckDriver("Boris", 5)
        driver.available_cargos["Rome"] = 1000
        expected_message = "Cargo for 900 to Venice was added as an offer."

        result = driver.add_cargo_offer("Venice", 900)

        self.assertEqual({"Rome": 1000, "Venice": 900}, driver.available_cargos)
        self.assertEqual(expected_message, result)

    def test_05_drive_best_cargo_offer_with_no_offers_raises(self):
        driver = TruckDriver("Boris", 5)
        expected_message = "There are no offers available."

        result = driver.drive_best_cargo_offer()
        self.assertEqual(expected_message, result)

    def test_06_check_for_activities_calculates_correct_values(self):
        driver = TruckDriver("Boris", 5)
        driver.earned_money = 20000
        driver.check_for_activities(10240)

        self.assertEqual(8250, driver.earned_money)

    def test_07_drive_best_cargo_offer_with_valid_data(self):
        driver = TruckDriver("Boris", 5)
        driver.miles = 1000
        driver.earned_money = 1750
        driver.add_cargo_offer("Rome", 10000)
        driver.add_cargo_offer("Venice", 9900)
        expected_message = "Boris is driving 10000 to Rome."

        result = driver.drive_best_cargo_offer()
        self.assertEqual(expected_message, result)

        self.assertEqual(40000, driver.earned_money)
        self.assertEqual(11000, driver.miles)

        driver.add_cargo_offer("Naples", 12000)
        driver.drive_best_cargo_offer()

        self.assertEqual(87000, driver.earned_money)
        self.assertEqual(23000, driver.miles)

    def test_08_repr_returns_valid_data(self):
        driver = TruckDriver("Boris", 5)
        self.assertEqual("Boris has 0 miles behind his back.", str(driver))

        driver.add_cargo_offer("Rome", 10000)
        driver.drive_best_cargo_offer()
        self.assertEqual("Boris has 10000 miles behind his back.", str(driver))

        driver.add_cargo_offer("Venice", 10900)
        driver.drive_best_cargo_offer()
        self.assertEqual("Boris has 20900 miles behind his back.", str(driver))


if __name__ == "__main__":
    main()
