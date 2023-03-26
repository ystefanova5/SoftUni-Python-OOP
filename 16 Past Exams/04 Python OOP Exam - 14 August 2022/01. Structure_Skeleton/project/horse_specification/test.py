from project.horse_race_app import HorseRaceApp
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey

horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))

horse1 = (Appaloosa("Shadow", 117))
horse2 = (Thoroughbred("Bolt", 130))
horseRaceApp.horses.append(horse1)
horseRaceApp.horses.append(horse2)
print(len(horseRaceApp.horses))

jockey1 = Jockey("Mark", 25)
jockey2 = Jockey("Lora", 25)

horseRaceApp.jockeys.append(jockey1)
horseRaceApp.jockeys.append(jockey2)
print(horse2.speed)
horse2.train()
print(horse2.speed)
horse2.train()
print(horse2.speed)
horse2.train()
print(horse2.speed)
horse2.train()
print(horse2.speed)
horse2.train()
print(horse2.speed)





