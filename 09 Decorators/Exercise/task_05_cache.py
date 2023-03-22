def cache(func):
    log_dict = {}

    def wrapper(num):
        log_dict[num] = func(num)

        return func(num)

    wrapper.log = log_dict

    return wrapper


# @cache
# def fibonacci(n):
#     if n < 2:
#
#         return n
#
#     else:
#
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# fibonacci(4)
# print(fibonacci.log)
