from project.animals.animal import Bird


class Owl(Bird):
    FOOD_PREFERENCE = ["Meat"]
    WEIGHT_INCREASE = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    FOOD_PREFERENCE = ["Vegetable", "Fruit", "Meat", "Seed"]
    WEIGHT_INCREASE = 0.35

    def make_sound(self):
        return "Cluck"
