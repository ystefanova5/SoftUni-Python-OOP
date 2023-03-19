class take_skip:
    def __init__(self, step:int, count: int):
        self.step = step
        self.count = count
        self.start = 0 - self.step
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration

        self.counter += 1
        self.start += self.step

        return self.start


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
