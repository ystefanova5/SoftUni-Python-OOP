from project.band_members.musician import Musician


class Singer(Musician):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []
        self.valid_skills = ["sing high pitch notes", "sing low pitch notes"]

    @property
    def can_play_rock(self):
        return "sing high pitch notes" in self.skills

    @property
    def can_play_metal(self):
        return "sing low pitch notes" in self.skills

    @property
    def can_play_jazz(self):
        return "sing low pitch notes" in self.skills and "sing high pitch notes" in self.skills
