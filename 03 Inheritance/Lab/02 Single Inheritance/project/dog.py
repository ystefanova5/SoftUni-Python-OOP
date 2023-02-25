from project.animal import Animal


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        return "barking..."
