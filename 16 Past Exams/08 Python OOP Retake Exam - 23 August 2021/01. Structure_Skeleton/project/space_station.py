from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in SpaceStation.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        if name in [x.name for x in self.astronaut_repository.astronauts]:
            return f"{name} is already added."

        new_astronaut = SpaceStation.ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.astronauts.append(new_astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if name in [x.name for x in self.planet_repository.planets]:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items = items.split(", ")

        self.planet_repository.planets.append(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        astronauts_with_enough_oxygen = []

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                astronauts_with_enough_oxygen.append(astronaut)

        if len(astronauts_with_enough_oxygen) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        mission_astronauts = sorted(astronauts_with_enough_oxygen, key=lambda x: -x.oxygen)[:5]

        participated_astronauts = 0
        for astronaut in mission_astronauts:
            if not planet.items:
                break

            while astronaut.oxygen > 0 and planet.items:

                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts += 1

        if len(planet.items) == 0:
            self.successful_missions += 1

            return f"Planet: {planet_name} was explored. " \
                   f"{participated_astronauts} astronauts participated in collecting items."
        else:
            self.not_completed_missions += 1

            return "Mission is not completed."

    def report(self):
        result = [f"{self.successful_missions} successful missions!",
                  f"{self.not_completed_missions} missions were not completed!",
                  "Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")
            backpack_items = "none"
            if len(astronaut.backpack) > 0:
                backpack_items = ', '.join(astronaut.backpack)
            result.append(f"Backpack items: {backpack_items}")

        return '\n'.join(result)
