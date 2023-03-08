from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people) -> str or None:
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        if room.take_room(people) is None:
            self.guests += room.guests

    def free_room(self, room_number) -> str or None:
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        self.guests -= self.guests
        room.free_room()

    def status(self) -> str:
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        result = [
            f"Hotel {self.name} has {self.guests} total guests",
            f"Free rooms: {', '.join(free_rooms)}",
            f"Taken rooms: {', '.join(taken_rooms)}"
        ]

        return '\n'.join(result)
