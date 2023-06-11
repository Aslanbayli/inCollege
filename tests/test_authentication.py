import bcrypt
import pytest
from user_auth import authentication as auth

# Test login function
def test_login():
    users = {
        "Admin": [bcrypt.hashpw(b"Admin123!", bcrypt.gensalt(rounds=12)), "AdminFirstName", "AdminLastName"],
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt(rounds=12)), "User1FirstName", "User2LastName"]
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

# Test file_save function
def test_file_save():
    users = {
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt(rounds=12)), "User1FirstName", "User1LastName"],
        "User2": [bcrypt.hashpw(b"Password2!", bcrypt.gensalt(rounds=12)), "User2FirstName", "User2LastName"],
    }

    test={}
    auth.file_save(users, filename="database.csv")

    # Read the saved file and check if the data is correct
    auth.file_read(test, filename="database.csv")
    assert "User1" in test
    assert "User2" in test
    assert bcrypt.checkpw(b"Password1!", test["User1"][0])
    assert bcrypt.checkpw(b"Password2!", test["User2"][0])

# Test database_check function
def test_database_check():
    test1_users_full = {}
    test_users_not_full = {}
    auth.file_read(test1_users_full, "test1.csv")
    auth.file_read(test_users_not_full, "test.csv")

    assert auth.database_check(test1_users_full) == True
    assert auth.database_check(test_users_not_full) == False

# Test file read function
def test_file_read():
    test1_users_full_file_read = {}
    test_users_not_full_file_read = {}
    auth.file_read(test1_users_full_file_read, "test1.csv")
    auth.file_read(test_users_not_full_file_read, "test.csv")

    # See if the read was successful for test1.csv
    assert "User1" in test1_users_full_file_read
    assert "User2" in test1_users_full_file_read
    assert "User3" in test1_users_full_file_read

    # See if the read was successful for test.csv
    assert "User1" in test_users_not_full_file_read
    assert "User2" in test_users_not_full_file_read


