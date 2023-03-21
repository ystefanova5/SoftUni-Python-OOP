from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAIN_RATE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.is_taken = False

    def train(self):
        if self.speed + Appaloosa.TRAIN_RATE > Appaloosa.MAX_SPEED:
            self.speed = Appaloosa.MAX_SPEED

        else:
            self.speed += Appaloosa.TRAIN_RATE
