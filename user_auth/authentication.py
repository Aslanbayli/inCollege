import bcrypt

def login(users, username, password):
    if username in users:
        password = password.encode("utf-8")
        if bcrypt.checkpw(password, users[username]):
            return True 

    return False

def register(users, username, password):
    password_bytes = password.encode("utf-8") # convert to byte string 
    salt = bcrypt.gensalt(12) # generate a salt
    password_hash = bcrypt.hashpw(password_bytes, salt) # hash the password 
    users[username] = password_hash

def file_save(users_dict, filename="database"):
    existing_dict = {}
    with open(filename, 'a+') as file:
        file.seek(0)
        for line in file:
            key, value = line.strip().split(',')
            existing_dict[key] = value

    with open(filename, 'a+') as file:
        for username, password in users_dict.items():
            if (username in existing_dict):
                continue
            file.write(f"{username},{password}\n")

def database_check(filename="database"):
    
    existing_dict = {}
    with open(filename, 'a+') as file:
        file.seek(0)
        for line in file:
            key, value = line.strip().split(',')
            existing_dict[key] = value
    
    if (len(existing_dict) > 5):
        return True
    else:
        return False

def save_to_dict(users, filename="database"):
    with open(filename, "r") as file:
        file.seek(0)
        for line in file:
            key, value = line.strip().split(',')
            value = value[2:-1]
            value = value.encode("utf-8")
            # print(key, value)
            users[key] = value
