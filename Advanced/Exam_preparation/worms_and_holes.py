from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

initial_number_of_worms = len(worms)

matches = 0


while holes and worms:

    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_hole == current_worm:
        matches += 1
    else:
        current_worm -= 3
        if not current_worm <= 0:
            worms.append(current_worm)


if matches:
    print(f"Matches: {matches}")
else:
    print(f"There are no matches.")


if initial_number_of_worms == matches:
    print("Every worm found a suitable hole!")
elif not worms:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")


if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")





