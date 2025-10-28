import textutils.core as c

def test_unique_words():
    text = "Red red BLUE"
    assert c.unique_words(text) == ["Red", "red", "BLUE"]