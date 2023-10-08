def sort_strings_alphabetically(lst):
    return sorted(lst)

my_list = input("Enter a list of strings separated by spaces: ").split()
sorted_list = sort_strings_alphabetically(my_list)
print("Sorted list:", sorted_list)
