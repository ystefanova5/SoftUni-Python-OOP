from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        ...


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calc_area(self):
        return (self.base * self.height) / 2


class Square(Shape):
    def __init__(self, base):
        self.base = base

    def calc_area(self):
        return self.base ** 2


class AreaCalculator:

    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3), Square(4)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
