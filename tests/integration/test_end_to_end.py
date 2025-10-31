import textutils.core as c
#testing unique_words
def test_unique_words_pipeline():
    text = "Red red BLUE"
    final_text = text.lower()
    result = c.unique_words(final_text)
    assert result == ["blue", "red"]
#testing average_word_lenght
def test_average_word_length_pipeline():
    text = "Hello, WORLD!  This is  great."    
    normalized_text = text.lower()
    cleaned_text = ''.join(ch for ch in normalized_text if ch.isalpha() or ch.isspace())
    result = c.average_word_length(cleaned_text)
    assert abs(result - 4.2) < 1e-6
#testing count_vowels
def test_count_vowels_basic_pipeline():
    text = "Hello World"
    result = c.count_vowels(text)
    print(f"The number of vowels in '{text}' is: {result}")
def test_check_for_vowels(text="Hello World"):
    result = c.count_vowels(text)
    has_vowels = result > 0
    print(f"Text: '{text}'")
    print(f"Does the text contain any vowels? {has_vowels}")