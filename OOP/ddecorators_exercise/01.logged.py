def logged(func):
    def wrapper(*args):
        func_name = func.__name__
        result = func(*args)
        parameters = [str(el) for el in args]

        to_return = (f"you called {func_name}({', '.join(parameters)})\n"
                     f"it returned {result}")

        return to_return

    return wrapper