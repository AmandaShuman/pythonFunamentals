def login(database, username, password):
    if username in database.values() and password in database.values():
        print("Welcome back", username, "\n") 
    elif username in database.values():
        print("Incorrect pasword for", username, "\n")
        return ""
    else:
        print("User not found. Please register. \n")
        return ""
