my_dict = {'a': 10, 'b': 5, 'c': 15}

max_key = max(my_dict, key=my_dict.get)
min_key = min(my_dict, key=my_dict.get)

print(f'Maximum value key: {max_key}, Minimum value key: {min_key}')
