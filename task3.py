# Codsoft Internship (Task 3 as per document)
# Password Generator

import random

# Function Definition
def create_password(length):

    # Input validation
    if length <= 0 :
        print("Please enter valid password length")
        return
    
    # Characters that the consitute the password
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = ")!@#$%^&*("

    characters = lowercase + uppercase + digits + special

    # Generation of password 
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

# User input
while True :
    choice = int(input("\nEnter:\n1 to generate a new password\n2 to exit\nYour choice: "))

    if choice == 1:
        length = int(input("Enter the password length: "))
        password = create_password(length)
        print(f"Generated password: {password}")

    elif choice == 2:
        print("\nExiting password generator\n")
        break

    else: 
        print("Enter valid choice")
