def genrange(start: int, end: int):
    while start <= end:
        yield start
        start += 1
