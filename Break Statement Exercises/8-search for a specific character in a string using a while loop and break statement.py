def search_character(text, char):
    index = 0
    while index < len(text):
        if text[index] == char:
            print(f"{char} found at position {index}")
            break
        index += 1
    else:
        print(f"{char} is not in the string")

text = "Hello, World!"
char = 'o'
search_character(text, char)
