from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        for member in self.pokemons:
            if pokemon.name == member.name:
                return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        for idx, member in enumerate(self.pokemons):
            if pokemon_name == member.name:
                self.pokemons.pop(idx)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for pok in self.pokemons:
            result += f"- {pok.pokemon_details()}\n"

        return result
