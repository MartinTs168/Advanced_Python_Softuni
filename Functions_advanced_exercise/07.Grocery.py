def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    result = []

    for product, quantity in kwargs:
        result.append(f"{product}: {quantity}")
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
