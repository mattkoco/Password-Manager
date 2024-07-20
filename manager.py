import random
import string
import json
import os

print("""
made by:      
   _______   ____ ___ 
  ╱       ╲╲╱    ╱   ╲
 ╱        ╱╱         ╱
╱         ╱╱       _╱ 
╲__╱__╱__╱╲╲___╱___╱ 
""")

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    password += random.choices(all_characters, k=length-3)
    
    random.shuffle(password)
    
    return ''.join(password)

def store_password(service, username, password):
    filename = "passwords.json"

    if os.path.exists(filename):
        with open(filename, "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}
    
    passwords[service] = {"username": username, "password": password}
    
    with open(filename, "w") as file:
        json.dump(passwords, file, indent=4)

def retrieve_password(service):
    filename = "passwords.json"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            passwords = json.load(file)
        
        if service in passwords:
            return passwords[service]
        else:
            return "Service not found."
    else:
        return "No passwords stored yet."

# Main function to determine user input
def main():
    while True:
        print("\nPassword Manager")
        print("1. Generate Password")
        print("2. Store Password")
        print("3. Retrieve Password")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            length = int(input("Enter the length of the password you want: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        
        elif choice == "2":
            service = input("Enter the name of the service (Twitter, Instagram, etc.): ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            store_password(service, username, password)
            print(f"Password for {service} stored successfully.")
        
        elif choice == "3":
            service = input("Enter the name of the service you would like to retrieve your credentials for: ")
            credentials = retrieve_password(service)
            if isinstance(credentials, dict):
                print(f"Username: {credentials['username']}\nPassword: {credentials['password']}")
            else:
                print(credentials)
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
