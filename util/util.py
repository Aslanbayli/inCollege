# Save the users dictionary to the database file
def file_save(users, filename="data/database.csv"):
    with open(filename, 'w') as file:
        for username in users:
            passwd = str(users[username][0])
            f_name = users[username][1]
            l_name = users[username][2]
            language = users[username][3]
            email_bool = users[username][4]
            sms_bool = users[username][5]
            targeted_ads_bool = users[username][6]
            file.write(f"{username},{passwd},{f_name},{l_name},{language},{email_bool},{sms_bool},{targeted_ads_bool}\n")
            
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
    if (len(users) > 5):
        return True
    else:
        return False

# Read from the database file and populate the users dictionary
def file_read(users, filename="data/database.csv"):
    with open(filename, "r") as file:
        file.seek(0)
        for line in file:
            if line.count(',') == 7:
                username, passwd, f_name, l_name, language, email_bool, sms_bool, targeted_ads_bool = line.strip().split(',')
                passwd = passwd[2:-1]
                passwd = passwd.encode("utf-8")
                users[username] = [passwd, f_name, l_name, language]
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
            
def connect(users, f_name, l_name):
    for username in users:
        first_name = users[username][1]
        last_name = users[username][2]
        if first_name.lower() == f_name and last_name.lower() == l_name:
            return True
    return False
    
