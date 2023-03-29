from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class Tests(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Lidl", 200)
        self.other_cart = ShoppingCart("Parkmart", 110)

    def test_01_init(self):
        self.assertEqual("Lidl", self.cart.shop_name)
        self.assertEqual(200, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_02_invalid_name_raises(self):
        expected_message = "Shop must contain only letters and must start with capital letter!"
        with self.assertRaises(ValueError) as ex:
            self.cart.shop_name = "Lidl1"

        self.assertEqual(expected_message, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.cart.shop_name = "lidl"

        self.assertEqual(expected_message, str(ex.exception))

    def test_03_add_to_cart_over_100_raises(self):
        expected_message = "Product Cheese cost too much!"
        with self.assertRaises(ValueError) as ex:
            self.cart.add_to_cart("Cheese", 100)

        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual({}, self.cart.products)

        expected_message = "Product Ham cost too much!"
        with self.assertRaises(ValueError) as ex:
            self.cart.add_to_cart("Ham", 101)

        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual({}, self.cart.products)

    def test_04_add_to_cart_success(self):
        expected_message = "Cheese product was successfully added to the cart!"
        result = self.cart.add_to_cart("Cheese", 10)
        self.cart.add_to_cart("Ham", 12)
        self.cart.add_to_cart("Ham", 15)

        self.assertEqual(expected_message, result)
        self.assertEqual({"Cheese": 10, "Ham": 15}, self.cart.products)

    def test_05_remove_from_cart_invalid_product_raises(self):
        expected_message = "No product with name Ham in the cart!"
        self.cart.add_to_cart("Cheese", 10)

        with self.assertRaises(ValueError) as ex:
            self.cart.remove_from_cart("Ham")

        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual({"Cheese": 10}, self.cart.products)

    def test_06_remove_from_cart_success(self):
        self.cart.add_to_cart("Cheese", 10)
        self.cart.add_to_cart("Ham", 12)

        result = self.cart.remove_from_cart("Cheese")
        expected_result = "Product Cheese was successfully removed from the cart!"

        self.assertEqual(expected_result, result)
        self.assertEqual({"Ham": 12}, self.cart.products)

    def test_07_add_method(self):
        self.cart.add_to_cart("Cheese", 10)
        self.other_cart.add_to_cart("Bread", 2)
        self.other_cart.add_to_cart("Ham", 15)

        merged_cart = self.cart + self.other_cart

        self.assertEqual("LidlParkmart", merged_cart.shop_name)
        self.assertEqual(310, merged_cart.budget)
        self.assertEqual({"Cheese": 10, "Bread": 2, "Ham": 15}, merged_cart.products)

    def test_08_buy_product_insufficient_budget_raises(self):
        expected_result = "Not enough money to buy the products! Over budget with 4.50lv!"
        self.cart.budget = 20.50
        self.cart.add_to_cart("Cheese", 10)
        self.cart.add_to_cart("Ham", 15)

        with self.assertRaises(ValueError) as ex:
            self.cart.buy_products()

        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(20.50, self.cart.budget)

    def test_09_buy_products_success(self):
        expected_result = "Products were successfully bought! Total cost: 25.00lv."
        self.cart.add_to_cart("Cheese", 10)
        self.cart.add_to_cart("Ham", 15)

        result = self.cart.buy_products()
        self.assertEqual(expected_result, result)

        self.cart.budget = 25
        result = self.cart.buy_products()
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
