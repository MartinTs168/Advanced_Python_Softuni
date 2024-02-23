size = int(input())
collected_tea_bags = 0
alice_pos = []
wonderland = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    wonderland.append(input().split())

    if 'A' in wonderland[row]:
        alice_pos = [row, wonderland[row].index("A")]
        wonderland[alice_pos[0]][alice_pos[1]] = "*"


command = input()
while command != "":

    r, c = alice_pos[0] + directions[command][0], alice_pos[1] + directions[command][1]
    if not (0 <= r < size and 0 <= c < size):
        wonderland[alice_pos[0]][alice_pos[1]] = "*"
        print("Alice didn't make it to the tea party.")
        break

    if wonderland[r][c].isdigit():
        collected_tea_bags += int(wonderland[r][c])
    elif wonderland[r][c] == 'R':
        wonderland[r][c] = "*"
        print("Alice didn't make it to the tea party.")
        break

    alice_pos = [r, c]
    wonderland[r][c] = "*"

    if collected_tea_bags >= 10:
        print("She did it! She went to the party.")
        break

    command = input()

[print(*row) for row in wonderland]
