import bcrypt
import pytest
from user_auth import authentication as auth

# Test login function
def test_login():
    users = {
        "Admin": bcrypt.hashpw(b"Admin123!", bcrypt.gensalt(rounds=12)),
        "User1": bcrypt.hashpw(b"Password1!", bcrypt.gensalt(rounds=12))
    }

    # Valid login
    assert auth.login(users, "Admin", "Admin123!") == True

    # Incorrect username
    assert auth.login(users, "UnknownUser", "Password123!") == False

    # Incorrect password
    assert auth.login(users, "User1", "WrongPassword!") == False

# Test register function
def test_register():
    users = {}

    # Register a new user
    auth.register(users, "NewUser", "NewPassword123!")

    # Check if the user is added to the users dictionary
    assert "NewUser" in users
    assert bcrypt.checkpw(b"NewPassword123!", users["NewUser"])

# Test file_save function
def test_file_save():
    users = {
        "User1": bcrypt.hashpw(b"Password1!", bcrypt.gensalt(rounds=12)),
        "User2": bcrypt.hashpw(b"Password2!", bcrypt.gensalt(rounds=12))
    }

    test={}
    auth.file_save(users_dict=users, filename="database")

    # Read the saved file and check if the data is correct
    auth.save_to_dict(test, filename="database")
    assert "User1" in test
    assert "User2" in test
    assert bcrypt.checkpw(b"Password1!", test["User1"])
    assert bcrypt.checkpw(b"Password2!", test["User2"])


# Test database_check function
def test_database_check():
    assert auth.database_check(filename="test1") == True
    assert auth.database_check("test") == False


