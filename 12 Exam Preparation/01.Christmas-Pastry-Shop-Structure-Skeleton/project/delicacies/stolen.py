from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    PORTION_SIZE = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, Stolen.PORTION_SIZE, price)

    def details(self):
        return f"{self.DELICACY_TYPE} {self.name}: {self.PORTION_SIZE}g - {self.price:.2f}lv."
