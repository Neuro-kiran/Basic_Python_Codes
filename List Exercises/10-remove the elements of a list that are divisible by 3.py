def remove_divisible_by_3(lst):
    return [x for x in lst if x % 3 != 0]

my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
result = remove_divisible_by_3(my_list)
print("List with elements divisible by 3 removed:", result)
