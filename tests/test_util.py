import bcrypt
from util import util

# Test file save function
def test_file_save():
    friend_request = {"User1": ["User2"]}
    users = {
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt()), "User1FirstName", "User1LastName", "English", "False", "False", "True", "USF", "Computer Science"],
        "User2": [bcrypt.hashpw(b"Password2!", bcrypt.gensalt()), "User2FirstName", "User2LastName", "Spanish", "False", "False", "True", "USF", "Computer Science"],
    }

    util.file_save(friend_request, users, database_path="tests/test_database.csv", friend_request_path="tests/test_friend_request.csv")

    # Read the saved file and check if the data is correct
    users_test = {}
    friend_request_test = {}
    util.file_read(users_test, friend_request_test, database_path="tests/test_database.csv", friend_request_path="tests/test_friend_request.csv")
    assert "User1" in users_test
    assert "User2" in users_test
    assert bcrypt.checkpw(b"Password1!", users_test["User1"][0])
    assert bcrypt.checkpw(b"Password2!", users_test["User2"][0])

# Test file job save function
def test_file_job_save():
    test_jobs_save = [
        {"title" : "TESTING TITLE", "description" : "TESTING DESCRIPTION", "employer" : "TESTING EMPLOYER", "location" : "TESTING LOCATION", "salary" : "TESTING SALARY", "first_name": "FIRST_NAME", "last_name": "LAST_NAME"},
        {"title" : "TESTING TITLE123", "description" : "TESTING DESCRIPTION123", "employer" : "TESTING EMPLOYER123", "location" : "TESTING LOCATION123", "salary" : "TESTING SALARY123", "first_name": "FIRST_NAME123", "last_name": "LAST_NAME123"}
    ]
    test_filename = "tests/test_jobs.csv"

    util.file_job_save(test_jobs_save, test_filename)

    test_jobs_read = []

    util.file_job_read(test_jobs_read, test_filename)

    assert test_jobs_read == test_jobs_save

# Test database_check function
def test_database_check():
    test1_users_full = {"user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10", "user11"}
    test_users_not_full = {"user1", "user2", "user3", "user4", "user5"}
    
    assert util.database_check(test1_users_full) == True
    assert util.database_check(test_users_not_full) == False

# Test file read function
def test_file_read():
    users_test = {}
    friend_request_test = {}
    util.file_read(users_test, friend_request_test, database_path="tests/test_database.csv", friend_request_path="tests/test_friend_request.csv")

    # See if the read was successful 
    assert "User1" in users_test
    assert "User2" in users_test

# Test file job read function
def test_file_job_read():
    test_jobs_compare1 = [
        {"title" : "TESTING TITLE", "description" : "TESTING DESCRIPTION", "employer" : "TESTING EMPLOYER", "location" : "TESTING LOCATION", "salary" : "TESTING SALARY", "first_name": "FIRST_NAME", "last_name": "LAST_NAME"},
        {"title" : "TESTING TITLE123", "description" : "TESTING DESCRIPTION123", "employer" : "TESTING EMPLOYER123", "location" : "TESTING LOCATION123", "salary" : "TESTING SALARY123", "first_name": "FIRST_NAME123", "last_name": "LAST_NAME123"}
    ]
    test_jobs_compare2 = [
        {"title" : "TESTING TITL", "description" : "TESTING DESCRPTION", "employer" : "TESTING EMPLOER", "location" : "TESTING LOCION", "salary" : "TESTING SRY", "first_name": "FIRST_adNAmE", "last_name": "LASsssT_NaAAMeME"},
        {"title" : "TESTING TITLE123", "description" : "TESTNG DESCRIPTIO23", "employer" : "TESTING EMPLOYER123", "location" : "TESTNG LO09ATION123", "salary" : "TESTING SALARY123", "first_name": "FIRST__NAME", "last_name": "LASt___NAME"}
    ]
    test_filename = "tests/test_jobs.csv"

    test_jobs_read = []

    util.file_job_read(test_jobs_read, test_filename)

    assert test_jobs_read == test_jobs_compare1
    assert test_jobs_read != test_jobs_compare2


# Test connect function
def test_find_friend(monkeypatch):
    inputs = iter(["l", "User1LastName", "l", "SomeLastName"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    users_test = {
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt()), "User1FirstName", "User1LastName"],
        "User2": [bcrypt.hashpw(b"Password2!", bcrypt.gensalt()), "User2FirstName", "User2LastName"]
    }

    # Test to see if the condition holds true
    assert util.find_friend(users_test) == True

    # Test to see if the condition holds false
    assert util.find_friend(users_test) == False    
