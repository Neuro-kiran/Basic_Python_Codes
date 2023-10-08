def sum_of_elements(lst):
    return sum(lst)

my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
result = sum_of_elements(my_list)
print("Sum of elements:", result)
