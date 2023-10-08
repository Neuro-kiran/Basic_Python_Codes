my_list = [2, 4, 6, 8, 10]
index = 0
all_even = True
while index < len(my_list):
    if my_list[index] % 2 != 0:
        all_even = False
        break
    index += 1
if all_even:
    print("All elements are even.")
else:
    print("Not all elements are even.")
