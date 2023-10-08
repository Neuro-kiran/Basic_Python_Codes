my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
largest = my_list[0]
index = 1
while index < len(my_list):
    if my_list[index] > largest:
        largest = my_list[index]
    index += 1
print("Largest element:", largest)
