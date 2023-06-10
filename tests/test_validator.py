import pytest

from user_auth import validator

@pytest.fixture
def users():
    return {
        "User1": "password1",
        "User2": "password2"
    }

def test_validate_username(users):
    # Test with an existing username
    existing_username = "User1"
    assert not validator.validate_username(users, existing_username)
    
    # Test with a new username
    new_username = "User3"
    assert validator.validate_username(users, new_username)

def test_validate_password():
    # Test with a valid password
    valid_password = "Passw0rd!"
    assert validator.validate_password(valid_password)

    # Test with a password missing special characters
    invalid_password = "Password1"
    assert not validator.validate_password(invalid_password)

    # Test with a password missing digits
    invalid_password = "Password!"
    assert not validator.validate_password(invalid_password)

    # Test with a password missing uppercase letters
    invalid_password = "password1!"
    assert not validator.validate_password(invalid_password)

    # Test with a password that is too short
    invalid_password = "Pwd1!"
    assert not validator.validate_password(invalid_password)

    # Test with a password that is too long
    invalid_password = "VeryLongPassword123!"
    assert not validator.validate_password(invalid_password)

    # Test with an empty password
    empty_password = ""
    assert not validator.validate_password(empty_password)

    # Test with a password that only contains special characters
    invalid_password = "@#$%^&*"
    assert not validator.validate_password(invalid_password)

    # Test with a password that only contains digits
    invalid_password = "12345678"
    assert not validator.validate_password(invalid_password)

    # Test with a password that only contains uppercase letters
    invalid_password = "PASSWORD"
    assert not validator.validate_password(invalid_password)

    # Test with a password that only contains lowercase letters
    invalid_password = "password"
    assert not validator.validate_password(invalid_password)

    # Test with a password that is missing multiple requirements
    invalid_password = "passw0rd"
    assert not validator.validate_password(invalid_password)

    # Test with a password that contains all requirements but is too long
    invalid_password = "Passw0rd!" * 3  # Length is 24
    assert not validator.validate_password(invalid_password)

    # Test with a password that contains all requirements but is too short
    invalid_password = "Pw0!"  # Length is 4
    assert not validator.validate_password(invalid_password)
