import bcrypt
import sys
import time

from user_auth import authentication as auth
from user_auth import validator as valid
from selection import selectionMenu as select

def main():
    # Password hashing using bcrypt
    password = "Admin123!" # Password string
    password_bytes = password.encode("utf-8") # Convert to byte string
    salt = bcrypt.gensalt(12) # Generate a salt
    password_hash = bcrypt.hashpw(password_bytes, salt) # Hash the password
    users = {"Admin": password_hash} # {username: password}
    states = {"start_menu": 0, "promotional_video": 1, "logging_in": 2, "register": 3, "logged_in": 4} # Add more states as needed
    state = states["start_menu"] # Current state

    auth.save_to_dict(users) # Load the data from file into the dictionary for faster access

    while state in states.values():
        #User Prompt Messages
        if(state == states["start_menu"]):
            print("***** Welcome to inCollege app! *****")
            print("\n\nListen to an inspiring success story:")
            success_story = "\"I had problems gaining traction on LinkedIn. Through InCollege, I now have an internship at Raytheon!"
            print(success_story)
            user_auth = input("\n(w)atch promotional video | (l)ogin | (r)egister | (e)xit: ")
            match user_auth.lower():
                case "w":
                    state = states["promotional_video"]
                case "l":
                    state = states["logging_in"]
                case "r":
                    state = states["register"]
                case "e":
                    print("Thank you for visiting!")
                    return
                case _:
                    print("\nInvalid option. Please try again.")

        #Promotional Video
        elif(state == states["promotional_video"]):
            if(user_auth.lower() == "w"):
                print("\nVideo is now playing.")
                end_video = input("\nPress Enter when ready to return to the log in screen...")
                state = states["start_menu"]

        #User Log-in
        elif(state == states["logging_in"]):
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
                        state = states["start_menu"] # return to main menu
                        break 
                username = input("Username: ")
                password = input("Password: ")
                is_valid_login = auth.login(users, username, password)

            state = states["logged_in"] # set the state to logged_in
            print("\nYou have succesfully logged in.")
            select.selection_menu_options()

        #User Register
        elif(state == states["register"]):
            if (auth.database_check() == True):
                sys.exit("All permitted accounts have been created, please come back later")

            print("\nFill out the prompts below to create an account.")
            username = input("Username: ")

            is_valid_username = valid.validate_username(users, username)
            while not is_valid_username:
                print("Username is already taken.\n")
                username = input("Username: ")
                is_valid_username = valid.validate_username(users, username)
                # Back "Button"
                continue_register = input("\nContinue? (y/n):")
                if(continue_register.lower() != "n"):
                    state = states["start_menu"]

            password = input("Password: ")
            is_valid_password = valid.validate_password(password)
            while not is_valid_password:
                print("Password doesn't meet the security requirements.")
                print("\tMustbe at least 8 characters long")
                print("\tMust be at most 12 characters long")
                print("\tMust contain at least one special character (!, @, #, $, %, ^, &, *, _)")
                print("\tMust contain at least one digit")
                print("\tMust contain at least one uppercase letter\n")
                # Back "Button"
                continue_register = input("\nContinue? (y/n):")
                if(continue_register.lower() == 'n'):
                    main()
                password = input("Password: ")
                
                is_valid_password = valid.validate_password(password)

            auth.register(users, username, password)
            auth.file_save(users)
            state = states["logged_in"] # set the state to logged_in
            print("\nYou have succesfully created an account.")
            select.selection_menu_options()

        #State not in states. Sending back to start menu
        else:
            state = states["start_menu"]

if __name__ == "__main__":
    main()
