from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_PREFERENCE = ["Vegetable", "Fruit"]
    WEIGHT_INCREASE = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    FOOD_PREFERENCE = ["Meat"]
    WEIGHT_INCREASE = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    FOOD_PREFERENCE = ["Vegetable", "Meat"]
    WEIGHT_INCREASE = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    FOOD_PREFERENCE = ["Meat"]
    WEIGHT_INCREASE = 1

    def make_sound(self):
        return "ROAR!!!"
