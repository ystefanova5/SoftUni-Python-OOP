class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            current_value = self.start
            self.start += 1

            return current_value

        raise StopIteration()
