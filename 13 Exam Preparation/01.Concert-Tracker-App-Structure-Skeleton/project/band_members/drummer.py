from project.band_members.musician import Musician


class Drummer(Musician):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []
        self.valid_skills = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    @property
    def can_play_rock(self):
        return "play the drums with drumsticks" in self.skills

    @property
    def can_play_metal(self):
        return "play the drums with drumsticks" in self.skills

    @property
    def can_play_jazz(self):
        return "play the drums with drum brushes" in self.skills
