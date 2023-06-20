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
    language = "English"
    email_bool = True
    sms_bool = True
    targeted_ads_bool = True
    
    users[username] = [password_hash, first_name, last_name, language, email_bool, sms_bool, targeted_ads_bool]
    user = [username, first_name, last_name, language, email_bool, sms_bool, targeted_ads_bool]
    return user
