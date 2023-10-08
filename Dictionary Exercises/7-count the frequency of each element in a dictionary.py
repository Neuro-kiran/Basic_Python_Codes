my_dict = {'a': 2, 'b': 3, 'c': 2, 'd': 4}
frequency_dict = {}

for key, value in my_dict.items():
    if value in frequency_dict:
        frequency_dict[value].append(key)
    else:
        frequency_dict[value] = [key]

print(frequency_dict)
