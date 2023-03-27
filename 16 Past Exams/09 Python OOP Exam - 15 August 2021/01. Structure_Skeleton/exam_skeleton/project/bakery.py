from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }
    DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }
    TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if name in [x.name for x in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in Bakery.FOOD_TYPES:
            new_food = Bakery.FOOD_TYPES[food_type](name, price)
            self.food_menu.append(new_food)

            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if name in [x.name for x in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in Bakery.DRINK_TYPES:
            new_drink = Bakery.DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)

            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [x.table_number for x in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in Bakery.TABLE_TYPES:
            new_table = Bakery.TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(new_table)

            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)

                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        if table_number not in [x.table_number for x in self.tables_repository]:
            return f"Could not find table {table_number}"

        table = [x for x in self.tables_repository if x.table_number == table_number][0]

        not_on_the_menu = []
        available_foods = [x.name for x in self.food_menu]

        for ordered_food in args:
            if ordered_food not in available_foods:
                not_on_the_menu.append(ordered_food)
                continue

            food = [x for x in self.food_menu if x.name == ordered_food][0]
            table.food_orders.append(food)

        result = [f"Table {table_number} ordered:"]
        for food_item in table.food_orders:
            result.append(str(food_item))

        result.append(f"{self.name} does not have in the menu:")
        for food_item in not_on_the_menu:
            result.append(food_item)

        return '\n'.join(result)

    def order_drink(self, table_number: int, *args):
        if table_number not in [x.table_number for x in self.tables_repository]:
            return f"Could not find table {table_number}"

        table = [x for x in self.tables_repository if x.table_number == table_number][0]

        not_on_the_menu = []
        available_drinks = [x.name for x in self.drinks_menu]

        for ordered_drink in args:
            if ordered_drink not in available_drinks:
                not_on_the_menu.append(ordered_drink)
                continue

            drink = [x for x in self.drinks_menu if x.name == ordered_drink][0]
            table.drink_orders.append(drink)

        result = [f"Table {table_number} ordered:"]
        for drink_item in table.drink_orders:
            result.append(str(drink_item))

        result.append(f"{self.name} does not have in the menu:")
        for drink_item in not_on_the_menu:
            result.append(drink_item)

        return '\n'.join(result)

    def leave_table(self, table_number: int):
        table = [x for x in self.tables_repository if x.table_number == table_number][0]
        bill = table.get_bill()
        table.clear()
        self.total_income += bill

        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())

        return '\n'.join(result)

    def get_total_income(self):

        return f"Total income: {self.total_income:.2f}lv"
