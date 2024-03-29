# Save the users dictionary to the database file
def file_save(friend_request, users, database_path = "data/database.csv", friend_request_path = "data/request.csv"):
    
    with open(database_path, 'w') as file:
        for username in users:
            passwd = str(users[username][0])
            f_name = users[username][1]
            l_name = users[username][2]
            language = users[username][3]
            email_bool = users[username][4]
            sms_bool = users[username][5]
            targeted_ads_bool = users[username][6]
            college = users[username][7]
            major = users[username][8]
            friends = users[username][9:]
            friends_str = ",".join(friends)
            line = f"{username},{passwd},{f_name},{l_name},{language},{email_bool},{sms_bool},{targeted_ads_bool},{college},{major}"
            if friends:
                line += f",{friends_str}"
            line += "\n"
            file.write(line)
    
    with open(friend_request_path, 'w') as file:
        for username in friend_request:
            request = friend_request[username][0:]
            request_str = ",".join(request)
            line = f"{username}"
            if request:
                line += f",{request_str}"
            line += "\n"
            file.write(line)

            
def file_job_save(jobs, filename = "data/jobs.csv"):
    with open(filename, 'w') as file:
        for job in jobs:
            j_title = job["title"]
            j_description = job["description"]
            j_employer = job["employer"]
            j_location = job["location"]
            j_salary = job["salary"]
            j_first_name = job["first_name"]
            j_last_name = job["last_name"]
            file.write(f"{j_title},{j_description},{j_employer},{j_location},{j_salary},{j_first_name},{j_last_name}\n")
            
# Check if the database is full
def database_check(users):
    if (len(users) > 10):
        return True
    else:
        return False

# Read from the database file and populate the users dictionary
def file_read(users, friend_request, database_path = "data/database.csv", friend_request_path = "data/request.csv"):
    with open(database_path, "r") as file:
        file.seek(0)
        for line in file:
            data = line.strip().split(',')
            if len(data) >= 7:
                username = data[0]
                passwd = data[1][2:-1].encode("utf-8")
                f_name = data[2]
                l_name = data[3]
                language = data[4]
                email_bool = data[5]
                sms_bool = data[6]
                targeted_ads_bool = data[7]
                university = data[8]
                major = data[9]
                
                # Additional data (if available)
                additional_data = data[10:]


                if username in users:
                    users[username] += additional_data
                else:
                    users[username] = [passwd, f_name, l_name, language, email_bool, sms_bool, targeted_ads_bool, university, major] + additional_data
            else:
                continue

    with open(friend_request_path, "r") as file:
        file.seek(0)
        for line in file:
            data = line.strip().split(',')
            if len(data) >= 0:
                username = data[0]
                # Additional data (if available)
                additional_data = data[1:]
                if username in friend_request:
                    friend_request[username] += additional_data
                else:
                    friend_request[username] =  additional_data
            else:
                continue

def file_job_read(jobs, filename="data/jobs.csv"):
    with open(filename, "r") as file:
        file.seek(0)
        for line in file:
            if line.count(',') == 6:
                j_title, j_description, j_employer, j_location, j_salary, j_first_name, j_last_name = line.strip().split(',')
                job = {"title" : j_title, "description" : j_description, "employer" : j_employer, "location" : j_location, "salary" : j_salary, "first_name" : j_first_name, "last_name" : j_last_name}
                jobs.append(job)
            else:
                continue
            
def find_friend(users):
    while True:
        found = 0
        print("\nSearch for other students:")
        search_option = input(
            "Search by (l)ast name, (u)niversity, (m)ajor or (r)eturn: "
        ).lower()
        matching_users = []
        if search_option == "l":
            search_type = input("Please type the last name: ")
            for user in users:
                if users[user][2] == search_type:
                    matching_users.append(user)
                    found = 1
        elif search_option == "u":
            search_type = input("Please type the university: ")
            for user in users:
                if users[user][7] == search_type:
                    matching_users.append(user)
                    found = 1
        elif search_option == "m":
            search_type = input("Please type the major: ")
            for user in users:
                if users[user][8] == search_type:
                    matching_users.append(user)
                    found = 1
        elif search_option == "r":
            return "return"
        else:
            print("\nInvalid option. Please try again.")
            continue

        if found == 0:
            return False
        elif found == 1:
            print("\nHere are the results:\n")
            for friend in matching_users:
                print(f"{friend}")
            return True
            
    
