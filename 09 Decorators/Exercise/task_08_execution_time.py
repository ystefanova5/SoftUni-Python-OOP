from time import time


def exec_time(function):
    def wrapper(*args):
        start = time()
        function(*args)
        end = time()

        return end - start

    return wrapper


# @exec_time
# def loop():
#     count = 0
#     for i in range(1, 9999999):
#         count += 1
# print(loop())
