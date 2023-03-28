from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_expenses = room.room_cost + room.expenses

            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")

            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(result)

    def status(self):
        total_population = sum([room.members_count for room in self.rooms])

        result = [f"Total population: {total_population}"]

        for room in self.rooms:
            result.append((f"{room.family_name} with {room.members_count} members. "
                           f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"))

            for index, child in enumerate(room.children):
                result.append(f"--- Child {index + 1} monthly cost: {child.get_monthly_expense():.2f}$")

            appliances_monthly_cost = sum([obj.get_monthly_expense() for obj in room.appliances])
            result.append(f"--- Appliances monthly cost: {appliances_monthly_cost:.2f}$")

        return '\n'.join(result)
