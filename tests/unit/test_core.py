import math
from textutils import average_word_length

def test_average_word_length_basic():
    assert average_word_length("Hello world") == 5.0

def test_average_word_length_punctuation():
    assert average_word_length("Hello, world!") == 5.0

def test_average_word_length_spaces_and_empty():
    assert average_word_length("   ") == 0.0
    assert average_word_length("") == 0.0

def test_average_word_length_mixed():
    assert math.isclose(average_word_length("This  is   text."), 10/3, rel_tol=1e-9)
import textutils.core as c

def test_unique_words():
    text = "Red red BLUE"
    assert c.unique_words(text) == ["blue", "red"]