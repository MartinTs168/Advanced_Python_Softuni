def read_next(*args):
    for seq in args:
        yield from seq  # basically a loop just shorter and prettier


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
