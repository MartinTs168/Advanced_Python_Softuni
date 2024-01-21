rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for i in range(rows):
    row_elements = [int(x) for x in input().split()]
    matrix.append(row_elements)
for j in range(cols):
    current_col_sum = 0
    for i in range(rows):
        current_col_sum += matrix[i][j]
    print(current_col_sum)
