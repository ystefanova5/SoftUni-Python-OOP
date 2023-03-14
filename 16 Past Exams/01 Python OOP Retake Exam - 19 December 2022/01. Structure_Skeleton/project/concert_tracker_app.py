from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Singer, Drummer, Guitarist] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        try:
            musician = next(filter(lambda x: x.name == name, self.musicians))
            raise Exception(f"{musician.name} is already a musician!")

        except StopIteration:
            current_class = ConcertTrackerApp.VALID_MUSICIAN_TYPES[musician_type]
            new_musician = current_class(name, age)
            self.musicians.append(new_musician)

            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        try:
            band = next(filter(lambda x: x.name == name, self.bands))
            raise Exception(f"{band.name} band is already created!")

        except StopIteration:
            new_band = Band(name)
            self.bands.append(new_band)

            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = next(filter(lambda x: x.place == place, self.concerts))
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        except StopIteration:
            new_concert = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(new_concert)

            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda x: x.name == musician_name, self.musicians))

        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda x: x.name == band_name, self.bands))

        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(filter(lambda x: x.name == band_name, self.bands))

        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda x: x.name == musician_name, band.members))

        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands))
        # method1:
        # concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        # method2:
        # concert = [c for c in self.concerts if c.place == concert_place][0] # method2

        # method3:
        concert = None
        for item in self.concerts:
            if item.place == concert_place:
                concert = item

        band_members = [member.__class__.__name__ for member in band.members]
        if set(band_members) != set(ConcertTrackerApp.VALID_MUSICIAN_TYPES):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        error_message = f"The {band_name} band is not ready to play at the concert!"

        if concert.genre == "Rock":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Guitarist" and "play rock" not in member.skills:
                    raise Exception(error_message)

        elif concert.genre == "Metal":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Singer" and "sing low pitch notes" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Guitarist" and "play metal" not in member.skills:
                    raise Exception(error_message)

        elif concert.genre == 'Jazz':
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in member.skills or "sing high pitch notes" not in member.skills:
                        raise Exception(error_message)
                elif member.__class__.__name__ == "Guitarist" and "play jazz" not in member.skills:
                    raise Exception(error_message)

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
