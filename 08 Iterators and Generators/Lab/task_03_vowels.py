from collections import deque


class vowels:
    VOWELS = "aeiouy"

    def __init__(self, text: str):
        self.vowels = deque([x for x in text if x.lower() in vowels.VOWELS])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels:
            raise StopIteration

        return self.vowels.popleft()
