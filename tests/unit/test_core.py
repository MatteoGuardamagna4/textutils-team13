import math
import textutils.core as c

# Average Word Length Tests
def test_average_word_length_basic():
    assert c.average_word_length("Hello world") == 5.0


def test_average_word_length_punctuation():
    assert c.average_word_length("Hello, world!") == 5.0


def test_average_word_length_empty():
    assert c.average_word_length("") == 0.0
    assert c.average_word_length("   ") == 0.0


def test_average_word_length_mixed():
    assert math.isclose(c.average_word_length("This  is   text."), 10/3, rel_tol=1e-9)


# Unique Words Tests
def test_unique_words_basic():
    assert c.unique_words("Red red BLUE") == ["blue", "red"]


# Count Vowels Tests
def test_count_vowels_basic():
    assert c.count_vowels("Hello World") == 3


# Word Count Tests
def test_word_count_basic():
    assert c.word_count("Red red BLUE") == {"red": 2, "blue": 1}


# Slugify Tests
def test_slugify_basic():
    assert c.slugify("Hello World") == "hello-world"


def test_slugify_with_hyphens():
    assert c.slugify("Python-Test Driven Development") == "python-test-driven-development"


# Count Sentences Tests
def test_count_sentences_basic():
    assert c.count_sentences("Hello world. How are you? Bye!") == 3


def test_count_sentences_trailing_spaces():
    assert c.count_sentences("Test.  ") == 1


def test_count_sentences_empty():
    assert c.count_sentences("") == 0


def test_count_sentences_mixed_punctuation():
    assert c.count_sentences("A! B? C.") == 3