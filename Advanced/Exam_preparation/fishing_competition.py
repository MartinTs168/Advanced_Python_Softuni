def check_boat_out_of_range(curr_row, curr_col):
    def move_boat_to_opposite_side(value):
        value = size - abs(value)
        return value

    if curr_row < 0 or curr_row >= size:
        curr_row = move_boat_to_opposite_side(curr_row)
    elif curr_col < 0 or curr_col >= size:
        curr_col = move_boat_to_opposite_side(curr_col)

    return curr_row, curr_col


size = int(input())
matrix = []
boat_pos = []
total_fish_caught = 0
FISH_NEEDED = 20

for row in range(size):
    matrix.append(list(input()))

    if "S" in matrix[row]:
        boat_pos = [row, matrix[row].index("S")]
        matrix[row][boat_pos[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()
while command != "collect the nets":

    row, col = boat_pos[0] + directions[command][0], boat_pos[1] + directions[command][1]
    row, col = check_boat_out_of_range(row, col)
    if matrix[row][col] == "W":
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{col}]")
        break

    elif matrix[row][col].isdigit():
        total_fish_caught += int(matrix[row][col])
        matrix[row][col] = "-"
    boat_pos = [row, col]

    command = input()

else:
    matrix[boat_pos[0]][boat_pos[1]] = "S"
    if total_fish_caught >= FISH_NEEDED:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't "
              f"reach the quota! You need {FISH_NEEDED - total_fish_caught} tons of fish more.")
    if total_fish_caught > 0:
        print(f"Amount of fish caught: {total_fish_caught} tons.")

    [print(*row, sep="") for row in matrix]

