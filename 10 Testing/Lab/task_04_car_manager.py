class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

from unittest import TestCase, main


class CarTests(TestCase):
    def test_01_class_is_initialized_correctly_with_valid_data(self):
        car = Car("Subaru", "Outback", 12, 80)

        self.assertEqual("Subaru", car.make)
        self.assertEqual("Outback", car.model)
        self.assertEqual(12, car.fuel_consumption)
        self.assertEqual(80, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_02_class_initialized__with_invalid_make_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "Outback", 12, 80)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car(None, "Outback", 12, 80)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_03_set_invalid_make_raises(self):
        car = Car("Subaru", "Outback", 12, 80)

        with self.assertRaises(Exception) as ex:
            car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.make = None

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_04_class_initialized__with_invalid_model_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Subaru", "", 12, 80)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("Subaru", None, 12, 80)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_05_set_invalid_model_raises(self):
        car = Car("Subaru", "Outback", 12, 80)

        with self.assertRaises(Exception) as ex:
            car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.model = None

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_06_class_initialized__with_invalid_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Subaru", "Outback", 0, 80)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("Subaru", "Outback", -5, 80)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_07_set_invalid_fuel_consumption_raises(self):
        car = Car("Subaru", "Outback", 12, 80)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -5

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_08_class_initialized__with_invalid_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Subaru", "Outback", 12, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("Subaru", "Outback", 12, -10)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_09_set_invalid_fuel_consumption_raises(self):
        car = Car("Subaru", "Outback", 12, 80)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -5

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_10_set_valid_make(self):
        car = Car("Subaru", "Outback", 12, 80)

        car.make = "Honda"

        self.assertEqual("Honda", car.make)

    def test_11_set_valid_model(self):
        car = Car("Subaru", "Outback", 12, 80)

        car.model = "Forester"

        self.assertEqual("Forester", car.model)

    def test_12_set_valid_fuel_consumption(self):
        car = Car("Subaru", "Outback", 12, 80)

        car.fuel_consumption = 15

        self.assertEqual(15, car.fuel_consumption)

    def test_13_set_valid_fuel_capacity(self):
        car = Car("Subaru", "Outback", 12, 80)

        car.fuel_capacity = 90

        self.assertEqual(90, car.fuel_capacity)

    def test_14_set_invalid_fuel_amount_raises(self):
        car = Car("Subaru", "Outback", 12, 80)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_15_set_valid_fuel_amount(self):
        car = Car("Subaru", "Outback", 12, 80)

        car.fuel_amount = 0
        self.assertEqual(0, car.fuel_amount)

        car.fuel_amount = 20
        self.assertEqual(20, car.fuel_amount)

    def test_16_refuel_with_invalid_data_raises(self):
        car = Car("Subaru", "Outback", 12, 80)

        with self.assertRaises(Exception) as ex:
            car.refuel(-10)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_17_refuel_with_valid_amount_increments_fuel_amount(self):
        car = Car("Subaru", "Outback", 12, 80)
        self.assertEqual(0, car.fuel_amount)

        car.refuel(10)
        self.assertEqual(10, car.fuel_amount)

    def test_18_refuel_with_valid_amoun_doesnt_exceed_fuel_capacity(self):
        car = Car("Subaru", "Outback", 12, 80)

        car.refuel(90)
        self.assertEqual(80, car.fuel_amount)

    def test_19_drive_with_not_enough_fuel_raises(self):
        car = Car("Subaru", "Outback", 12, 80)
        car.refuel(12)

        with self.assertRaises(Exception) as ex:
            car.drive(101)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_20_drive_reduces_fuel_amount_correctly(self):
        car = Car("Subaru", "Outback", 12, 80)
        car.refuel(36)

        car.drive(100)
        self.assertEqual(24, car.fuel_amount)


if __name__ == "__main__":
    main()
