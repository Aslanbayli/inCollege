special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '_']

def validate_username(users, username):    
    # Check if username is already taken
    if username in users:
        return False
    
    return True # username is valid

def validate_password(password):
    has_length = False
    has_special = False
    has_digit = False
    has_upper = False

    # Check if password is at least 8 and at most 12 charaters long
    if len(password) >= 8 and len(password) <= 12:
        has_length = True
    
    # perform special character, digit, upper, and lower checks
    for char in password:
        if char in special_characters:
            has_special = True
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    # if any of the checks fail, return false
    if not has_length or not has_special or not has_digit or not has_upper:
        return False
    
    return True # password is valid
    
