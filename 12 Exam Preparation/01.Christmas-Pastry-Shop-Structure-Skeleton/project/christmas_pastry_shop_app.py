from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }
    BOOTHS = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [x.name for x in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ChristmasPastryShopApp.DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = ChristmasPastryShopApp.DELICACIES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [x.booth_number for x in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = ChristmasPastryShopApp.BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)

                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if booth_number not in [x.booth_number for x in self.booths]:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy_name not in [x.name for x in self.delicacies]:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        delicacy = [x for x in self.delicacies if x.name == delicacy_name][0]
        booth = [x for x in self.booths if x.booth_number == booth_number][0]

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [x for x in self.booths if x.booth_number == booth_number][0]

        bill = booth.calculate_bill()
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
