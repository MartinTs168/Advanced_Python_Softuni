first_length, second_length = [int(x) for x in input().split()]
first = {input() for _ in range(first_length)}
second = {input() for _ in range(second_length)}
matching_elements = first & second
print(*matching_elements, sep="\n")