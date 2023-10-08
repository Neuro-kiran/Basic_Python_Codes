string = "Hello, World!"
for char in string:
    if char.isalpha() and char.lower() not in 'aeiou':
        print(char)
