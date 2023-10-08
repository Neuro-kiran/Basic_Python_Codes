def find_first_occurrence(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            print(f"The first occurrence of {target} is at index {i}.")
            break
    else:
        print(f"{target} not found in the list.")

numbers = [10, 20, 30, 40, 50, 60]
target = 30
find_first_occurrence(numbers, target)
