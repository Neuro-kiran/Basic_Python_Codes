def remove_nth_occurrence(lst, element, n):
    count = 0
    for i, item in enumerate(lst):
        if item == element:
            count += 1
            if count == n:
                del lst[i]
                break

my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
element_to_remove = int(input("Enter the element to remove: "))
occurrence_to_remove = int(input("Enter the occurrence to remove: "))
remove_nth_occurrence(my_list, element_to_remove, occurrence_to_remove)
print("List with the specified occurrence removed:", my_list)
