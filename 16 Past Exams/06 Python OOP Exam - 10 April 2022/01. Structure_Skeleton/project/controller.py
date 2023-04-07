class Controller:
    VALID_SUSTENANCE_TYPES = ["Food", "Drink"]
    PLAYER_NAMES = []

    def __init__(self):
        self.players = []
        self.supplies = []

    @staticmethod
    def find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def add_player(self, *args):
        players_added = []
        for player in args:
            if player.name not in Controller.PLAYER_NAMES:
                Controller.PLAYER_NAMES.append(player.name)
                players_added.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(players_added)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if player_name not in [x.name for x in self.players]:
            return

        if sustenance_type not in Controller.VALID_SUSTENANCE_TYPES:
            return

        player = self.find_object(player_name, "name", self.players)

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        if len([x for x in self.supplies if x.__class__.__name__ == "Food"]) == 0:
            raise Exception("There are no food supplies left!")

        if len([x for x in self.supplies if x.__class__.__name__ == "Drink"]) == 0:
            raise Exception("There are no drink supplies left!")

        supply = None

        for supply_item in self.supplies:
            if supply_item.__class__.__name__ == sustenance_type:
                supply = supply_item

        if supply.energy + player.stamina > 100:
            player.stamina = 100

        else:
            player.stamina += supply.energy

        self.supplies.reverse()
        self.supplies.remove(supply)
        self.supplies.reverse()

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = self.find_object(first_player_name, "name", self.players)
        player_two = self.find_object(second_player_name, "name", self.players)

        if player_one.stamina == 0 and player_two.stamina == 0:
            return f"Player {player_one.name} does not have enough stamina.\n" \
                   f"Player {player_two.name} does not have enough stamina."

        elif player_one.stamina == 0:
            return f"Player {player_one.name} does not have enough stamina."

        elif player_two.stamina == 0:
            return f"Player {player_two.name} does not have enough stamina."

        if player_one.stamina > player_two.stamina:
            player_one, player_two = player_two, player_one

        if player_two.stamina > player_one.stamina / 2:
            player_two.stamina -= player_one.stamina / 2
        else:
            player_two.stamina = 0
            winner = player_one
            return f"Winner: {winner.name}"

        if player_one.stamina > player_two.stamina / 2:
            player_one.stamina -= player_two.stamina / 2
        else:
            player_one.stamina = 0
            winner = player_two
            return f"Winner: {winner.name}"

        if player_one.stamina > player_two.stamina:
            winner = player_one
        else:
            winner = player_two

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.reduce_stamina()
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = [str(player) for player in self.players]
        result.extend([supply.details() for supply in self.supplies])

        return '\n'.join(result)
