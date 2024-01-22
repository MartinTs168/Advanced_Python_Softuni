n_rows = int(input())
# matrix = [[int(x) for x in input().split(", ")] for i in range(n_rows)]
# flatten = [number for sublist in matrix for number in sublist]

flatten = []
for i in range(n_rows):
    row_data = [int(x) for x in input().split(", ")]
    flatten.extend(row_data)
print(flatten)