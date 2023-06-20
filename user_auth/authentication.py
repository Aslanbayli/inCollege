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
    salt = bcrypt.gensalt(rounds=12) # generate a salt
    password_hash = bcrypt.hashpw(password_bytes, salt) # hash the password 
    language = "English"
    users[username] = [password_hash, first_name, last_name, language]
    user = [username, first_name, last_name, language]
    return user
