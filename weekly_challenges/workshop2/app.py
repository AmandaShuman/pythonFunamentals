from banking_pkg import account, validation

# -------------------------------------------------------------
# Create an ATM application that imports from a banking package
# -------------------------------------------------------------


def atm_menu(name="", body=False):
  print("")
  print("          === Automated Teller Machine ===          ")
  if body:
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


atm_menu()
# Acquire a name and pin in order to register customer
user = validation.get_valid_name()
pin = validation.get_valid_pin()
balance = 0
print(f"{user} has been registered with a starting balance of ${balance}")

while True:
  atm_menu()
  print("LOGIN")
  # Acquire name and pin in order to validate to allow login
  name_to_validate = input("Enter name: ").capitalize()
  pin_to_validate = input("Enter PIN: ")
  if user == name_to_validate and pin == pin_to_validate:
    print("Login successful!\n")
    break
  else:
    print("Invalid credentials!, stop it\n")

# Options Menu Loop
while True:
  atm_menu(user, body=True)
  option = input("Choose an option: ")
  if option == "1":
    account.show_balance(balance)
  elif option == "2":
    balance = account.deposit(balance)
    account.show_balance(balance)
  elif option == "3":
    balance = account.withdraw(balance)
    account.show_balance(balance)
  elif option == "4":
    account.logout(user)
    break
  else:
    print("Does not compute, Please input valid inputs\n")
