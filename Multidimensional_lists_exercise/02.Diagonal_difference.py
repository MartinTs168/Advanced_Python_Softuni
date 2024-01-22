# n_rows = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n_rows)]
#
# sum_primary, sum_secondary = 0, 0
# for i in range(n_rows):
#     sum_primary += matrix[i][i]
#     sum_secondary += matrix[i][n_rows - i - 1]
#
# result = abs(sum_primary - sum_secondary)
# print(result)

# Solution 2 optimal solution because it is faster due to the existence of only 2 loops
n_rows = int(input())

sum_primary, sum_secondary = 0, 0
for i in range(n_rows):
    line = [int(x) for x in input().split()]
    sum_primary += line[i]
    sum_secondary += line[n_rows - i - 1]

result = abs(sum_primary - sum_secondary)
print(result)
