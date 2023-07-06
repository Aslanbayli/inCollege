import json

def profile_options(user):
    while True:
        print("*** (1) EDIT TITLE ***")
        print("*** (2) EDIT MAJOR ***")
        print("*** (3) EDIT UNIVERSITY NAME ***")
        print("*** (4) EDIT ABOUT ***")
        print("*** (5) EDIT JOB EXPERIENCE ***")
        print("*** (6) EDIT EDUCATION EXPERIENCE ***")
        print("*** (7) VIEW PROFILE ***")
        print("*** (8) VIEW YOUR FRIEND\'S PROFILE ***")
        print("*** (9) RETURN ***")

        choice = input("Select which part of your profile you would like to edit (e.g. \"1\"). Or, just view your profile: ")
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
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
                view_friends_profile(user)
            elif choice == '9':
                break
            else:
                print("\nInvalid option, please try again.\n")
        else:
            print("\n Invalid option, try again.\n")

def load_user_data(username):
    # We load all the user_data that is stored in the user_data json file
    with open('../data/user_data.json', 'r') as f:
        user_data = json.load(f)
    
    # We now return profile data that is specific to the user we want to deal with
    if username in user_data:
        return user_data[username]
    else:
        return {}

def save_user_data(username, user_data):
    # get the existing user_data that exists for our specific user 
    with open('../data/user_data.json', 'r') as f:
        existing_user_data = json.load(f)

    # updating the existing user_data with new input from the user
    existing_user_data[username] = user_data

    with open('../data/user_data.json', 'w') as f:
        json.dump(existing_user_data, f)

# --- Title Edit Section ---
def edit_title(user):
    # loading our user data from json file
    user_data = load_user_data(user[0])

    # We'll get the current contents of our title for the user
    existing_title = user_data.get('Title', '')

    # if the title is empty initially, just grab the input from the user and save it to the json file
    if existing_title == '': 
        title = input("Please enter the title for your profile: ")
        user_data["Title"] = title
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
                user_data["Title"] = existing_title + (' ' if existing_title else '') + additional_stuff
                save_user_data(user[0], user_data)
                break
            elif choice == 'o':
                new_title = input("Please enter the new title for your profile: ")
                user_data["Title"] = new_title
                save_user_data(user[0], user_data)
                break
            else:
                print("\nInvalid option, try again.\n")

# --- College Major Edit Section ---    
def edit_major(user):
    # loading our user data from json file
    user_data = load_user_data(user[0])

    # We'll get the current contents of our major for the user
    existing_major = user_data.get('Major', '')

    # if the major is empty initially, just grab the input from the user and save it to the json file
    if existing_major == '': 
        major = input("Please type out your official major on your profile: ")
        capitalized_major = ' '.join([word[0].upper() + word[1:].lower() for word in major.split()])
        user_data["Major"] = capitalized_major
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
                user_data["Major"] = existing_major + (' ' if existing_major else '') + capitalized_additional_stuff
                save_user_data(user[0], user_data)
                break
            elif choice == 'o':
                new_major = input("Please enter the new major for your profile: ")
                capitalized_major = ' '.join([word[0].upper() + word[1:].lower() for word in new_major.split()])
                user_data["Major"] = capitalized_major
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
    
