class Band:
    REQUIRED_MEMBERS = {"Drummer", "Singer", "Guitarist"}

    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Band name should contain at least one character!")

        self.__name = value

    @property
    def member_types(self):
        return [member.__class__.__name__ for member in self.members]

    @property
    def has_member_of_each_type(self):
        return all(["Drummer" in self.member_types, "Singer" in self.member_types, "Guitarist" in self. member_types])

    @property
    def can_play_rock(self):
        return all([member.can_play_rock for member in self.members])

    @property
    def can_play_metal(self):
        return all([member.can_play_metal for member in self.members])

    @property
    def can_play_jazz(self):
        return all([member.can_play_jazz for member in self.members])

    def add_member(self, musician):
        self.members.append(musician)

    def remove_member(self, name):
        for musician in self.members:
            if musician.name == name:
                self.members.remove(musician)

                return

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
