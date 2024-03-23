class store_results:
    _FILE_NAME = "files/log.txt"

    def __init__(self, func):  # that's the decorator
        self.func = func

    def __call__(self, *args, **kwargs):  # the same as wrapper
        with open(self._FILE_NAME, "a") as log_file:
            log_file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}\n")


class store_results_param:
    _DIR = "files"

    def __init__(self, file_name):
        self.file_name = file_name

    def __call__(self, func):  # decorator
        def wrapper(*args, **kwargs):  # wrapper
            with open(f"{self._DIR}/{self.file_name}", "a") as log_file:
                log_file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")

        return wrapper


@store_results_param("results.txt")
def add(a, b):
    return a + b


# @store_results
# def mult(a, b):
#     return a * b


add(2, 2)
# mult(6, 4)
