import bcrypt

# Login an existing user
def login(users, username, password):
    if username in users:
        password = password.encode("utf-8")
        if bcrypt.checkpw(password, users[username][0]):
            return True 

    return False

# Register a new user
def register(users, username, password, first_name, last_name):
    password_bytes = password.encode("utf-8") # convert to byte string 
    salt = bcrypt.gensalt() # generate a salt
    password_hash = bcrypt.hashpw(password_bytes, salt) # hash the password 
    users[username] = [password_hash, first_name, last_name]

# Save the users dictionary to the database file
def file_save(users, filename="database.csv"):
    with open(filename, 'a+') as file:
        for username in users:
            passwd = str(users[username][0])
            f_name = users[username][1]
            l_name = users[username][2]
            file.write(f"{username},{passwd},{f_name},{l_name}\n")
def file_job_save(jobs, filename = "jobs.csv"):
    with open(filename, 'a+') as file:
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
def file_read(users, filename="database.csv"):
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
def file_job_read(jobs, filename="jobs.csv"):
    with open(filename, "r") as file:
        file.seek(0)
        for line in file:
            if line.count(',') == 4:
                j_title, j_description, j_employer, j_location, j_salary = line.strip().split(',')
                job = [j_title, j_description, j_employer, j_locaiton, j_salary]
                jobs.append(job)
            else:
                continue
