rows, cols = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0
for i in range(rows):
    row_elements = [int(x) for x in input().split(", ")]
    total_sum += sum(row_elements)
    matrix.append(row_elements)

print(total_sum)
print(matrix)
