class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.start = self.count + 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            raise StopIteration

        self.start -= 1

        return self.start
