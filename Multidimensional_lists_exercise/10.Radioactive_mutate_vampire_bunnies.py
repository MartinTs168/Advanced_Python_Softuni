import copy

rows, cols = [int(x) for x in input().split()]
matrix = []
player_pos = []
directions = {
    "L": [0, -1],
    "R": [0, 1],
    "D": [1, 0],
    "U": [-1, 0],
}
for row in range(rows):
    matrix.append(list(input()))

    if "P" in matrix[row]:
        player_pos = [row, matrix[row].index("P")]
        matrix[player_pos[0]][player_pos[1]] = "."


final_message = ""
player_won = False
matrix_copy = copy.deepcopy(matrix)

commands = list(input())
for command in commands:
    r, c = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]
    if r < 0 or r >= rows or c < 0 or c >= cols:
        final_message = f"won: {player_pos[0]} {player_pos[1]}"
        player_won = True
    else:
        player_pos = [r, c]
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                if 0 <= (col - 1) < cols:
                    matrix_copy[row][col - 1] = "B"
                if 0 <= (col + 1) < cols:
                    matrix_copy[row][col + 1] = "B"
                if 0 <= (row - 1) < rows:
                    matrix_copy[row - 1][col] = "B"
                if 0 <= (row + 1) < rows:
                    matrix_copy[row + 1][col] = "B"

    if player_won:
        matrix = copy.deepcopy(matrix_copy)
        break
    elif matrix_copy[player_pos[0]][player_pos[1]] == "B":
        final_message = f"dead: {player_pos[0]} {player_pos[1]}"
        matrix = copy.deepcopy(matrix_copy)
        break
    matrix = copy.deepcopy(matrix_copy)

# noinspection PyUnboundLocalVariable
[print(*row, sep="") for row in matrix]
print(final_message)