# --- Job Edit Section ---
def edit_job(user):
    # loading our user data from json file
    user_data = load_user_data(user[0])
    user_data.setdefault('Job History', [])

    # We'll get the current contents of our about section for the user
    existing_job_history = user_data.get('Job History', '')

    # Stop the user from adding more than 3 past jobs
    if len(user_data['Job History']) >= 3:
        print("You have already entered 3 past jobs.")
        return

    while True:
        choice1 = input("Would you like to change something about your Job History in your inCollege profile? Input (y)es or (n)o: ")

        if choice1 == 'y':
            # if the job history section is initially empty, just grab the input from the user and save it to the json file
            if existing_job_history == []: 
                job_title = input("Enter the job title: ")
                employer = input("Enter the employer: ")
                date_started = input("Enter the date you started this job: ")
                date_ended = input("Enter the date you ended this job: ")
                location = input("Enter the location of this job: ")
                description = input("Enter a description of what you did at this job: ")

                user_data["Job History"].append({
                    'job_title': job_title,
                    'employer': employer,
                    'date_started': date_started,
                    'date_ended': date_ended,
                    'location': location,
                    'description': description
                })
                save_user_data(user[0], user_data)

            # If it's not empty, we are adding/updating to the job section
            else:
                while True:
                    # Print out the jobs so the user can see what jobs they have
                    for i, job in enumerate(user_data['Job History'], start=1):
                        print(f"Job {i}: {job['job_title']} at {job['employer']}, from {job['date_started']} to {job['date_ended']}, in {job['location']}")

                    choice = input("Would you like to (a)dd a new job, (u)pdate an existing one, or (r)eturn to previous screen?: ")

                    if choice == 'u':
                        while True:
                            # Print out the jobs so the user can see what jobs they have
                            for i, job in enumerate(user_data['Job History'], start=1):
                                print(f"Job {i}: {job['job_title']} at {job['employer']}, from {job['date_started']} to {job['date_ended']}, in {job['location']}")

                            # This code deals with the issue if a user types an invalid number within the range, but if a job doesn't exist
                            try: 
                                # Ask the user which job they want to update
                                job_num = int(input("Enter the number of the job you want to update: "))

                                # If a user types in a number outside the range of 1 to 3 jobs
                                if (job_num < 1) or (job_num > 3):
                                    print("Invalid input, please try again.\n")
                                    raise ValueError
                            
                                # Get the job that the user wants to update
                                job = user_data['Job History'][job_num - 1]

                            except IndexError:
                                print("Invalid choice. You selected a choice that does not exist.\n") 
                                continue
                            except ValueError:
                                print("Please pass in a valid number as your input.\n")
                                continue

                            while True:
                                try:
                                    # Ask the user which attribute they want to update
                                    attribute = int(input("Enter the attribute you want to update ((1) job title, (2) employer, (3) date started, (4) date ended, (5) location, or (6) description): "))

                                    if attribute == 1:
                                        new_job_title = input("Enter your new job title: ")
                                        job['job_title'] = new_job_title
                                        break
                                    elif attribute == 2:
                                        new_employer = input("Enter your new employer: ")
                                        job['employer'] = new_employer
                                        break
                                    elif attribute == 3:
                                        new_date_started = input("Enter your new date started: ")
                                        job['date_started'] = new_date_started
                                        break
                                    elif attribute == 4:
                                        new_date_ended = input("Enter your new date ended: ")
                                        job['date_ended'] = new_date_ended
                                        break
                                    elif attribute == 5:
                                        new_location = input("Enter your new location: ")
                                        job['location'] = new_location
                                        break
                                    elif attribute == 6:
                                        new_description = input("Enter your new description: ")
                                        job['description'] = new_description
                                        break
                                    else:
                                        print("\nInvalid option. Please try again.")
                                        raise ValueError
                            
                                except ValueError:
                                    print("Please enter a valid input.")
                           
                            save_user_data(user[0], user_data)

                            # This block ensures that we aren't stuck forever in the (u)pdate option
                            user_choice = input("Would you like to continue in updating your jobs? Type (y)es or (n)o: ")
                            if (user_choice == 'y'):
                                continue
                            elif (user_choice == 'n'):
                                break
                            else:
                                print("Invalid option, please try again.")
                                break

                    elif choice == 'a':
                        job_title_add = input("Enter the job title: ")
                        employer_add = input("Enter the employer: ")
                        date_started_add = input("Enter the date you started this job: ")
                        date_ended_add = input("Enter the date you ended this job: ")
                        location_add = input("Enter the location of this job: ")
                        description_add = input("Enter a description of what you did at this job: ")
                        print()

                        user_data["Job History"].append({
                            'job_title': job_title_add,
                            'employer': employer_add,
                            'date_started': date_started_add,
                            'date_ended': date_ended_add,
                            'location': location_add,
                            'description': description_add
                        })
                        save_user_data(user[0], user_data)

                    elif choice == 'r':
                        break
                        
                    else:
                        print("\nInvalid option, please try again.\n")

        elif choice1 == 'n':
            break

        else:
            print("\nInvalid option, please try again.\n")

