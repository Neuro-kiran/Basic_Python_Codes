def find_substring_index(text, substring):
    index = 0
    while index < len(text):
        if text[index:index + len(substring)] == substring:
            print(f"The substring '{substring}' found at index {index}")
            break
        index += 1
    else:
        print(f"The substring '{substring}' is not in the string")

text = "Hello, World!"
substring = "World"
find_substring_index(text, substring)
