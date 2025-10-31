import math
import textutils.core as c
#testing unique_words
#testing average_word_lenght
#testing count_vowels
#testing word_count

def test_average_word_length_basic():
    assert c.average_word_length("Hello world") == 5.0
def test_average_word_length_punctuation():
    assert c.average_word_length("Hello, world!") == 5.0
def test_average_word_length_spaces_and_empty():
    assert c.average_word_length("   ") == 0.0
    assert c.average_word_length("") == 0.0
def test_average_word_length_mixed():
    assert math.isclose(c.average_word_length("This  is   text."), 10/3, rel_tol=1e-9)



def test_unique_words():
    text = "Red red BLUE"
    assert c.unique_words(text) == ["blue", "red"]


def test_count_vowels_basic():
    """Test that count_vowels returns the correct number of vowels for a basic string."""
    text = "Hello World"
    assert c.count_vowels(text) == 3
import textutils.core as c

def test_word_count_basic():
    text = "Red red BLUE"
    assert c.word_count(text) == {"red": 2, "blue": 1}
