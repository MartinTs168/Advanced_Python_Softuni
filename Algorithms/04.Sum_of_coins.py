def choose_coins(coins, target):
    coins.sort(reverse=True)
    index = 0
    used_coins = {}

    while target > 0 and index < len(coins):
        count_current_coins = target // coins[index]
        target = target % coins[index]

        if count_current_coins > 0:
            used_coins[coins[index]] = count_current_coins

        index += 1

    if target != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"

        for coin, count in used_coins.items():
            result += f"{count} coin(s) with value {coin}\n"

        return result


coins = [int(x) for x in input().split(", ")]
target = int(input())
print(choose_coins(coins, target))
