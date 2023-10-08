from collections import Counter

def first_non_repeating_char(string):
    char_count = Counter(string)
    for char in string:
        if char_count[char] == 1:
            return char
    return None

input_string = input("Enter a string: ")
non_repeating = first_non_repeating_char(input_string)
print("First non-repeating character:", non_repeating)
