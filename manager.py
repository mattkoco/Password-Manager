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
        print("1. Store Password")
        print("2. Retrieve Password")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            service = input("Enter the name of the service (Twitter, Instagram, etc.): ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            store_password(service, username, password)
            print(f"Password for {service} stored successfully.")
        
        elif choice == "2":
            service = input("Enter the name of the service you would like to retrieve your credentials for: ")
            credentials = retrieve_password(service)
            if isinstance(credentials, dict):
                print(f"Username: {credentials['username']}\nPassword: {credentials['password']}")
            else:
                print(credentials)
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Function to generate a random secure password coming soon...
