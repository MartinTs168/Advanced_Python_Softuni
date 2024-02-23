even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    name = input()
    name_value = sum(ord(z) for z in name) // row
    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

even_set_sum = sum(even_set)
odd_set_sum = sum(odd_set)
if even_set_sum == odd_set_sum:
    print(*even_set.union(odd_set), sep=", ")
elif odd_set_sum > even_set_sum:
    print(*odd_set.difference(even_set), sep=", ")
elif even_set_sum > odd_set_sum:
    print(*even_set.symmetric_difference(odd_set), sep=", ")
