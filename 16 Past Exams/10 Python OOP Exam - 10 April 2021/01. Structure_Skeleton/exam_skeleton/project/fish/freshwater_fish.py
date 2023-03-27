from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        self.name = name
        self.species = species
        self.price = price
        self.size = 3
        self.allowed_aquarium = "FreshwaterAquarium"
        self.type = "FreshwaterFish"

    def eat(self):
        self.size += 3
