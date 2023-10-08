numbers = [2, 4, 6, 8, 10]
all_even = True

for num in numbers:
    if num % 2 != 0:
        all_even = False
        break

if all_even:
    print("All elements are even.")
else:
    print("Not all elements are even.")