# --- Education Experience Section ---
def edit_education(user):
    # loading our user data from json file
    user_data = load_user_data(user[0])

    # We'll get the current contents of our about section for the user
    existing_education = user_data.get('Education', '')

    while True:
        choice1 = input("Would you like to change something about your Education History in your inCollege profile? Input (y)es or (n)o: ")

        if choice1 == 'y':
            # if the existing education section is initially empty, just grab the input from the user and save it to the json file
            if existing_education == '':
                school_name = input("Enter the name of your school: ")
                degree = input("Enter what degree you obtained: ")
                years_attended = input("Enter what years did you attended the university for (e.g. 1997 - 2001): ")

                user_data["Education"] = []
                user_data["Education"].append({
                    'school_name': school_name,
                    'degree': degree,
                    'years_attended': years_attended
                })
                save_user_data(user[0], user_data)

            # If it's not empty, we are adding/updating to the education section
            else:
                while True:
                    # Print out the jobs so the user can see what education experience they have
                    for i, education in enumerate(user_data['Education'], start=1):
                        print(f"Education Experience {i}: {education['school_name']} with {education['degree']} degree, in the following years: {education['years_attended']}")

                    choice = input("Would you like to (a)dd a new education experience, (u)pdate an existing one, or (r)eturn to the previous screen?: ")

                    if choice == 'u':
                        while True:
                            # Print out the jobs so the user can see what jobs they have
                            for i, education in enumerate(user_data['Education'], start=1):
                                print(f"Education Experience {i}: {education['school_name']} at {education['degree']}, in the following years: {education['years_attended']}")

                            # This code deals with the issue if a user types an invalid number within the range, but if a education experience doesn't exist
                            try: 
                                # Ask the user which education they want to update
                                job_num = int(input("Enter the number of the education experience you want to update: "))

                                # If a user types in a number outside the range
                                if (job_num < 1):
                                    print("Invalid input, please try again.\n")
                                    raise ValueError
                                    continue

                                # Get the education that the user wants to update
                                education = user_data['Education'][job_num - 1]

                            except IndexError:
                                print("Invalid choice. You selected a choice that does not exist.\n") 
                                continue
                            except ValueError:
                                print("Please pass in a valid number as your input.\n")
                                continue
                            
                            while True:
                                try:
                                    # Ask the user which attribute they want to update
                                    attribute = int(input("Enter the attribute you want to update ((1) education title, (2) degree, (3) years attended): "))

                                    if attribute == 1:
                                        new_school_name = input("Enter the new education title you want to update: ")
                                        education['school_name'] = new_school_name
                                        break
                                    elif attribute == 2:
                                        new_degree = input("Enter the degree you want to update: ")
                                        education['degree'] = new_degree
                                        break
                                    elif attribute == 3:
                                        new_years_attended = input("Enter the new years that you attended the school for: ")
                                        education['years_attended'] = new_years_attended
                                        break
                                    else:
                                        print("\nInvalid option. Please try again.")
                                        raise ValueError

                                except ValueError:
                                    print("Please enter a number.")
                                
                            save_user_data(user[0], user_data)

                            # This block ensures that we aren't stuck forever in the (u)pdate option
                            user_choice = input("Would you like to continue in updating education experience? Type (y)es or (n)o: ")
                            if (user_choice == 'y'):
                                continue
                            elif (user_choice == 'n'):
                                break
                            else:
                                print("Invalid option, please try again.")
                                break

                    elif choice == 'a':
                        school_name = input("Enter the name of your school: ")
                        degree = input("Enter what degree you obtained: ")
                        years_attended = input("Enter what years did you attended the university for (e.g. 1997 - 2001): ")

                        user_data["Education"].append({
                            'school_name': school_name,
                            'degree': degree,
                            'years_attended': years_attended
                        })
                        save_user_data(user[0], user_data)

                    elif choice == 'r':
                        break
                        
                    else:
                        print("\nInvalid option, please try again.\n")

        elif choice1 == 'n':
            break

        else:
            print("\nInvalid option, please try again.\n")

