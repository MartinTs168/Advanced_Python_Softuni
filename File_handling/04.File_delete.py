import os

path = os.path.join("my_first_file.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File is already deleted")