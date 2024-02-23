n_row, n_col = [int(el) for el in input().split()]
identical_matrix_count = 0
matrix = [input().split() for _ in range(n_row)]

for row in range(n_row - 1):
    for col in range(n_col - 1):
        symbol = matrix[row][col]

        if symbol == matrix[row][col + 1] and symbol == matrix[row + 1][col] and symbol == matrix[row + 1][col + 1]:
            identical_matrix_count += 1

print(identical_matrix_count)
