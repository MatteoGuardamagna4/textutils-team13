import textutils.core as c

# Replace Numbers Tests
def test_replace_numbers_basic():
    assert c.replace_numbers("I have 2 cats and 1 dog.") == "I have two cats and one dog."

def test_replace_numbers_multiple_digits():
    assert c.replace_numbers("Room 42 is ready.") == "Room fourtwo is ready."

def test_replace_numbers_no_digits():
    assert c.replace_numbers("Hello world!") == "Hello world!"

def test_replace_numbers_only_digits():
    assert c.replace_numbers("1234567890") == "onetwothreefourfivesixseveneightninezero"

def test_replace_numbers_mixed():
    assert c.replace_numbers("He won 3 out of 5 games.") == "He won three out of five games."

