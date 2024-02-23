def eat_cookie(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighbourhood[r][c].isalpha():
            if neighbourhood[r][c] == "V":
                nice_kids += 1
            neighbourhood[r][c] = "-"
            presents_left -= 1
        if not presents_left:
            break

    return presents_left, nice_kids


num_of_presents = int(input())
size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

neighbourhood = []
santa_pos = []

total_nice_kids = 0
nice_kids_visited = 0

for row in range(size):
    line = input().split()
    neighbourhood.append(line)

    if "S" in line:
        santa_pos = [row, line.index("S")]
        neighbourhood[row][santa_pos[1]] = "-"

    total_nice_kids += line.count("V")

command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]
    house = neighbourhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        num_of_presents -= 1
    elif house == "C":
        num_of_presents, nice_kids_visited = eat_cookie(num_of_presents, nice_kids_visited)

    neighbourhood[santa_pos[0]][santa_pos[1]] = "-"
    if not num_of_presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

neighbourhood[santa_pos[0]][santa_pos[1]] = "S"

if not num_of_presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in neighbourhood]

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")