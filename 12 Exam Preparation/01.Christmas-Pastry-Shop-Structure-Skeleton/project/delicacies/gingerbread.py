from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION_SIZE = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, Gingerbread.PORTION_SIZE, price)

    def details(self):
        return f"{self.DELICACY_TYPE} {self.name}: {self.PORTION_SIZE}g - {self.price:.2f}lv."
