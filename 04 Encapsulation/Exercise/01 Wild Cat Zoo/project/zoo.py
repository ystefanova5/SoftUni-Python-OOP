from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: [Lion, Tiger, Cheetah], price: [int, float]) -> str:
        if self.__animal_capacity > len(self.animals):
            if self.__budget > price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: [Keeper, Caretaker, Vet]) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            matched_worker = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(matched_worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        cost_to_tend_animals = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= cost_to_tend_animals:
            self.__budget -= cost_to_tend_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join(map(str, lions)) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += '\n'.join(map(str, tigers)) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(map(str, cheetahs))

        return result

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join(map(str, keepers)) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += '\n'.join(map(str, caretakers)) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += '\n'.join(map(str, vets))

        return result
