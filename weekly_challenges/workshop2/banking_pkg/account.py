def show_balance(balance):
    print(f"Current Balance: ${balance:.2f}")

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return float(amount) + balance

def withdraw(balance):
    while True:
        amount = input("Enter amount to withdraw: ")
        if float(amount) <= balance:
            return balance - float(amount)
        else: 
            print("Insufficient funds for withdrawal request. Please request a different amount.")
            show_balance(balance)
            continue

def logout(name):
    print("Goodbye", name +"!")

def name_validation(user):
    while True:
        if len(user) == 0:
            print("You must enter a name")
            user = input("Enter name to register: ")
        elif len(user) >10:
            print("The maximum length is 10 characters")
            user = input("Enter name to register: ")
        else:
            break

def pin_validation(pin):
    while True:
        if len(pin) != 4:
            print("PIN must contain 4 numbers")
            pin = input("Enter PIN: ")
        else:
            break
