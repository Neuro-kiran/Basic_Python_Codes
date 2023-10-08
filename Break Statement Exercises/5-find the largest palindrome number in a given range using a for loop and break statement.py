def is_palindrome(num):
    return str(num) == str(num)[::-1]

largest_palindrome = 0
for num in range(1000, 0, -1):
    if is_palindrome(num):
        largest_palindrome = num
        break

print(f"The largest palindrome number in the given range is {largest_palindrome}")
