def remove_duplicates(lst):
    return list(set(lst))

my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
result = remove_duplicates(my_list)
print("List with duplicates removed:", result)
