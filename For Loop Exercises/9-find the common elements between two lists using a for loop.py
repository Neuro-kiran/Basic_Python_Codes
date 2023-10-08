list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)

print("Common elements:", common_elements)
