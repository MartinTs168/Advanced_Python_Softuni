def math_operations(*args, **kwargs):
    keys = list(kwargs.keys())

    for i in range(len(args)):
        key = keys[i % 4]  # 0 % 4 = 0 and 1 % 4 = 1 so this way we use this indexing to skip ifs
        operations = {
            "a": lambda x: x + kwargs["a"],
            "s": lambda x: kwargs["s"] - x,
            "d": lambda x: kwargs["d"] / x if x != 0 else kwargs["d"],
            "m": lambda x: kwargs["m"] * x,
        }
        kwargs[key] = operations[key](args[i])
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{k}: {v:.1f}"for k, v in kwargs)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
