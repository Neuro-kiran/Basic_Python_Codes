def remove_vowels(string):
    vowels = "AEIOUaeiou"
    return "".join(char for char in string if char not in vowels)

input_string = input("Enter a string: ")
without_vowels = remove_vowels(input_string)
print("String without vowels:", without_vowels)
