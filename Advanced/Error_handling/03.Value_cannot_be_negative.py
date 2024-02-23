class ValueCannotBeNegative(Exception):
    """ Raised when the value is negative. """
    pass


for _ in range(5):
    num = int(input())

    if num < 0:
        raise ValueCannotBeNegative
