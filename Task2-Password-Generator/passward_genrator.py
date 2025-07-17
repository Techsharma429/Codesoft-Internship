import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)