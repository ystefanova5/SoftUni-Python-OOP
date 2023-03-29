from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        if name in [x.name for x in self.musicians]:
            raise Exception(f"{name} is already a musician!")

        new_musician = ConcertTrackerApp.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [x.name for x in self.bands]:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in [x.place for x in self.concerts]:
            concert = [x for x in self.concerts if x.place == place][0]

            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in [x.name for x in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in [x.name for x in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        musician = [x for x in self.musicians if x.name == musician_name][0]
        band = [x for x in self.bands if x.name == band_name][0]

        band.add_member(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in [x.name for x in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        band = [x for x in self.bands if x.name == band_name][0]

        if musician_name not in [x.name for x in band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.remove_member(musician_name)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = [x for x in self.concerts if x.place == concert_place][0]
        band = [x for x in self.bands if x.name == band_name][0]

        if not band.has_member_of_each_type:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        error_message = f"The {band_name} band is not ready to play at the concert!"
        if concert.genre == "Rock" and not band.can_play_rock:
            raise Exception(error_message)

        elif concert.genre == "Metal" and not band.can_play_metal:
            raise Exception(error_message)

        elif concert.genre == "Jazz" and not band.can_play_jazz:
            raise Exception(error_message)

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
