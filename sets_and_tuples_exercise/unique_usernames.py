n_lines = int(input())
usernames = set()
for _ in range(n_lines):
    usernames.add(input())
for name in usernames:
    print(name)