from collections import Counter

def most_frequent_char(string):
    char_count = Counter(string)
    return max(char_count, key=char_count.get)

input_string = input("Enter a string: ")
most_frequent = most_frequent_char(input_string)
print("Most frequent character:", most_frequent)
