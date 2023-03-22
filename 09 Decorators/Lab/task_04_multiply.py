def multiply(times):
    def decorator(function):
        def wrapper(number):
            return function(number) * times

        return wrapper

    return decorator
