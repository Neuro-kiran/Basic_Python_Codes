def find_first_vowel(text):
    for index, char in enumerate(text):
        if char.lower() in 'aeiou':
            print(f"The first vowel '{char}' is at index {index}")
            break
    else:
        print("No vowels found in the string")

text = "Hello, World!"
find_first_vowel(text)
