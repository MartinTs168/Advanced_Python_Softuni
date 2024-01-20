lines = int(input())
elements = set()
for _ in range(lines):
    for el in input().split():
        elements.add(el)
print(*elements, sep="\n")
