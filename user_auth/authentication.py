def login(users, username, password):
    if username in users:
        if password == users[username]:
            return True 
        
    return False

def register(users, username, password):
    users[username] = password
