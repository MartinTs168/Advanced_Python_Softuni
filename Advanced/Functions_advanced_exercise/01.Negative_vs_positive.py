def split_numbers(numbers):
    negative_list = []
    positive_list = []
    for num in numbers:
        if num < 0:
            negative_list.append(num)
        else:
            positive_list.append(num)
    return negative_list, positive_list


numbers_input = [int(x) for x in input().split()]
negative_numbers, positive_numbers = split_numbers(numbers_input)
negative_sum = sum(negative_numbers)
positive_sum = sum(positive_numbers)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
