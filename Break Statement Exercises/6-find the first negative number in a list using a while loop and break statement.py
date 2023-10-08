def find_first_negative(numbers):
    index = 0
    while index < len(numbers):
        if numbers[index] < 0:
            print(f"The first negative number is {numbers[index]}")
            break
        index += 1
    else:
        print("No negative numbers found in the list")

numbers = [10, 20, -5, 30, 40, -8]
find_first_negative(numbers)