def view_profile(user):
    # loading our user data from json file
    user_data = load_user_data(user[0])

    keys_possibility_1 = ['Title', 'Major', 'University', 'About', 'Job History', 'Education']
    keys_possibility_2 = ['Title', 'Major', 'University', 'About', 'Education']

    # Checks to see if the user filled out all sections of their profile before they can see it
    if ((all(key in user_data for key in keys_possibility_1)) or (all(key in user_data for key in keys_possibility_2))):

        print("*** YOUR PROFILE ***")
        print(user[1] + " " + user[2])
        for key, value in user_data.items():
            if type(value) is list:
                print(f"{key}: \t")
                for i, item in enumerate(value, start=1):
                    print(f"\t{i}:")
                    for subkey, subvalue in item.items():
                        print(f"\t\t{subkey}: {subvalue}")
            else:
                print(f"{key}: {value}")
        print()

    else:
        print("\nYou must complete all required sections of your profile. You don\'t need to have a job experience section, but you must have the other sections!\n")
        return

def view_friends_profile(user):
    with open("../data/database.csv", "r") as file:
        lines = file.readlines()

    friends = []
    for line in lines:
        data = line.strip().split(',')
        if data[0] == user[0]:
            friends = data[10:]

    if not friends:
        print("You have no friends! Go get some friends.\n")
        return

    friend_list_view = []
    for f in friends:
        user_data_friend = load_user_data(f)

        keys_possibility_1 = ['Title', 'Major', 'University', 'About', 'Job History', 'Education']
        keys_possibility_2 = ['Title', 'Major', 'University', 'About', 'Education']

        first_name = ''
        last_name = ''
        for line in lines:
            data = line.strip().split(',')
            if data[0] == f:
                first_name = data[2]
                last_name = data[3]

        if ((all(key in user_data_friend for key in keys_possibility_1)) or (all(key in user_data_friend for key in keys_possibility_2))):
            friend_list_view.append((f, f + " [PROFILE]", first_name, last_name))
        else:
            friend_list_view.append((f, f, first_name, last_name))

    while True:
        print("*** FRIENDS ***")
        for index, friend in enumerate(friend_list_view, start=1):
            print(f"{index} {friend[1]}")

        choice = input("Please type the number next to your friend whose profile you would like to see. Only enter the number of the friend whose name has \'[PROFILE]\' tag next to them. Press (11) if you want to go back: ")
        try:
            choice1 = int(choice)
        except ValueError:
            print("Invalid input, please enter a number.\n")
            continue
        if choice1 == 11:
            break
        if 1 <= choice1 <= len(friend_list_view):
            friend_username, friend_name, first_name, last_name = friend_list_view[choice1 - 1]
            if "[PROFILE]" in friend_name:
                user_data_view = load_user_data(friend_username)
                print("*** THEIR PROFILE ***")
                print(f"{first_name} {last_name}")
                for key, value in user_data_view.items():
                    if type(value) is list:
                        print(f"{key}: \t")
                        for i, item in enumerate(value, start=1):
                            print(f"\t{i}:")
                            for subkey, subvalue in item.items():
                                print(f"\t\t{subkey}: {subvalue}")
                    else:
                        print(f"{key}: {value}")
                print()
            else:
                print("The selected friend does not have a profile.\n")
        else:
            print("Invalid option, please try again. Their profile is probably not displayed, or you didn't pass in a correct input.\n")
