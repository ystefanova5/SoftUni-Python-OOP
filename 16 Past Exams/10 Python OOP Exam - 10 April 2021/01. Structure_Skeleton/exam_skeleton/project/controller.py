from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUMS = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }
    VALID_DECORATION = {
        "Ornament": Ornament,
        "Plant": Plant
    }
    VALID_FISH = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums: list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in Controller.VALID_AQUARIUMS:
            return "Invalid aquarium type."

        new_aquarium = Controller.VALID_AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in Controller.VALID_DECORATION:
            return "Invalid decoration type."

        new_decoration = Controller.VALID_DECORATION[decoration_type]()
        self.decorations_repository.add(new_decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        if decoration_type not in [x.decoration_type for x in self.decorations_repository.decorations]:
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium_name in [x.name for x in self.aquariums]:
            aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]

            for index, item in enumerate(self.decorations_repository.decorations):
                if item.decoration_type == decoration_type:
                    decoration = self.decorations_repository.decorations.pop(index)
                    aquarium.add_decoration(decoration)

                    return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in Controller.VALID_FISH:
            return f"There isn't a fish of type {fish_type}."

        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        fish = Controller.VALID_FISH[fish_type](fish_name, fish_species, price)

        if fish.allowed_aquarium != aquarium.type:
            return "Water not suitable."

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]

        for fish in aquarium.fish:
            fish.eat()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        total_value = 0

        for fish in aquarium.fish:
            total_value += fish.price

        for decoration in aquarium.decorations:
            total_value += decoration.price

        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result = []

        for aquarium in self.aquariums:
            result.append(str(aquarium))

        return '\n'.join(result)
