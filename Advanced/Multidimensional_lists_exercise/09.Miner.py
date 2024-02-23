field_size = int(input())
commands = [x for x in input().split()]
mine = []
miner_pos = []  # miner_row, miner_col
collected_coal, total_coal = 0, 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(field_size):
    mine.append(input().split())

    if "s" in mine[row]:
        miner_pos = [row, mine[row].index("s")]
        mine[miner_pos[0]][miner_pos[1]] = "*"

    total_coal += mine[row].count("c")

for command in commands:
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]

    if not (0 <= r < field_size and 0 <= c < field_size):
        continue

    miner_pos = [r, c]
    if mine[r][c] == "c":
        collected_coal += 1

        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break
    elif mine[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    mine[r][c] = "*"
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")



