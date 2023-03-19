class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.items = list(dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.items:
            raise StopIteration

        key_value_pair = self.items.pop(0)

        return key_value_pair
