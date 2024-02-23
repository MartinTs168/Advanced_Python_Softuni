rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for i in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] == "swap" and len(command) == 5:
        row1, col1, row2, col2 = [int(x) for x in command[1::]]
        if row1 < rows and row2 < rows and col1 < cols and col2 < cols:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]
        else:
            print("Invalid input!")
            continue
    else:
        print("Invalid input!")
        continue
