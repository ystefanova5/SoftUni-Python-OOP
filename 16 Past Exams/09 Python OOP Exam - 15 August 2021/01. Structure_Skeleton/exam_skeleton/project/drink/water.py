from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = 1.50
        self.brand = brand
