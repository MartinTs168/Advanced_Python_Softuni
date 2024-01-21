n_rows = int(input())
matrix = [[x for x in input()] for i in range(n_rows)]
symbol = input()
for i in range(n_rows):
    symbol_found = False
    for j in range(n_rows):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            symbol_found = True
            break
    if symbol_found:
        break
else:
    print(f"{symbol} does not occur in the matrix")