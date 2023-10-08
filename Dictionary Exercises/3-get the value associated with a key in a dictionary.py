my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_get = 'b'

value = my_dict.get(key_to_get)
if value is not None:
    print(f'Value for key {key_to_get}: {value}')
else:
    print(f'Key {key_to_get} not found in the dictionary.')
