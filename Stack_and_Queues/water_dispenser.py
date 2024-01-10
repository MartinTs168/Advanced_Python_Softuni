from collections import deque

water_quantity = int(input())
people = deque()
while True:
    name = input()
    if name == 'Start':
        break
    else:
        people.append(name)

command = input()
while command != 'End':
    if command.startswith('refill'):
        water_quantity += int(command.split()[1])
    else:
        if water_quantity >= int(command):
            water_quantity -= int(command)
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    command = input()
print(f"{water_quantity} liters left")

