# -------------------------
# User Validation Functions
# -------------------------
def get_valid_name():
  while True:
    user = input("Enter name to register: ").capitalize()
    if len(user) == 0:
      print("Enter a name dummy! \n")
    elif len(user) > 10:
      print("\nThat is too long, shorter please. We cannot afford this data. Your membership only pays for up to 10 characters. Your money is important to us!\n")
    else:
      return user


def get_valid_pin():
  while True:
    pin = input("Enter PIN: ")
    if len(pin) == 0:
      print("\nWhere is your pin? We need something that is not in imagainary land. Please enter 4 digit-pin. \n")
    elif pin.isnumeric() == False:
      print("\nHow did you get letters in here?!?! Numbers only, you fool! We graciously accept numbers only. Try again.\n")
    elif len(pin) != 4:
      print("\nYou fool, only 4 digits, not FDIC approved. Try again.\n")
    else:
      return pin
