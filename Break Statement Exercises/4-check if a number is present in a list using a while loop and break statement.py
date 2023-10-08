def check_number_in_list(numbers, target):
    found = False
    index = 0
    while index < len(numbers):
        if numbers[index] == target:
            found = True
            break
        index += 1
    if found:
        print(f"{target} is in the list")
    else:
        print(f"{target} is not in the list")

numbers = [10, 20, 30, 40, 50, 60]
target = 30
check_number_in_list(numbers, target)
