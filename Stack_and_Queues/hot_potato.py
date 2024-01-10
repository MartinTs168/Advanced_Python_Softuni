from collections import deque


children = deque(input().split())
n = int(input())
counter = 1
while len(children) > 1:
    if counter == n:
        print(f"Removed {children.popleft()}")
        counter = 1
    else:
        children.rotate(-1)
        counter += 1
    
print(f"Last is {children.popleft()}")
