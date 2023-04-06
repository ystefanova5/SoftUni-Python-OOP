from abc import ABC, abstractmethod


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        ...

    @abstractmethod
    def create_sofa(self):
        ...

    @abstractmethod
    def create_table(self):
        ...


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair("victorian chair")

    def create_sofa(self):
        return Sofa("victorian sofa")

    def create_table(self):
        return Sofa("victorian table")


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair("modern chair")

    def create_sofa(self):
        return Sofa("modern sofa")

    def create_table(self):
        return Sofa("modern table")


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair("futuristic chair")

    def create_sofa(self):
        return Sofa("futuristic sofa")

    def create_table(self):
        return Sofa("futuristic table")


def get_factory(style):
    if style == "victorian":
        return VictorianFactory()

    elif style == "modern":
        return ModernFactory()

    elif style == "futuristic":
        return FuturisticFactory()


if __name__ == "__main__":
    style = input("Please provide factory style (victorian, modern, futuristic): ")
    factory = get_factory(style)
    print(factory.create_chair())
    print(factory.create_sofa())
    print(factory.create_table())
