size = int(input())
matrix = []
jet_pos = []
jet_health = 300
enemies = 0


for row in range(size):
    matrix.append(list(input()))

    if "J" in matrix[row]:
        jet_pos = [row, matrix[row].index("J")]
        matrix[row][jet_pos[1]] = "-"

    enemies += matrix[row].count("E")


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


while True:
    command = input()

    row, col = jet_pos[0] + directions[command][0], jet_pos[1] + directions[command][1]

    if matrix[row][col] == "E":
        enemies -= 1
        matrix[row][col] = "-"
        if enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        else:
            jet_health -= 100

    elif matrix[row][col] == "R":
        jet_health = 300
        matrix[row][col] = "-"

    if jet_health <= 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
        break

    jet_pos = [row, col]

matrix[row][col] = "J"
[print(*row, sep="") for row in matrix]

