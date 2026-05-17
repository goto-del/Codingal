import random
import string

def generate_password(length=12):
    """Generates a random password with upper, lower, and numeric characters."""
    
    # Define the character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    
    # Ensure we have at least one character from each required set
    password_list = [
        random.choice(lowercase_chars),
        random.choice(uppercase_chars),
        random.choice(number_chars)
    ]
    
    # Combine all allowed characters for the remaining length
    all_allowed_chars = lowercase_chars + uppercase_chars + number_chars
    
    # Fill the rest of the password length
    remaining_length = length - 3
    for _ in range(remaining_length):
        password_list.append(random.choice(all_allowed_chars))
        
    # Shuffle the characters using the random module so it isn't predictable
    random.shuffle(password_list)
    
    # Convert the list of characters back into a string
    password = "".join(password_list)
    return password

if __name__ == "__main__":
    print("--- Random Password Generator ---")
    try:
        user_input = input("Enter password length (press Enter for default 12): ")
        pw_length = int(user_input) if user_input.strip() else 12
        
        if pw_length < 3:
            print("Error: Password length must be at least 3 to include uppercase, lowercase, and numbers.")
        else:
            new_password = generate_password(pw_length)
            print(f"\nYour generated password is: {new_password}")
            
    except ValueError:
        print("Error: Please enter a valid number for the length.")
