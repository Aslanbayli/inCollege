def login(users, username, password):
    if username in users:
        if password == users[username]:
            return True 
        
    return False

def register(users, username, password):
    users[username] = password

def file_save(users_dict):
    with open('database', 'a+') as file:
        for users, password in users_dict.items():
            file.write(users + ' ' + password + '\n')
