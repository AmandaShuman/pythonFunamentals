import sys
from donations_pkg.homepage import show_homepage
from donations_pkg.user import login

database = {"key": "admin", "password": "password123"}
donations = {}
authorized_user = ""
show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")
else: 
    print("Logged in as:", authorized_user)

while True:
    option = input("Choose an option: ")
    if option == "1":
        print()
        username = input("Enter username: ")
        password = input("Enter password: ")
        print()
        authorized_user = login(database, username, password)
    elif option == "2":
        print("TODO: Write Login Functionality")
    elif option == "3":
        print("TODO: Write Login Functionality")
    elif option == "4":
        print("TODO: Write Login Functionality")
    elif option == "5":
        print("Leaving DonateMe...")
        sys.exit()
    else:
        print("Invalid input. Try again.")
    
