import time

from user_auth import authentication as auth
from user_auth import validator as valid
from selection import selection_menu as select
from util import util as util

def main():
    users = {} # {username: [password, first_name, last_name, language]}

    states = {"start_menu": 0, "promotional_video": 1, "logging_in": 2, "register": 3, "logged_in": 4, "connect": 5, "useful_links" : 6, "important_links" : 7} # Add more states as needed
    state = states["start_menu"] # Current state

    util.file_read(users) # Load the data from file into the dictionary for faster access

    while state in states.values():
        # User Prompt Messages
        if (state == states["start_menu"]):
            user_auth = input("\n(w)atch promotional video | (f)ind people you might know | (u)seful link | InCollege (i)mportant links | (l)ogin | (r)egister | (e)xit: ")
            match user_auth.lower():
                case "w":
                    state = states["promotional_video"]
                case "f":
                    state = states["connect"]
                case "l":
                    state = states["logging_in"]
                case "r":
                    state = states["register"]
                case "i":
                    state = states["important_links"]
                case "u":
                    state = states["useful_links"]
                case "e":
                    print("\nThank you for visiting!")
                    return
                case _:
                    print("\nInvalid option. Please try again.")

        # Promotional Video
        elif (state == states["promotional_video"]):
            print("\nVideo is now playing.")
            input("\nPress Enter when ready to return to the log in screen...")
            state = states["start_menu"]

        # Connect
        elif (state == states["connect"]):
            print("\nFill out the prompts below to find people you might know.")
            f_name = input("First Name: ")
            l_name = input("Last Name: ")
            found = util.connect(users, f_name, l_name)
            if found:
                print("\nThey are a part of the InCollege system.")

                user_auth = input("\nJoin inCollege to connect with them. (l)ogin | (r)egister: ")
                while not valid.validate_input_lrm(user_auth):
                    print("\nInvalid option. Please try again.")
                    user_auth = input("\nJoin inCollege to connect with them. (l)ogin | (r)egister: ")

                if user_auth.lower() == "l":
                    state = states["logging_in"]
                elif user_auth.lower() == "r":
                    state = states["register"]
                else:
                    state = states["start_menu"]
            else:
                print("\nThey are not yet a part of the InCollege system yet.")
                state = states["start_menu"]
        # Important Links 
        elif(state == states["important_links"]):
            check = select.important_links("not_logged_in")
            if check == "logging_in":
                state = states["logging_in"]
            elif check == "registering":
                state = states["register"]
            else:
                state = states["start_menu"]
        # Useful Links    
        elif(state == states["useful_links"]):
            check = select.useful_links("not_logged_in")
            if check == "logging_in":
                state = states["logging_in"]
            elif check == "registering":
                state = states["register"]
            else:
                state = states["start_menu"]

        # User Log-in
        elif (state == states["logging_in"]):
            print("\nEnter your credentials to login.")
            username = input("Username: ")
            password = input("Password: ")

            is_valid_login = auth.login(users, username, password)
            while not is_valid_login:
                print("Incorrect username / password")
                try_again = input("\nWould you like to try again? (y)es | (n)o: ")

                while not valid.validate_input_yn(try_again):
                    print("\nInvalid option. Please try again.")
                    try_again = input("\nWould you like to try again? (y)es | (n)o: ")

                # return to main menu if the answer is no
                if try_again.lower() == "n":
                    print("\nReturning to main menu...")
                    time.sleep(0.5) # wait 0.5 seconds
                    state = states["start_menu"] # return to main menu
                    break 

                username = input("\nUsername: ")
                password = input("Password: ")
                is_valid_login = auth.login(users, username, password)
        
            if is_valid_login:
                state = states["logged_in"] # set the state to logged_in
                print("\nYou have succesfully logged in.")
                user = [users[username][1], users[username][2], users[username][3]]
                

        # User Register
        elif (state == states["register"]):
            if (util.database_check(users) == True):
                print("All permitted accounts have been created, please come back later")
                state = states["start_menu"]
                continue

            print("\nFill out the prompts below to create an account.")
            username = input("Username: ")

            is_valid_username = valid.validate_username(users, username)
            while not is_valid_username:
                print("Username is already taken.\n")

                # Back "Button"
                continue_register = input("\nContinue? (y/n):")
                while not valid.validate_input_yn(continue_register):
                    print("\nInvalid option. Please try again.")
                    continue_register = input("\nContinue? (y/n):")
                    
                if(continue_register.lower() == "n"):
                    state = states["start_menu"]
                    break
                username = input("Username: ")
                is_valid_username = valid.validate_username(users, username)

            if (state == states["start_menu"]):
                continue

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
                while not valid.validate_input_yn(continue_register):
                    print("\nInvalid option. Please try again.")
                    continue_register = input("\nContinue? (y/n):")

                if(continue_register.lower() == 'n'):
                    state = states["start_menu"]
                    break

                password = input("Password: ")
                is_valid_password = valid.validate_password(password)

            if (state == states["start_menu"]):
                continue

            first_name = input("First Name: ")
            last_name = input("Last Name: ")

            user = auth.register(users, username, password, first_name, last_name) #User is an array of username, firstname, lastname
            util.file_save(users)
            state = states["logged_in"] # set the state to logged_in
            print("\nYou have succesfully created an account.")
        elif (state == states["logged_in"]):
            select.selection_menu_options(user)
            state = states["start_menu"]

        #State not in states. Sending back to start menu
        else:
            state = states["start_menu"]

if __name__ == "__main__":
    # Display the banner
    with open("assets/banner.txt", "r") as file:
        print(file.read())

    print("\n***** Welcome to inCollege app! *****")
    print("\n\nListen to an inspiring success story:")
    success_story = "\"I had problems gaining traction on LinkedIn. Through InCollege, I now have an internship at Raytheon!\""
    print(success_story)
    main()
