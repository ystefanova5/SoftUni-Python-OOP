def even_parameters(function):
    def wrapper(*args):
        for element in args:
            if isinstance(element, str) or element % 2 != 0:
                return "Please use only even numbers!"

        return function(*args)

    return wrapper
