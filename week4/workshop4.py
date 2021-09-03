import sys

class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        name = name.strip()
        if 2 <= len(name) <= 10:
            self.name = name
            return self.name
        else:
            print("New names must be between 2 and 10 characters long.")

    def change_pin(self, pin):
        pin = pin.strip()
        if len(pin) == 4 and self.pin != pin and type(pin) is int:
            self.pin = pin
            return self.pin
        else:
            if len(pin) != 4:
                print("PINs must be 4 numbers.")
            elif self.pin == pin:
                print("PIN cannot be previously used PIN.")
            else:
                print("PIN can only contain numbers.")

    def change_password(self, password):
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

    def switch_on_hold(self):
        if self.on_hold == True:
            self.on_hold = False
        else:
            self.on_hold = True

    def show_balance(self):
        print(f"{self.name} has a balance of: ${self.balance:.2f}")

    def withdraw(self, amt):
        if (type(amt) is float or type(amt) is int) and amt >= 0:
            self.balance -= amt
            return self.balance
        else:
            print("Please enter a number bigger than 0. Transaction cancelled.")
            sys.exit()

    def deposit(self, amt):
        if (type(amt) is float or type(amt) is int) and amt >= 0:
            self.balance += amt
            return self.balance
        else:
            print("Please enter a number bigger than 0. Transaction cancelled.")
            sys.exit()

    def transfer_money(self, user, amt):
        if (type(amt) is float or type(amt) is int) and amt >= 0 and amt <= self.balance:
            print("\nYou are transferring $" + str(amt), "to", user.name)
            print("Authentication required")
            pin_check = input("Enter your PIN: ")
            if pin_check in str(self.pin):
                print("Transfer authorized")
                print(f"Transferring ${amt:.2f} to {user.name}")
                self.withdraw(amt)
                user.deposit(amt)
                return True
            else:
                print("Invalid PIN. Transaction cancelled")
                return False
        else:
            if (amt > self.balance):
                print("You don't have enough money to make the transfer. Transaction cancelled.")
                sys.exit()
            else:
                print("Please enter a number bigger than 0. Transaction cancelled.")
                sys.exit()

    def request_money(self, user, amt):
        if (type(amt) is float or type(amt) is int) and amt >= 0 and amt <= user.balance:
            print(f"\nYou are requesting ${amt:.2f} from ${user.name}")
            print("User authentication is required...")
            pin_check = input(f"Enter ${user.name}'s PIN: ")
            if pin_check in str(user.pin):
                pw_check = input("Enter your password: ")
                if pw_check in self.password:
                    print("Request authorized")
                    print(f"${user.name} sent ${amt:.2f}")
                    user.withdraw(amt)
                    self.deposit(amt)
                    return True
                else:
                    print("Invalid password. Transaction cancelled.")
                    return False
            else:
                print("Invalid PIN. Transaction cancelled.")
                return False
        else:
            if (amt > user.balance):
                print(f"${user.name} doesn't have that much money! Transaction cancelled")
                sys.exit()
            else:
                print("Please enter a number bigger than 0. Transaction cancelled.")
                sys.exit()
        

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
user1 = BankUser("Bob", 1234, "password")
user2 = BankUser("Alice", 1223, "happy")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
valid = user2.transfer_money(user1, 500)
user2.show_balance()
user1.show_balance()
if valid == True:
    user2.request_money(user1, 250)
    user2.show_balance()
    user1.show_balance()

""" Driver Code for Bonus """
# user1 = BankUser("Bob", 1234, "password")
# user2 = BankUser("Alice", 1223, "happy")
# user1.show_balance()
# user1.deposit(100)
# user1.show_balance()
# user1.withdraw(25.32)
# user1.show_balance()
# user2.transfer_money(user1, 100)
# user1.transfer_money(user2, 50)


