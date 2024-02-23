longest_intersection = set()
for _ in range(int(input())):
    range1, range2 = input().split("-")
    start1, end1 = [int(x) for x in range1.split(",")]
    first_set = set(range(start1, end1 + 1))
    start2, end2 = [int(x) for x in range2.split(",")]
    second_set = set(range(start2, end2 + 1))
    new_intersection = first_set & second_set
    if len(new_intersection) > len(longest_intersection):
        longest_intersection = new_intersection

print(
    f"Longest intersection is [{', '.join(str(n) for n in longest_intersection)}] with length {len(longest_intersection)}")
