import json
from pathlib import Path

password_file = Path("passwords.json")

class Password:      #placeholder
    service = ""
    username = ""  
    password = ""
    valid = False

def load_passwords():
    with password_file.open("r") as file:
        return json.load(file)

def save_passwords(passwords):
    with password_file.open("w") as file:
        json.dump(passwords, file)

def menu():
    while True:
        print("\n--- PasswordTrue ---\n")
        print("1. View passwords")
        print("2. Save password")
        print("3. Generate random password")
        print("4. Delete password")
        print("5. Exit")

        choice = input("\nSelect an option by typing a number:")

        if choice == "1":
            print("to be implemented")
            print(passwords)
            #view_passwords()
        elif choice == "2":
            print("to be implemented")
            #save_password
        elif choice == "3":
            print("to be implemented")
            #generate_password
        elif choice == "4":
            print("to be implemented")
            #delete_password
        elif choice == "5":
            print("Your passwords are safe!")
            break
        else:
            print("Invalid option.")


passwords = load_passwords()

menu()

#TODO implement writing and reading of passwords from JSON files first
#TODO implement menu functions
