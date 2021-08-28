def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    print("----------------------------------------------")
    print("| 1.    Login         | 2.    Register        |")
    print("----------------------------------------------")
    print("| 3.    Donate        | 4.    Show Donations  |")
    print("----------------------------------------------")
    print("|                5.    Exit                   |")
    print("----------------------------------------------")


def donate(username):
    while True:
        donation_amt = input("Enter amount to donate: ")
        if donation_amt.islower() == True:
            print("You may only enter numbers to donate.")
            return ""
        elif float(donation_amt) <= 0:
            print("Invalid input. Enter a positive number.")
            return ""
        else:
            donation_amt = "%0.2f" % float(donation_amt)
            donation = str(username) + " donated $" + str(donation_amt)
            print("Thank you for your donation!")
            return donation


def show_donations(donations):
    total = 0
    print("\n---All Donations---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for amt in donations:
            total += float(amt.split("$",1)[1])
            print(amt)
        print (f"Total = ${total:.2f}")
