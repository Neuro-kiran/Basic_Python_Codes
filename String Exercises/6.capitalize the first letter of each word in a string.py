def capitalize_words(string):
    return " ".join(word.capitalize() for word in string.split())

input_string = input("Enter a string: ")
capitalized_str = capitalize_words(input_string)
print("Capitalized string:", capitalized_str)
