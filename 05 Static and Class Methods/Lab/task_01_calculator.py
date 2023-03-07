from functools import reduce


class Calculator:
    @staticmethod
    def add(*args) -> int or float:
        return sum(args)

    @staticmethod
    def multiply(*args) -> int or float:
        return reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args) -> int or float:
        return reduce(lambda a, b: a + b if a == 0 or b == 0 else a / b, args)

    @staticmethod
    def subtract(*args) -> int or float:
        return reduce(lambda a, b: a - b, args)
