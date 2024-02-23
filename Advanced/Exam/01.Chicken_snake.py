from collections import deque

money = [int(x) for x in input().split()]
prices = deque(int(x) for x in input().split())
foods_eaten = 0

change = 0

while money and prices:

    current_price = prices.popleft()
    current_money = money.pop() + change
    change = 0

    if current_price == current_money:
        foods_eaten += 1

    elif current_money > current_price:
        change = current_money - current_price
        foods_eaten += 1


if foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")

elif foods_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")

else:
    if foods_eaten == 1:
        print(f"Henry ate: {foods_eaten} food.")
    else:
        print(f"Henry ate: {foods_eaten} foods.")