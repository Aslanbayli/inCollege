from selection import selection_menu as select

def test_selection_menu_options(monkeypatch, capsys):
    inputs = iter(['2', '6','r','8'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    user = ["username", "first_name", "last_name", "language", False, False, False, "university", "major"]
    select.selection_menu_options(user, [], [], [], [])
    
    out, _ = capsys.readouterr()
    assert """\n****** SELECTION MENU ******
***(1) SEARCH FOR A JOB***
***(2) FIND SOMEONE YOU KNOW***
***(3) LEARN A NEW SKILL***
***(4) USEFUL LINKS***
***(5) IMPORTANT LINKS***
***(6) SHOW MY NETWORK***
***(7) VIEW/EDIT MY PROFILE***
***(8) LOG OUT***""" in out

def test_job_search(monkeypatch, capsys):
    inputs = iter(['1', '3', 'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    user = ["username", "first_name", "last_name", "language"]
    select.job_search(user)

    out, _ = capsys.readouterr()
    assert out == "\n****** JOB SEARCH ******\n\
***(1) FIND JOB***\n\
***(2) CREATE JOB***\n\
***(3) RETURN TO SELECTION MENU***\n\
\nUnder construction, check back later...\n\
\n****** JOB SEARCH ******\n\
***(1) FIND JOB***\n\
***(2) CREATE JOB***\n\
***(3) RETURN TO SELECTION MENU***\n"

def test_skill_selection(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    select.skill_selection()

    out, _ = capsys.readouterr()
    assert out == "\n****** SKILL SELECTION ******\n\
***(1) TIME MANAGEMENT SKILLS***\n\
***(2) CODING LANGUAGE SKILLS***\n\
***(3) PUBLIC SPEAKING SKILLS***\n\
***(4) PERSONAL FINANCE MANAGEMENT SKILLS***\n\
***(5) COLLABORATION SKILLS***\n\
*(6) RETURN TO PREVIOUS SCREEN*\n\
\nUnder construction, check back later...\n"

def test_useful_links(monkeypatch, capsys):
    inputs = iter(['2', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    res = select.useful_links("not_logged_in")

    out, _ = capsys.readouterr()
    assert out == "\n****** USEFUL LINKS ******\n\
***(1) GENERAL***\n\
***(2) BROWSE INCOLLEGE***\n\
***(3) BUSINESS SOLUTIONS***\n\
***(4) DIRECTORIES***\n\
***(5) RETURN***\n\
\nUnder construction, check back later ...\n\
\n****** USEFUL LINKS ******\n\
***(1) GENERAL***\n\
***(2) BROWSE INCOLLEGE***\n\
***(3) BUSINESS SOLUTIONS***\n\
***(4) DIRECTORIES***\n\
***(5) RETURN***\n"

    assert res == "menu"
