def print_triangle(n):
    print_top(n)
    print_bottom(n)


def print_top(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=' ')
        print()


def print_bottom(n):
    for row in range(n, 0, -1):
        for num in range(1, row):
            print(num, end=' ')
        print()


def execute_expression(exp):
    num1_text, symbol, num2_text = exp.split()
    num1 = float(num1_text)
    num2 = float(num2_text)

    return sign_mapper[symbol](num1, num2)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def power(num1, num2):
    return num1 ** num2


sign_mapper = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,

}


