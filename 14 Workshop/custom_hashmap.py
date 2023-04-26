import time


class HashTable:
    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity
        self.__min_index = 0

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(f"{key} is not a valid key!")

    def __setitem__(self, key, value):
        if key in self.__keys:  # First we check if this key is already created, and if it is we update its value
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if self.size() == self.__max_capacity:  # Then we check if we have reached the array's capacity
            self.__resize()

        index = self.__calc_index(key)
        index = self.__get_index(index)

        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key):  # This is our Hash Function, we decide how to hash the data
        return sum(ord(c) for c in key) % self.__max_capacity

    def __get_index(self, index):  # We check if there is a collision
        if index == self.__max_capacity:
            index = self.__min_index

        if self.__keys[index] is None:
            return index

        return self.__get_index(index + 1)

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__values = self.__values + [None] * self.__max_capacity

        # self.__min_index = self.__max_capacity
        self.__max_capacity *= 2

    def size(self):
        return len([k for k in self.__keys if k is not None])

    def get(self, key, default=None):
        try:
            return self[key]

        except KeyError:
            return default

    def get_representation(self):
        print("{", end="")
        for i in range(self.__max_capacity):
            if self.__keys[i] is not None:
                print(f"{self.__keys[i]}: {self.__values[i]},", end=" ")

        print("}")

    def __len__(self):
        return self.__max_capacity


start_time = time.time()

table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table["last name"] = "Jackson"
table["is_married"] = "No"
table["has_drivers_license"] = "Yes"

print(table["name"])
# print(table["pets"])  # returns KeyError: 'pets is not a valid key!'

# table.get_representation()

print(table)
print(table.get("name"))
print(table.get("n"))  # returns None

print(table["age"])
print(len(table))

time.sleep(1)
end_time = time.time()
execution = end_time - start_time
# print(f"Executed in: {execution * 1000 - 1000:.10f} milliseconds")
