from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food):

    def __init__(self, quantity: int):
        self.quantity = quantity


class Fruit(Food):

    def __init__(self, quantity: int):
        self.quantity = quantity


class Meat(Food):

    def __init__(self, quantity: int):
        self.quantity = quantity


class Seed(Food):

    def __init__(self, quantity: int):
        self.quantity = quantity
