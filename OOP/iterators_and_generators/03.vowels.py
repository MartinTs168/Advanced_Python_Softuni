class vowels:
    VOWELS_LIST = ['a', 'e', 'o', 'u', 'i', 'y']

    def __init__(self, string):
        self.string = string
        self.index = -1
        self.vowels_values = [x for x in self.string if x.lower() in self.VOWELS_LIST]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
