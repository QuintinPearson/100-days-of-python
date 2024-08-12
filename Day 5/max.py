# Find the max number in a list of numbers

numbers = [10, 233, 234, 98, 9238, 92, 98, 96, 39, 123, 34, 98]

biggest_num = 0

for num in numbers:
    if num > biggest_num:
        biggest_num = num


print(biggest_num)