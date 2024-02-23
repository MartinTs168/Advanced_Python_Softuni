from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_indexes = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

message = ""
reached_altitudes = []

for index in range(1, len(fuel_needed) + 1):
    current_fuel = initial_fuel.pop()
    current_consumption = consumption_indexes.popleft()
    fuel_left = current_fuel - current_consumption

    curr_fuel_needed = fuel_needed.popleft()

    if fuel_left < curr_fuel_needed:
        print(f"John did not reach: Altitude {index}")
        message = "John failed to reach the top."
        break

    print(f"John has reached: Altitude {index}")
    reached_altitudes.append(f"Altitude {index}")

else:
    message = "John has reached all the altitudes and managed to reach the top!"
    print(message)
    raise SystemExit

if index == 1:
    message += "\nJohn didn't reach any altitude."
else:
    message += f"\nReached altitudes: {', '.join(reached_altitudes)}"

print(message)
