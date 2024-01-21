n_rows = int(input())
diagonal_sum = 0
for i in range(n_rows):
    row_data = [int(x) for x in input().split()]
    diagonal_sum += row_data[i]
print(diagonal_sum)