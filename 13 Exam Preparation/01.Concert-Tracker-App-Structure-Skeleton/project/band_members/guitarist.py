from project.band_members.musician import Musician


class Guitarist(Musician):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []
        self.valid_skills = ["play metal", "play rock", "play jazz"]

    @property
    def can_play_rock(self):
        return "play rock" in self.skills

    @property
    def can_play_metal(self):
        return "play metal" in self.skills

    @property
    def can_play_jazz(self):
        return "play jazz" in self.skills
