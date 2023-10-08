def print_until_condition(numbers, condition):
    for num in numbers:
        if num == condition:
            break
        print(num, end=' ')

numbers = [10, 20, 30, 40, 50, 60, 30, 70]
condition = 30
print_until_condition(numbers, condition)
