class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def spaces_or_equal_check(self, item):
        if ' ' in item:
            print("Cannot contain empty spaces. Change cancelled.")
            return False
        if self.name == item or self.pin == item or self.password == item:
            print("This is the same as before. Pick a new one!")
        else:
            return True

    def change_name(self, name):
        name = name.strip()  # remove beginning/end spaces
        if self.spaces_or_equal_check(name):        
            if 2 <= len(name) <= 10:
                self.name = name
                return self.name
            else:
                print("New names must be between 2 and 10 characters long.")

    def change_pin(self, pin):
        pin = pin.strip()
        if self.spaces_or_equal_check(pin):
            if len(pin) == 4 and type(pin) is int:
                self.pin = pin
                return self.pin
            else:
                print("PINs must be 4 numbers.")

    def change_password(self, password):
        if self.spaces_or_equal_check(password):
            if len(password) >= 5:
                self.password = password
                return self.password
            else:
                print("Passwords must be at least 5 characters long.")


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    # ========================================================
    # methods to check for valid inputs - BONUS 1 & 2
    # ========================================================
    def value_check(self, amt):
        if not (type(amt) is float or type(amt) is int):
            print("You must enter a number.")
            return False
        elif amt < 0:
            print("You need to enter a positive number")
            return False
        else:
            return True

    def enough_money_check(self, amt):
        if amt > self.balance:
            print("You do not have enough money to proceed with this transaction.")
            return False
        else:
            return True

    def password_check(self, pin_check):
        if str(self.pin) == pin_check:
            return True
        else:
            print("Invalid PIN. Transaction cancelled.")
            return False

    def switch_on_hold(self):
        if self.on_hold == True:
            self.on_hold = False
        else:
            self.on_hold = True

    def check_on_hold(self):
        if self.on_hold == True:
            print("Account is on hold. You cannot complete this transaction. Please see manager for assistance.")
            return False
        else:
            return True

    # =============================================================
    # methods to withdraw, deposit, transfer, and request money
    # =============================================================
    def show_balance(self):
        if self.check_on_hold():
            print(f"{self.name} has a balance of: ${self.balance:.2f}")  # <= BONUS Task 4

    def withdraw(self, amt):
        if self.check_on_hold() and self.value_check(amt) and self.enough_money_check(amt):
            self.balance -= amt
            return self.balance

    def deposit(self, amt):
        if self.value_check(amt) and self.check_on_hold():
            self.balance += amt
            return self.balance

    def transfer_money(self, user, amt):
        if self.value_check(amt) and self.check_on_hold():  # first check if valid input and on hold or not
            print("\nYou are transferring $" + str(amt), "to", user.name)
            print("Authentication required")
            pin_check = input("Enter your PIN: ")
            if self.password_check(pin_check):  # check if pw match
                print("Transfer authorized")
                print(f"Transferring ${amt:.2f} to {user.name}")
                if self.enough_money_check(amt) and user.check_on_hold():  # check if enough money and user on hold
                    self.withdraw(amt)
                    user.deposit(amt)
                    return True
                else:
                    return False

    def request_money(self, user, amt):
        if self.value_check(amt) and self.check_on_hold():
            print(f"\nYou are requesting ${amt:.2f} from {user.name}")
            print("User authentication is required...")
            pin_check = input(f"Enter {user.name}'s PIN: ")
            if user.password_check(pin_check):
                pw_check = input("Enter your password: ")
                if pw_check == self.password:
                    print("Request authorized")
                    print(f"{user.name} sent ${amt:.2f}")
                    if user.enough_money_check(amt) and user.check_on_hold():
                        user.withdraw(amt)
                        self.deposit(amt)
                        return True
                else:
                    print("Invalid password. Transaction cancelled.")
                    return False


""" Driver Code for Task 1 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Bobby")
# user1.change_pin(4321)
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 3"""
# user1 = BankUser("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password, user1.balance)

""" Driver Code for Task 4"""
# user1 = BankUser("Bob", 1234, "password")
# user1.show_balance()
# user1.deposit(100)
# user1.show_balance()
# user1.withdraw(25.32)
# user1.show_balance()

""" Driver Code for Task 5"""
# user1 = BankUser("Bob", 1234, "password")
# user2 = BankUser("Alice", 1223, "happy")
# user2.deposit(5000)
# user2.show_balance()
# user1.show_balance()
# valid = user2.transfer_money(user1, 500)
# user2.show_balance()
# user1.show_balance()
# if valid == True:
#     user2.request_money(user1, 250)
#     user2.show_balance()
#     user1.show_balance()

""" Driver Code for Bonus 1 """
# user1 = BankUser("Bob", 1234, "password")
# user2 = BankUser("Alice", 1223, "happy")
# user1.deposit(100)
# user1.show_balance()
# user2.show_balance()

#######################
# for deposit method
#######################
""" user1.show_balance()
user1.deposit("a")
user1.show_balance()
user1.deposit(-2)
user1.show_balance()
user1.deposit(10.25)
user1.show_balance() """

#######################
# for withdraw method
#######################
""" user1.withdraw("b")
user1.show_balance()
user1.withdraw(-5)
user1.show_balance()
user1.withdraw(25.32)
user1.show_balance()
user1.withdraw(500000)
user1.show_balance() """

#############################
# for transfer_money method
#############################
""" user2.transfer_money(user1, "a")
user2.show_balance()
user1.show_balance()
user2.transfer_money(user1, -10)
user2.show_balance()
user1.show_balance()
user1.transfer_money(user2, 50)
user2.show_balance()
user1.show_balance()
user2.transfer_money(user1, 100)
user2.show_balance()
user1.show_balance() """

#############################
# for request_money method
#############################
""" user1 = BankUser("Bob", 1234, "password")
user2 = BankUser("Alice", 1223, "happy")
user2.deposit(100)
user2.request_money(user1, "a")
user2.show_balance()
user1.show_balance()
user2.request_money(user1, -10)
user2.show_balance()
user1.show_balance()
user1.request_money(user2, 50)
user2.show_balance()
user1.show_balance()
user2.request_money(user1, 100)
user2.show_balance()
user1.show_balance() """

""" Driver code for Bonus 3"""
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Bob")
# user1.change_name("Bo Bo")
# user1.change_name("d")
# user1.change_name("dkdkdkdkdkdkdkd")
# user1.change_name("Bobby")
# user1.change_pin(4321)
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)

""" Driver code for Bonus 5"""
user1 = BankUser("Bob", 1234, "password")
user2 = BankUser("Alice", 1235, "duh")
user1.deposit(1000)
print(f"Account on hold: {user1.on_hold}")
# user1.switch_on_hold()
# print(f"Account on hold: {user1.on_hold}")
# user1.show_balance()
# user1.withdraw(10)
# user1.switch_on_hold()
# user1.withdraw(20)
# user1.show_balance()
user2.switch_on_hold()
user1.transfer_money(user2, 100)
