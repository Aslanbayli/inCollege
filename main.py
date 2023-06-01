from user_auth import authentication as auth
from user_auth import validator as valid

users = {"Admin": "Admin23!"} # {username: password}
states = ["logged_in"] # add more states as needed
state = ""

print("***** Welcome to inCollege app! *****")
user_auth = input("(l)ogin | (r)egister: ")
if user_auth.lower() == "l":
    print("\nEnter your credentiasls to login.")
    username = input("Username: ")
    password = input("Password: ")

    is_valid_login = auth.login(users, username, password)
    while not is_valid_login:
        print("Incorrect username / password, please try again\n")
        username = input("Username: ")
        password = input("Password: ")
        is_valid_login = auth.login(users, username, password)

    state = states[0] # set the state to loggedn_in
    print("\nYou have succesfully logged in.")

elif user_auth.lower() == "r":
    print("\nFill out the prompts below to create an account.")
    username = input("Username: ")

    is_valid_username = valid.validate_username(users, username)
    while not is_valid_username:
        print("Username is already taken.\n")
        username = input("Username: ")
        is_valid_username = valid.validate_username(users, username)

    password = input("Password: ")
    is_valid_password = valid.validate_password(password)
    while not is_valid_password:
        print("Password doesn't meet the security requirements.")
        print("\tMustbe at least 8 characters long")
        print("\tMust be at most 12 characters long")
        print("\tMust contain at least one special character (!, @, #, $, %, ^, &, *, _)")
        print("\tMust contain at least one digit")
        print("\tMust contain at least one uppercase letter\n")
        password = input("Password: ")
        is_valid_password = valid.validate_password(password)

    auth.register(users, username, password)
    state = states[0] # set the state to loggedn_in
    print("\nYou have succesfully created an account.")
else:
    print("\nInvalid option. Please try again.")



