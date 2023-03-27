from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        self.name = name
        self.capacity = 25
        self.decorations = []
        self.fish = []
        self.type = "SaltwaterAquarium"
