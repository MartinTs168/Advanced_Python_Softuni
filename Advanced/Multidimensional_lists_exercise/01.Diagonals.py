n_rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n_rows)]
primary = [matrix[r][r] for r in range(n_rows)]
secondary = [matrix[r][n_rows - r -1] for r in range(n_rows)]
print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")