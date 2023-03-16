from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Chicken(Animal):
    def make_sound(self):
        return "pluck-pluck"


class Cow(Animal):
    def make_sound(self):
        return "moo"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
animals = [Cat(), Dog(), Chicken(), Cow()]
animal_sound(animals)
