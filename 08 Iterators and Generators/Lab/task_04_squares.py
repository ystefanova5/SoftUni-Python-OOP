def squares(end: int):
    num = 1

    while num <= end:
        yield num ** 2
        num += 1

# class squares:
#     def __init__(self, end: int):
#         self.start = 0
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#
#         self.start += 1
#
#         return self.start ** 2
#
#
# print(list(squares(5)))
