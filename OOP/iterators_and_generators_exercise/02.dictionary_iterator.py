class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count < len(self.items):
            return self.items[self.count]

        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)


