from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = ["Gingerbread", "Stolen"]
    VALID_BOOTHS = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        try:
            delicacy = next(filter(lambda x: x.name == name, self.delicacies))
            raise Exception(f"{delicacy.name} already exists!")

        except StopIteration:
            if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACIES:
                raise Exception(f"{type_delicacy} is not on our delicacy menu!")

            if type_delicacy == "Gingerbread":
                self.delicacies.append(Gingerbread(name, price))
            else:
                self.delicacies.append(Stolen(name, price))

            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        else:
            self.booths.append(PrivateBooth(booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth_item in self.booths:
            if not booth_item.is_reserved and booth_item.capacity >= number_of_people:
                booth_item.reserve(number_of_people)

                return f"Booth {booth_item.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))

        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda x: x.name == delicacy_name, self.delicacies))

        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        bill = sum(delicacy.price for delicacy in booth.delicacy_orders) + booth.price_for_reservation
        self.income += bill
        booth.price_for_reservation = 0
        booth.is_reserved = False
        booth.delicacy_orders.clear()

        return f"Booth {booth.booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
