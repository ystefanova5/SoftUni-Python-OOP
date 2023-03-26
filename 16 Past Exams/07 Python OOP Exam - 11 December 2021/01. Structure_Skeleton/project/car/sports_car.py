from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def min_speed(self):
        return 400

    @property
    def max_speed(self):
        return 600

    @property
    def car_type(self):
        return "SportsCar"
