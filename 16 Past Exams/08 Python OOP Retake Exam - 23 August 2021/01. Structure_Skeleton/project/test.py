from project.astronaut.biologist import Biologist
from project.space_station import SpaceStation

space_station = SpaceStation()

print(space_station.add_astronaut("Meteorologist", "Anton"))
print(space_station.add_astronaut("Biologist", "Ivan"))

print(space_station.add_planet("Venus", "rocks, iron, dust, rocks, iron, dust, rock"))

print(space_station.retire_astronaut("Ivan"))
# print(space_station.add_astronaut("Geodesist", "Boris"))

print(space_station.add_astronaut("Geodesist", "Boris"))
# print(space_station.add_astronaut("Biologist", "Ivan"))



print(space_station.add_astronaut("Geodesist", "Stoyan"))
# print(space_station.add_astronaut("Meteorologist", "Maya"))
# print(space_station.add_astronaut("Biologist", "Lora"))
print("--------------")
[print(a.name,"-", a.__class__.__name__, a.oxygen) for a in space_station.astronaut_repository.astronauts]
print("--------------")
print(space_station.send_on_mission("Venus"))
# [print(a.name,"-", a.oxygen) for a in space_station.send_on_mission("Venus")]
print("--------------")
[print(a.name,"-", a.__class__.__name__, a.oxygen) for a in space_station.astronaut_repository.astronauts]

print(space_station.report())