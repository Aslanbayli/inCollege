import pytest

from user_auth import validator as valid

@pytest.fixture
def users():
    return {
        "User1": "password1",
        "User2": "password2"
    }

def test_validate_username(users):
    # Test with an existing username
    existing_username = "User1"
    assert not valid.validate_username(users, existing_username)
    
    # Test with a new username
    new_username = "User3"
    assert valid.validate_username(users, new_username)

def test_validate_password():
    # Test with a valid password
    valid_password = "Passw0rd!"
    assert valid.validate_password(valid_password)

    # Test with a password missing special characters
    invalid_password = "Password1"
    assert not valid.validate_password(invalid_password)

    # Test with a password missing digits
    invalid_password = "Password!"
    assert not valid.validate_password(invalid_password)

    # Test with a password missing uppercase letters
    invalid_password = "password1!"
    assert not valid.validate_password(invalid_password)

    # Test with a password that is too short
    invalid_password = "Pwd1!"
    assert not valid.validate_password(invalid_password)

    # Test with a password that is too long
    invalid_password = "VeryLongPassword123!"
    assert not valid.validate_password(invalid_password)

    # Test with an empty password
    empty_password = ""
    assert not valid.validate_password(empty_password)

    # Test with a password that only contains special characters
    invalid_password = "@#$%^&*"
    assert not valid.validate_password(invalid_password)

    # Test with a password that only contains digits
    invalid_password = "12345678"
    assert not valid.validate_password(invalid_password)

    # Test with a password that only contains uppercase letters
    invalid_password = "PASSWORD"
    assert not valid.validate_password(invalid_password)

    # Test with a password that only contains lowercase letters
    invalid_password = "password"
    assert not valid.validate_password(invalid_password)

    # Test with a password that is missing multiple requirements
    invalid_password = "passw0rd"
    assert not valid.validate_password(invalid_password)

    # Test with a password that contains all requirements but is too long
    invalid_password = "Passw0rd!" * 3  # Length is 24
    assert not valid.validate_password(invalid_password)

    # Test with a password that contains all requirements but is too short
    invalid_password = "Pw0!"  # Length is 4
    assert not valid.validate_password(invalid_password)

def test_validate_input_yn():
    # Test to see if the conditions hold true
    assert valid.validate_input_yn("y") == True
    assert valid.validate_input_yn("n") == True
    assert valid.validate_input_yn("Y") == True
    assert valid.validate_input_yn("N") == True

    # Test to see if the conditions are false
    assert valid.validate_input_yn("Ye") == False
    assert valid.validate_input_yn("No") == False
    assert valid.validate_input_yn("BUrdfGEr") == False
    assert valid.validate_input_yn("KOPLEsxvbe") == False

def test_validate_input_lrm():
    # Test to see if the conditions hold true
    assert valid.validate_input_lrm("l") == True
    assert valid.validate_input_lrm("r") == True
    assert valid.validate_input_lrm("m") == True
    assert valid.validate_input_lrm("L") == True
    assert valid.validate_input_lrm("R") == True
    assert valid.validate_input_lrm("M") == True

    # Test to see if conditons hold false
    assert valid.validate_input_lrm("sdfsadf") == False
    assert valid.validate_input_lrm("dbrebebfk") == False
    assert valid.validate_input_lrm("Rwqndke") == False
    assert valid.validate_input_lrm("Pikachu") == False