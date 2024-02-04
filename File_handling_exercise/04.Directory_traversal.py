import os


def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split('.')[-1]

            extensions[extension] = extensions.get(extension, []) + [filename]
        elif os.path.isdir(file):
            save_extensions(file)


directory = input()
extensions = {}  # {py: [python.py]}
result = []
try:
    save_extensions(directory)
except FileNotFoundError:
    print("Directory not found!")
extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("files/report.txt", "w") as report:
    report.write("\n".join(result))



