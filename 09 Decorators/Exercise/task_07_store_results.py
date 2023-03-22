class store_results:
    _store_file = "results.txt"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        current_line = f"Function {self.function.__name__} was called. Result: {self.function(*args)}"

        with open(self._store_file, "a") as file:
            file.write(current_line + "\n")

        return self.function(*args)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
