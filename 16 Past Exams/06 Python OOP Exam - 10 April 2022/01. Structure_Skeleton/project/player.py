class Player:
    EXISTING_PLAYERS = []
    MAX_STAMINA = 100
    MIN_STAMINA = 0

    def __init__(self, name: str, age: int, stamina=MAX_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")

        if value in Player.EXISTING_PLAYERS:
            raise Exception(f"Name {value} is already used!")

        self.__name = value
        Player.EXISTING_PLAYERS.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < Player.MAX_STAMINA

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    def reduce_stamina(self):
        reduction = self.age * 2

        if reduction > self.stamina:
            self.stamina = 0

        else:
            self.stamina -= reduction
