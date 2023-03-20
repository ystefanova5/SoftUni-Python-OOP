from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    RECEIPT_ID = 0
    VALID_MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []

    @staticmethod
    def find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def register_client(self, client_phone_number: str):
        if client_phone_number in [client.phone_number for client in self.clients_list]:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, Meal):
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        menu = [meal.details() for meal in self.menu]

        return "\n".join(menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        cart = []
        bill = 0

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if client_phone_number not in [client.phone_number for client in self.clients_list]:
            self.register_client(client_phone_number)

        client = self.find_object(client_phone_number, "phone_number", self.clients_list)

        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in [x.name for x in self.menu]:
                raise Exception(f"{meal_name} is not on the menu!")

            meal = [m for m in self.menu if m.name == meal_name][0]

            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

            meal.quantity -= quantity

            bought_meal = FoodOrdersApp.VALID_MEALS[meal.__class__.__name__](meal_name, meal.price, quantity)
            cart.append(bought_meal)
            bill += quantity * meal.price

        client.shopping_cart.extend(cart)
        client.bill += bill

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(x.name for x in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_object(client_phone_number, "phone_number", self.clients_list)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            for menu_item in self.menu:
                if meal.name == menu_item.name:
                    menu_item.quantity += meal.quantity

        client.bill = 0
        client.shopping_cart.clear()

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart.clear()
        FoodOrdersApp.RECEIPT_ID += 1

        return f"Receipt #{FoodOrdersApp.RECEIPT_ID} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
