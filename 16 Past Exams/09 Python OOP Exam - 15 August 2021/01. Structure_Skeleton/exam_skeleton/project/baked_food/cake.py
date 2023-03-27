from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.portion = 245
