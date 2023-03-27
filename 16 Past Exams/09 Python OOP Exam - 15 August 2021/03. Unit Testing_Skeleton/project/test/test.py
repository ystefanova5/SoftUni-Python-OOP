from project.pet_shop import PetShop
from unittest import TestCase, main


class Tests(TestCase):
    def test_01_init(self):
        shop = PetShop("Animalia")

        self.assertEqual("Animalia", shop.name)
        self.assertEqual({}, shop.food)
        self.assertEqual([], shop.pets)

    def test_02_add_food_invalid_quantity_raises(self):
        shop = PetShop("Animalia")

        with self.assertRaises(ValueError) as ex:
            shop.add_food("Dog Food", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))
        self.assertEqual({}, shop.food)

        with self.assertRaises(ValueError) as ex:
            shop.add_food("Dog Food", -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))
        self.assertEqual({}, shop.food)

    def test_03_add_food_success(self):
        shop = PetShop("Animalia")

        result = shop.add_food("Fish Food", 10.4)
        expected_result = "Successfully added 10.40 grams of Fish Food."

        self.assertEqual(expected_result, result)
        self.assertEqual({"Fish Food": 10.4}, shop.food)

        result = shop.add_food("Fish Food", 10)
        expected_result = "Successfully added 10.00 grams of Fish Food."

        self.assertEqual(expected_result, result)
        self.assertEqual({"Fish Food": 20.4}, shop.food)

        result = shop.add_food("Bird Food", 15)
        expected_result = "Successfully added 15.00 grams of Bird Food."

        self.assertEqual(expected_result, result)
        self.assertEqual({"Fish Food": 20.4, "Bird Food": 15}, shop.food)

    def test_04_add_pet_success(self):
        shop = PetShop("Animalia")

        result = shop.add_pet("Jackie")
        expected_message = "Successfully added Jackie."

        self.assertEqual(expected_message, result)
        self.assertEqual(["Jackie"], shop.pets)

    def test_05_add_invalid_pet_raises(self):
        shop = PetShop("Animalia")
        shop.add_pet("Jackie")

        with self.assertRaises(Exception) as ex:
            shop.add_pet("Jackie")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(["Jackie"], shop.pets)

    def test_06_feed_pet_with_invalid_name_raises(self):
        shop = PetShop("Animalia")
        shop.add_food("Dog Food", 200)
        shop.add_pet("Jackie")

        with self.assertRaises(Exception) as ex:
            shop.feed_pet("Dog Food", "Charlie")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_07_feed_pet_with_invalid_food_raises(self):
        shop = PetShop("Animalia")
        shop.add_food("Fish Food", 200)
        shop.add_pet("Jackie")

        result = shop.feed_pet("Dog Food", "Jackie")

        self.assertEqual("You do not have Dog Food", result)

    def test_08_feed_with_available_less_than_100_adds_food_and_returns_message(self):
        shop = PetShop("Animalia")
        shop.add_food("Dog Food", 99)
        shop.add_pet("Jackie")

        result = shop.feed_pet("Dog Food", "Jackie")

        self.assertEqual("Adding food...", result)
        self.assertEqual({"Dog Food": 1099}, shop.food)

    def test_09_feed_pet_success(self):
        shop = PetShop("Animalia")
        shop.add_food("Dog Food", 100)
        shop.add_pet("Jackie")

        result = shop.feed_pet("Dog Food", "Jackie")

        self.assertEqual("Jackie was successfully fed", result)
        self.assertEqual({"Dog Food": 0}, shop.food)

    def test_10_repr(self):
        shop = PetShop("Animalia")
        shop.add_pet("Jackie")
        shop.add_pet("Charlie")

        result = repr(shop)
        expected_result = "Shop Animalia:\nPets: Jackie, Charlie"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
