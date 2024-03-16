def squares(n: int):
    for num in range(1, n + 1):
        yield num ** 2


print(list(squares(5)))
