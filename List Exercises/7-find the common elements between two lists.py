def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

list1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]
common_elements_list = common_elements(list1, list2)
print("Common elements:", common_elements_list)
