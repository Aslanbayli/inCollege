import pytest
import bcrypt
from util import util
from user_auth import authentication as auth

# Test file save function
def test_file_save():
    users = {
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt(rounds=12)), "User1FirstName", "User1LastName"],
        "User2": [bcrypt.hashpw(b"Password2!", bcrypt.gensalt(rounds=12)), "User2FirstName", "User2LastName"],
    }

    test={}
    auth.file_save(users, filename="test_database.csv")

    # Read the saved file and check if the data is correct
    auth.file_read(test, filename="test_database.csv")
    assert "User1" in test
    assert "User2" in test
    assert bcrypt.checkpw(b"Password1!", test["User1"][0])
    assert bcrypt.checkpw(b"Password2!", test["User2"][0])

# Test file job save function
def test_file_job_save():
    test_jobs_save = [
        {"title" : "TESTING TITLE", "description" : "TESTING DESCRIPTION", "employer" : "TESTING EMPLOYER", "location" : "TESTING LOCATION", "salary" : "TESTING SALARY"},
        {"title" : "TESTING TITLE123", "description" : "TESTING DESCRIPTION123", "employer" : "TESTING EMPLOYER123", "location" : "TESTING LOCATION123", "salary" : "TESTING SALARY123"}
    ]
    test_filename = "test_jobs.csv"

    util.file_job_save(test_jobs_save, test_filename)

    test_jobs_read = []

    util.file_job_read(test_jobs_read, test_filename)

    assert test_jobs_read == test_jobs_save

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

# Test file job read function
def test_file_job_read():
    test_jobs_compare1 = [
        {"title" : "TESTING TITLE", "description" : "TESTING DESCRIPTION", "employer" : "TESTING EMPLOYER", "location" : "TESTING LOCATION", "salary" : "TESTING SALARY"},
        {"title" : "TESTING TITLE123", "description" : "TESTING DESCRIPTION123", "employer" : "TESTING EMPLOYER123", "location" : "TESTING LOCATION123", "salary" : "TESTING SALARY123"}
    ]
    test_jobs_compare2 = [
        {"title" : "TESTING TITL", "description" : "TESTING DESCRPTION", "employer" : "TESTING EMPLOER", "location" : "TESTING LOCION", "salary" : "TESTING SRY"},
        {"title" : "TESTING TITLE123", "description" : "TESTNG DESCRIPTIO23", "employer" : "TESTING EMPLOYER123", "location" : "TESTNG LO09ATION123", "salary" : "TESTING SALARY123"}
    ]
    test_filename = "test_jobs.csv"

    test_jobs_read = []

    util.file_job_read(test_jobs_read, test_filename)

    assert test_jobs_read == test_jobs_compare1
    assert test_jobs_read != test_jobs_compare2


# Test connect function
def test_connect():
    users_test = {
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt(rounds=12)), "User1FirstName", "User1LastName"],
        "User2": [bcrypt.hashpw(b"Password2!", bcrypt.gensalt(rounds=12)), "User2FirstName", "User2LastName"]
    }

    # Test to see if the condition holds true
    test_first_name = "User1FirstName"
    test_last_name = "User1LastName"

    assert util.connect(users_test, test_first_name, test_last_name) == True

    # Test for false conditions
    test_first_name = "User1FitName"
    test_last_name = "User1LName"

    assert util.connect(users_test, test_first_name, test_last_name) == False    
