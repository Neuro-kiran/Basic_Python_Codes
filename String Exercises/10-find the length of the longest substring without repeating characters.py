def longest_substring_length(string):
    char_index = {}
    max_length = start = 0

    for i, char in enumerate(string):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

input_string = input("Enter a string: ")
length = longest_substring_length(input_string)
print("Length of longest substring without repeating characters:", length)
