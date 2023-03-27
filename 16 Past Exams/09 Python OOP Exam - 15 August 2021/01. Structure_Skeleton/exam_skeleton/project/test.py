from project.bakery import Bakery

bakery = Bakery("Cafe Noir")

print(bakery.add_drink("Tea", "Herbal Tea", 250, "Pickwick"))
print(bakery.add_drink("Tea", "Black Tea", 250, "Pickwick"))
print(bakery.add_drink("Water", "Mineral", 500, "Devin"))
print(bakery.add_drink("Water", "Spring", 500, "Devin"))

print(bakery.add_food("Bread", "Croissant", 2.10))
print(bakery.add_food("Bread", "Wholegrain Croissant", 2.40))
print(bakery.add_food("Cake", "Vanilla Cake", 4.40))
print(bakery.add_food("Cake", "Chocolate Delight", 5.40))

print(bakery.add_table("InsideTable", 1, 5))
print(bakery.add_table("InsideTable", 2, 6))
print(bakery.add_table("OutsideTable", 51, 5))
print(bakery.add_table("OutsideTable", 52, 10))

print(bakery.reserve_table(5))
print(bakery.reserve_table(8))
print(bakery.get_free_tables_info())
print(bakery.order_food(1, "Chocolate Delight", "Vanilla Cake", "Wholegrain Bread", "Vanilla Cake"))

print(bakery.order_drink(52, "Chocolate Delight", "Mineral", "Herbal Tea"))

print(bakery.leave_table(1))
print(bakery.leave_table(52))

print(bakery.get_total_income())
print(bakery.get_free_tables_info())



# [print(table.table_number, table.number_of_people, table.is_reserved, table.food_orders, table.drink_orders) for table in bakery.tables_repository]

