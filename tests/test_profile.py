import json
from user_profile.user_profile import profile_options, view_friends_profile, load_user_data, save_user_data, edit_title, edit_major

def test_profile_options_menu(monkeypatch, capsys):
    user = ["username", "first_name", "last_name", "language", False, False, False, "university", "major"]
    inputs = iter(['9'])
    monkeypatch.setattr('builtins.input', lambda _: '9')
    profile_options(user)
    out, _ = capsys.readouterr()
    print(out)
    assert out == """\n*** (1) EDIT TITLE ***
*** (2) EDIT MAJOR ***
*** (3) EDIT UNIVERSITY NAME ***
*** (4) EDIT ABOUT ***
*** (5) EDIT JOB EXPERIENCE ***
*** (6) EDIT EDUCATION EXPERIENCE ***
*** (7) VIEW PROFILE ***
*** (8) VIEW YOUR FRIEND'S PROFILE ***
*** (9) RETURN ***
"""

def test_profile_option_view_friends(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    inputs = iter(['11'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    view_friends_profile(user)
    out, _ = capsys.readouterr()
    assert "You have no friends! Go get some friends.\n" in out or "*** FRIENDS ***" in out

def test_load_user_data_existing_user(tmp_path):
    # Create a temporary file for testing
    user_data_file = tmp_path / "testing.json"
    user_data_file.write_text('{"john": {"name": "John Doe"}}')

    # Test data
    username = 'john'
    expected_data = {"name": "John Doe"}

    # Perform the test
    result = load_user_data(username, str(user_data_file))

    # Assertion
    assert result == expected_data

def test_load_user_data_nonexistent_user(tmp_path):
    # Create a temporary file for testing
    user_data_file = tmp_path / "user_data.json"
    user_data_file.write_text('{"john": {"name": "John Doe"}}')

    # Test data
    username = 'adam'
    expected_data = {}

    # Perform the test
    result = load_user_data(username, str(user_data_file))

    # Assertion
    assert result == expected_data

def test_save_user_data(tmp_path):
    # Create a temporary file for testing
    user_data_file = tmp_path / "user_data.json"

    # Test data
    username = 'john'
    user_data = {"name": "John Doe"}

    # Write initial data to the temporary file
    with open(user_data_file, 'w') as f:
        json.dump({}, f)

    # Perform the test
    save_user_data(username, user_data, str(user_data_file))

    # Read the saved user data
    with open(user_data_file, 'r') as f:
        saved_data = json.load(f)

    # Assertion
    assert saved_data[username] == user_data



def test_edit_title(tmp_path, monkeypatch):
    # Create a temporary file for testing
    user_data_file = tmp_path / "testing.json"
    user_data_file.write_text('{"john": {"name": "John Doe", "Title": "Existing Title"}}')

    # Test data
    user = ['john']

    # Mock the input() function to provide user inputs
    user_input = iter(['a', 'Test'])

    # Patch the input() function to use user_input values
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

    # Perform the test (calling the function after mocking input)
    edit_title(user, str(user_data_file))

    # Assertions
    # Check if the title was updated correctly
    updated_user_data = load_user_data(user[0], str(user_data_file))
    assert updated_user_data['Title'] == 'Existing Title Test'

    user_data_file = tmp_path / "testing.json"
    user_data_file.write_text('{"john": {"name": "John Doe", "Title": "Existing Title"}}')

    # Test data
    user = ['john']

    # Mock the input() function to provide user inputs
    user_input = iter(['o', 'New Title'])

    # Patch the input() function to use user_input values
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

    # Perform the test (calling the function after mocking input)
    edit_title(user, str(user_data_file))

    # Assertions
    # Check if the title was updated correctly
    updated_user_data = load_user_data(user[0], str(user_data_file))
    assert updated_user_data['Title'] == 'New Title'

    user_data_file = tmp_path / "testing.json"
    user_data_file.write_text('{"john": {"name": "John Doe"}}')

    # Test data
    user = ['john']

    # Mock the input() function to provide user inputs
    user_input = iter(['New Title'])

    # Patch the input() function to use user_input values
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

    # Perform the test (calling the function after mocking input)
    edit_title(user, str(user_data_file))

    # Assertions
    # Check if the title was updated correctly
    updated_user_data = load_user_data(user[0], str(user_data_file))
    assert updated_user_data['Title'] == 'New Title'

def test_edit_major(tmp_path, monkeypatch):
    # Create a temporary file for testing
    user_data_file = tmp_path / "testing.json"
    user_data_file.write_text('{"john": {"name": "John Doe", "Major": "Cse"}}')

    # Test data
    user = ['john']

    # Mock the input() function to provide user inputs
    user_input = iter(['a', 'Test'])

    # Patch the input() function to use user_input values
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

    # Perform the test (calling the function after mocking input)
    edit_major(user, str(user_data_file))

    # Assertions
    # Check if the major was updated correctly
    updated_user_data = load_user_data(user[0], str(user_data_file))
    assert updated_user_data['Major'] == 'Cse Test'

    user_data_file = tmp_path / "testing.json"
    user_data_file.write_text('{"john": {"name": "John Doe", "Major": "Cse"}}')

    # Test data
    user = ['john']

    # Mock the input() function to provide user inputs
    user_input = iter(['o', 'Computer Science'])

    # Patch the input() function to use user_input values
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

    # Perform the test (calling the function after mocking input)
    edit_major(user, str(user_data_file))

    # Assertions
    # Check if the major was updated correctly
    updated_user_data = load_user_data(user[0], str(user_data_file))
    assert updated_user_data['Major'] == 'Computer Science'

    user_data_file = tmp_path / "testing.json"
    user_data_file.write_text('{"john": {"name": "John Doe"}}')

    # Test data
    user = ['john']

    # Mock the input() function to provide user inputs
    user_input = iter(['Computer Engineering'])

    # Patch the input() function to use user_input values
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

    # Perform the test (calling the function after mocking input)
    edit_major(user, str(user_data_file))

    # Assertions
    # Check if the major was updated correctly
    updated_user_data = load_user_data(user[0], str(user_data_file))
    assert updated_user_data['Major'] == 'Computer Engineering'
