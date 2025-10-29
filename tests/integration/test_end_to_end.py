import textutils.core as c
def test_unique_words_pipeline():
    text = "Red red BLUE"
    final_text = text.lower()
    result = c.unique_words(final_text)
    assert result == ["blue", "red"]

def test_average_word_length_pipeline():
    text = "Hello, WORLD!  This is  great."    
    normalized_text = text.lower()
    cleaned_text = ''.join(ch for ch in normalized_text if ch.isalpha() or ch.isspace())
    result = c.average_word_length(cleaned_text)
    assert abs(result - 4.2) < 1e-6
