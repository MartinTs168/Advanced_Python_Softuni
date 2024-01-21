import sys

rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]
biggest_sum = -sys.maxsize
biggest_submatrix_coordinates = []
for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_submatrix_coordinates = [row, col]
row, col = biggest_submatrix_coordinates
print(f"{matrix[row][col]} {matrix[row][col + 1]}")
print(f"{matrix[row + 1][col]} {matrix[row + 1][col + 1]}")
print(biggest_sum)