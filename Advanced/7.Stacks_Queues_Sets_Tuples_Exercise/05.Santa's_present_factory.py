from collections import deque


def craft_toy(magic_value):
    if magic_value == 150:
        presents_made["Doll"] += 1
    elif magic_value == 250:
        presents_made["Wooden train"] += 1
    elif magic_value == 300:
        presents_made["Teddy bear"] += 1
    elif magic_value == 400:
        presents_made["Bicycle"] += 1
    else:
        material_boxes.append(current_materials + 15)


presents_made = {
    "Bicycle": 0,
    "Doll": 0,
    "Teddy bear": 0,
    "Wooden train": 0,
}

material_boxes = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

while material_boxes and magic_levels:
    current_materials = material_boxes.pop()
    current_magic = magic_levels.popleft()
    if current_materials == 0 and current_magic == 0:
        continue
    elif current_materials == 0:
        magic_levels.appendleft(current_magic)
        continue
    elif current_magic == 0:
        material_boxes.append(current_materials)
        continue

    total_magic_level = current_magic * current_materials
    if total_magic_level < 0:
        material_boxes.append(current_materials + current_magic)
    else:
        craft_toy(total_magic_level)
if (presents_made["Doll"] > 0 and presents_made["Wooden train"] > 0) or (
        presents_made["Teddy bear"] > 0 and presents_made["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_boxes:
    print(f"Materials left: {', '.join(str(x) for x in material_boxes[::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for key, value in presents_made.items():
    if value > 0:
        print(f"{key}: {value}")
