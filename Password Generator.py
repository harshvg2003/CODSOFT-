import random
import string

def generate_password(length):
    # Define the character sets to generate the password from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password randomly
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of your password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated passwordṆ,,ṇ
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
