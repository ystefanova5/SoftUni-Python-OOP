from typing import List

from project.band_members.musician import Musician


class Singer(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.skills: List[str] = []
