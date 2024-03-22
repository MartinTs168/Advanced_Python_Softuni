def even_parameters(func):
    def wrapper(*args, **kwargs):
        for el in args:

            if not isinstance(el, int):
                return "Please use only even numbers!"

            if el % 2 != 0:
                return "Please use only even numbers!"

        return func(*args)

    return wrapper