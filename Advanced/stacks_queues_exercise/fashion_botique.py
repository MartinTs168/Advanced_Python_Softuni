clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

racks_count = 1
current_rack_capacity = rack_capacity
while clothes:
    # if current_rack_load == rack_capacity:
    #     racks_count += 1
    #     current_rack_load = 0
    current_cloth = clothes.pop()

    if current_rack_capacity >= current_cloth:
        current_rack_capacity -= current_cloth
    else:
        racks_count += 1
        current_rack_capacity = rack_capacity - current_cloth


print(racks_count)

