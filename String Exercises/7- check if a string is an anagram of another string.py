def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

input_string1 = input("Enter the first string: ")
input_string2 = input("Enter the second string: ")
result = is_anagram(input_string1, input_string2)
print("Is anagram?", result)
