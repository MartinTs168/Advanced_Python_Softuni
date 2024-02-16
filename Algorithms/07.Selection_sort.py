def selection_sort(nums):
    for idx in range(len(nums)):
        min_index = idx

        for current_index in range(idx + 1, len(nums)):
            if nums[current_index] < nums[min_index]:
                min_index = current_index

        nums[idx], nums[min_index] = nums[min_index], nums[idx]


numbers = [int(x) for x in input().split()]
selection_sort(numbers)
print(*numbers)

