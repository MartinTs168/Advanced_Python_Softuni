from collections import deque


food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))

for current_order in orders.copy():
    if food_quantity >= current_order:
        food_quantity -= current_order
        orders.popleft()
    else:
        print(f"Orders left:", *orders)
        break
else:
    print("Orders complete")