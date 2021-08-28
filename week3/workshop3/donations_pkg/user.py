import re

def login(database, username, password):
    if username in database and password in database.values():
        print("Welcome back", username + "!")
        return username
    elif username in database:
        print("Incorrect pasword for", username, "\n")
        return ""
    else:
        print("User not found. Please register. \n")
        return ""


def register(database, username, password):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        if 0 < len(username) <= 10 and len(password) >= 5 and re.match("^[a-z]*$", username):
            print("Username", username, "registered!")
            return username
        elif len(username) == 0 or len(username) > 10:
            print("Username must be between 1 and 10 characters long.")
            return ""
        elif len(password) < 5:
            print("Password must be at least 5 characters long.")
            return ""
        else:
            print("Username can only contain letters.")
            return ""
