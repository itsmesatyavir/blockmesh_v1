import os
import subprocess

# ANSI Escape Codes for Bright Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def display_menu():
    print(CYAN + "\nF O R E S T A R M Y -BLOCKMESH SETUP TOOL" + RESET)
    print(YELLOW + "[1] Account Setup" + RESET)
    print(YELLOW + "[2] Proxy Setup" + RESET)
    print(YELLOW + "[3] Run Script" + RESET)
    print(YELLOW + "[4] Exit" + RESET)

def account_setup():
    num_accounts = int(input(GREEN + "How many accounts do you want to save? " + RESET))
    
    with open("emails.txt", "a") as email_file, open("passwords.txt", "a") as pass_file:
        for i in range(num_accounts):
            email = input(YELLOW + f"Enter Email {i+1}: " + RESET)
            password = input(YELLOW + f"Enter Password {i+1}: " + RESET)
            email_file.write(email + "\n")
            pass_file.write(password + "\n")
    
    print(GREEN + "Accounts saved successfully!" + RESET)

def proxy_setup():
    proxy = input(YELLOW + "Enter Proxy (Format: http://user:pass@host:port): " + RESET)
    
    with open("proxies.txt", "a") as proxy_file:
        proxy_file.write(proxy + "\n")
    
    print(GREEN + "Proxy saved successfully!" + RESET)

def run_script():
    print(CYAN + "Running runBlock.js..." + RESET)
    subprocess.run(["node", "runBlock.js"])

while True:
    display_menu()
    choice = input(YELLOW + "Select an option: " + RESET)
    
    if choice == "1":
        account_setup()
    elif choice == "2":
        proxy_setup()
    elif choice == "3":
        run_script()
    elif choice == "4":
        print(RED + "Exiting..." + RESET)
        break
    else:
        print(RED + "Invalid choice! Please try again." + RESET)