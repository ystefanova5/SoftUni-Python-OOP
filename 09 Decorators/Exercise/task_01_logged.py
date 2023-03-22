def logged(function):
    def wrapper(*args):
        func_result = function(*args)
        return f"you called {function.__name__}({', '.join(map(str, args))})\n" \
               f"it returned {func_result}"

    return wrapper
