def fibonacci():
    first = 0
    second = 1

    while True:
        third = first + second

        if first == 0:
            yield first
            yield second

        yield third
        first = second
        second = third
