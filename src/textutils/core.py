import textutils.core as c

def unique_words():
    text = "Red red BLUE"
    assert c.unique_words(text) == ["Red", "red", "BLUE"]