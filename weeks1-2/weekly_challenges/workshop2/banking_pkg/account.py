def show_balance(balance):
    print(f"Current Balance: ${balance:.2f}")


def deposit(balance):
  while True:
    amount = input("What do you wanna give me?: ")
    if float(amount) == False:
      print("\nPlease enter a numeric value and enjoy our rare courtesy\n")
    else:
      return float(amount) + balance


def withdraw(balance):
    while True:
      money = input("Enter amount to withdraw?: ")
      if money.isnumeric() == False:
        print("\nPlease enter a whole number value.\n")
      elif balance - float(money) < 0:
        print("\nYou popper! Please proceed to the loan officer, you don't have that kind of money bro!\n")
      else:
        return balance - float(money)


def logout(name):
    print(
        f"Get OUT {name}! And don't come back Jack! Best from your friendly neighborhood bank: YEET of America, YOA LLC"
    )
