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
    SEARCH_STUDENTS = 8
    PENDING_REQUESTS = 9
    EXIT = 10


def main():
    users = {}  # {username: [password, first_name, last_name, language, email_bool, sms_bool, targeted_ads_bool, university, major, [friend_requests]]}
    user = []  # [username, first_name, last_name, language, email_bool, sms_bool, targeted_ads_bool, university, major]
    friend_request = {}

    state = States.START_MENU  # Current state

    util.file_read(users, friend_request)  # Load the data from file into the dictionary for faster access

    while state != States.EXIT:
        # User Prompt Messages
        if state == States.START_MENU:
            user_auth = input(
                "\n(w)atch promotional video | (f)ind people you might know | (s)earch students | (u)seful link | InCollege (i)mportant links | (l)ogin | (r)egister | (p)ending friend requests | (e)xit: "
            )
            match user_auth.lower():
                case "w":
                    state = States.PROMOTIONAL_VIDEO
                case "f":
                    state = States.CONNECT
                case "s":
                    state = States.SEARCH_STUDENTS
                case "l":
                    state = States.LOGGING_IN
                case "r":
                    state = States.REGISTER
                case "i":
                    state = States.IMPORTANT_LINKS
                case "u":
                    state = States.USEFUL_LINKS
                case "p":
                    state = States.PENDING_REQUESTS
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
            print("\nFill out the prompts below to find people you might know.")
            f_name = input("First Name: ")
            l_name = input("Last Name: ")
            found = util.connect(users, f_name, l_name)
            if found:
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
            else:
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
            select.selection_menu_options(user, friend_list, request_list, users)
            state = States.START_MENU

        # Search Students
        elif state == States.SEARCH_STUDENTS:
            print("\nSearch for other students:")
            search_option = input(
                "Search by (l)ast name, (u)niversity, or (m)ajor: "
            ).lower()

            if search_option == "l":
                search_criteria = "last name"
            elif search_option == "u":
                search_criteria = "university"
            elif search_option == "m":
                search_criteria = "major"
            else:
                print("\nInvalid option. Please try again.")
                state = States.START_MENU
                continue

            search_value = input("Enter the search value: ")
            found_students = util.search_students(users, search_value, search_criteria)
            if found_students:
                print("\nStudents found:")
                for index, student in enumerate(found_students):
                    print(f"{index + 1}. {student[1]} {student[2]}")

                send_request = input("Enter the number of the student to send a friend request (or 'c' to cancel): ")
                if send_request.lower() == 'c':
                    state = States.START_MENU
                else:
                    try:
                        send_request_index = int(send_request) - 1
                        if send_request_index >= 0 and send_request_index < len(found_students):
                            selected_student = found_students[send_request_index]
                            recipient_username = users[selected_student[0]][0]
                            users[user[0]][9].append(recipient_username)  # Add the friend request to current user's friend requests
                            print(f"\nFriend request sent to {selected_student[1]} {selected_student[2]} ({selected_student[0]}).")
                        else:
                            print("\nInvalid option. Please try again.")
                    except ValueError:
                        print("\nInvalid option. Please try again.")
            else:
                print("\nNo students found with the given search criteria.")

            state = States.START_MENU

        # Pending Friend Requests
        elif state == States.PENDING_REQUESTS:
            print("\nPending Friend Requests:")
            # pending_requests = users[user[0]][9]  # Get the list of friend requests for the current user
            if len(pending_requests) == 0:
                print("You have no pending friend requests.")
            else:
                for request in pending_requests:
                    print(f"- {request}")

            input("\nPress Enter to return to the main menu...")
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
