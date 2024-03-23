from time import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time()  # gets current time
        func(*args, **kwargs)
        end = time()  # gets current time

        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop())
