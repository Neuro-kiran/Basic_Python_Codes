def second_largest(lst):
    if len(lst) < 2:
        return None
    sorted_list = sorted(set(lst), reverse=True)
    return sorted_list[1]

my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
second_largest_val = second_largest(my_list)
print("Second largest element:", second_largest_val)
