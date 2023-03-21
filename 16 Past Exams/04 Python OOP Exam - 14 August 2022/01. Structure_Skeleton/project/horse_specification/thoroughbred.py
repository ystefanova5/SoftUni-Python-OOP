from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TRAIN_RATE = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.is_taken = False

    def train(self):
        if self.speed + Thoroughbred.TRAIN_RATE > Thoroughbred.MAX_SPEED:
            self.speed = Thoroughbred.MAX_SPEED

        else:
            self.speed += Thoroughbred.TRAIN_RATE
