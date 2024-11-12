# Password Generator 

import random
import string


def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    

    password = ''.join(random.choice(characters) for i in range(length))
    
    return password


def main():

    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 1:
            print("Password length must be greater than 0.")
        else:
          
            password = generate_password(length)
            print(f"Generated Password: {password}")
    
    except ValueError:
        print("Please enter a valid number for the length.")


if __name__ == "__main__":
    main()
