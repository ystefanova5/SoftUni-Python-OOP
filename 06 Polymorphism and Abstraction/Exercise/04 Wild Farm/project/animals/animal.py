from abc import ABC, abstractmethod
from typing import Any


class Animal(ABC):
    FOOD_PREFERENCE = []
    WEIGHT_INCREASE = 0

    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Any):
        food_type = food.__class__.__name__

        if food_type not in self.FOOD_PREFERENCE:
            return f"{self.__class__.__name__} does not eat {food_type}!"

        self.weight += self.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
