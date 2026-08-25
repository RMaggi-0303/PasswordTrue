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

passwords = load_passwords()

print(passwords)

#TODO implement writing and reading of passwords from JSON files first
