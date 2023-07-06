import time
from enum import Enum

from user_auth import authentication as auth
from user_auth import validator as valid
from selection import selection_menu as select
from util import util as util


class States(Enum):
    START_MENU = 0
    PROMOTIONAL_VIDEO = 1
    LOGGING_IN = 2
    REGISTER = 3
    LOGGED_IN = 4
    CONNECT = 5
    USEFUL_LINKS = 6
    IMPORTANT_LINKS = 7
    EXIT = 8


def main():
    users = {}  # {username: [password, first_name, last_name, language, email_bool, sms_bool, targeted_ads_bool, university, major, friend 1, friend 2]}
    user = []  # [username, first_name, last_name, language, email_bool, sms_bool, targeted_ads_bool, university, major]
    friend_request = {} #{username: [friend 1, friend 2, ...]}

    state = States.START_MENU  # Current state

    util.file_read(users, friend_request)  # Load the data from file into the dictionary for faster access

    while state != States.EXIT:
        # User Prompt Messages
        if state == States.START_MENU:
            user_auth = input(
                "\n(w)atch promotional video | (f)ind people you might know | (u)seful link | InCollege (i)mportant links | (l)ogin | (r)egister | (e)xit: "
            )
            match user_auth.lower():
                case "w":
                    state = States.PROMOTIONAL_VIDEO
                case "f":
                    state = States.CONNECT
                case "u":
                    state = States.USEFUL_LINKS
                case "i":
                    state = States.IMPORTANT_LINKS
                case "l":
                    state = States.LOGGING_IN
                case "r":
                    state = States.REGISTER
                case "e":
                    print("\nThank you for visiting!")
                    state = States.EXIT
                case _:
                    print("\nInvalid option. Please try again.")

        # Promotional Video
        elif state == States.PROMOTIONAL_VIDEO:
            print("\nVideo is now playing.")
            input("\nPress Enter when ready to return to the log in screen...")
            state = States.START_MENU

        # Connect
        elif state == States.CONNECT:
            # print("\nFill out the prompts below to find people you might know.")
            # f_name = input("First Name: ")
            # l_name = input("Last Name: ")
            # found = util.connect(users, f_name, l_name)
            found = util.find_friend(users)
            if found == True:
                
                print("\nThey are a part of the InCollege system.")

                user_auth = input(
                    "\nJoin inCollege to connect with them. (l)ogin | (r)egister | (m)ain menu: ")
                while not valid.validate_input_lrm(user_auth):
                    print("\nInvalid option. Please try again.")
                    user_auth = input(
                        "\nJoin inCollege to connect with them. (l)ogin | (r)egister | (m)ain menu: ")

                if user_auth.lower() == "l":
                    state = States.LOGGING_IN
                elif user_auth.lower() == "r":
                    state = States.REGISTER
                else:
                    state = States.START_MENU
            elif found == "return":
                    state = States.START_MENU
            elif found == False:
                print("\nThey are not yet a part of the InCollege system yet.")
                state = States.START_MENU

        # Useful Links
        elif state == States.USEFUL_LINKS:
            check = select.useful_links("not_logged_in")
            if check == "logging_in":
                state = States.LOGGING_IN
            elif check == "registering":
                state = States.REGISTER
            else:
                state = States.START_MENU

        # Important Links
        elif state == States.IMPORTANT_LINKS:
            check = select.important_links("not_logged_in")
            if check == "logging_in":
                state = States.LOGGING_IN
            elif check == "registering":
                state = States.REGISTER
            else:
                state = States.START_MENU

        # User Log-in
        elif state == States.LOGGING_IN:
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

                if try_again.lower() == "n":
                    print("\nReturning to main menu...")
                    time.sleep(0.5)  # wait 0.5 seconds
                    state = States.START_MENU
                    break

                username = input("\nUsername: ")
                password = input("Password: ")
                is_valid_login = auth.login(users, username, password)

            if is_valid_login:
                state = States.LOGGED_IN
                print("\nYou have successfully logged in.")

                # Check for pending friend requests
                user = [
                    username,
                    users[username][1],
                    users[username][2],
                    users[username][3],
                    users[username][4],
                    users[username][5],
                    users[username][6],
                    users[username][7],
                    users[username][8]
                ]

        # User Register
        elif state == States.REGISTER:
            if util.database_check(users):
                print(
                    "All permitted accounts have been created, please come back later"
                )
                state = States.START_MENU
                continue

            print("\nFill out the prompts below to create an account.")
            username = input("Username: ")

            is_valid_username = valid.validate_username(users, username)
            while not is_valid_username:
                print("Username is already taken.\n")

                continue_register = input("\nContinue? (y/n):")
                while not valid.validate_input_yn(continue_register):
                    print("\nInvalid option. Please try again.")
                    continue_register = input("\nContinue? (y/n):")

                if continue_register.lower() == "n":
                    state = States.START_MENU
                    break
                username = input("Username: ")
                is_valid_username = valid.validate_username(users, username)

            if state == States.START_MENU:
                continue

            password = input("Password: ")
            is_valid_password = valid.validate_password(password)
            while not is_valid_password:
                print("Password doesn't meet the security requirements.")
                print("\tMust be at least 8 characters long")
                print("\tMust be at most 12 characters long")
                print("\tMust contain at least one special character (!, @, #, $, %, ^, &, *, _)")
                print("\tMust contain at least one digit")
                print("\tMust contain at least one uppercase letter\n")

                continue_register = input("\nContinue? (y/n):")
                while not valid.validate_input_yn(continue_register):
                    print("\nInvalid option. Please try again.")
                    continue_register = input("\nContinue? (y/n):")

                if continue_register.lower() == "n":
                    state = States.START_MENU
                    break

                password = input("Password: ")
                is_valid_password = valid.validate_password(password)

            if state == States.START_MENU:
                continue

            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            college = input("College: ")
            major = input("Major: ")

            user = auth.register(
                friend_request, users, username, password, first_name, last_name, college, major
            )
            util.file_save(friend_request,users)
            state = States.LOGGED_IN
            print("\nYou have successfully created an account.")

        # User Logged In
        elif state == States.LOGGED_IN:
            friend_list = users[username][9:]
            request_list = friend_request[username][0:]
            select.selection_menu_options(user, friend_list, request_list, users, friend_request)
            state = States.START_MENU

        else:
            state = States.START_MENU


if __name__ == "__main__":
    # Display the banner
    with open("assets/banner.txt", "r") as file:
        print(file.read())
    print("\n***** Welcome to inCollege app! *****")
    print("\n\nListen to an inspiring success story:")
    success_story = "\"I had problems gaining traction on LinkedIn. Through InCollege, I now have an internship at Raytheon!\""
    print(success_story)
    main()
