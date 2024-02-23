def set_cover(universe, sets):
    chosen_sets = []

    while universe:
        best_set = max(sets, key=lambda s: len(universe.intersection(s)))
        chosen_sets.append(best_set)
        universe -= best_set

    return chosen_sets


universe = {int(x) for x in input().split(", ")}
num_sets = int(input())
sets = [{int(x) for x in input().split(", ")} for _ in range(num_sets)]


chosen_sets = set_cover(universe, sets)

for i in range(len(chosen_sets)):
    chosen_sets[i] = sorted(chosen_sets[i])

print(f"Sets to take ({len(chosen_sets)}):")
[print("{ " + f"{', '.join(str(s) for s in _set)}" + " }") for _set in chosen_sets]

