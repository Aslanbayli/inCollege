# Save the users dictionary to the database file
def file_save(users, filename="data/database.csv"):
    with open(filename, 'w') as file:
        for username in users:
            passwd = str(users[username][0])
            f_name = users[username][1]
            l_name = users[username][2]
            file.write(f"{username},{passwd},{f_name},{l_name}\n")
            
def file_job_save(jobs, filename = "data/jobs.csv"):
    with open(filename, 'w') as file:
        for job in jobs:
            j_title = job["title"]
            j_description = job["description"]
            j_employer = job["employer"]
            j_location = job["location"]
            j_salary = job["salary"]
            file.write(f"{j_title},{j_description},{j_employer},{j_location},{j_salary}\n")

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
            if line.count(',') == 3:
                username, passwd, f_name, l_name = line.strip().split(',')
                passwd = passwd[2:-1]
                passwd = passwd.encode("utf-8")
                users[username] = [passwd, f_name, l_name]
            else:
                continue

def file_job_read(jobs, filename="data/jobs.csv"):
    with open(filename, "r") as file:
        file.seek(0)
        for line in file:
            if line.count(',') == 4:
                j_title, j_description, j_employer, j_location, j_salary = line.strip().split(',')
                job = {"title" : j_title, "description" : j_description, "employer" : j_employer, "location" : j_location, "salary" : j_salary}
                jobs.append(job)
            else:
                continue

def connect(users, f_name, l_name):
    for username in users:
        if users[username][1] == f_name and users[username][2] == l_name:
            return True
    return False
    