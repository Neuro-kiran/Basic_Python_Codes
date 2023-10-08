def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

list1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]
difference_list = list_difference(list1, list2)
print("Difference between lists:", difference_list)
