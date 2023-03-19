def squares(end: int):
    num = 1

    while num < end + 1:
        yield num ** 2
        num += 1
