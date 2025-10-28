import textutils.core as c
def unique_words_pipeline():
    text = "Red red BLUE"
    result = c.unique_words(text)
    assert result == ["Red", "red", "BLUE"]