import bcrypt
from user_auth import authentication as auth

# Test login function
def test_login():
    users = {
        "Admin": [bcrypt.hashpw(b"Admin123!", bcrypt.gensalt(rounds=12)), "AdminFirstName", "AdminLastName", "English"],
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt(rounds=12)), "User1FirstName", "User2LastName", "Spanish"]
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

    # Register some new users
    auth.register(users, "NewUser", "NewPassword123!", "NewUserFirstName", "NewUserLastName")
    auth.register(users, "NewUser1", "NewPassword456@", "NewUser1FirstName", "NewUser1LastName")

    # Check if the users are added to the users dictionary
    assert "NewUser" in users
    assert "NewUser1" in users
    assert bcrypt.checkpw(b"NewPassword123!", users["NewUser"][0])
    assert bcrypt.checkpw(b"NewPassword456@", users["NewUser1"][0])
