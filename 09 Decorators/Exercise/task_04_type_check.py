def type_check(parameter_type):
    def decorator(function):
        def wrapper(*args):
            for element in args:
                if not isinstance(element, parameter_type):
                    return "Bad Type"

            return function(*args)

        return wrapper

    return decorator
