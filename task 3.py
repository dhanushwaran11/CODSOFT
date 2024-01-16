import random
import string

def codsoft(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("*****************************************Password Generator******************************************5555")
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            print("Please enter a valid positive length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    password = codsoft(password_length)
    print("\nGenerated Password: ", password)

if __name__ == "__main__":
    main()
