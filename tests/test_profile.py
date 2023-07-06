import json
from profile import profile

def test_profile_options_menu(monkeypatch, capsys):
    user = ["username", "first_name", "last_name", "language", False, False, False, "university", "major"]
    inputs = iter(['9'])
    monkeypatch.setattr('builtins.input', lambda _: '9')
    profile.profile_options(user)
    out, _ = capsys.readouterr()
    print(out)
    assert out == """*** (1) EDIT TITLE ***
*** (2) EDIT MAJOR ***
*** (3) EDIT UNIVERSITY NAME ***
*** (4) EDIT ABOUT ***
*** (5) EDIT JOB EXPERIENCE ***
*** (6) EDIT EDUCATION EXPERIENCE ***
*** (7) VIEW PROFILE ***
*** (8) VIEW YOUR FRIEND'S PROFILE ***
*** (9) RETURN ***
"""

def test_profile_option_edit_title(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    inputs = iter(['o','title'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    profile.edit_title(user)
    out, _ = capsys.readouterr()
    assert "\nInvalid option, try again.\n" not in out
def test_profile_option_edit_major(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    inputs = iter(['o','major'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    profile.edit_major(user)
    out, _ = capsys.readouterr()
    assert "\nInvalid option, try again.\n" not in out
def test_profile_option_edit_university(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    inputs = iter(['o','university'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    profile.edit_university(user)
    out, _ = capsys.readouterr()
    assert "\nInvalid option, try again.\n" not in out
def test_profile_option_edit_about(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    inputs = iter(['o','about me'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    profile.edit_about(user)
    out, _ = capsys.readouterr()
    assert "\nInvalid option, try again.\n" not in out
def test_profile_option_edit_job(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    inputs = iter(['y','a','job title', 'employer', 'start_date','end_date','location','description','r'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    profile.edit_job(user)
    out, _ = capsys.readouterr()
    assert "\nInvalid option, try again.\n" not in out
def test_profile_option_edit_education(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    inputs = iter(['y','a','school_name','degree','years_attended','r', 'n'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    profile.edit_education(user)
    out, _ = capsys.readouterr()
    assert "\nInvalid option, try again.\n" not in out
def test_profile_option_view_profile(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    profile.view_profile(user)
    out, _ = capsys.readouterr()
    assert "*** YOUR PROFILE ***" in out or out == "\nYou must complete all required sections of your profile. You don\'t need to have a job experience section, but you must have the other sections!\n"
def test_profile_option_view_friends(monkeypatch, capsys):
    user = ["A", "A", "A", "language", False, False, False, "university", "major"]
    inputs = iter(['11'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    profile.view_friends_profile(user)
    out, _ = capsys.readouterr()
    assert "You have no friends! Go get some friends.\n" in out or "*** FRIENDS ***" in out
