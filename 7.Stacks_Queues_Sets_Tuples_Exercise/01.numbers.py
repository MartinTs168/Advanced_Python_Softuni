sequence1 = set(int(x) for x in input().split())
sequence2 = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    if first_command == 'Add':
        if second_command == 'First':
            [sequence1.add(int(x)) for x in data]
        elif second_command == 'Second':
            [sequence2.add(int(x)) for x in data]
    elif first_command == 'Remove':
        if second_command == 'First':
            [sequence1.discard(int(number)) for number in data]
        elif second_command == 'Second':
            [sequence2.discard(int(number)) for number in data]
    elif first_command + " " + second_command == 'Check Subset':
        print(sequence1.issubset(sequence2) or sequence2.issubset(sequence1))

print(*sorted(sequence1), sep=', ')
print(*sorted(sequence2), sep=', ')
