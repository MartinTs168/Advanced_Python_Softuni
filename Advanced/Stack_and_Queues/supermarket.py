from collections import deque

customers = deque()
while True:
    name = input()
    if name == 'End':
        break
    if name == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(name)
print(f"{len(customers)} people remaining.")
