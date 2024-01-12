stack = []
num_lines = int(input())
for _ in range(num_lines):
    query = input().split()
    command = query[0]
    if command == '1':
        stack.append(int(query[1]))
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command == '4':
        if stack:
            print(min(stack))
stack.reverse()
print(*stack, sep=", ")



