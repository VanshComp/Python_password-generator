import re
import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
    

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

# Define all parameters
    
length=int(input("Enter length of your password: "))
nums=int(input("Enter length of numerical letters you want in password: "))
special_chars=int(input("Enter length of special characters you want in password: "))
uppercase=int(input("Enter length of uppercase letters you want in password: "))
lowercase=int(input("Enter length of lowercase letters you want in password: "))   

total_chars = nums + special_chars + uppercase + lowercase

if length < total_chars:
    print("Length of password is succeeded... Please select numerical letter, special characters, uppercase and lowercase just equal to length of password")
elif length > total_chars:
    print("Password is incomplete... Please select numerical letter, special characters, uppercase and lowercase just equal to length of password")
else:
    new_password = generate_password(length, nums, special_chars, uppercase, lowercase)
    print('Generated password:', new_password)