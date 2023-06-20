import bcrypt
from util import util

# Test file save function
def test_file_save():
    users = {
        "User1": [bcrypt.hashpw(b"Password1!", bcrypt.gensalt(rounds=12)), "User1FirstName", "User1LastName", "English"],
        "User2": [bcrypt.hashpw(b"Password2!", bcrypt.gensalt(rounds=12)), "User2FirstName", "User2LastName", "Spanish"],
    }

    test = {}
    util.file_save(users, filename="tests/test_database.csv")

    # Read the saved file and check if the data is correct
    util.file_read(test, filename="tests/test_database.csv")
    assert "User1" in test
    assert "User2" in test
    assert bcrypt.checkpw(b"Password1!", test["User1"][0])
    assert bcrypt.checkpw(b"Password2!", test["User2"][0])

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
    test1_users_full = {"user1", "user2", "user3", "user4", "user5", "user6"}
    test_users_not_full = {"user1", "user2", "user3", "user4", "user5"}
    
    assert util.database_check(test1_users_full) == True
    assert util.database_check(test_users_not_full) == False

# Test file read function
def test_file_read():
    test_users_file_read = {}
    test_filename = "tests/test_database.csv"
    util.file_read(test_users_file_read, test_filename)

    # See if the read was successful 
    assert "User1" in test_users_file_read
    assert "User2" in test_users_file_read

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
