def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
is_sorted = is_sorted_ascending(my_list)
print("Is the list sorted in ascending order?", is_sorted)
