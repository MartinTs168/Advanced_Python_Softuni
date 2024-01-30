import os

file_name = "text.txt"
path = os.path.join("text.txt", 'r')
try:
    file = open(path)
    print("File found")
except FileNotFoundError:
    print("File not found")
