import bcrypt
from user_auth import authentication as auth

# Test login function
def test_login():
    users = {
        "Admin": [bcrypt.hashpw(b"Admin123!", bcrypt.gensalt()), "AdminFirstName", "AdminLastName", "English"],
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt()), "User1FirstName", "User2LastName", "Spanish"]
    }

    # Valid login
    assert auth.login(users, "Admin", "Admin123!") == True
    assert auth.login(users, "User1", "Password1!") == True

    # Incorrect username
    assert auth.login(users, "UnknownUser", "Password1!") == False
    assert auth.login(users, "UnknownUSEr245", "Password1!") == False

    # Incorrect password
    assert auth.login(users, "User1", "WrongPassword!") == False
    assert auth.login(users, "Admin", "NotADMiN123!") == False

# Test register function
def test_register():
    users = {}
    friend_request_1 = {"NewUser1": ["NewUser2"]}
    friend_request_2 = {"NewUser2": ["NewUser1"]}

    # Register some new users
    auth.register(friend_request_1, users,  "NewUser1", "NewPassword123!", "NewUserFirstName1", "NewUserLastName1", "USF", "Computer Science")
    auth.register(friend_request_2, users,  "NewUser2", "NewPassword456@", "NewUserFirstName2", "NewUserLastName2", "USF", "Computer Science")

    # Check if the users are added to the users dictionary
    assert "NewUser1" in users
    assert "NewUser2" in users
    assert bcrypt.checkpw(b"NewPassword123!", users["NewUser1"][0])
    assert bcrypt.checkpw(b"NewPassword456@", users["NewUser2"][0])
