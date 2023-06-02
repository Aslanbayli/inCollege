import bcrypt

def login(users, username, password):
    if username in users:
        password = password.encode("utf-8")
        if bcrypt.checkpw(password, users[username]):
            return True 
        
    return False

def register(users, username, password):
    password_bytes = password.encode("utf-8") # convert to byte string 
    salt = bcrypt.gensalt(rounds=12) # generate a salt
    password_hash = bcrypt.hashpw(password_bytes, salt) # hash the password 
    users[username] = password_hash
