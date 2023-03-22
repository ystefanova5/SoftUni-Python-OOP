from math import log

from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @staticmethod
    def validate_ram(ram):
        if ram in [2, 4, 8, 16, 32, 64]:
            return True

        return False

    @staticmethod
    def calculate_ram_price(ram):
        base = 2
        price = int(log(ram, base)) * 100

        return price

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if not self.validate_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.AVAILABLE_PROCESSORS[processor] + self.calculate_ram_price(ram)

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
