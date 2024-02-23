text = input()
try:
    repeat_text = int(input())
    print(text*repeat_text)
except ValueError:
    print("Variable times must be an integer")