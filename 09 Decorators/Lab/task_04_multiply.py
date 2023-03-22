def multiply(times):
    def decorator(function):
        def wrapper(number):
            return function(number) * times

        return wrapper

    return decorator

# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))
