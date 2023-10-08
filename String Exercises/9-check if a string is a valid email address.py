import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

email = input("Enter an email address: ")
valid = is_valid_email(email)
print("Is valid email?", valid)
