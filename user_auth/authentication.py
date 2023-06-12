import bcrypt

# Login an existing user
def login(users, username, password):
    if username in users:
        password = password.encode("utf-8")
        if bcrypt.checkpw(password, users[username][0]):
            user = [username, users[username][1], users[username][2]] #username, firstname, lastname
            return user

    return False

# Register a new user
def register(users, username, password, first_name, last_name):
    password_bytes = password.encode("utf-8") # convert to byte string 
    salt = bcrypt.gensalt() # generate a salt
    password_hash = bcrypt.hashpw(password_bytes, salt) # hash the password 
    users[username] = [password_hash, first_name, last_name]
    user = [username, first_name, last_name]
    return user

