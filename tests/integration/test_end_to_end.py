import textutils.core as c
def test_unique_words_pipeline():
    text = "Red red BLUE"
    final_test=text.lower()
    result = c.unique_words(text)
    assert result == ["blue", "red"]
