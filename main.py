import bcrypt
import sys
import time

from user_auth import authentication as auth
from user_auth import validator as valid
from selection import selectionMenu as select

# password hashing using bcrypt
password = "Admin123!" # password string
password_bytes = password.encode("utf-8") # convert to byte string 
salt = bcrypt.gensalt(rounds=12) # generate a salt
password_hash = bcrypt.hashpw(password_bytes, salt) # hash the password 

users = {"Admin": password_hash} # {username: password}
states = ["logged_in"] # add more states as needed
state = "" # current state

auth.save_to_dict(users) # load the data from file into the dictionary for faster access

print("***** Welcome to inCollege app! *****")
def main():
    user_auth = input("\n(l)ogin | (r)egister: ")
    if user_auth.lower() == "l":
        print("\nEnter your credentiasls to login.")
        username = input("Username: ")
        password = input("Password: ")

        is_valid_login = auth.login(users, username, password)
        while not is_valid_login:
            print("Incorrect username / password")
            try_again = input("\nWould you like to try again? (y)es | (n)o: ")
            if valid.validate_input(try_again):
                # return to main menu if the answer is no
                if try_again.lower() == "n":
                    print("\nReturning to main menu...")
                    time.sleep(0.5) # wait 0.5 seconds
                    main() # return to main menu
                    break 
            username = input("Username: ")
            password = input("Password: ")
            is_valid_login = auth.login(users, username, password)

        state = states[0] # set the state to logged_in
        print("\nYou have succesfully logged in.")
        select.selection_menu_options()

    elif user_auth.lower() == "r":

        if (auth.database_check() == True):
            sys.exit("All permitted accounts have been created, please come back later")

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
        auth.file_save(users)
        state = states[0] # set the state to logged_in
        print("\nYou have succesfully created an account.")
        select.selection_menu_options()
    else:
        print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()