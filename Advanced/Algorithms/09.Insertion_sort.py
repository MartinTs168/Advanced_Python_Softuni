def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        # докато не стигнем началото и
        # докато не стигнем на позиция на която да поставим ключа
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key


numbers = [int(x) for x in input().split()]
insertion_sort(numbers)
print(*numbers)

