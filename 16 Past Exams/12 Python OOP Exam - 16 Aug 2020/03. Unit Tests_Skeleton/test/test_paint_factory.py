from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class Tests(TestCase):
    def test_01_init(self):
        factory = PaintFactory("Rainbow", 100)

        self.assertEqual("Rainbow", factory.name)
        self.assertEqual(100, factory.capacity)
        self.assertEqual({}, factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], factory.valid_ingredients)

    def test_02_can_add(self):
        factory = PaintFactory("Rainbow", 100)
        factory.ingredients = {"white": 90}

        result = factory.can_add(11)
        self.assertFalse(result)

        result = factory.can_add(10)
        self.assertTrue(result)

    def test_03_add_valid_product_with_invalid_quantity_raises(self):
        factory = PaintFactory("Rainbow", 100)
        factory.ingredients = {"white": 90}

        with self.assertRaises(ValueError)as ex:
            factory.add_ingredient("yellow", 11)

        self.assertEqual("Not enough space in factory", str(ex.exception))
        self.assertEqual({"white": 90}, factory.ingredients)

    def test_04_add_invalid_product_raises(self):
        factory = PaintFactory("Rainbow", 100)
        factory.ingredients = {"white": 20}

        with self.assertRaises(TypeError)as ex:
            factory.add_ingredient("pink", 10)

        expected_message = "Ingredient of type pink not allowed in PaintFactory"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual({"white": 20}, factory.ingredients)

    def test_05_add_ingredient_success(self):
        factory = PaintFactory("Rainbow", 100)

        factory.add_ingredient("white", 20)
        self.assertEqual({"white": 20}, factory.ingredients)

        factory.add_ingredient("white", 10)
        self.assertEqual({"white": 30}, factory.ingredients)

        factory.add_ingredient("blue", 20)
        self.assertEqual({"white": 30, "blue": 20}, factory.ingredients)

    def test_06_remove_valid_ingredient_with_invalid_quantity_raises(self):
        factory = PaintFactory("Rainbow", 100)
        factory.add_ingredient("white", 20)
        factory.add_ingredient("blue", 10)

        with self.assertRaises(ValueError) as ex:
            factory.remove_ingredient("blue", 15)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))
        self.assertEqual({"white": 20, "blue": 10}, factory.ingredients)

    def test_07_remove_invalid_ingredient_raises(self):
        factory = PaintFactory("Rainbow", 100)
        factory.add_ingredient("white", 20)
        factory.add_ingredient("blue", 10)

        with self.assertRaises(KeyError) as ex:
            factory.remove_ingredient("green", 5)

        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))
        self.assertEqual({"white": 20, "blue": 10}, factory.ingredients)

    def test_08_remove_ingredient_success(self):
        factory = PaintFactory("Rainbow", 100)
        factory.add_ingredient("white", 20)
        factory.add_ingredient("blue", 10)

        factory.remove_ingredient("white", 10)
        self.assertEqual({"white": 10, "blue": 10}, factory.ingredients)

        factory.remove_ingredient("blue", 10)
        self.assertEqual({"white": 10, "blue": 0}, factory.ingredients)

    def test_09_product(self):
        factory = PaintFactory("Rainbow", 100)
        factory.add_ingredient("white", 20)
        factory.add_ingredient("blue", 10)

        result = factory.products

        self.assertEqual({"white": 20, "blue": 10}, result)

    def test_10_repr(self):
        factory = PaintFactory("Rainbow", 100)
        factory.add_ingredient("white", 20)
        factory.add_ingredient("blue", 10)

        result = repr(factory)
        expected_result = "Factory name: Rainbow with capacity 100.\n" \
                          "white: 20\n" \
                          "blue: 10\n"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
