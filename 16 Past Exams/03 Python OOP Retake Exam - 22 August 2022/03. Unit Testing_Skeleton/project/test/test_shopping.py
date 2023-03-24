from project.shopping_cart import ShoppingCart

from unittest import TestCase, main


class Tests(TestCase):
    def test_01_init(self):
        cart = ShoppingCart("Lidl", 50.50)
        self.assertEqual("Lidl", cart.shop_name)
        self.assertEqual(50.50, cart.budget)
        self.assertEqual({}, cart.products)

    def test_02_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("lidl1", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_03_add_with_price_equal_to_100_raises(self):
        cart = ShoppingCart("Lidl", 200)

        with self.assertRaises(ValueError) as ex:
            cart.add_to_cart("Cheese", 100)

        self.assertEqual("Product Cheese cost too much!", str(ex.exception))
        self.assertEqual({}, cart.products)

    def test_04_add_with_price_over_100_raises(self):
        cart = ShoppingCart("Lidl", 200)

        with self.assertRaises(ValueError) as ex:
            cart.add_to_cart("Cheese", 100.01)

        self.assertEqual("Product Cheese cost too much!", str(ex.exception))
        self.assertEqual({}, cart.products)

    def test_05_add_to_cart_valid_price(self):
        cart = ShoppingCart("Lidl", 100)

        cart.add_to_cart("Cheese", 10)
        self.assertEqual({"Cheese": 10}, cart.products)

        result = cart.add_to_cart("Bread", 2)
        self.assertEqual({"Cheese": 10, "Bread": 2}, cart.products)
        self.assertEqual("Bread product was successfully added to the cart!", result)

        cart.add_to_cart("Bread", 2.50)
        self.assertEqual({"Cheese": 10, "Bread": 2.50}, cart.products)

    def test_06_remove_invalid_product_raises(self):
        cart = ShoppingCart("Lidl", 200)
        cart.add_to_cart("Cheese", 10)

        with self.assertRaises(ValueError) as ex:
            cart.remove_from_cart("Ham")

        self.assertEqual("No product with name Ham in the cart!", str(ex.exception))

    def test_07_remove_valid_product(self):
        cart = ShoppingCart("Lidl", 200)
        cart.add_to_cart("Cheese", 10)
        cart.add_to_cart("Ham", 8)
        self.assertEqual({"Cheese": 10, "Ham": 8}, cart.products)

        result = cart.remove_from_cart("Ham")

        self.assertEqual("Product Ham was successfully removed from the cart!", result)
        self.assertEqual({"Cheese": 10}, cart.products)

    def test_08_add_two_shops(self):
        cart = ShoppingCart("Lidl", 150)
        cart.add_to_cart("Cheese", 10)
        cart.add_to_cart("Ham", 8)

        other_cart = ShoppingCart("Parkmart", 200)
        other_cart.add_to_cart("Cheese", 10)
        other_cart.add_to_cart("Bread", 3)

        new_cart = cart + other_cart
        self.assertEqual("LidlParkmart", new_cart.shop_name)
        self.assertEqual(350, new_cart.budget)
        self.assertEqual({'Cheese': 10, 'Ham': 8, 'Bread': 3}, new_cart.products)

    def test_09_buy_product_over_budget_raises(self):
        cart = ShoppingCart("Lidl", 15)
        cart.add_to_cart("Cheese", 10.20)
        cart.add_to_cart("Ham", 8)

        with self.assertRaises(ValueError) as ex:
            cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 3.20lv!", str(ex.exception))

    def test_10_buy_product_success(self):
        cart = ShoppingCart("Lidl", 100)
        cart.add_to_cart("Cheese", 10.20)
        cart.add_to_cart("Ham", 8)

        result = cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 18.20lv.", result)
        self.assertEqual({'Cheese': 10.20, 'Ham': 8}, cart.products)
        self.assertEqual(100, cart.budget)


if __name__ == "__main__":
    main()
