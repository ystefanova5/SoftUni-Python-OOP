from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total_comfort = sum([decoration.comfort for decoration in self.decorations])

        return total_comfort

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return f"Not enough capacity."

        self.fish.append(fish)

        return f"Successfully added {fish.type} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = [x.name for x in self.fish]

        if not fish_names:
            fish_names = ["none"]

        return f"{self.name}:\n" \
               f"Fish: {' '.join(name for name in fish_names)}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
