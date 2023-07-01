import json

def profile_options(user):
    print(user)
    while True:
        print("*** (1) EDIT TITLE ***")
        print("*** (2) EDIT MAJOR ***")
        print("*** (3) EDIT UNIVERSITY NAME ***")
        print("*** (4) EDIT ABOUT ***")
        print("*** (5) EDIT JOB EXPERIENCE ***")
        print("*** (6) EDIT EDUCATION EXPERIENCE ***")
        print("*** (7) VIEW PROFILE ***")
        print("*** (8) RETURN ***")

        choice = input("Select which part of your profile you would like to edit (e.g. \"1\"). Or, just view your profile: ")
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
            if choice == '1':
                edit_title(user)
            elif choice == '2':
                edit_major(user)
            elif choice == '3':
                edit_university(user)
            elif choice == '4':
                edit_about(user)
            elif choice == '5':
                edit_job(user)
            elif choice == '6':
                edit_education(user)
            elif choice == '7':
                view_profile(user)
            elif choice == '8':
                break
            else:
                print("\nInvalid option, please try again.\n")
        else:
            print("\n Invalid option, try again.\n")

def load_user_data(username):
    # We load all the user_data that is stored in the user_data json file
    with open('data/user_data.json', 'r') as f:
        user_data = json.load(f)
    
    # We now return profile data that is specific to the user we want to deal with
    if username in user_data:
        return user_data[username]
    else:
        return {}

def save_user_data(username, user_data):
    # get the existing user_data that exists for our specific user 
    with open('data/user_data.json', 'r') as f:
        existing_user_data = json.load(f)

    # updating the existing user_data with new input from the user
    existing_user_data[username] = user_data

    with open('data/user_data.json', 'w') as f:
        json.dump(existing_user_data, f)

# --- Title Edit Section ---
def edit_title(user):
    # loading our user data from json file
    user_data = load_user_data(user[0])

    # We'll get the current contents of our title for the user
    existing_title = user_data.get('title', '')

    # if the title is empty initially, just grab the input from the user and save it to the json file
    if existing_title == '': 
        title = input("Please enter the title for your profile: ")
        user_data["title"] = title
        save_user_data(user[0], user_data)

    # if it's not empty, add-on to the existing title
    else:
        while True:
            # show existing title to the user
            print(f"\nYour current title is this: {existing_title}\n")

            # give user option to add on to the existing title, or override it
            choice = input("Would you like to (a)dd onto your title, or (o)verride your current title?: ")

            if choice == 'a': 
                additional_stuff = input("Please enter what you want to add to your title: ")
                user_data["title"] = existing_title + (' ' if existing_title else '') + additional_stuff
                save_user_data(user[0], user_data)
                break
            elif choice == 'o':
                new_title = input("Please enter the new title for your profile: ")
                user_data["title"] = new_title
                save_user_data(user[0], user_data)
                break
            else:
                print("\nInvalid option, try again.\n")

# --- College Major Edit Section ---    
def edit_major(user):
    # loading our user data from json file
    user_data = load_user_data(user[0])

    # We'll get the current contents of our major for the user
    existing_major = user_data.get('major', '')

    # if the major is empty initially, just grab the input from the user and save it to the json file
    if existing_major == '': 
        major = input("Please type out your official major on your profile: ")
        capitalized_major = ' '.join([word[0].upper() + word[1:].lower() for word in major.split()])
        user_data["major"] = capitalized_major
        save_user_data(user[0], user_data)

    # if it's not empty, add-on to the existing major
    else:
        while True:
            # show existing major to the user
            print(f"\nYour current major is this: {existing_major}\n")

            # give user option to add on to the existing major, or override it
            choice = input("Would you like to (a)dd onto your major, or (o)verride your current major?: ")

            if choice == 'a': 
                additional_stuff = input("Please enter what you want to add to your major: ")
                capitalized_additional_stuff = ' '.join([word[0].upper() + word[1:].lower() for word in additional_stuff.split()])
                user_data["major"] = existing_major + (' ' if existing_major else '') + capitalized_additional_stuff
                save_user_data(user[0], user_data)
                break
            elif choice == 'o':
                new_major = input("Please enter the new major for your profile: ")
                capitalized_major = ' '.join([word[0].upper() + word[1:].lower() for word in new_major.split()])
                user_data["major"] = capitalized_major
                save_user_data(user[0], user_data)
                break
            else:
                print("\nInvalid option, try again.\n")

# --- University Edit Section ---
def edit_university(user):
    # loading our user data from json file
    user_data = load_user_data(user[0])

    # We'll get the current contents of our university name for the user
    existing_university_name = user_data.get('University', '')

    # if the university name is empty initially, just grab the input from the user and save it to the json file
    if existing_university_name == '': 
        university_name = input("Please type out the name of your university for your profile: ")
        capitalized_university_name = ' '.join([word[0].upper() + word[1:].lower() for word in university_name.split()])
        user_data["University"] = capitalized_university_name
        save_user_data(user[0], user_data)

    # if it's not empty, add-on to the existing university name
    else:
        while True:
            # show existing university name to the user
            print(f"\nYour current university name is: {existing_university_name}\n")

            # give user option to add on to the existing university name, or override it
            choice = input("Would you like to (a)dd onto your university name, or (o)verride your current university name?: ")

            if choice == 'a': 
                additional_stuff = input("Please enter what you want to add to your university name: ")
                capitalized_additional_stuff = ' '.join([word[0].upper() + word[1:].lower() for word in additional_stuff.split()])
                user_data["University"] = existing_university_name + (' ' if existing_university_name else '') + capitalized_additional_stuff
                save_user_data(user[0], user_data)
                break
            elif choice == 'o':
                new_major = input("Please enter the new university name for your profile: ")
                capitalized_university_name = ' '.join([word[0].upper() + word[1:].lower() for word in new_major.split()])
                user_data["University"] = capitalized_university_name
                save_user_data(user[0], user_data)
                break
            else:
                print("\nInvalid option, try again.\n")


# --- About Section Edit ---
def edit_about(user):
# loading our user data from json file
    user_data = load_user_data(user[0])

    # We'll get the current contents of our about section for the user
    existing_about = user_data.get('About', '')

    # if the about section is empty initially, just grab the input from the user and save it to the json file
    if existing_about == '': 
        about_section = input("Please type out the about section for your profile: ")
        user_data["About"] = about_section
        save_user_data(user[0], user_data)

    # if it's not empty, add-on to the existing about section
    else:
        while True:
            # show existing about section to the user
            print(f"\nYour current about section is as follows: \n{existing_about}\n")

            # give user option to add on to the existing about section, or override it
            choice = input("Would you like to (a)dd onto your about section, or (o)verride your current about section?: ")

            if choice == 'a': 
                additional_stuff = input("Please enter what you want to add to your current about section: ")
                user_data["About"] = existing_about + (' ' if existing_about else '') + additional_stuff
                save_user_data(user[0], user_data)
                break
            elif choice == 'o':
                new_about_section = input("Please enter the new about section for your profile: ")
                user_data["About"] = new_about_section
                save_user_data(user[0], user_data)
                break
            else:
                print("\nInvalid option, try again.\n")
    
def edit_job(user):
    
# def edit_education(user):
    
# def view_profile(user):