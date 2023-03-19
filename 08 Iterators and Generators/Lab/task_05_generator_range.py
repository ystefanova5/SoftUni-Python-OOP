def genrange(start: int, end: int):
    while start <= end:
        yield start
        start += 1

# def genrange(start: int, end: int):
#     for num in range(start, end + 1):
#         yield num
