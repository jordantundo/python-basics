import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = []
    
    # Ensure at least one of each character type
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice("!@#$%^&*"))
    
    # Fill remaining characters
    for _ in range(length - 4):
        password.append(random.choice(characters))
    
    # Shuffle and return as string
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter password length (minimum 4): ") or 12)
    print("Generated Password:", generate_password(length))
