import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[@$!%*?&]", password):
        return False
    return True

password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")

