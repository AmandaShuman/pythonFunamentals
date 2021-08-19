from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
user = input("Enter name to register: ")
account.name_validation(user)
pin = input("Enter PIN: ")
account.pin_validation(pin)
balance = 0
print(f"{user.capitalize()} has been registered with a starting balance of ${balance:.2f}")

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    user_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if user.lower() == user_to_validate.lower() and pin == pin_to_validate:
        print("Login successful!")
        break
    else: 
        print("Invalid credentials. Try again.")

while True:
    atm_menu(user)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        if balance == 0:
            print("You do not have any money in your account to make a withdrawal.")
            continue
        else:
            balance = account.withdraw(balance)
            account.show_balance(balance)
    elif option == "4": 
        account.logout(user)
        break
    else:
        print("Invalid option. Please try again.")
