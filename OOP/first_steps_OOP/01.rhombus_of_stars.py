def print_upper_half(size):
    for row in range(1, size + 1):
        print(" " * (size - row), "* " * row)


def print_lower_half(size):
    for row in range(size - 1, 0, -1):
        print(" " * (size - row), "* " * row)


def print_rhombus(size):
    print_upper_half(size)
    print_lower_half(size)


n = int(input())
print_rhombus(n)

