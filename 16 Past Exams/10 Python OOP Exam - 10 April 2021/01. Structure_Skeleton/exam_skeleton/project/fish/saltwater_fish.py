from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        self.name = name
        self.species = species
        self.price = price
        self.size = 5
        self.allowed_aquarium = "SaltwaterAquarium"
        self.type = "SaltwaterFish"

    def eat(self):
        self.size += 2
