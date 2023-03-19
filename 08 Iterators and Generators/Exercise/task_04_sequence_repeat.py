class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration

        self.number -= 1
        self.index += 1

        if self.index == len(self.sequence):
            self.index = 0

        return self.sequence[self.index]
