import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True): #function to generate a paswword
    characters = string.ascii_letters  # includes uppercase and lowercase letters by default
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    password_length = int(input("Enter the length of the password (0 to exit): "))

    if password_length == 0: #to check if user wants to exit
        break

    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(password_length, use_digits, use_special_chars) #generates and displays the password
    print("Generated Password: " + password)
